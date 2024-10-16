# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Seguro Agricola Sazonal

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/">Edmar Ferreira Souza</a>
- <a href="https://www.linkedin.com/company/">Thiago Lima Bernardes</a>
- <a href="https://www.linkedin.com/company/">Alexandre Oliveira Mantovani</a> 
- <a href="https://www.linkedin.com/company/">Ricardo Lourenço Coube</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>


## 📜 Descrição

Este projeto é uma aplicação para simulação de seguros sazonais agrícolas, permitindo calcular prêmios mensais e anuais com base em diferentes tipos de cobertura e regiões. Além disso, oferece funcionalidades para cadastrar, consultar, alterar e excluir propostas de novas modalidades de seguro no banco de dados.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

1. Abra o script do programa "Seguro_Sazonal.py"
2. Configure as credenciais do banco de dados no local indicado.
3. Baixe e configure o Oracle SQL Developer com suas credenciais de conexão. 
2. Execute o "Script_Tabela_Simulacoes" no Oracle SQL Developer.
3. Execute o programa "Seguro_Sazonal.py"


### Funcionalidades
Conexão com Banco de Dados: Conecta-se ao banco de dados Oracle para armazenar e manipular dados das sugestões de nosvos seguros.

Cálculo de Prêmios: 
Calcula prêmios mensais e anuais com base no custo anual da operação, tipo de cobertura e região.

Exportação de Dados: 
Exporta os resultados das simulações para arquivos .txt e .json.

CRUD de Sugestões:  
Permite cadastrar, consultar, alterar e excluir Sugestões de novas modalidades de seguro no banco de dados.

Funções Principais

calcular_valor_cobertura(custo_anual, tipo_cobertura): Calcula o valor da cobertura com base no tipo de cobertura.
calcular_premio_anual(valor_cobertura, taxa_premio=0.11): Calcula o prêmio anual.
calcular_premio_mensal(premio_anual, atividade, mes, estado): Calcula o prêmio mensal considerando a atividade e a região.
exibir_detalhes(atividade, custo_anual, tipo_cobertura, valor_cobertura, premio_mensal): Exibe os detalhes da simulação.
exportar_para_txt(...): Exporta os dados da simulação para um arquivo .txt.
exportar_para_json(...): Exporta os dados da simulação para um arquivo .json.
menu_exportacao(...): Menu para escolher o formato de exportação.
contratar_seguro(): Função principal para contratar seguro.
menu_crud(conn): Menu para operações CRUD no banco de dados.


## 🗃 Histórico de lançamentos

* 1.0.0 - 14/10/2024
    * 
* 0.1.0 - 07/10/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
