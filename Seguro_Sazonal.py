# Importação dos módulos
import os
import oracledb
import pandas as pd
import json
import cx_Oracle
import pandas

# Try para tentativa de Conexão com o Banco de Dados
try:
    # Efetua a conexão com o Usuário no servidor (Insira aqui seu usuário e senha)
    conn = oracledb.connect(user='RMXXXXXX', password="XXXXXX", dsn='oracle.fiap.com.br:1521/ORCL')
    # Cria as instruções para cada módulo
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    # Informa o erro
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao = False
else:
    # Flag para executar a Aplicação
    conexao = True

def calcular_valor_cobertura(custo_anual, tipo_cobertura):
    if tipo_cobertura == "desastres_climaticos":
        return custo_anual * 0.852
    elif tipo_cobertura == "pragas_doencas":
        return custo_anual * 0.735
    elif tipo_cobertura == "cobertura_total":
        return custo_anual
    else:
        raise ValueError("Tipo de cobertura inválido")

def calcular_premio_anual(valor_cobertura, taxa_premio=0.11):
    return valor_cobertura * taxa_premio

def calcular_premio_mensal(premio_anual, atividade, mes, estado):
    premio_mensal = premio_anual / 12
    meses_seca = {
        "Centro-Oeste": [5, 6, 7, 8, 9],  # Maio a Setembro
        "Sudeste": [6, 7, 8, 9, 10],      # Junho a Outubro
        "Nordeste": [9, 10, 11, 12, 1],   # Setembro a Janeiro
        "Sul": [11, 12, 1, 2, 3]          # Novembro a Março
    }

    if mes in meses_seca.get(estado, []):
        if atividade == "Cultivo de Grãos" or atividade == "Horticultura":
            premio_mensal *= 1.47  # Aumento de 47%
        elif atividade == "Pecuária":
            premio_mensal *= 1.75  # Aumento de 75%

    return premio_mensal

def exibir_detalhes(atividade, custo_anual, tipo_cobertura, valor_cobertura, premio_mensal):
    print(f"\nAtividade: {atividade}")
    print(f"Custo Anual da Operação: R${custo_anual:.2f}")
    print(f"Tipo de Cobertura: {tipo_cobertura}")
    print(f"Valor da Cobertura: R${valor_cobertura:.2f}")
    print(f"Valor mensalidade: R${premio_mensal:.2f}")

def mostrar_menu(lista_opcoes, mensagem, incluir_voltar=False):
    while True:
        print(mensagem)
        for i, opcao in enumerate(lista_opcoes, 1):
            print(f"{i}. {opcao}")
        if incluir_voltar:
            print(f"{len(lista_opcoes) + 1}. Voltar ao Menu de Atividade")
        print(f"{len(lista_opcoes) + 2}. Sair do Programa")
        try:
            escolha = int(input("Escolha uma opção: "))
            if 1 <= escolha <= len(lista_opcoes):
                return lista_opcoes[escolha - 1]
            elif incluir_voltar and escolha == len(lista_opcoes) + 1:
                return "Voltar ao Menu de Atividade"
            elif escolha == len(lista_opcoes) + 2:
                print("Saindo do programa...")
                exit()
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.\n")

def exportar_para_txt(atividade, custo_anual, tipo_cobertura, valor_cobertura, premios_mensais, valor_total_seguradora):
    with open("simulacao.txt", "w") as file:
        file.write(f"Atividade: {atividade}\n")
        file.write(f"Custo Anual da Operação: R${custo_anual:.2f}\n")
        file.write(f"Tipo de Cobertura: {tipo_cobertura}\n")
        file.write(f"Valor da Cobertura: R${valor_cobertura:.2f}\n")
        file.write("Premios Mensais:\n")
        for mes, premio in enumerate(premios_mensais, 1):
            file.write(f"Mês {mes}: R${premio:.2f}\n")
        file.write(f"Total das Mensalidades: R${sum(premios_mensais):.2f}\n")
        file.write(f"Valor Total Correspondente à Seguradora: R${valor_total_seguradora:.2f}\n")

