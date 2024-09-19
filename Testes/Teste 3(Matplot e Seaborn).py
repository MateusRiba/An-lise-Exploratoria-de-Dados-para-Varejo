import pandas as pd  
import matplotlib.pyplot as plt 
import matplotlib.pylab as lab 

#Definindo eixo de graficos

#plot1 = plt.plot([1,3,5],[2,4,7])
plt.xlabel('Caneta azul')
plt.ylabel('azul Caneta')
plt.title('Manoel Gomes')
#plt.show()

#Grafico de barras

#plt.legend()
#plot2 = plt.bar(['Casa','Apto','Rua'],[2,4,7], label = 'What de ddog doing', color = 'green')

#plt.show()

#Grafico de Dispersão

x = [1, 2, 3, 4, 5]  # Eixo X
y = [5, 7, 8, 5, 10]  # Eixo Y

plt.scatter(x, y, color='blue', marker='o')

plt.title('Gráfico de Dispersão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

#plt.show()

#Area Empilhada

dias = [1, 2, 3, 4, 5]
comida = [5, 6, 7, 8, 9]
transporte = [2, 3, 4, 3, 2]
diversao = [1, 2, 1, 1, 2]

# Criando o gráfico de área empilhada
plt.stackplot(dias, comida, transporte, diversao, labels=['Comida', 'Transporte', 'Diversão'])

# Adicionando título e rótulos aos eixos
plt.title('Gastos ao Longo dos Dias')
plt.xlabel('Dias')
plt.ylabel('Gastos (em unidades)')

# Adicionando a legenda
plt.legend(loc='upper left')

# Exibindo o gráfico
#plt.show()

#Pizza

# Dados de exemplo
categorias = ['Comida', 'Transporte', 'Diversão', 'Educação']
gastos = [300, 150, 100, 200]

# Criando o gráfico de pizza
plt.pie(gastos, labels=categorias, autopct='%1.1f%%', startangle=90)

# Adicionando título
plt.title('Distribuição dos Gastos')

# Exibindo o gráfico
#plt.show()

#OBS: Tem como fazer graficos personalizados, definindo exatamente todos os parametros, inclusive:
# ESCALAS DIFERENTES
# Grid (Quadriculado)
# Estogramas tambem são possiveis de ser feitos


#Grafico em 3D

from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Gerando os dados
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Criando a figura
fig = plt.figure()

# Adicionando um eixo 3D
ax = fig.add_subplot(111, projection='3d')

# Plotando o gráfico de superfície
ax.plot_surface(x, y, z, cmap='viridis')

# Adicionando título e rótulos
ax.set_title('Gráfico 3D de Superfície')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Exibindo o gráfico
plt.show()