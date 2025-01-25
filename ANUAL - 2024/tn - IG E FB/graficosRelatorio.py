import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates
import csv

def formataNumero(numero):
    numero_formatado = '{:,}'.format(numero).replace(',', '.')
    return numero_formatado

def fixacao(atual, anterior):
    taxa = (atual-anterior)/abs(atual)
    if taxa > 0:
        return f'{str(round((taxa*100),2)).replace('.', ',')}%'
    return f'{str(round((taxa*100),2)).replace('.', ',')}%'

def crescimento(atual, antigo):
    taxa = ((atual - antigo) / abs(antigo))
    if taxa > 0:
        return f'+{str(round((taxa*100),2)).replace('.', ',')}%'
    return f'{str(round((taxa*100),2)).replace('.', ',')}%'

# def primeirosElementos(string):
#     # Encontra a posição do primeiro '.'
#     dot_index = string.find('.')
    
#     # Se não houver '.', retorna a string inteira e 0 como o número de elementos após o '.'
#     if dot_index == -1:
#         return string, 0
    
#     # Retorna a parte da string antes do primeiro '.' 
#     before_dot = string[:dot_index]
    
#     return before_dot

def primeirosElementos(numero):
    
    # Verifica se o número é menor que 1000
    if numero < 1000:
        # Retorna apenas a parte inteira do número
        return str(numero)
    
    string = formataNumero(numero)
    # Encontra a posição do primeiro '.'
    dot_index = string.find('.')
    
    # Se não houver '.', retorna a string inteira e 0 como o número de elementos após o '.'
    if dot_index == -1:
        return string, 0
    
    # Retorna a parte da string antes do primeiro '.' 
    before_dot = string[:dot_index]
    after_dot = string[dot_index+1:dot_index+3]  # Removendo o ponto decimal e incluindo dois dígitos após o ponto
    # print(string[dot_index+2])
    # print(string[dot_index+1:dot_index+3])
    # Convertendo a parte depois do '.' em uma lista para poder modificá-la
    after_dot_list = list(after_dot)
    
    if int(after_dot_list[1]) >= 6:
        after_dot_list[0] = str(int(after_dot_list[0]) + 1)
    
    # Convertendo a lista de volta para uma string
    after_dot_modified = "".join(after_dot_list)
    
    if after_dot_modified[0] == '0':
        return before_dot
    
    return before_dot + ',' + after_dot_modified[0]

def contaElementos(primeirosElementos):
    # Remove os pontos da string
    string_without_dots = primeirosElementos.replace('.', '')
    # Conta a quantidade de elementos na string sem os pontos
    element_count = len(string_without_dots)
    return element_count

def extensso(contaElementos):
    # if contaElementos == 2:
    #     texto = ''
    # elif contaElementos == 3:
    #     texto = ''
    if contaElementos >=4 and contaElementos<=6:
        texto = 'mil'
    elif contaElementos >=7 and contaElementos<=9:
        texto = 'milhões'
    else:
        texto = ''
        pass
    return texto

def extensso2(contaElementos):
    # if contaElementos == 2:
    #     texto = ''
    # elif contaElementos == 3:
    #     texto = ''
    if contaElementos >=4 and contaElementos<=6:
        texto = 'mil'
    elif contaElementos >=7 and contaElementos<=9:
        texto = 'milhões'
    else:
        texto = ''
        pass
    return texto

def numeroPorExtensso(numero):
    return f"{primeirosElementos((numero))} {extensso(contaElementos(formataNumero(numero)))}"

def numeroPorExtensso2(numero):
    return f"{primeirosElementos((numero))} {extensso2(contaElementos(formataNumero(numero)))}"

path_aliss = 'aliss'
path_Usuarios = 'aliss'
# path_Usuarios = 'usuario'


import os
import numpy as np
import matplotlib.pyplot as plt

