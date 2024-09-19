import pandas as pd  
import matplotlib.pyplot as plt 
import matplotlib.pylab as lab 
import seaborn as sea
import numpy as np
import matplotlib as mat 
import warnings
warnings.filterwarnings("ignore")
import sqlite3 #banco de dados sqlite3
import random

#Leitura do CSV com o Pandas
df = pd.read_csv("dataset.csv")

#Visualização do Dataframe

dfHead = df.head()
dfTail = df.tail()

print(dfHead)
print('\n')
print(dfTail)
print('\n----------------------------------------------------------Pergunta 1----------------------------------------------------------------------------------\n')

#PERGUNTA 1: Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?


CidadesOS = df[df['Categoria'] == 'Office Supplies'] #Organização do Dataframe para apenas mostrar aqueles com a Categoria "Office Supplies"
CidadeMaisVendas = CidadesOS.groupby('Cidade')['Valor_Venda'].sum().idxmax() #groupby que soma todos os valores venda de cada cidade e com IDXMAX verifica a maior

print(f'Qual Cidade com Maior Valor de Venda de Produtos da Categoria Office Supplies? Resposta:')
print(CidadeMaisVendas)
print('\n')

#Lista de top Cidades em numero de vendas para visualização:
print(CidadesOS.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False))
print('\n-----------------------------------------------------------Pergunta 2---------------------------------------------------------------------------------\n')

#PERGUNTA 2: Qual o total de vendas por Data do pedido? Demonstre via gráfico de Barras (OBS: Não é uma serie temporal)

Df_Data_Pedido = df['Data_Pedido'] #DataFrame Baseado na data dos pedidos
Datas_e_Vendas = df.groupby('Data_Pedido')['Valor_Venda'].sum()
print(Datas_e_Vendas)

#Criação do gráfico de barras
plt.figure(figsize=(18,9))

Datas_e_Vendas.plot(x = 'Data_Pedido', y = 'Valor_Vendas', color= 'skyblue')

plt.title('Total de Vendas por Data de Pedido')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()  # Ajusta o layout para que os rótulos não se sobreponham
plt.show()

print('\n-----------------------------------------------------------Pergunta 3---------------------------------------------------------------------------------\n')

#PERGUNTA 3: Qual o Total de vendas por estado? (Demonstre o resultado através de um gráfico de barras)

Vendas_Por_Estado = df.groupby('Estado')['Valor_Venda'].sum()
print(f' Vendas por estado: \n {Vendas_Por_Estado}')

plt.figure(figsize= (18, 9))
Vendas_Por_Estado.plot(kind = 'bar', x = 'Estado', y = 'Valor_Vendas', color= 'green')
plt.title('Total de vendas por estado')

plt.tight_layout()
plt.xticks(rotation=75, ha='right')
plt.show()

print('\n-----------------------------------------------------------Pergunta 4---------------------------------------------------------------------------------\n')

#PERGUNTA 4: Quais São as 10 Cidades com Maior Total de Vendas?

print(CidadesOS.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).head(10))
top10Cidades = CidadesOS.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize= (18, 9))
top10Cidades.plot(kind = 'bar', x = 'Cidade', y = 'Valor_Vendas', color= 'green')
plt.title('10 Cidades com maior total de vendas')

plt.tight_layout()
plt.xticks(rotation=75, ha='right')
plt.show()
