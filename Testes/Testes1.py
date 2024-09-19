import pandas as pd
import numpy as np

#Exemplo de Dataframe
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
dataf = pd.DataFrame(data)
print(dataf.head(5))


#Exemplo de Dataframe com tamanhos diferentes (Espaços vazios são preenchidos com "none")
data2 = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24],
    'City': ['New York', 'Paris', 'Berlin']
}
dataf2 = pd.DataFrame.from_dict(data2, orient='index').T

#print("\n")
#print(dataf2)
#print(dataf2.head(5))

#Exemplo de Dataframe de dicionario com dicionarios nestados
data3 = {
    'John': {'Age': 28, 'City': 'New York'},
    'Anna': {'Age': 24, 'City': 'Paris'},
    'Peter': {'Age': 35, 'City': 'Berlin'},
}

dataf3 = pd.DataFrame.from_dict(data3, orient='index')

#print("\n")
#print(dataf3)

#Data 3 sem a orientação index (funciona como um gráfico)
dataf3s = pd.DataFrame(data3)
#print("\n")
#print(dataf3s)

#No data 4 os valores são tuplas, funciona com tanto que eles tenham o mesmo tamanho
data4 = {
    'Name': ('John', 'Anna', 'Peter', 'Linda'),
    'Age': (28, 24, 35, 32),
    'City': ('New York', 'Paris', 'Berlin', 'London')
}

dataf4 = pd.DataFrame(data4)

#print("\n")
#print(dataf4)

#Reorganização de colunas e adição de uma a mais

dataf1v2 = pd.DataFrame(data, columns = ['Age', 'Name', 'City','Street Number'], index = ['user1','user2','user3', 'user4'])

print("\n")
print(dataf1v2)
#Printando apenas 2 colunas
#print(dataf1v2[["Age", "City"]])

#Filtrando, por coluna(1) ou row(0)
#print(dataf1v2.filter(items=["Age"], axis = 1))
#print(dataf1v2.filter(items=["user1"], axis = 0))

#Resumo estatistico (Apenas os numeros)
#print(dataf1v2.describe())

#Verificação de NA
#print(dataf1v2.isna())

#Adição de numeros em Street Number com Numpy
dataf1v2['Street Number'] = np.arange(4)
print(dataf1v2)