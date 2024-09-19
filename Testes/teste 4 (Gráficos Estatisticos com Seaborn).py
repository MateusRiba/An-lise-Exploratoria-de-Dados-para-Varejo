import pandas as pd  
import matplotlib.pyplot as plt 
import matplotlib.pylab as lab 
import seaborn as sea
import numpy as np
import matplotlib as mat 
import random
import warnings
warnings.filterwarnings("ignore")

#Dataset de tips
dados = sea.load_dataset("tips")
dadosHead = dados.head(10)
print(dados.head())

#Metodo joinplot de 2 variaveis (nesse caso a conta e a gorjeta)
# Perceba que varios graficos estatisticos são colocados todos acima um dos outros

jointPlot1 = sea.jointplot(data = dadosHead, x = "total_bill", y = "tip", kind = 'reg')
plt.show()

#Metodo para fazer um grafico relacionado a outra variavel (Dados e modelo de regressão)
# são 2 graficos comparando quando por exemplo, é fumante ou não

jointPlot2 = sea.lmplot(data = dados, x = "total_bill", y = "tip", col = 'smoker')
plt.show()

#Criando base de dados Random
df = pd.DataFrame()

df['Idade'] = random.sample(range(20, 100), 30)
df['Peso'] = random.sample(range(55, 150), 30)

print(f'\n {df.shape}')
print(df.head())

#Modelo de Regressão
sea.lmplot(data = df, x = 'Idade', y = 'Peso', fit_reg=True)
plt.show()

#Modelo de Densidade
sea.kdeplot(df.Idade)
plt.show()