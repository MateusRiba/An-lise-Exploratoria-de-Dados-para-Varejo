import sqlite3 #banco de dados sqlite3
import pandas as pd
from faker import Faker
import random

#Criando automaticamente o Banco de Dados
conn = sqlite3.connect('Banco de Dados')
cursor = conn.cursor() #Canal de comunicação com o cursor

# Criar uma tabela no banco de dados, caso ainda não exista
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
)
''')

# Inicializar o Faker
fake = Faker()

# Lista de cursos fictícios
cursos = ['Sistemas de Informação', 'Engenharia de Software', 'Ciência da Computação', 'Administração']

# Inserir 20 alunos aleatórios no banco de dados
for _ in range(20):
    nome = fake.name()
    idade = random.randint(18, 30)
    curso = random.choice(cursos)
    
    cursor.execute('''
    INSERT INTO alunos (nome, idade, curso)
    VALUES (?, ?, ?)
    ''', (nome, idade, curso))

# Salvar (commit) as alterações
conn.commit()

# Consultar e exibir os registros inseridos
query1 = 'SELECT * FROM alunos'
cursor.execute(query1) #executa
alunos = cursor.fetchall() #fetchall servve para visualizar o resultado 
print(alunos) #executa uma lista com todos os alunos

for aluno in alunos:
    print(aluno)

#Conseguir os nomes das colunas (perceba que funciona visto que cursor já se refere especificamente ao nosso banco de dados)
nomes_colunas = [description[0] for description in cursor.description]
print(nomes_colunas)

#Visualizando a media
query2 = 'SELECT AVG(idade) FROM alunos'
cursor.execute(query2)

print('\n Média Idades:')
print(cursor.fetchall())
print('\n')

#Serve para uma média de CADA item especifico, porem nesse caso cada aluno tem apenas 1 valor (idade)
query3 = 'SELECT AVG(idade) FROM alunos GROUP BY curso'
cursor.execute(query3)

print('\n Média Idades 2:')
print(cursor.fetchall())
print('\n')

#Filtrando o Banco de dados (WHERE), pode ser usado para =, >, < e etc... 
query4 = '''SELECT AVG(idade)
            FROM alunos
            WHERE curso = 'Sistemas de Informação'
            GROUP BY curso'''
cursor.execute(query4)

print('\n Média Idades em S.I:')
print(cursor.fetchall())
print('\n')

#OBS: HAVING é uma clausula para filtrar APÓS a ordem de execução ocorrer: A cláusula HAVING em SQL é usada para filtrar resultados 
# após o uso da cláusula GROUP BY. 
# Ela funciona de maneira semelhante à cláusula WHERE, mas enquanto WHERE é aplicada antes da agregação (para filtrar linhas individuais), 
# a cláusula HAVING é aplicada após a agregação, ou seja, para filtrar grupos de resultados criados pelo GROUP BY

#OBS2: é possivel apenas importar como uma variavel o fetchall, transformando em uma lista pandas e aplicar SQL nelas
df = pd.DataFrame(alunos, columns= ['id','nome','idade','curso'])
print('\n Lista em Pandas:')
print(df.head())
print('\n')

MediadeIdadePorCurso = df.groupby('curso')['idade'].mean()
print('\n Media de Idade por Curso:')
print(MediadeIdadePorCurso)


# Fechar a conexão (IMPORTANTE)
conn.close()