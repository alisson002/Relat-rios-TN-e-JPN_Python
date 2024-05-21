import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
from datetime import datetime
import datetime
import matplotlib.dates as mdates
import csv

def ultimo_sabado():
    hoje = datetime.date.today()
    dia_da_semana = hoje.weekday()  # Retorna um número de 0 (segunda-feira) a 6 (domingo)
    if dia_da_semana == 0: #segunda
        dias_para_subtrair = (dia_da_semana + 2) % 7  # Dias a subtrair para chegar ao último sabado
    elif dia_da_semana == 1: #terça
        dias_para_subtrair = (dia_da_semana + 2) % 7  # Dias a subtrair para chegar ao último sabado
    ultimo_domingo = hoje - datetime.timedelta(days=dias_para_subtrair)
    return ultimo_domingo

def penultimo_domingo():
    hoje = datetime.date.today()
    dia_da_semana = hoje.weekday()  # Retorna um número de 0 (segunda-feira) a 6 (domingo)
    if dia_da_semana == 0: #segunda
        dias_para_subtrair = (dia_da_semana + 8) % 7  # Dias a subtrair para chegar ao último sabado
    elif dia_da_semana == 1: #terça
        dias_para_subtrair = (dia_da_semana + 8) % 7  # Dias a subtrair para chegar ao último sabado
    ultimo_domingo = hoje - datetime.timedelta(days=dias_para_subtrair)
    penultimo_domingo = ultimo_domingo - datetime.timedelta(days=7)
    return penultimo_domingo

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

def numeroPorExtensso(numero):
    return f"{primeirosElementos((numero))} {extensso(contaElementos(formataNumero(numero)))}"

path_aliss = 'aliss'
path_Usuarios = 'aliss'

def origemPortal():

    '''
    LINK: https://analytics.google.com/

    https://analytics.google.com/analytics/web/#/p308444970/reports/explorer?params=_u..nav%3Dmaui&r=lifecycle-traffic-acquisition-v2&ruid=lifecycle-traffic-acquisition-v2,life-cycle,acquisition&collectionId=life-cycle

    CAMINHO: barra lateral > Relatórios > Aquisição (dropdown) > Aquisição de tráfego

    Ações: Grupo de canais padrão da sessão (dropdown do gráfico) >>> Origem / mídia da sessão

    Compartilhar esse relatorio (icone) >>> Fazer o download do arquivo >>> Fazer download do CSV

    '''

    # Carregar o DataFrame a partir do CSV
    df = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\origem.csv', skiprows=9)

    # Função para agrupar os usuários por mídia
    def agrupar_por_midia(row):
        if 'facebook' in row['Origem / mídia da sessão']:
            return 'facebook'
        elif 'instagram' in row['Origem / mídia da sessão']:
            return 'instagram'
        elif 'google' in row['Origem / mídia da sessão']:
            return 'google'
        elif 'yahoo' in row['Origem / mídia da sessão']:
            return 'yahoo'
        elif 'bing' in row['Origem / mídia da sessão']:
            return 'bing'
        elif 't.co' in row['Origem / mídia da sessão']:
            return 'twitter'
        elif '(direct) / (none)' in row['Origem / mídia da sessão']:
            return 'Acesso Direto'
        else:
            return 'outras'

    df['Midia'] = df.apply(agrupar_por_midia, axis=1)

    # Agrupar e somar usuários por mídia
    agrupado = df.groupby('Midia')['Usuários'].sum().reset_index()

    # Ordenar as barras da maior para a menor
    agrupado = agrupado.sort_values(by='Usuários', ascending=False)

    # Cores correspondentes às mídias

    cores = {
        'Acesso Direto': '#FF4D02',
        'google': '#F4B400',
        'outras': '#000',
        'facebook': '#bc2a8d',
        'instagram': '#1877f2',
        'twitter': '#1DA1F2',
        'bing': '#50bf40',
        'yahoo': '#008373'
    }

    # Inicializar o estilo do Seaborn
    sns.set_theme()

    # Criar o gráfico de barras horizontais com Seaborn e Matplotlib
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Usuários', y='Midia', data=agrupado, palette=cores.values(), edgecolor='black', width=0.9)

    # Adicionar rótulos e título
    plt.xlabel('Número de Usuários')
    plt.ylabel('Mídia')
    plt.title('Número de Usuários por Mídia de Origem (Ordenado)')

    # Exibir o gráfico
    #plt.show()

    origem_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/origem.png"
    plt.savefig(origem_plot_path, bbox_inches="tight")
    
origem_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/origem.png"

def top10():
    '''
    LINK: https://analytics.google.com/

    https://analytics.google.com/analytics/web/#/p308444970/reports/explorer?params=_u..nav%3Dmaui&r=all-pages-and-screens&ruid=all-pages-and-screens,life-cycle,engagement&collectionId=life-cycle

    CAMINHO: barra lateral > Relatórios > Engajamento (dropdown) > Páginas e telas

    Ações: Compartilhar esse relatorio (icone) >>> Fazer o download do arquivo >>> Fazer download do CSV

    '''
    # Ler o DataFrame diretamente do arquivo CSV, começando da linha 10
    df = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\top10.csv', skiprows=9)

    # Filtrar apenas as linhas que representam notícias
    df = df[df['Caminho da página e classe da tela'].str.contains('-')]

    # Ordenar o DataFrame pelas visualizações e pegar as 10 primeiras
    df = df.sort_values(by='Visualizações', ascending=False).head(10)

    # Extrair os nomes das notícias sem caracteres especiais
    df['Noticia'] = df['Caminho da página e classe da tela'].apply(lambda x: x.split('/')[-2].replace('-', ' ')).str.title()

    df['Texto'] = df['Noticia'] + ' - ' + df['Visualizações'].astype(str)

    # Criar o gráfico de barras horizontais com o tema do Seaborn
    sns.set_theme()
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Visualizações', y='Noticia', data=df, hue='Noticia', palette='summer_r')

    # # Adicionar os rótulos (números de visualizações) diretamente nas barras
    # ax.bar_label(ax.containers[0], fmt='%g', label_type='edge', fontsize=8, color='black')

    # Adicionar os rótulos (números de visualizações e nomes das notícias) diretamente nas barras
    for i, (value, name) in enumerate(zip(df['Visualizações'], df['Noticia'])):
        ax.text(int(df['Visualizações'][3])*0.006, i, f'{name} - {value}', va='center', ha='left', fontsize=9)


    # Modificar os ticks do eixo Y para números de 1 a 10
    ax.set_yticks(range(10))
    ax.set_yticklabels(range(1, 11))

    # # Adicionar os nomes das notícias no início das barras
    # for bar, label in zip(bars, df['Texto']):
    #     plt.text(0, bar.get_y() + bar.get_height() / 2, label, va='center', ha='left', fontsize=8)


    plt.xlabel('Visualizações')
    plt.ylabel('Posição')
    plt.title('Top 10 Notícias Mais Vistas')

    plt.tight_layout()
    #plt.show()
    top10_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/top10.png"
    plt.savefig(top10_plot_path, bbox_inches="tight")
    
top10_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/top10.png"

