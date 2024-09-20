# Análise-Exploratoria-de-Dados-para-Varejo

Este projeto utiliza bibliotecas de análise de dados e visualização gráfica em Python para demonstrar como a linguagem pode ser usada para análise de grandes volumes de dados e geração de insights valiosos. Através da manipulação de DataFrames do Pandas e da criação de gráficos utilizando Matplotlib e Seaborn, o projeto resolve várias perguntas de negócio baseadas nos dados de vendas de uma empresa.

Os dados são reais e foram extraídos do link abaixo:
https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxlsFizemos 


## Funcionalidades do Projeto:

### Interface Gráfica (Versão Principal)
A versão principal do projeto usa Tkinter para criar uma interface gráfica onde o usuário pode selecionar perguntas específicas sobre os dados de vendas e visualizar tanto as respostas textuais quanto os gráficos gerados para análise.

As perguntas cobertas pelo projeto são:

1. Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
2. Qual o Total de Vendas Por Data do Pedido? (Mostra o resultado em um gráfico de barras)
3. Qual o Total de Vendas por Estado? (Mostra o resultado em um gráfico de barras)
4. Quais São as 10 Cidades com Maior Total de Vendas? (Mostra o resultado em um gráfico de barras)
5. Qual Segmento Teve o Maior Total de Vendas? (Mostra o resultado em um gráfico de pizza)
6. Qual o Total de Vendas Por Segmento e Por Ano?
7. Quantas Vendas Receberiam 15% de Desconto?
8. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?
9. Qual o Média de Vendas Por Segmento, Por Ano e Por Mês? (Mostra o resultado em um gráfico de linha)
10. Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? (Mostra o resultado em um gráfico de barras)

### Versão via Terminal - terminarversion.py 
Esta versão do projeto, chamada terminarversion.py, é executada diretamente no terminal sem interface gráfica. Ela contém as mesmas perguntas e realiza as mesmas análises, mas a interação é feita puramente via o terminal, com a saída dos resultados sendo exibida no console. Essa versão é útil para quem prefere um ambiente mais leve e sem GUI.

## Estrutura do Projeto:

### Bibliotecas Utilizadas
Pandas: Para manipulação e análise de dados tabulares, facilitando operações como agrupamento e filtragem.
Matplotlib e Seaborn: Para a criação de gráficos e visualizações que ajudam a entender os dados em questão.
Tkinter: Usado na versão principal para criar a interface gráfica que permite interação do usuário com o projeto.
NumPy: Para cálculos matemáticos e manuseio eficiente de arrays numéricos.
Funcionalidade do Código
O projeto realiza diversas tarefas relacionadas à análise de dados, incluindo:

Leitura e manipulação de arquivos CSV com os dados de vendas.
Criação de gráficos para responder perguntas específicas de negócio, facilitando a compreensão das vendas por cidade, estado, segmento e categoria.
Aplicação de regras de desconto e cálculo do impacto dessas alterações nas vendas.
Uso de gráficos como barras, pizza e linhas para visualizar padrões e tendências nos dados.
Diferença Entre as Versões
Versão Principal (Interface Gráfica): Possui uma interface amigável onde o usuário pode escolher perguntas e ver respostas com gráficos gerados automaticamente.
Versão Terminal (terminarversion.py): Focada em usuários que preferem uma experiência de linha de comando, sem interface gráfica, com a mesma lógica de análise aplicada.

### Como Executar o Projeto
Certifique-se de que você tem o Python instalado em sua máquina.
Instale as dependências necessárias executando:
pip install pandas matplotlib seaborn tk
Para rodar a versão principal com interface gráfica, execute:
python main.py
Para rodar a versão terminal, execute:
python terminarversion.py

## Conclusão
Este projeto demonstra como o Python, combinado com bibliotecas poderosas como Pandas e Matplotlib, pode ser usado para realizar análises de dados robustas e criar visualizações informativas que ajudam a responder perguntas de negócio. Seja através de uma interface gráfica ou via terminal, o projeto facilita a exploração de grandes volumes de dados e oferece uma visão clara dos padrões de vendas.