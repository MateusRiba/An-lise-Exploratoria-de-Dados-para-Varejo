import pandas as pd  
import matplotlib.pyplot as plt 
import matplotlib.pylab as lab 
import seaborn as sns
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
#plt.show()

print('\n-----------------------------------------------------------Pergunta 3---------------------------------------------------------------------------------\n')

#PERGUNTA 3: Qual o Total de vendas por estado? (Demonstre o resultado através de um gráfico de barras)

Vendas_Por_Estado = df.groupby('Estado')['Valor_Venda'].sum()
print(f' Vendas por estado: \n {Vendas_Por_Estado}')

plt.figure(figsize= (18, 9))
Vendas_Por_Estado.plot(kind = 'bar', x = 'Estado', y = 'Valor_Vendas', color= 'green')
plt.title('Total de vendas por estado')

plt.tight_layout()
plt.xticks(rotation=75, ha='right')
#plt.show()

print('\n-----------------------------------------------------------Pergunta 4---------------------------------------------------------------------------------\n')

#PERGUNTA 4: Quais São as 10 Cidades com Maior Total de Vendas? (Demonstre o resultado através de um gráfico de barras)

print(CidadesOS.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).head(10))
top10Cidades = CidadesOS.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize= (18, 9))
top10Cidades.plot(kind = 'bar', x = 'Cidade', y = 'Valor_Vendas', color= 'green')
plt.title('10 Cidades com maior total de vendas')

plt.tight_layout()
plt.xticks(rotation=75, ha='right')
#plt.show()

print('\n-----------------------------------------------------------Pergunta 5---------------------------------------------------------------------------------\n')

#PERGUNTA 5: Qual Segmento Teve o Maior Total de Vendas? (Demonstre atraves de um gráfico de pizza)

Vendas_Por_Segmento = df.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by= 'Valor_Venda', ascending= False)
print(Vendas_Por_Segmento) #Localiza o primeiro valor

print(f'\nSegmento que teve o maior numero de vendas totais:\n Resposta: {Vendas_Por_Segmento.iloc[0]["Segmento"]}') #Localiza o primeiro valor 

#Grafico Pizza:

def valorBruto(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return f"${absolute:,d}"  # Formata o valor com separadores de milhar

plt.figure(figsize= (18,9))

Vendas_Por_Segmento.set_index('Segmento')['Valor_Venda'].plot(kind= 'pie', autopct=lambda pct: valorBruto(pct, Vendas_Por_Segmento['Valor_Venda']), startangle=90, y= 'Valor_Venda', legend=True,  ylabel='', wedgeprops={'linewidth': 1, 'edgecolor': 'white'})

centre_circle = plt.Circle((0, 0), 0.70, fc='white') #Define o circulo central
#Adiciona o círculo ao gráfico
plt.gca().add_artist(centre_circle)

plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(df['Valor_Venda']))), xy = (-0.25, 0))
plt.title('Total de Vendas por segmentos')
plt.tight_layout()
#plt.show()

print('\n-----------------------------------------------------------Pergunta 6---------------------------------------------------------------------------------\n')

#PERGUNTA 6: Qual o total de vendas por segmento e por ano

#Convertendo a coluna "data" para conseguir o ano.

df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format= '%d/%m/%Y') #Transformando a coluna "Data_Pedido" para um formato real de data
df['Ano'] = df['Data_Pedido'].dt.year #Adicionando uma nova coluna

print(df)

Vendas_Por_Segmento_e_Ano = df.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
print(f'\n Aqui estão as Vendas por segmento e por ano: \n{Vendas_Por_Segmento_e_Ano}')

print('\n-----------------------------------------------------------Pergunta 7---------------------------------------------------------------------------------\n')

#PERGUNTA 7: Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
#- Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
#- Se o Valor_Venda for menor que 1000 recebe 10% de desconto.

### Quantas Vendas Receberiam 15% de Desconto?

