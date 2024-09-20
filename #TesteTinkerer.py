#TesteTinkerer

import tkinter as tk
from tkinter import ttk, scrolledtext
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import numpy as np

# Carregar dataset
df = pd.read_csv("dataset.csv")
df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format= '%d/%m/%Y')
df['Ano'] = df['Data_Pedido'].dt.year
df['Mês'] = df['Data_Pedido'].dt.month

CidadesOS = df[df['Categoria'] == 'Office Supplies']

# Funções de perguntas
def visualizar_dados_finais():
    print(df)
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, str(df.head())  

def pergunta_1():
    CidadeMaisVendas = CidadesOS.groupby('Cidade')['Valor_Venda'].sum().idxmax()
    print(f'Cidade com maior valor de venda de produtos da categoria Office Supplies: {CidadeMaisVendas}')

def pergunta_2():
    
    Datas_e_Vendas = df.groupby('Data_Pedido')['Valor_Venda'].sum()
    print(Datas_e_Vendas)

    #Criação do gráfico de barras
    plt.figure(figsize=(18,9))

    Datas_e_Vendas.plot(x = 'Data_Pedido', y = 'Valor_Vendas', color= 'skyblue')

    plt.title('Total de Vendas por Data de Pedido')

    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()  # Ajusta o layout para que os rótulos não se sobreponham
    plt.show()

def pergunta_3():
    Vendas_Por_Estado = df.groupby('Estado')['Valor_Venda'].sum()
    print(f' Vendas por estado: \n {Vendas_Por_Estado}')

    plt.figure(figsize= (18, 9))
    Vendas_Por_Estado.plot(kind = 'bar', x = 'Estado', y = 'Valor_Vendas', color= 'green')
    plt.title('Total de vendas por estado')

    plt.tight_layout()
    plt.xticks(rotation=75, ha='right')
    plt.show()

def pergunta_4():
    print(CidadesOS.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).head(10))
    top10Cidades = CidadesOS.groupby('Cidade')['Valor_Venda'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize= (18, 9))
    top10Cidades.plot(kind = 'bar', x = 'Cidade', y = 'Valor_Vendas', color= 'green')
    plt.title('10 Cidades com maior total de vendas')

    plt.tight_layout()
    plt.xticks(rotation=75, ha='right')
    plt.show()

def pergunta_5():
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
    plt.show()

def pergunta_6():
    df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format= '%d/%m/%Y') #Transformando a coluna "Data_Pedido" para um formato real de data
    df['Ano'] = df['Data_Pedido'].dt.year #Adicionando uma nova coluna

    print(df)

    Vendas_Por_Segmento_e_Ano = df.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()
    print(f'\n Aqui estão as Vendas por segmento e por ano: \n{Vendas_Por_Segmento_e_Ano}')

def pergunta_7():
    QuantidadeQueRecebe15PorCento = df[df['Valor_Venda'] > 1000].shape[0]
    print(f'Quantidade de vendas que receberiam 15% de desconto: {QuantidadeQueRecebe15PorCento}')

def pergunta_8():
    df['Valor_Venda_Com_Desconto_15%'] = df['Valor_Venda'].where(df['Valor_Venda'] <= 1000, df['Valor_Venda'] * 0.85) #uma maneira
    #df['Valor_Venda_Com_Desconto_15%'] = df['Valor_Venda'].apply(lambda x: x * 0.85 if x > 1000 else x) #outra maneira

    #Descontos aplicados
    print(df[df['Valor_Venda'] > 1000])

    #Conseguir a media entre as duas colunas

    media = df['Valor_Venda'].mean()
    media2 = df['Valor_Venda_Com_Desconto_15%'].mean()

    print(f'\nA média dos valores venda sem desconto é: {media}\n A média dos valores venda com desconto é {media2}')

def pergunta_9():
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

def pergunta_10():
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
        plt.text(top12Subcategorias['Valor_Venda'].max() * 1.05, i * 4,  f'Total {categoria}: R$ {total_vendas:,.2f}', fontsize=12, color='black')

    plt.tight_layout()

    plt.show()

#Função principal que será chamada ao selecionar uma pergunta
def selecionar_pergunta(pergunta):
    if pergunta == 1:
        pergunta_1()
    elif pergunta == 2:
        pergunta_2()
    elif pergunta == 3:
        pergunta_3()
    elif pergunta == 4:
        pergunta_4()
    elif pergunta == 5:
        pergunta_5()
    elif pergunta == 6:
        pergunta_6()
    elif pergunta == 7:
        pergunta_7()
    elif pergunta == 8:
        pergunta_8()
    elif pergunta == 9:
        pergunta_9()
    elif pergunta == 10:
        pergunta_10()
    else:
        print("Pergunta não reconhecida")

#UI

def criar_ui():
    global janela, texto_resultado
    janela = tk.Tk()
    janela.title("Projeto de Análise de Dados")

    # Aumentar o tamanho da janela
    janela.geometry("800x600")

    frame = ttk.Frame(janela)
    frame.pack(pady=20)

    # Botão para visualizar dados finais
    btn_dados_finais = ttk.Button(frame, text="Visualizar Dados", command=visualizar_dados_finais)
    btn_dados_finais.pack(pady=10)

    # Label para escolha da pergunta
    label = ttk.Label(frame, text="Escolha uma pergunta:")
    label.pack(pady=5)

    # Dropdown de perguntas
    perguntas = list(range(1, 11))  # Perguntas de 1 a 10
    perguntas_str = [f"Pergunta {i}" for i in perguntas]

    combo_perguntas = ttk.Combobox(frame, values=perguntas_str, state="readonly")
    combo_perguntas.pack(pady=10)

    # Função chamada ao selecionar uma pergunta
    def callback(event):
        indice = combo_perguntas.current() + 1
        selecionar_pergunta(indice)

    combo_perguntas.bind("<<ComboboxSelected>>", callback)

    # Caixa de texto para exibir o resultado
    texto_resultado = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=80, height=20, font=("Arial", 10))
    texto_resultado.pack(pady=20)

    janela.mainloop()

# Inicializar a UI
criar_ui()