def top15():
    '''
    LINK: https://analytics.google.com/

    https://analytics.google.com/analytics/web/#/p308444970/reports/dashboard?params=_u..nav%3Dmaui%26_u.comparisonOption%3Ddisabled%26_u.date00%3D20231101%26_u.date01%3D20231130&r=lifecycle-acquisition-overview&ruid=lifecycle-acquisition-overview,life-cycle,acquisition&collectionId=life-cycle

    CAMINHO: barra lateral > Relatórios > Aquisição (dropdown) > Visão geral

    Ações: Grupo de canais padrão da sessão (dropdown do gráfico) >>> Origem / mídia da sessão

    Compartilhar esse relatorio (icone) >>> Fazer o download do arquivo >>> Fazer download do CSV

    '''

    # Nome do arquivo CSV
    nome_arquivo = fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TN\top15.csv'

    # Lê o arquivo CSV, ignorando linhas com problemas
    #df = pd.read_csv(nome_arquivo, encoding='utf-8', skiprows=8)

    import csv

    def encontrar_frase_em_csv(nome_arquivo, frase_procurada):
        try:
            with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)
                
                for numero_linha, linha in enumerate(leitor_csv, start=1):
                    if frase_procurada in linha:
                        return numero_linha

            # Se a frase não for encontrada em nenhuma linha
            return -1

        except FileNotFoundError:
            print(f'O arquivo {nome_arquivo} não foi encontrado.')
            return -1

    # Substitua 'Impressões orgânicas da Pesquisa Google' pela frase que você está procurando
    frase_procurada = 'Impressões orgânicas da Pesquisa Google'
    nome_arquivo = fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\top15.csv'

    numero_linha_encontrada = encontrar_frase_em_csv(nome_arquivo, frase_procurada)

    # Ler o DataFrame diretamente do arquivo CSV, começando da linha 10
    df = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\top15.csv', skiprows = numero_linha_encontrada-1)

    # Filtrar apenas as linhas que representam notícias
    #df = df[df['Página de destino + string de consulta'].str.contains('-')& ~df['Página de destino + string de consulta'].str.contains('/quem-somos/')]

    excluded_keywords = ['/quem-somos/', '/plantao-de-noticias/','/colunas/','/alex-medeiros/']
    df = df[df['Página de destino + string de consulta'].str.contains('-') & ~df['Página de destino + string de consulta'].str.contains('|'.join(excluded_keywords))]

    df['Impressões orgânicas da Pesquisa Google'] = pd.to_numeric(df['Impressões orgânicas da Pesquisa Google'], errors='coerce')

    # Ordenar o DataFrame pelas visualizações e pegar as 10 primeiras
    df = df.sort_values(by='Impressões orgânicas da Pesquisa Google', ascending=False).head(15)

    # Extrair os nomes das notícias sem caracteres especiais
    df['Noticia'] = df['Página de destino + string de consulta'].apply(lambda x: x.split('/')[-2].replace('-', ' ')).str.title()

    # Criar uma coluna combinada de Noticia e Visualizações
    df['Texto'] = df['Noticia'] + ' - ' + df['Impressões orgânicas da Pesquisa Google'].astype(str)

    # Criar o gráfico de barras horizontais com o tema do Seaborn
    sns.set_theme()
    plt.figure(figsize=(10, 6))
    bars = plt.barh(range(1, 16), df['Impressões orgânicas da Pesquisa Google'], color=sns.color_palette('Spectral', n_colors=15))

    # Adicionar os nomes das notícias no início das barras
    for bar, label in zip(bars, df['Texto']):
        plt.text(int(df['Impressões orgânicas da Pesquisa Google'][0])*0.006, bar.get_y() + bar.get_height() / 2, label, va='center', ha='left', fontsize=9)

    plt.xlabel('Impressões')
    plt.title('Top 15 Notícias Mais Pesquisadas no Google')
    plt.yticks(range(1, 16), range(1, 16))  # Numerar as barras no eixo Y de 1 a 10
    plt.ylabel('Posição')
    plt.gca().invert_yaxis()  # Inverter a ordem para exibir a mais vista no topo
    top15_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/top15.png"
    plt.savefig(top15_plot_path, bbox_inches="tight")

top15_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/top15.png"

def top15cliques():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    '''
    LINK: https://analytics.google.com/

    https://analytics.google.com/analytics/web/#/p308444970/reports/dashboard?params=_u..nav%3Dmaui%26_u.comparisonOption%3Ddisabled%26_u.date00%3D20231101%26_u.date01%3D20231130&r=lifecycle-acquisition-overview&ruid=lifecycle-acquisition-overview,life-cycle,acquisition&collectionId=life-cycle

    CAMINHO: barra lateral > Relatórios > Aquisição (dropdown) > Visão geral

    Compartilhar esse relatorio (icone) >>> Fazer o download do arquivo >>> Fazer download do CSV

    '''

    # Nome do arquivo CSV
    nome_arquivo = fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TN\top15cliques.csv'

    # Lê o arquivo CSV, ignorando linhas com problemas
    #df = pd.read_csv(nome_arquivo, encoding='utf-8', skiprows=8)

    import csv

    def encontrar_frase_em_csv(nome_arquivo, frase_procurada):
        try:
            with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)
                
                for numero_linha, linha in enumerate(leitor_csv, start=1):
                    if frase_procurada in linha:
                        return numero_linha

            # Se a frase não for encontrada em nenhuma linha
            return -1

        except FileNotFoundError:
            print(f'O arquivo {nome_arquivo} não foi encontrado.')
            return -1

    # Substitua 'Cliques orgânicos da Pesquisa Google' pela frase que você está procurando
    frase_procurada = 'Cliques orgânicos da Pesquisa Google'
    nome_arquivo = fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TN\top15cliques.csv'

    numero_linha_encontrada = encontrar_frase_em_csv(nome_arquivo, frase_procurada)

    # Ler o DataFrame diretamente do arquivo CSV, começando da linha 10
    df = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\top15cliques.csv', skiprows = 9)

    # Filtrar apenas as linhas que representam notícias
    #df = df[df['Página de destino + string de consulta'].str.contains('-')& ~df['Página de destino + string de consulta'].str.contains('/quem-somos/')]

    excluded_keywords = ['/quem-somos/', '/plantao-de-noticias/','/colunas/','/alex-medeiros/']
    df = df[df['Página de destino + string de consulta'].str.contains('-') & ~df['Página de destino + string de consulta'].str.contains('|'.join(excluded_keywords))]

    df['Cliques orgânicos da Pesquisa Google'] = pd.to_numeric(df['Cliques orgânicos da Pesquisa Google'], errors='coerce')

    # Ordenar o DataFrame pelas visualizações e pegar as 10 primeiras
    df = df.sort_values(by='Cliques orgânicos da Pesquisa Google', ascending=False).head(15)

    # Extrair os nomes das notícias sem caracteres especiais
    df['Noticia'] = df['Página de destino + string de consulta'].apply(lambda x: x.split('/')[-2].replace('-', ' ')).str.title()

    # Criar uma coluna combinada de Noticia e Visualizações
    df['Texto'] = df['Noticia'] + ' - ' + df['Cliques orgânicos da Pesquisa Google'].astype(str)

    # Criar o gráfico de barras horizontais com o tema do Seaborn
    sns.set_theme()
    plt.figure(figsize=(10, 6))
    bars = plt.barh(range(1, 16), df['Cliques orgânicos da Pesquisa Google'], color=sns.color_palette('PuOr', n_colors=15))

    # Adicionar os nomes das notícias no início das barras
    for bar, label in zip(bars, df['Texto']):
        plt.text(int(df['Cliques orgânicos da Pesquisa Google'][1])*0.006, bar.get_y() + bar.get_height() / 2, label, va='center', ha='left', fontsize=8)

    plt.xlabel('Impressões')
    plt.title('Top 15 Notícias com mais cliques através de pesquisa no google')
    plt.yticks(range(1, 16), range(1, 16))  # Numerar as barras no eixo Y de 1 a 10
    plt.ylabel('Posição')
    plt.gca().invert_yaxis()  # Inverter a ordem para exibir a mais vista no topo
    top15cliques_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/top15cliques.png"
    plt.savefig(top15cliques_plot_path, bbox_inches="tight")

top15cliques_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/top15cliques.png"


def encontrar_frase_em_csv(nome_arquivo, frase_procurada):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            
            for numero_linha, linha in enumerate(leitor_csv, start=1):
                if frase_procurada in linha:
                    return numero_linha

        # Se a frase não for encontrada em nenhuma linha
        return -1

    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado.')
        return -1

def remover_ultima_linha(arquivo):
    dados = arquivo
    
    # Verificar se a última linha atende ao critério
    ultima_linha = dados.iloc[-1]
    if ultima_linha['Nº dia'] not in ['0030', '0029', '0028', '28', '29', '30']:
        # Se não atender ao critério, remover a última linha
        dados = dados.iloc[:-1]
    
    return dados

def transforma_int(arquivo):
    
    for i in range(len(arquivo.iloc[:,0])):
        arquivo.iloc[i,0] = int(arquivo.iloc[i,0])
    
    for i in range(len(arquivo.iloc[:,1])):
        arquivo.iloc[i,1] = int(arquivo.iloc[i,1])
    
    return arquivo