QuantidadeQueRecebe15PorCento =  df[df['Valor_Venda'] > 1000].shape[0]
print(f'\n A quantidade de vendas que receberiam 15% de desconto são: {QuantidadeQueRecebe15PorCento}')

#OBS: Outro metodo de fazer:

# Cria uma nova coluna de acordo com a regra definida acima  ------> Dessa maneira uma nova coluna com os valores de desconto são criadas,
#mais complexo para responder a pergunta porem util em outros casos
#df['Desconto'] = np.where(df['Valor_Venda'] > 1000, 0.15, 0.10)

print('\n-----------------------------------------------------------Pergunta 8---------------------------------------------------------------------------------\n')

#PERGUNTA 8: Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

df['Valor_Venda_Com_Desconto_15%'] = df['Valor_Venda'].where(df['Valor_Venda'] <= 1000, df['Valor_Venda'] * 0.85) #uma maneira
#df['Valor_Venda_Com_Desconto_15%'] = df['Valor_Venda'].apply(lambda x: x * 0.85 if x > 1000 else x) #outra maneira

#Descontos aplicados
print(df[df['Valor_Venda'] > 1000])

#Conseguir a media entre as duas colunas

media = df['Valor_Venda'].mean()
media2 = df['Valor_Venda_Com_Desconto_15%'].mean()

print(f'\nA média dos valores venda sem desconto é: {media}\n A média dos valores venda com desconto é {media2}')

print('\n-----------------------------------------------------------Pergunta 9---------------------------------------------------------------------------------\n')

#PERGUNTA 9: Qual o Média de Vendas Por Segmento, Por Ano e Por Mês? (Demonstre o resultado através de gráfico de linha.)

df['Mês'] = df['Data_Pedido'].dt.month

Média_Segmento = df.groupby(['Segmento','Ano','Mês'])['Valor_Venda'].mean().reset_index()

print(Média_Segmento)

#Cria uma paleta de cores personalizada
paleta = sns.color_palette("husl", len(Média_Segmento['Segmento'].unique()))

#Cria o grid de gráficos com base no ano
g = sns.FacetGrid(Média_Segmento, col="Ano", hue="Segmento", palette=paleta, col_wrap=2, height=5, aspect=1.5)

#Adiciona os gráficos de linha em cada subplot
g.map(sns.lineplot, 'Mês', 'Valor_Venda', marker="o")

#Adicionar título geral
g.figure.suptitle('Média de Vendas por Segmento, Ano e Mês', fontsize=16)

#Ajusta os rótulos dos eixos e o layout
g.set_axis_labels("Mês", "Média do Valor de Vendas")
g.add_legend(title="Segmento")

#Adiciona o grid
g.set(xticks=range(1, 13))  # Colocar todos os meses no eixo x (1-12)
plt.subplots_adjust(top=0.9)  # Ajustar a posição do título geral

plt.show()

print('\n-----------------------------------------------------------Pergunta 10---------------------------------------------------------------------------------\n')

#PERGUNTA 10: Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? (Demonstre tudo através de um único gráfico.)

top12Subcategorias = df.groupby(['Categoria','SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda',ascending = False).head(12).reset_index()
total_vendas_categoria = df.groupby('Categoria')['Valor_Venda'].sum().reset_index()

print(top12Subcategorias)

plt.figure(figsize=(14, 8))
sns.barplot(x='Valor_Venda', y='SubCategoria', hue='Categoria', data=top12Subcategorias, palette='Set2')

plt.title('Total de Vendas por Categoria e SubCategoria (Top 12 SubCategorias)')
plt.xlabel('Total de Vendas')
plt.ylabel('SubCategoria')

for i, categoria in enumerate(total_vendas_categoria['Categoria']):
    total_vendas = total_vendas_categoria[total_vendas_categoria['Categoria'] == categoria]['Valor_Venda'].values[0]
    plt.text(top12Subcategorias['Valor_Venda'].max() * 1.05, i * 4,  
             f'Total {categoria}: R$ {total_vendas:,.2f}', 
             fontsize=12, color='black')


plt.tight_layout()

plt.show()