def gerar_grafico_comparativo(lista_2023, lista_2024, titulo, ylabel, caminho_salvamento, cor_2023, cor_2024):
    """
    Gera um gráfico comparativo entre os dados de 2023 e 2024.
    
    :param lista_2023: Lista de valores para o ano de 2023 (12 elementos).
    :param lista_2024: Lista de valores para o ano de 2024 (12 elementos).
    :param titulo: Título do gráfico.
    :param ylabel: Rótulo do eixo Y.
    :param caminho_salvamento: Caminho completo para salvar o arquivo do gráfico.
    :param cor_2023: Cor das barras para 2023.
    :param cor_2024: Cor das barras para 2024.
    """
    # Verifica se ambas as listas têm exatamente 12 elementos
    if len(lista_2023) != 12 or len(lista_2024) != 12:
        raise ValueError("Ambas as listas devem conter exatamente 12 elementos.")

    # Nome dos meses
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    # Dados para o gráfico
    x = np.arange(12)  # Posição das barras para 12 meses
    width = 0.4  # Largura das barras

    fig, ax = plt.subplots(figsize=(12, 6))

    # Barras para o ano de 2023
    bars1 = ax.bar(x - width/2, lista_2023, width, label='2023', color=cor_2023, edgecolor='black')
    # Barras para o ano de 2024
    bars2 = ax.bar(x + width/2, lista_2024, width, label='2024', color=cor_2024, edgecolor='black')

    # Adiciona os valores no topo das barras
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, f'{height:,.0f}', ha='center', va='bottom', fontsize=8)

    # Adiciona os meses como rótulos do eixo X
    ax.set_xticks(x)
    ax.set_xticklabels(meses)

    # Configurações do gráfico
    ax.set_title(titulo, fontsize=14)
    ax.set_ylabel(ylabel)
    ax.set_xlabel('Meses')
    ax.legend()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Garante que o diretório de salvamento exista
    diretorio = os.path.dirname(caminho_salvamento)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Salva o gráfico no caminho especificado
    plt.tight_layout()
    plt.savefig(caminho_salvamento, bbox_inches="tight")
    plt.close()