def exportar_para_json(atividade, custo_anual, tipo_cobertura, valor_cobertura, premios_mensais, valor_total_seguradora):
    dados = {
        "Atividade": atividade,
        "Custo Anual da Operacao": custo_anual,
        "Tipo de Cobertura": tipo_cobertura,
        "Valor da Cobertura": valor_cobertura,
        "Premios Mensais": premios_mensais,
        "Total das Mensalidades": sum(premios_mensais),
        "Valor Total Correspondente à Seguradora": valor_total_seguradora
    }
    with open("simulacao.json", "w") as file:
        json.dump(dados, file, indent=4)

def menu_exportacao(atividade, custo_anual, tipo_cobertura, valor_cobertura, premios_mensais, valor_total_seguradora):
    opcoes_exportacao = ["Exportar Arquivo '.txt'", "Exportar Arquivo '.json'", "Retornar ao Menu Principal"]
    while True:
        escolha = mostrar_menu(opcoes_exportacao, "\nEscolha uma opção de exportação:", incluir_voltar=True)
        if escolha == "Exportar Arquivo '.txt'":
            exportar_para_txt(atividade, custo_anual, tipo_cobertura, valor_cobertura, premios_mensais, valor_total_seguradora)
            print("\nDados exportados para 'simulacao.txt'.")
        elif escolha == "Exportar Arquivo '.json'":
            exportar_para_json(atividade, custo_anual, tipo_cobertura, valor_cobertura, premios_mensais, valor_total_seguradora)
            print("\nDados exportados para 'simulacao.json'.")
        elif escolha == "Retornar ao Menu Principal":
            return True  # Indica que o usuário deseja retornar ao menu principal
        elif escolha == "Voltar ao Menu de Atividade":
            return "Voltar ao Menu de Atividade"

def contratar_seguro():
    while True:
        atividades = ["Cultivo de Grãos", "Pecuária", "Horticultura"]
        tipos_cobertura = ["desastres_climaticos", "pragas_doencas", "cobertura_total"]
        regioes = ["Centro-Oeste", "Sudeste", "Nordeste", "Sul"]

        atividade = mostrar_menu(atividades, "\nEscolha a atividade:")
        while True:
            try:
                custo_anual = float(input("\nDigite o custo anual da operação em R$: "))
                if custo_anual <= 0:
                    raise ValueError("O custo anual deve ser um número positivo.")
                break
            except ValueError as e:
                print(f"\nEntrada inválida: {e}. Por favor, digite um número válido.")

        tipo_cobertura = mostrar_menu(tipos_cobertura, "\nEscolha o tipo de cobertura:", incluir_voltar=True)
        if tipo_cobertura == "Voltar ao Menu de Atividade":
            continue

        regiao = mostrar_menu(regioes, "\nEscolha a Região:", incluir_voltar=True)
        if regiao == "Voltar ao Menu de Atividade":
            continue

        valor_cobertura = calcular_valor_cobertura(custo_anual, tipo_cobertura)
        premio_anual = calcular_premio_anual(valor_cobertura)

        soma_premios_mensais = 0  # Inicializa a soma dos prêmios mensais
        premios_mensais = []  # Lista para armazenar os prêmios mensais

        for mes in range(1, 13):
            premio_mensal = calcular_premio_mensal(premio_anual, atividade, mes, regiao)
            soma_premios_mensais += premio_mensal  # Acumula o valor do prêmio mensal
            premios_mensais.append(premio_mensal)  # Adiciona o prêmio mensal à lista
            print(f"\nMês: {mes}")
            exibir_detalhes(atividade, custo_anual, tipo_cobertura, valor_cobertura, premio_mensal)

        valor_total_seguradora = soma_premios_mensais * 0.11  # Calcula o valor total correspondente à seguradora
        print(f"\nTotal das Mensalidades: R${soma_premios_mensais:.2f}")
        print(f"\nValor Total Correspondente à Seguradora: R${valor_total_seguradora:.2f}")

        # Menu de exportação
        resultado_exportacao = menu_exportacao(atividade, custo_anual, tipo_cobertura, valor_cobertura, premios_mensais, valor_total_seguradora)
        if resultado_exportacao == "Voltar ao Menu de Atividade":
            continue
        elif resultado_exportacao:
            return True  # Indica que o usuário deseja reiniciar o programa

