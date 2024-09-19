#Teste com arquivo CSV do Governo dos EUA
import pandas as pd
import numpy as np

#Leitura do CSV
df = pd.read_csv("Testes2/4136febc-e217-40f5-a05a-70d116562703.csv")
#print(df.head(70))
#print('\n')

#Leitura com filto apenas dos 60km/h
df_filtered = df[df['velocidade_via'] == '60 Km/h']
#print(df_filtered)
#print(df.describe())

#Teste Groupby
dfGrouped = df[['latitude', 'velocidade_via', '_id']].groupby(['velocidade_via']).agg(['mean','std','count'])
print(dfGrouped)
print('\n')

#filtrando com base em strings
dfFotosensores = df[df.tipo.str.startswith("F")]
print(dfFotosensores)

#Função que define graficamente no pandas
#dfFotosensores.plot()
dfFotosensores['latitude'].plot(kind='hist', bins=10, title='Histograma de Latitude')

#vizualização do ggráfico
#import matplotlib.pyplot as plt
#plt.show()