# Funções específicas para cada gráfico do Instagram
def seguidorIG(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/seguidoresIG.png"
    gerar_grafico_comparativo(
        lista_2023, lista_2024,
        titulo='Comparativo Mensal de Seguidores no Instagram',
        ylabel='Quantidade de Seguidores',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#FCAF45',
        cor_2024='#E1306C'
    )
    return caminho_salvamento

def visitaIG(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visitasIG.png"
    gerar_grafico_comparativo(
        lista_2023, lista_2024,
        titulo='Comparativo Mensal de Visitas no Instagram',
        ylabel='Quantidade de Visitas',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#5851DB',
        cor_2024='#E1306C'
    )
    return caminho_salvamento

def alcanceIG(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/alcanceIG.png"
    gerar_grafico_comparativo(
        lista_2023, lista_2024,
        titulo='Comparativo Mensal de Alcance no Instagram',
        ylabel='Quantidade de Alcance',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#FD1D1D',
        cor_2024='#E1306C'
    )
    return caminho_salvamento

def visualizacoesIG(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visualizacoesIG.png"
    gerar_grafico_comparativo(
        lista_2023, lista_2024,
        titulo='Comparativo Mensal de Visualizações no Instagram',
        ylabel='Quantidade de Visualizações',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#833AB4',
        cor_2024='#E1306C'
    )
    return caminho_salvamento

# Funções específicas para cada gráfico com caminhos diretos
def seguidorFB(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/seguidoresFB.png"
    gerar_grafico_comparativo(
        lista_2023, lista_2024,
        titulo='Comparativo Mensal de Seguidores no Facebook',
        ylabel='Quantidade de Seguidores',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#c4a667',
        cor_2024='#3b5998'
    )
    return caminho_salvamento

def visitaFB(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visitasFB.png"
    gerar_grafico_comparativo(
        lista_2023, lista_2024,
        titulo='Comparativo Mensal de Visitas no Facebook',
        ylabel='Quantidade de Visitas',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#5851DB',
        cor_2024='#3b5998'
    )
    return caminho_salvamento

def alcanceFB(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/alcanceFB.png"
    gerar_grafico_comparativo(
        lista_2023, lista_2024,
        titulo='Comparativo Mensal de Alcance no Facebook',
        ylabel='Quantidade de Alcance',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#5874af',
        cor_2024='#3b5998'
    )
    return caminho_salvamento

def visualizacoesFB(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visualizacoesFB.png"
    gerar_grafico_comparativo(
        lista_2023, lista_2024,
        titulo='Comparativo Mensal de Visualizações no Facebook',
        ylabel='Quantidade de Visualizações',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#054f77',
        cor_2024='#3b5998'
    )
    return caminho_salvamento

def gerar_grafico_comparativo_ANUAL(total_2023, total_2024, titulo, ylabel, caminho_salvamento, cor_2023, cor_2024):
    """
    Gera um gráfico comparativo entre os totais de 2023 e 2024.
    
    :param total_2023: Valor total para o ano de 2023.
    :param total_2024: Valor total para o ano de 2024.
    :param titulo: Título do gráfico.
    :param ylabel: Rótulo do eixo Y.
    :param caminho_salvamento: Caminho completo para salvar o arquivo do gráfico.
    :param cor_2023: Cor da barra para 2023.
    :param cor_2024: Cor da barra para 2024.
    """
    
    # Nome dos anos
    anos = ['2023', '2024']
    
    # Valores para o gráfico
    valores = [total_2023, total_2024]
    x = np.arange(len(anos))  # Posições das barras

    fig, ax = plt.subplots(figsize=(8, 6))

    # Barras
    bars = ax.bar(x, valores, color=[cor_2023, cor_2024], edgecolor='black', width=0.6)

    # Adiciona os valores no topo das barras
    for bar, value in zip(bars, valores):
        if value > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, value + 0.5, f'{value:,.0f}', ha='center', va='bottom', fontsize=10)

    # Adiciona os anos como rótulos do eixo X
    ax.set_xticks(x)
    ax.set_xticklabels(anos)

    # Configurações do gráfico
    ax.set_title(titulo, fontsize=14)
    ax.set_ylabel(ylabel)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Garante que o diretório de salvamento exista
    diretorio = os.path.dirname(caminho_salvamento)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Salva o gráfico no caminho especificado
    plt.tight_layout()
    plt.savefig(caminho_salvamento, bbox_inches="tight")
    plt.close()

# Funções específicas para cada gráfico do Instagram
def seguidorIG_ANUAL(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/seguidoresIG_ANUAL.png"
    gerar_grafico_comparativo_ANUAL(
        lista_2023, lista_2024,
        titulo='Comparativo Anual de Seguidores no Instagram',
        ylabel='Seguidores',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#FCAF45',
        cor_2024='#E1306C'
    )
    return caminho_salvamento

def visitaIG_ANUAL(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visitasIG_ANUAL.png"
    gerar_grafico_comparativo_ANUAL(
        lista_2023, lista_2024,
        titulo='Comparativo Anual de Visitas no Instagram',
        ylabel='Visitas',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#5851DB',
        cor_2024='#E1306C'
    )
    return caminho_salvamento

def alcanceIG_ANUAL(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/alcanceIG_ANUAL.png"
    gerar_grafico_comparativo_ANUAL(
        lista_2023, lista_2024,
        titulo='Comparativo Anual de Alcance no Instagram',
        ylabel='Alcance',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#FD1D1D',
        cor_2024='#E1306C'
    )
    return caminho_salvamento

def visualizacoesIG_ANUAL(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visualizacoesIG_ANUAL.png"
    gerar_grafico_comparativo_ANUAL(
        lista_2023, lista_2024,
        titulo='Comparativo Anual de Visualizações no Instagram',
        ylabel='Visualizações',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#833AB4',
        cor_2024='#E1306C'
    )
    return caminho_salvamento

# Funções específicas para cada gráfico com caminhos diretos
def seguidorFB_ANUAL(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/seguidoresFB_ANUAL.png"
    gerar_grafico_comparativo_ANUAL(
        lista_2023, lista_2024,
        titulo='Comparativo Anual de Seguidores no Facebook',
        ylabel='Seguidores',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#c4a667',
        cor_2024='#3b5998'
    )
    return caminho_salvamento

def visitaFB_ANUAL(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visitasFB_ANUAL.png"
    gerar_grafico_comparativo_ANUAL(
        lista_2023, lista_2024,
        titulo='Comparativo Anual de Visitas no Facebook',
        ylabel='Visitas',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#5851DB',
        cor_2024='#3b5998'
    )
    return caminho_salvamento

def alcanceFB_ANUAL(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/alcanceFB_ANUAL.png"
    gerar_grafico_comparativo_ANUAL(
        lista_2023, lista_2024,
        titulo='Comparativo Anual de Alcance no Facebook',
        ylabel='Alcance',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#5874af',
        cor_2024='#3b5998'
    )
    return caminho_salvamento

def visualizacoesFB_ANUAL(lista_2023, lista_2024):
    caminho_salvamento = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visualizacoesFB_ANUAL.png"
    gerar_grafico_comparativo_ANUAL(
        lista_2023, lista_2024,
        titulo='Comparativo Anual de Visualizações no Facebook',
        ylabel='Visualizações',
        caminho_salvamento=caminho_salvamento,
        cor_2023='#054f77',
        cor_2024='#3b5998'
    )
    return caminho_salvamento   