def cadastrar_simulacao(conn, atividade, custo_anual, tipo_cobertura, valor_cobertura, premio_anual, premio_mensal, mes, regiao):
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO SIMULACOES (ATIVIDADE, CUSTO_ANUAL, TIPO_COBERTURA, VALOR_COBERTURA, PREMIO_ANUAL, PREMIO_MENSAL, MES, REGIAO)
                 VALUES (:1, :2, :3, :4, :5, :6, :7, :8)"""
        cursor.execute(sql, (atividade, custo_anual, tipo_cobertura, valor_cobertura, premio_anual, premio_mensal, mes, regiao))
        conn.commit()
        print("Atividade cadastrada com sucesso!")
    except Exception as e:
        print("Erro ao cadastrar Atividade:", e)

def consultar_simulacoes(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SIMULACOES")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Erro ao consultar Atividade:", e)

def alterar_simulacao(conn, id_simulacao, novo_valor_cobertura):
    try:
        cursor = conn.cursor()
        sql = "UPDATE SIMULACOES SET VALOR_COBERTURA = :1 WHERE ID = :2"
        cursor.execute(sql, (novo_valor_cobertura, id_simulacao))
        conn.commit()
        print("Atividade alterada com sucesso!")
    except Exception as e:
        print("Erro ao alterar Atividade:", e)

def excluir_simulacao(conn, id_simulacao):
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM SIMULACOES WHERE ID = :1"
        cursor.execute(sql, (id_simulacao,))
        conn.commit()
        print("Atividade excluída com sucesso!")
    except Exception as e:
        print("Erro ao excluir Atividade:", e)


def menu_crud(conn):
    while True:
        opcoes_crud = ["Cadastrar Atividade", "Consultar Atividade", "Alterar Atividade", "Excluir Atividade",
                       "Voltar ao Menu Principal"]
        escolha = mostrar_menu(opcoes_crud, "\nEste é o 'Controle de Sugestões'. As propostas inseridas serão estudadas pela gestão:")

        if escolha == "Cadastrar Atividade":
            # Solicitar dados para cadastro
            atividade = input("Atividade: ")
            custo_anual = float(input("Custo Anual: "))
            tipo_cobertura = input("Tipo de Cobertura: ")
            valor_cobertura = float(input("Valor da Cobertura: "))
            premio_anual = float(input("Prêmio Anual: "))
            premio_mensal = float(input("Prêmio Mensal: "))
            mes = int(input("Mês: "))
            regiao = input("Região: ")
            cadastrar_simulacao(conn, atividade, custo_anual, tipo_cobertura, valor_cobertura, premio_anual,
                                premio_mensal, mes, regiao)

        elif escolha == "Consultar Atividade":
            consultar_simulacoes(conn)

        elif escolha == "Alterar Atividade":
            id_simulacao = int(input("ID da Atividade a ser alterada: "))
            novo_valor_cobertura = float(input("Novo Valor da Cobertura: "))
            alterar_simulacao(conn, id_simulacao, novo_valor_cobertura)

        elif escolha == "Excluir Atividade":
            id_simulacao = int(input("ID da Atividade a ser excluída: "))
            excluir_simulacao(conn, id_simulacao)

        elif escolha == "Voltar ao Menu Principal":
            break


# Definição da função main
def main():
    while True:
        # Menu principal do programa
        atividades = ["Contratar Seguro", "Sugestões de Seguro", "Sair do Programa"]
        escolha = mostrar_menu(atividades, "\nEscolha uma opção:")

        if escolha == "Contratar Seguro":
            contratar_seguro()
        elif escolha == "Sugestões de Seguro":
            menu_crud(conn)
        elif escolha == "Sair do Programa":
            print("Você escolheu sair do programa.")
            # Chama o menu CRUD antes de sair
            menu_crud(conn)
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Chamada da função principal
if __name__ == "__main__":
    main()