def visualizacoesUsuarios():

    # USUÁRIO ÚNICOS
    usuarios_unicos_final = encontrar_frase_em_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', 'Novos usuários')

    usuarios_unicos = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', skiprows=8, nrows=usuarios_unicos_final-12)

    usuarios_unicos = remover_ultima_linha(usuarios_unicos)
    usuarios_unicos = transforma_int(usuarios_unicos)

    usuarios_unicos['Nº dia'] = usuarios_unicos['Nº dia']+1


    # NOVOS USUÁRIOS
    novos_usuarios_final = encontrar_frase_em_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', 'Tempo médio de engajamento')

    novos_usuarios = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', skiprows=usuarios_unicos_final-1, nrows=novos_usuarios_final-21).dropna()

    novos_usuarios = remover_ultima_linha(novos_usuarios)
    novos_usuarios = transforma_int(novos_usuarios)

    novos_usuarios['Nº dia'] = novos_usuarios['Nº dia']+1


    # VISUALIZAÇÕES
    visualizacoes_inicio = encontrar_frase_em_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\visualizacoes.csv', 'Visualizações')
    visualizacoes_final = encontrar_frase_em_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\visualizacoes.csv', 'Contagem de eventos')

    visualizacoes = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\visualizacoes.csv', skiprows=visualizacoes_inicio-1, nrows=visualizacoes_final-44).dropna()

    visualizacoes = remover_ultima_linha(visualizacoes)
    visualizacoes = transforma_int(visualizacoes)

    visualizacoes['Nº dia'] = visualizacoes['Nº dia']+1


    # USUARIOS RECORRENTES
    recorrentes_inicio = encontrar_frase_em_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\novosRec.csv', 'Usuários recorrentes')
    recorrentes_final = encontrar_frase_em_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\novosRec.csv', 'Dia 1')

    usuarios_recorrentes = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\novosRec.csv', skiprows=recorrentes_inicio-1, nrows=8)

    usuarios_recorrentes = remover_ultima_linha(usuarios_recorrentes)
    usuarios_recorrentes = transforma_int(usuarios_recorrentes)

    usuarios_recorrentes['Nº dia'] = usuarios_recorrentes['Nº dia']+1
    #CORRIGIR ERRO COM OS RECORRENTES NÃO ESTA PEGANDO OS 7 APENAS 6

    # Configurando o tema do Seaborn
    sns.set_theme(style="whitegrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#EE7B12", "#355424", "#ED3013", "#9EC274"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Nº dia", y="Visualizações", data=visualizacoes, label="Visualizações", linewidth=2.5, color=cores[2])
    sns.lineplot(x="Nº dia", y="Usuários", data=usuarios_unicos, label="Usuários únicos", linewidth=2.5, color=cores[0])
    sns.lineplot(x="Nº dia", y="Novos usuários", data=novos_usuarios, label="Novos usuários", linewidth=2.5, color=cores[1])
    sns.lineplot(x="Nº dia", y="Usuários recorrentes", data=usuarios_recorrentes, label="Usuários recorrentes", linewidth=2.5, color=cores[3])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    #plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance | Visitas | Seguidores")
    plt.title("Dados semanais do portal")

    #plt.yticks([])

    plt.legend()

    # Exibindo o gráfico
    #plt.show()
    visualizacoesUsuarios_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visualizacoesUsuarios.png"
    plt.savefig(visualizacoesUsuarios_plot_path, bbox_inches="tight")

visualizacoesUsuarios_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visualizacoesUsuarios.png"

def visu_cumsum():
    
    # VISUALIZAÇÕES
    visualizacoes_inicio = encontrar_frase_em_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\visualizacoes.csv', 'Visualizações')
    visualizacoes_inicio_anterior = encontrar_frase_em_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\visualizacoes.csv', 'Visualizações')
    # visualizacoes_final = encontrar_frase_em_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\visualizacoes.csv', 'Contagem de eventos')

    # visualizacoes = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\visualizacoes.csv', skiprows=visualizacoes_inicio-1, nrows=visualizacoes_final-44).dropna()
    # visualizacoes = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\visualizacoes.csv', skiprows=visualizacoes_inicio-1, nrows=10).dropna()

    # SEMANA ANTERIOR
    visualizacoesANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\visualizacoes.csv', skiprows=visualizacoes_inicio_anterior-1, nrows=8)

    visualizacoesANTERIOR = remover_ultima_linha(visualizacoesANTERIOR)
    visualizacoesANTERIOR = transforma_int(visualizacoesANTERIOR)

    visualizacoesANTERIOR['Nº dia'] = visualizacoesANTERIOR['Nº dia']+1

    # SEMANA ANALISADA
    visualizacoes = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\visualizacoes.csv', skiprows=visualizacoes_inicio-1, nrows=8)

    visualizacoes = remover_ultima_linha(visualizacoes)
    visualizacoes = transforma_int(visualizacoes)

    visualizacoes['Nº dia'] = visualizacoes['Nº dia']+1

    # Configurando o tema do Seaborn
    sns.set_theme(style="whitegrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#ED3013", "#F79B8D"]

    visualizacoes_acumuladas = visualizacoes['Visualizações'].cumsum()

    visualizacoes_acumuladasANTERIOR = visualizacoesANTERIOR['Visualizações'].cumsum()

    # Plotando o gráfico de linhas
    sns.lineplot(x="Nº dia", y=visualizacoes_acumuladasANTERIOR, data=visualizacoesANTERIOR, label=f"Visualizações {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    sns.lineplot(x="Nº dia", y=visualizacoes_acumuladas, data=visualizacoes, label=f"Visualizações {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    # Adicionando os valores de cada ponto de visualizacoesANTERIOR
    for x, y, acumulado in zip(visualizacoesANTERIOR['Nº dia'], visualizacoesANTERIOR['Visualizações'], visualizacoes_acumuladasANTERIOR):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(visualizacoes['Nº dia'], visualizacoes['Visualizações'], visualizacoes_acumuladas):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))


    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    #plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance | Visitas | Seguidores")
    plt.title("Visualizações do portal ao longo da semana")

    #plt.yticks([])

    plt.legend()
    visu_cumsum_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visu_cumsum.png"
    plt.savefig(visu_cumsum_plot_path, bbox_inches="tight")

visu_cumsum_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visu_cumsum.png"

def usuUni_cumsum():
    # USUÁRIO ÚNICOS
    # usuarios_unicos_final = encontrar_frase_em_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', 'Novos usuários')

    # SEMANA ANTERIOR
    usuarios_unicosANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\uniNovos.csv', skiprows=8, nrows=8)

    usuarios_unicosANTERIOR = remover_ultima_linha(usuarios_unicosANTERIOR)
    usuarios_unicosANTERIOR = transforma_int(usuarios_unicosANTERIOR)

    usuarios_unicosANTERIOR['Nº dia'] = usuarios_unicosANTERIOR['Nº dia']+1

    # SEMANA ANALISADA
    usuarios_unicos = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', skiprows=8, nrows=8)

    usuarios_unicos = remover_ultima_linha(usuarios_unicos)
    usuarios_unicos = transforma_int(usuarios_unicos)

    usuarios_unicos['Nº dia'] = usuarios_unicos['Nº dia']+1

    # Configurando o tema do Seaborn
    sns.set_theme(style="whitegrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#F6B679","#EE7B12"]

    usuarios_unicos_acumuladasANTERIOR = usuarios_unicosANTERIOR['Usuários'].cumsum()

    usuarios_unicos_acumuladas = usuarios_unicos['Usuários'].cumsum()

    # Plotando o gráfico de linhas
    sns.lineplot(x="Nº dia", y=usuarios_unicos_acumuladasANTERIOR, data=usuarios_unicosANTERIOR, label=F"Usuários únicos {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x="Nº dia", y=usuarios_unicos_acumuladas, data=usuarios_unicos, label=F"Usuários únicos  {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(usuarios_unicosANTERIOR['Nº dia'], usuarios_unicosANTERIOR['Usuários'], usuarios_unicos_acumuladasANTERIOR):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(usuarios_unicos['Nº dia'], usuarios_unicos['Usuários'], usuarios_unicos_acumuladas):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    #plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance | Visitas | Seguidores")
    plt.title("Usuários únicos do portal ao longo da semana")

    #plt.yticks([])

    plt.legend()

    # Exibindo o gráfico
    usuUni_cumsum_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/usuUni_cumsum.png"
    plt.savefig(usuUni_cumsum_plot_path, bbox_inches="tight")

usuUni_cumsum_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/usuUni_cumsum.png"

def newUsu_cumsum():
    # NOVOS USUÁRIOS
    #novos_usuarios_final = encontrar_frase_em_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', 'Tempo médio de engajamento')
    usuarios_unicos_final = encontrar_frase_em_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', 'Novos usuários')

    # SEMANA ANTERIOR
    novos_usuariosANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\uniNovos.csv', skiprows=usuarios_unicos_final-1, nrows=8).dropna()

    novos_usuariosANTERIOR = remover_ultima_linha(novos_usuariosANTERIOR)
    novos_usuariosANTERIOR = transforma_int(novos_usuariosANTERIOR)

    novos_usuariosANTERIOR['Nº dia'] = novos_usuariosANTERIOR['Nº dia']+1

    # SEMANA ANALISADA
    novos_usuarios = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\uniNovos.csv', skiprows=usuarios_unicos_final-1, nrows=8).dropna()

    novos_usuarios = remover_ultima_linha(novos_usuarios)
    novos_usuarios = transforma_int(novos_usuarios)

    novos_usuarios['Nº dia'] = novos_usuarios['Nº dia']+1

    # Configurando o tema do Seaborn
    sns.set_theme(style="whitegrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#639D43", "#355424"]

    novos_usuarios_acumuladasANTERIOR = novos_usuariosANTERIOR['Novos usuários'].cumsum()

    novos_usuarios_acumuladas = novos_usuarios['Novos usuários'].cumsum()

    # Plotando o gráfico de linhas
    sns.lineplot(x="Nº dia", y=novos_usuarios_acumuladasANTERIOR, data=novos_usuariosANTERIOR, label=F"Novos usuários {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x="Nº dia", y=novos_usuarios_acumuladas, data=novos_usuarios, label=F"Novos usuários {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')


    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(novos_usuariosANTERIOR['Nº dia'], novos_usuariosANTERIOR['Novos usuários'], novos_usuarios_acumuladasANTERIOR):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(novos_usuarios['Nº dia'], novos_usuarios['Novos usuários'], novos_usuarios_acumuladas):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))


    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    #plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance | Visitas | Seguidores")
    plt.title("Dados semanais do portal")

    #plt.yticks([])

    plt.legend()

    # Exibindo o gráfico
    newUsu_cumsum_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/newUsu_cumsum.png"
    plt.savefig(newUsu_cumsum_plot_path, bbox_inches="tight")

newUsu_cumsum_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/newUsu_cumsum.png"

def usuRec_cumsum():
    # USUARIOS RECORRENTES
    recorrentes_inicio = encontrar_frase_em_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\novosRec.csv', 'Usuários recorrentes')
    # recorrentes_final = encontrar_frase_em_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\novosRec.csv', 'Dia 1')

    # SEMANA ANTERIOR
    usuarios_recorrentesANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\novosRec.csv', skiprows=recorrentes_inicio-1, nrows=8)

    usuarios_recorrentesANTERIOR = remover_ultima_linha(usuarios_recorrentesANTERIOR)
    usuarios_recorrentesANTERIOR = transforma_int(usuarios_recorrentesANTERIOR)

    usuarios_recorrentesANTERIOR['Nº dia'] = usuarios_recorrentesANTERIOR['Nº dia']+1

    # SEMANA ANALISADA
    usuarios_recorrentes = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\novosRec.csv', skiprows=recorrentes_inicio-1, nrows=8)

    usuarios_recorrentes = remover_ultima_linha(usuarios_recorrentes)
    usuarios_recorrentes = transforma_int(usuarios_recorrentes)

    usuarios_recorrentes['Nº dia'] = usuarios_recorrentes['Nº dia']+1


    # Configurando o tema do Seaborn
    sns.set_theme(style="whitegrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#CDE0B8", "#9EC274"]

    usuarios_recorrentes_acumuladasANTERIOR = usuarios_recorrentesANTERIOR['Usuários recorrentes'].cumsum()

    usuarios_recorrentes_acumuladas = usuarios_recorrentes['Usuários recorrentes'].cumsum()

    sns.lineplot(x="Nº dia", y=usuarios_recorrentes_acumuladasANTERIOR, data=usuarios_recorrentesANTERIOR, label=F"Usuários recorrentes {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x="Nº dia", y=usuarios_recorrentes_acumuladas, data=usuarios_recorrentes, label=F"Usuários recorrentes {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')


    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(usuarios_recorrentesANTERIOR['Nº dia'], usuarios_recorrentesANTERIOR['Usuários recorrentes'], usuarios_recorrentes_acumuladasANTERIOR):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(usuarios_recorrentes['Nº dia'], usuarios_recorrentes['Usuários recorrentes'], usuarios_recorrentes_acumuladas):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    #plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance | Visitas | Seguidores")
    plt.title("Usuários recorrentes do portal ao longo da semana")

    #plt.yticks([])

    plt.legend()

    # Exibindo o gráfico
    usuRec_cumsum_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/usuRec_cumsum.png"
    plt.savefig(usuRec_cumsum_plot_path, bbox_inches="tight")

usuRec_cumsum_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/usuRec_cumsum.png"

def faixaEtaria():
    import pandas as pd
    '''
    LINK: https://analytics.google.com/

    VISUALIZAÇÕES POR FAIXA ETÁRIA

    https://analytics.google.com/analytics/web/#/analysis/p308444970/edit/SPUMRb6cSOur-ylh_X1_Qw

    CAMINHO: barra lateral > Analisar > 'visualizações por faixa etária'

    Ações: Exportar dados (icone de download - superior direito) >>> Planilhas google >>> nova guia >>> Import the data (batão)>>> Arquivo >>> Fazer download >>> Valores separados por vírgula (.csv)
    '''
    def transforma_int_coluna(arquivo):
        for i in range(len(arquivo.iloc[1,:])):
            arquivo.iloc[1,i] = int(arquivo.iloc[1,i])
        
        return arquivo

    visualizacoes_faixa_etaria = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\download.csv', skiprows=6, encoding='utf-8')


    visualizacoes_faixa_etaria = visualizacoes_faixa_etaria.iloc[0:2,1:-1]
    #visualizacoes_faixas_etarias_conhecidas = visualizacoes_faixa_etaria.iloc[1,2:-2]

    visualizacoes_faixa_etaria = transforma_int_coluna(visualizacoes_faixa_etaria)

    fe_1824 = visualizacoes_faixa_etaria['18-24'][1]
    fe_2534 = visualizacoes_faixa_etaria['25-34'][1]
    fe_3544 = visualizacoes_faixa_etaria['35-44'][1]
    fe_4554 = visualizacoes_faixa_etaria['45-54'][1]
    fe_5564 = visualizacoes_faixa_etaria['55-64'][1]
    fe_65 = visualizacoes_faixa_etaria['65+'][1]

    # Dados
    faixas_etarias = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    visualizacoes = [fe_1824, fe_2534, fe_3544, fe_4554, fe_5564, fe_65]

    # Criar um DataFrame com os dados
    import pandas as pd
    df = pd.DataFrame({'Faixa Etária': faixas_etarias, 'Visualizações': visualizacoes})

    # Configurar o estilo seaborn
    sns.set(style="whitegrid")

    # Criar o gráfico de barras com a paleta "magma"
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Faixa Etária', y='Visualizações', data=df, palette="magma")

    # Adicionar rótulos diretamente acima de cada barra
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                    textcoords='offset points')

    # Adicionar rótulos e título
    plt.xlabel('Faixa Etária')
    plt.ylabel('Visualizações')
    plt.title('Visualizações por Faixa Etária Conhecida')

    # Ajustar os rótulos do eixo Y para valores correspondentes
    #plt.yticks(range(0, max(visualizacoes)+100000, 200000))

    # Desativar a notação científica no eixo Y
    plt.ticklabel_format(axis='y', style='plain')

    # Mostrar o gráfico
    #plt.show()
    faixaEtaria_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/faixaEtaria.png"
    plt.savefig(faixaEtaria_plot_path, bbox_inches="tight")

faixaEtaria_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/faixaEtaria.png"

def faixaEtaria_desconhecidaAndTotal():
    import pandas as pd
    
    '''
    LINK: https://analytics.google.com/

    VISUALIZAÇÕES POR FAIXA ETÁRIA

    https://analytics.google.com/analytics/web/#/analysis/p308444970/edit/SPUMRb6cSOur-ylh_X1_Qw

    CAMINHO: barra lateral > Analisar > 'visualizações por faixa etária'

    Ações: Exportar dados (icone de download - superior direito) >>> Planilhas google >>> nova guia >>> Import the data (batão)>>> Arquivo >>> Fazer download >>> Valores separados por vírgula (.csv)

    '''
    def transforma_int_coluna(arquivo):
        for i in range(len(arquivo.iloc[1,:])):
            arquivo.iloc[1,i] = int(arquivo.iloc[1,i])
        
        return arquivo

    visualizacoes_faixa_etaria2 = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\download.csv', skiprows=6, encoding='utf-8')


    visualizacoes_faixa_etaria2 = visualizacoes_faixa_etaria2.iloc[0:2,1:-1]
    #visualizacoes_faixas_etarias_conhecidas = visualizacoes_faixa_etaria.iloc[1,2:-2]

    visualizacoes_faixa_etaria2 = transforma_int_coluna(visualizacoes_faixa_etaria2)


    fe_deconhecida = visualizacoes_faixa_etaria2['unknown'][1]
    fe_total = visualizacoes_faixa_etaria2['Totais'][1]


    # Dados
    faixas_etarias = ['Desconhecida', 'Total']
    visualizacoes = [fe_deconhecida, fe_total]

    # Criar um DataFrame com os dados
    import pandas as pd
    df = pd.DataFrame({'Faixa Etária': faixas_etarias, 'Visualizações': visualizacoes})

    # Configurar o estilo seaborn
    sns.set(style="whitegrid")

    # Criar o gráfico de barras com a paleta "magma"
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Faixa Etária', y='Visualizações', data=df, palette="magma")

    # Adicionar rótulos diretamente acima de cada barra
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 5),
                    textcoords='offset points')

    # Adicionar rótulos e título
    plt.xlabel('Faixa Etária')
    plt.ylabel('Visualizações')
    plt.title('Visualizações por Faixa Etária - Desconhecida e Total')

    # Ajustar os rótulos do eixo Y para valores correspondentes
    #plt.yticks(range(0, max(visualizacoes)+100000, 200000))

    # Desativar a notação científica no eixo Y
    plt.ticklabel_format(axis='y', style='plain')

    # Mostrar o gráfico
    #plt.show()
    faixaEtaria_desconhecidaAndTotal_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/faixaEtaria_desconhecidaAndTotal.png"
    plt.savefig(faixaEtaria_desconhecidaAndTotal_plot_path, bbox_inches="tight")
    
faixaEtaria_desconhecidaAndTotal_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/faixaEtaria_desconhecidaAndTotal.png"

def fePublico_FBIG():
    '''
    https://business.facebook.com

    https://business.facebook.com/latest/insights/people?asset_id=146958865328939&ad_account_id=23862053469140633&entity_type=FB_PAGE

    CAMINHO: Insights (barra lateral) >>> Público (menu lateral) >>> 

    Ações: Exportar (dropdown) >>> Exportar como csv
    '''

    idade = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows= 10, encoding='utf-16')

    idade2 = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows= 10, encoding='utf-16')

    idadeFB = idade2[0:6]

    idade['m_fb'] = idadeFB['Mulheres'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')
    idade['h_fb'] = idadeFB['Homens'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')

    idade3 = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows= 19, encoding='utf-16')

    idadeIG = idade3.iloc[0:6]

    idade['m_ig'] = idadeIG['Mulheres'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')
    idade['h_ig'] = idadeIG['Homens'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')

    followersFB = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows= 1, encoding='utf-16', delimiter=';')

    FB_followers = followersFB[1:2]

    FB_followers  = int(FB_followers['Seguidores no Facebook'][1])

    followersIG = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows= 5, encoding='utf-16', delimiter=';')

    IG_followers = followersIG[1:2]

    IG_followers = int(IG_followers['Seguidores do Instagram'][1])

    # Calcula os totais das colunas de homens e mulheres,
    idade['t_h'] = ((FB_followers * idade['h_fb']) + (IG_followers * idade['h_ig'])) / (FB_followers+IG_followers)

    idade['t_m'] = ((FB_followers * idade['m_fb']) + (IG_followers * idade['m_ig'])) / (FB_followers+IG_followers)

    # Reorganização da estrutura dos dados usando a função melt
    melted_data = pd.melt(idade, id_vars=['Idade'], value_vars=['t_m', 't_h'])

    # Cria o gráfico usando matplotlib
    plt.figure(figsize=(10, 6))

    # Escolhe uma paleta de cores do seaborn (pode ser alterada conforme desejado)
    colors = sns.color_palette("husl", 2)

    # Gera o gráfico de barras empilhadas com cores personalizadas
    bottom = None
    for i, gender in enumerate(melted_data['variable'].unique()):
        subset = melted_data[melted_data['variable'] == gender]
        plt.bar(subset['Idade'], subset['value'], label=gender, bottom=bottom, color=colors[i])
        if bottom is None:
            bottom = subset['value']
        else:
            bottom += subset['value']

    # Adiciona rótulos e títulos ao gráfico
    plt.xlabel('faixa etária')
    plt.ylabel('porcentagem por faixa etária')
    plt.title('Audiência por faixa etária e gênero')

    # Adiciona rótulos no meio das barras
    for age, t_m, t_h in zip(idade['Idade'][0:6], idade['t_m'], idade['t_h']):
        plt.text(age, t_m / 2, f'{t_m:.2f}%', ha='center', va='center', fontsize=8, color='black')
        plt.text(age, t_m + t_h / 2, f'{t_h:.2f}%', ha='center', va='center', fontsize=8, color='black')

    # Adiciona rótulos nos topos das barras
    for age, t_m, t_h in zip(idade['Idade'][0:6], idade['t_m'], idade['t_h']):
        plt.text(age, t_m + t_h, f'{t_m + t_h:.2f}%', ha='center', va='bottom', fontsize=8)

    # Adiciona a legenda com cores personalizadas
    legend_labels = ['Mulheres', 'Homens']
    plt.legend(title="Gênero", labels=legend_labels, loc='upper left', bbox_to_anchor=(1, 1), fontsize=8)

    # Exibe o gráfico
    #plt.show()
    fePublico_FBIG_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/fePublico_FBIG.png"
    plt.savefig(fePublico_FBIG_plot_path, bbox_inches="tight")
    
    return fePublico_FBIG_plot_path, FB_followers, IG_followers

def publicoCidades():
    '''
    https://business.facebook.com

    https://business.facebook.com/latest/insights/people?asset_id=146958865328939&ad_account_id=23862053469140633&entity_type=FB_PAGE

    CAMINHO: Insights (barra lateral) >>> Público (menu lateral) >>> 

    Ações: Exportar (dropdown) >>> Exportar como csv
    '''

    cidadesFB = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows=28, encoding='utf-16')

    cidadesFB = cidadesFB.iloc[0:10]

    cidadesFB['Valor'] = cidadesFB['Valor'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')

    cidadesIG = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows=41, encoding='utf-16')

    cidadesIG = cidadesIG.iloc[0:5]

    cidadesIG['Valor'] = cidadesIG['Valor'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')

    followersFB = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows= 1, encoding='utf-16', delimiter=';')

    FB_followers = followersFB[1:2]

    FB_followers  = int(FB_followers['Seguidores no Facebook'][1])

    followersIG = pd.read_csv(fr"C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Público.csv", skiprows= 5, encoding='utf-16', delimiter=';')

    IG_followers = followersIG[1:2]

    IG_followers = int(IG_followers['Seguidores do Instagram'][1])

    cidades = pd.DataFrame({
        'cidade': cidadesFB['Principais cidades'],
        'facebook': cidadesFB['Valor'],
        'instagram': [np.nan] * len(cidadesFB['Valor'])
    })

    #cidades['instagram'].fillna(np.nan)

    for citys,valor in zip(cidadesIG['Principais cidades'],cidadesIG['Valor']):
        numero_linha = cidadesFB.index[cidadesFB['Principais cidades'] == citys].tolist()[0]
        # cidades['instagram'][numero_linha] = cidadesIG['Valor'][numero_linha]
        cidades.loc[cidades['cidade'] == citys, 'instagram'] = valor

    cidades.loc[len(cidades)] = {'cidade':'Outras', 'facebook': abs(cidades['facebook'].sum()-100), 'instagram': abs(cidades['instagram'].sum()-100)}

    cidades['facebook'] = cidades['facebook']*FB_followers/100
    cidades['instagram'] = cidades['instagram']*IG_followers/100

    # Total de seguidores
    total_fb = cidades['facebook'].sum(skipna=True)
    total_ig = cidades['instagram'].sum(skipna=True)
    total = total_fb + total_ig

    # Criar gráfico
    sns.set(style="darkgrid") # Define o estilo do seaborn
    plt.figure(figsize=(10, 6))

    # Mapeamento de cores
    # cor_fb = sns.color_palette("#3b5998")
    # cor_ig = sns.color_palette("#DF2A77")

    # Plotagem
    sns.barplot(data=pd.melt(cidades, id_vars='cidade'), x='value', y='cidade', hue='variable', dodge=True, palette={  'instagram': '#DF2A77','facebook': '#3b5998' })

    # Adicionar percentuais
    for i, p in enumerate(plt.gca().patches):
        percentage = 100 * p.get_width() / total
        plt.text(p.get_x() + p.get_width() + 0.02, p.get_y() + p.get_height() / 2, f"{percentage:.2f}%", ha='left', va='center', size=8)

    # Ajustes estéticos
    plt.title('Cidades com mais seguidores da Tribuna do Norte no Facebook e Instagram')
    plt.xlabel('Seguidores')
    plt.ylabel('Cidade')
    plt.xlim(0, 250000)
    plt.legend(title='Plataforma')
    sns.despine(left=True, bottom=True)

    # Exibir gráfico
    #plt.show()
    publicoCidades_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/publicoCidades.png"
    plt.savefig(publicoCidades_plot_path, bbox_inches="tight")
    
    return publicoCidades_plot_path

def encontrar_frase_em_csv_meta(nome_arquivo, frase_procurada):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-16') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            
            for numero_linha, linha in enumerate(leitor_csv, start=1):
                if frase_procurada in linha:
                    return numero_linha

        # Se a frase não for encontrada em nenhuma linha
        return -1

    except FileNotFoundError:
        print(f'O arquivo {nome_arquivo} não foi encontrado.')
        return -1

def curtidasFB():
    # SEGUIDORES FB
    final_seguidoresFB = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', 'Seguidos no Instagram')

    #SEMANA ANTERIOR
    seguidoresFB_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\Seguidores.csv', skiprows=2, encoding='utf-16', skip_blank_lines=True, nrows=7).dropna()

    seguidoresFB_ANTERIOR['Data'] = pd.to_datetime(seguidoresFB_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    #SEMANA ANALISADA
    seguidoresFB = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', skiprows=2, encoding='utf-16', skip_blank_lines=True, nrows=7).dropna()

    seguidoresFB['Data'] = pd.to_datetime(seguidoresFB['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#ACB9D7", "#5874af"]

    seguidoresFB_ANTERIOR_acumulado = seguidoresFB_ANTERIOR['Primary'].cumsum()

    seguidoresFB_acumulado = seguidoresFB['Primary'].cumsum()

    dia = [1,2,3,4,5,6,7]

    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=seguidoresFB_ANTERIOR_acumulado, data=seguidoresFB_ANTERIOR, label=f"Seguidores {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=seguidoresFB_acumulado, data=seguidoresFB, label=f"Seguidores {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, seguidoresFB_ANTERIOR['Primary'], seguidoresFB_ANTERIOR_acumulado):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, seguidoresFB['Primary'], seguidoresFB_acumulado):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Seguidores")
    plt.title("Novos seguidores no FB")

    plt.legend()

    # Exibindo o gráfico
    #plt.show()
    curtidasFB_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/curtidasFB.png"
    plt.savefig(curtidasFB_plot_path, bbox_inches="tight")
    
    return curtidasFB_plot_path

def visitasFB():
    #VISITAS FB
    final_visitasFB = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Visitas.csv', 'Visitas ao perfil do Instagram')

    #SEMANA ANTERIOR
    visitasFB_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\Visitas.csv', skiprows=2, encoding='utf-16', skip_blank_lines=True, nrows=final_visitasFB-4).dropna()

    visitasFB_ANTERIOR['Data'] = pd.to_datetime(visitasFB_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    #SEMANA ANALISADA
    visitasFB = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Visitas.csv', skiprows=2, encoding='utf-16', skip_blank_lines=True, nrows=final_visitasFB-4).dropna()

    visitasFB['Data'] = pd.to_datetime(visitasFB['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#7B94CC", "#3b5998"]

    visitasFB_ANTERIOR_ACUMULADO = visitasFB_ANTERIOR['Primary'].cumsum()

    visitasFB_ACUMULADO = visitasFB['Primary'].cumsum()

    dia = [1,2,3,4,5,6,7]
    
    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=visitasFB_ANTERIOR_ACUMULADO, data=visitasFB_ANTERIOR, label=f"Visitas {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=visitasFB_ACUMULADO, data=visitasFB, label=f"Visitas {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, visitasFB_ANTERIOR['Primary'], visitasFB_ANTERIOR_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, visitasFB['Primary'], visitasFB_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Visitas")
    plt.title("Visitas na página do Facebook")

    # Ajustar os rótulos do eixo Y para valores correspondentes
    # plt.yticks(range(0, max(int(visitasFB["Curtidas na Página do Facebook"])), 100))

    plt.legend()

    # Exibindo o gráfico
    #plt.show()
    visitasFB_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visitasFB.png"
    plt.savefig(visitasFB_plot_path, bbox_inches="tight")
    
    return visitasFB_plot_path

def alcanceFB():
    #ALCANCE
    final_alcanceFB = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', 'Alcance do Instagram')

    inicio_alcanceFB = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', 'Alcance no Facebook')

    #SEMANA ANTERTIOR
    alcanceFB_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\Alcance.csv', skiprows=inicio_alcanceFB, encoding='utf-16', skip_blank_lines=True, nrows=final_alcanceFB-4).dropna()

    alcanceFB_ANTERIOR['Data'] = pd.to_datetime(alcanceFB_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    #SEMANA ANALISADA
    alcanceFB = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', skiprows=inicio_alcanceFB, encoding='utf-16', skip_blank_lines=True, nrows=final_alcanceFB-4).dropna()

    alcanceFB['Data'] = pd.to_datetime(alcanceFB['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#6184D1", "#2f55a4"]

    alcanceFB_ANTERIOR_ACUMULADO = alcanceFB_ANTERIOR['Primary'].cumsum()

    alcanceFB_ACUMULADO = alcanceFB['Primary'].cumsum()

    dia = [1,2,3,4,5,6,7]
    
    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=alcanceFB_ANTERIOR_ACUMULADO, data=alcanceFB_ANTERIOR, label=f"Alcance {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=alcanceFB_ACUMULADO, data=alcanceFB, label=f"Alcance {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, alcanceFB_ANTERIOR['Primary'], alcanceFB_ANTERIOR_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, alcanceFB['Primary'], alcanceFB_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("usuários alcançados")
    plt.title("Alcance da página do Facebook")

    plt.legend()

    # Exibindo o gráfico
    #plt.show()
    alcanceFB_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/alcanceFB.png"
    plt.savefig(alcanceFB_plot_path, bbox_inches="tight")
    
    return alcanceFB_plot_path

def dadosFB():
    # ALCANCE
    final_alcanceFB = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', 'Alcance do Instagram')
    inicio_alcanceFB = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', 'Alcance no Facebook')

    alcanceFB = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', skiprows=inicio_alcanceFB, encoding='utf-16', skip_blank_lines=True,nrows=final_alcanceFB-4).dropna()
    #alcanceFB = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', skiprows=inicio_alcanceFB, encoding='utf-16', skip_blank_lines=True).dropna().iloc[0:7]

    alcanceFB['Data'] = pd.to_datetime(alcanceFB['Data']).dt.strftime('%d-%m-%Y')

    # VISITAS
    final_visitasFB = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Visitas.csv', 'Visitas ao perfil do Instagram')

    visitasFB = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Visitas.csv', skiprows=2, encoding='utf-16', skip_blank_lines=True, nrows=final_visitasFB-4).dropna()

    visitasFB['Data'] = pd.to_datetime(visitasFB['Data']).dt.strftime('%d-%m-%Y')

    visitasFB['Primary'] = visitasFB['Primary']*20

    # CURTIDAS
    final_seguidoresFB = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', 'Seguidos no Instagram')

    seguidoresFB = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', skiprows=2, encoding='utf-16', skip_blank_lines=True, nrows=7).dropna()

    seguidoresFB['Data'] = pd.to_datetime(seguidoresFB['Data']).dt.strftime('%d-%m-%Y')

    seguidoresFB['Primary'] = seguidoresFB['Primary']*800

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#5874af", "#2F79A3", "#2f55a4"]

    # Plotando o gráfico de linhas
    #sns.lineplot(x="Data", y="Novas curtidas da Página do Facebook", data=seguidoresFB, label="seguidores", linewidth=2.5, color=cores[0])
    sns.lineplot(x="Data", y="Primary", data=alcanceFB, label="alcance", linewidth=2.5, color=cores[2])
    sns.lineplot(x="Data", y="Primary", data=visitasFB, label="visitas", linewidth=2.5, color=cores[1])
    sns.lineplot(x="Data", y="Primary", data=seguidoresFB, label="seguidores", linewidth=2.5, color=cores[0])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Alcance | Visitas | Seguidores")
    plt.title("Dados do facebook ao longo da semana")

    plt.yticks([])

    plt.legend()
    
    dadosFB_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/dadosFB.png"
    plt.savefig(dadosFB_plot_path, bbox_inches="tight")
    
    return dadosFB_plot_path

def seguidoresIG():
    #SEGUIDORES IG
    inicio_seguidoresIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', 'Seguidores no Instagram')

    #SEMANA ANTERIOR
    seguidoresIG_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\Seguidores.csv', skiprows=inicio_seguidoresIG, encoding='utf-16', skip_blank_lines=True)

    seguidoresIG_ANTERIOR['Data'] = pd.to_datetime(seguidoresIG_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    #SEMANA ANALISADA
    seguidoresIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', skiprows=inicio_seguidoresIG, encoding='utf-16', skip_blank_lines=True)

    seguidoresIG['Data'] = pd.to_datetime(seguidoresIG['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#B684D7", "#833AB4"]

    seguidoresIG_ANTERIOR_acumulado = seguidoresIG_ANTERIOR['Primary'].cumsum()

    seguidoresIG_acumulado = seguidoresIG['Primary'].cumsum()

    dia = [1,2,3,4,5,6,7]
    
    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=seguidoresIG_ANTERIOR_acumulado, data=seguidoresIG_ANTERIOR, label=f"Seguidores {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=seguidoresIG_acumulado, data=seguidoresIG, label=f"Seguidores {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, seguidoresIG_ANTERIOR['Primary'], seguidoresIG_ANTERIOR_acumulado):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, seguidoresIG['Primary'], seguidoresIG_acumulado):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Seguidores")
    plt.title("Novos seguidores no IG")

    plt.legend()

    # Exibindo o gráfico
    # plt.show()
    seguidoresIG_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/seguidoresIG.png"
    plt.savefig(seguidoresIG_plot_path, bbox_inches="tight")
    
    return seguidoresIG_plot_path, seguidoresIG

def visitasIG():
    # VISITAS ig
    inicio_visitasIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Visitas.csv', 'Visitas ao perfil do Instagram')

    #semana anterior
    visitasIG_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\Visitas.csv', skiprows=inicio_visitasIG, encoding='utf-16', skip_blank_lines=True)

    visitasIG_ANTERIOR['Data'] = pd.to_datetime(visitasIG_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    #semana anlisada
    visitasIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Visitas.csv', skiprows=inicio_visitasIG, encoding='utf-16', skip_blank_lines=True)

    visitasIG['Data'] = pd.to_datetime(visitasIG['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#EB7099", "#E1306C"]

    visitasIG_ANTERIOR_acumuladas = visitasIG_ANTERIOR['Primary'].cumsum()

    visitasIG_acumuladas = visitasIG['Primary'].cumsum()

    dia = [1,2,3,4,5,6,7]
    
    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=visitasIG_ANTERIOR_acumuladas, data=visitasIG_ANTERIOR, label=F"Visitas {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=visitasIG_acumuladas, data=visitasIG, label=F"Visitas {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, visitasIG_ANTERIOR['Primary'], visitasIG_ANTERIOR_acumuladas):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, visitasIG['Primary'], visitasIG_acumuladas):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Visitas")
    plt.title("Visitas no perefil do IG")

    plt.legend()
    
    visitasIG_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visitasIG.png"
    plt.savefig(visitasIG_plot_path, bbox_inches="tight")
    
    return visitasIG_plot_path, visitasIG

def alcanceIG():
    # ALCANCE ig
    #final_alcanceIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', 'Alcance no Facebook')
    inicio_alcanceIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', 'Alcance do Instagram')

    #SEMANA ANTERIOR
    alcanceIG_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\Alcance.csv', skiprows=inicio_alcanceIG, encoding='utf-16', skip_blank_lines=True) #, nrows=final_alcanceIG-5

    alcanceIG_ANTERIOR['Data'] = pd.to_datetime(alcanceIG_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    #SEMANA ANALISADA
    alcanceIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', skiprows=inicio_alcanceIG, encoding='utf-16', skip_blank_lines=True) #, nrows=final_alcanceIG-5

    alcanceIG['Data'] = pd.to_datetime(alcanceIG['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#FDCC86", "#FCAF45"]

    alcanceIG_ANTERIOR_ACUMULADA = alcanceIG_ANTERIOR['Primary'].cumsum()

    alcanceIG_ACUMULADA = alcanceIG['Primary'].cumsum()

    dia = [1,2,3,4,5,6,7]
    
    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=alcanceIG_ANTERIOR_ACUMULADA, data=alcanceIG_ANTERIOR, label=F"Alcance {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=alcanceIG_ACUMULADA, data=alcanceIG, label=F"Alcance {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, alcanceIG_ANTERIOR['Primary'], alcanceIG_ANTERIOR_ACUMULADA):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, alcanceIG['Primary'], alcanceIG_ACUMULADA):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Alcance")
    plt.title("Alcance do perefil do IG")

    plt.legend()
    
    alcanceIG_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/alcanceIG.png"
    plt.savefig(alcanceIG_plot_path, bbox_inches="tight")
    
    return alcanceIG_plot_path, alcanceIG

def dadosIG(intVisistas, intSeg):
    
    # ALCANCE
    #final_alcanceIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', 'Alcance no Facebook')
    inicio_alcanceIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', 'Alcance do Instagram')

    alcanceIG = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Alcance.csv', skiprows=inicio_alcanceIG, encoding='utf-16', skip_blank_lines=True) #, nrows=final_alcanceIG-5

    alcanceIG['Data'] = pd.to_datetime(alcanceIG['Data']).dt.strftime('%d-%m-%Y')

    # VISITAS
    inicio_visitasIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Visitas.csv', 'Visitas ao perfil do Instagram')

    visitasIG = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Visitas.csv', skiprows=inicio_visitasIG, encoding='utf-16', skip_blank_lines=True)

    visitasIG['Data'] = pd.to_datetime(visitasIG['Data']).dt.strftime('%d-%m-%Y')

    visitasIG['Primary'] = visitasIG['Primary']*intVisistas

    # SEGUIDORES
    inicio_seguidoresIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', 'Seguidores no Instagram')

    final_segIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', 'Seguidores')
    print(final_segIG)
    seguidoresIG = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\Seguidores.csv', skiprows=inicio_seguidoresIG, encoding='utf-16', skip_blank_lines=True).dropna()

    seguidoresIG['Data'] = pd.to_datetime(seguidoresIG['Data']).dt.strftime('%d-%m-%Y')

    seguidoresIG['Primary'] = seguidoresIG['Primary']*intSeg


    # social_media_data['Data'] = pd.to_datetime(social_media_data['Data'])
    # social_media_data['Seguidores'] = social_media_data['Seguidores']*200
    # social_media_data['Seguidores do Instagram'] = social_media_data['Seguidores do Instagram']*20

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#833AB4", "#E1306C", "#FCAF45"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Data", y="Primary", data=alcanceIG, label="alcance", linewidth=2.5, color=cores[2])
    sns.lineplot(x="Data", y="Primary", data=visitasIG, label="visitas", linewidth=2.5, color=cores[1])
    #sns.lineplot(x="Data", y="Primary", data=seguidoresIG, label="seguidores", linewidth=2.5, color=cores[0])

    # Ajustando o intervalo entre as datas no eixo x
    #plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Alcance | Visitas | Seguidores")
    plt.title("Dados do IG")

    plt.yticks([])

    plt.legend()
    
    dadosIG_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/dadosIG.png"
    plt.savefig(dadosIG_plot_path, bbox_inches="tight")
    
    return dadosIG_plot_path

def engajamentoTW():
    tw_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\twitter.csv')

    twFiltrado_ANTERIOR = tw_ANTERIOR[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado_ANTERIOR['Data'] = pd.to_datetime(twFiltrado_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    tw = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\twitter.csv')

    twFiltrado = tw[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado['Data'] = pd.to_datetime(twFiltrado['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#8BCFF8", "#1DA1F2"]

    twFiltrado_ANTERIOR_ACUMULADO = twFiltrado_ANTERIOR['engajamentos'].cumsum()

    twFiltrado_ACUMULADO =  twFiltrado['engajamentos'].cumsum()

    dia = [1,2,3,4,5,6,7]
    
    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=twFiltrado_ANTERIOR_ACUMULADO, data=twFiltrado_ANTERIOR, label=f"Engajamento {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=twFiltrado_ACUMULADO, data=twFiltrado, label=f"Engajamento {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, twFiltrado_ANTERIOR['engajamentos'], twFiltrado_ANTERIOR_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, twFiltrado['engajamentos'], twFiltrado_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance")
    plt.title("Engajamento do Twitter")

    plt.legend()

    # Exibindo o gráfico
    #plt.show()
    
    engajamentoTW_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/engajamentoTW.png"
    plt.savefig(engajamentoTW_plot_path, bbox_inches="tight")
    
    return engajamentoTW_plot_path

def impressoesTW():
    tw_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\twitter.csv')

    twFiltrado_ANTERIOR = tw_ANTERIOR[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado_ANTERIOR['Data'] = pd.to_datetime(twFiltrado_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    tw = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\twitter.csv')

    twFiltrado = tw[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado['Data'] = pd.to_datetime(twFiltrado['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#596673", "#14171A"]

    twFiltrado_ANTERIOR_ACUMULADO = twFiltrado_ANTERIOR['impressões'].cumsum()

    twFiltrado_ACUMULADO =  twFiltrado['impressões'].cumsum()
    dia = [1,2,3,4,5,6,7]
    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=twFiltrado_ANTERIOR_ACUMULADO, data=twFiltrado_ANTERIOR, label=f"Impressões {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=twFiltrado_ACUMULADO, data=twFiltrado, label=f"Impressões {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, twFiltrado_ANTERIOR['impressões'], twFiltrado_ANTERIOR_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, twFiltrado['impressões'], twFiltrado_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance")
    plt.title("Impressões do Twitter")

    plt.legend()
    
    impressoesTW_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/impressoesTW.png"
    plt.savefig(impressoesTW_plot_path, bbox_inches="tight")
    
    return impressoesTW_plot_path

def seguidoresTW():
    tw_ANTERIOR = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\ANTERIOR\TNsemanal\twitter.csv')

    twFiltrado_ANTERIOR = tw_ANTERIOR[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado_ANTERIOR['Data'] = pd.to_datetime(twFiltrado_ANTERIOR['Data']).dt.strftime('%d-%m-%Y')

    tw = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\twitter.csv')

    twFiltrado = tw[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado['Data'] = pd.to_datetime(twFiltrado['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#A2AFB9", "#657786"]

    twFiltrado_ANTERIOR_ACUMULADO = twFiltrado_ANTERIOR['seguiram'].cumsum()

    twFiltrado_ACUMULADO =  twFiltrado['seguiram'].cumsum()
    dia = [1,2,3,4,5,6,7]
    # Plotando o gráfico de linhas
    sns.lineplot(x=dia, y=twFiltrado_ANTERIOR_ACUMULADO, data=twFiltrado_ANTERIOR, label=f"Seguiram {(penultimo_domingo()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")} a {(ultimo_sabado()- datetime.timedelta(days=7)).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[0], marker='o')

    sns.lineplot(x=dia, y=twFiltrado_ACUMULADO, data=twFiltrado, label=f"Seguiram {(penultimo_domingo()).strftime("%d-%m-%Y")} a {(ultimo_sabado()).strftime("%d-%m-%Y")}", linewidth=2.5, color=cores[1], marker='o')

    # Adicionando os valores de cada ponto de usuarios_unicosANTERIOR
    for x, y, acumulado in zip(dia, twFiltrado_ANTERIOR['seguiram'], twFiltrado_ANTERIOR_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='left', va='top', fontsize=8, color='white', bbox=dict(facecolor='#474747', alpha=0.4))

    # Adicionando os valores de cada ponto 
    for x, y, acumulado in zip(dia, twFiltrado['seguiram'], twFiltrado_ACUMULADO):
        plt.text(x, acumulado, f'Dia: {int(y)}\nAcumulado: {int(acumulado)}', ha='right', va='bottom', fontsize=8, color='black', bbox=dict(facecolor='#E1E1E1', alpha=0.5))

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=0)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance")
    plt.title("Novos seguidores do Twitter")

    plt.legend()

    seguidoresTW_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/seguidoresTW.png"
    plt.savefig(seguidoresTW_plot_path, bbox_inches="tight")
    
    return seguidoresTW_plot_path

def dadosTW():
    tw = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\TNsemanal\twitter.csv')

    twFiltrado = tw[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado['Data'] = pd.to_datetime(twFiltrado['Data']).dt.strftime('%d-%m-%Y')

    twFiltrado['engajamentos'] = twFiltrado['engajamentos']*12
    twFiltrado['seguiram'] = twFiltrado['seguiram']*15
    # Configurando o tema do Seaborn
    sns.set_theme(style="whitegrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#1DA1F2", "#14171A", "#657786"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Data", y="impressões", data=twFiltrado, label="Impressões", linewidth=2.5, color=cores[0])
    sns.lineplot(x="Data", y="engajamentos", data=twFiltrado, label="Engajamentos", linewidth=2.5, color=cores[1])
    sns.lineplot(x="Data", y="seguiram", data=twFiltrado, label="Seguidores", linewidth=2.5, color=cores[2])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance")
    plt.title("Comparativo do comportamento dos dados do twitter")
    plt.yticks([])
    plt.legend()

    dadosTW_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/dadosTW.png"
    plt.savefig(dadosTW_plot_path, bbox_inches="tight")
    
    return dadosTW_plot_path

def visualizacoesIdadeYTB():
    ytb_idade_visualizações = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\idadeytb.csv')
    ytb_idade_visualizações['Visualizações (%)'] = ytb_idade_visualizações['Visualizações (%)'].str.replace(',','.').astype(float)
    # Configurar o estilo seaborn
    sns.set(style="whitegrid")

    # Criar o gráfico de barras com a paleta "magma"
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Idade do espectador', y='Visualizações (%)', data=ytb_idade_visualizações, palette="gist_heat")#"blend:#7AB,#EDA"

    # Adicionar rótulos diretamente acima de cada barra
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')

    # Adicionar rótulos e título
    plt.xlabel('Faixa Etária')
    plt.ylabel('Visualizações')
    plt.title('Visualizações por Faixa Etária')

    # Ajustar os rótulos do eixo Y para valores correspondentes
    #plt.yticks(range(0, max(visualizacoes)+100000, 200000))

    # Desativar a notação científica no eixo Y
    plt.ticklabel_format(axis='y', style='plain')

    # Ajustar os rótulos do eixo Y para valores correspondentes
    #plt.yticks(range(0, max(visualizacoes)+100000, 200000))

    # Desativar a notação científica no eixo Y
    plt.ticklabel_format(axis='y', style='plain')
    
    visualizacoesIdadeYTB_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visualizacoesIdadeYTB.png"
    plt.savefig(visualizacoesIdadeYTB_plot_path, bbox_inches="tight")
    
    return visualizacoesIdadeYTB_plot_path

def horasIdadeYTB():
    ytb_idade_horas = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\idadeytb.csv')
    ytb_idade_horas['Tempo de exibição (horas) (%)'] = ytb_idade_horas['Tempo de exibição (horas) (%)'].str.replace(',','.').astype(float)
    # Configurar o estilo seaborn
    sns.set(style="whitegrid")

    # Criar o gráfico de barras com a paleta "magma"
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Idade do espectador', y='Tempo de exibição (horas) (%)', data=ytb_idade_horas, palette="copper")#"blend:#7AB,#EDA"

    # Adicionar rótulos diretamente acima de cada barra
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')

    # Adicionar rótulos e título
    plt.xlabel('Faixa Etária')
    plt.ylabel('Visualizações')
    plt.title('Horas de exibição por Faixa Etária')

    # Ajustar os rótulos do eixo Y para valores correspondentes
    #plt.yticks(range(0, max(visualizacoes)+100000, 200000))

    # Desativar a notação científica no eixo Y
    plt.ticklabel_format(axis='y', style='plain')
    
    horasIdadeYTB_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/horasIdadeYTB.png"
    plt.savefig(horasIdadeYTB_plot_path, bbox_inches="tight")
    
    return horasIdadeYTB_plot_path

def generoYTB():
    generoytb = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\generoytb.csv')
    generoytb['Visualizações (%)'] = generoytb['Visualizações (%)'].str.replace(',','.').astype(float)
    # Criar um gráfico de pizza usando Matplotlib
    plt.figure(figsize=(8, 8))  # Ajuste o tamanho da figura conforme necessário

    # Plotar o gráfico de pizza usando Matplotlib
    plt.pie(generoytb['Visualizações (%)'], labels=generoytb['Gênero do espectador'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("light:#787878"))

    # Adicionar título
    plt.title('Sexo dos usuários do YouTube')
    
    generoYTB_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/generoYTB.png"
    plt.savefig(generoYTB_plot_path, bbox_inches="tight")
    
    return generoYTB_plot_path

def visualizacoesCidadeYTB():
    ytb_cidades_visualizacoes = pd.read_csv(fr'C:\Users\{path_Usuarios}\Documents\Repositórios\csv\TNsemanal\cidadesytb.csv')

    # Configurar o estilo seaborn
    sns.set(style="whitegrid")

    # Criar o gráfico de barras com a paleta "magma"
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Nome da cidade', y='Visualizações', data=ytb_cidades_visualizacoes.iloc[1:11,1:5], palette="copper")#"blend:#7AB,#EDA"

    total_visualizacoes_cidades = ytb_cidades_visualizacoes.iloc[0,:]['Visualizações']


    # Adicionar rótulos diretamente acima de cada barra
    for p in ax.patches:
        ax.annotate(f'{(p.get_height()/total_visualizacoes_cidades)*100:,.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                    textcoords='offset points')

    # Adicionar rótulos e título
    plt.xlabel('Cidades')
    plt.ylabel('Visualizações')
    plt.title('Audiência por cidade')

    # Ajustar os rótulos do eixo Y para valores correspondentes
    #plt.yticks(range(0, max(visualizacoes)+100000, 200000))

    # Desativar a notação científica no eixo Y
    plt.ticklabel_format(axis='y', style='plain')

    plt.xticks(rotation=90)

    visualizacoesCidadeYTB_plot_path = fr"C:/Users/{path_Usuarios}/Documents/Repositórios/Imagens/TN/visualizacoesCidadeYTB.png"
    plt.savefig(visualizacoesCidadeYTB_plot_path, bbox_inches="tight")
    
    return visualizacoesCidadeYTB_plot_path
