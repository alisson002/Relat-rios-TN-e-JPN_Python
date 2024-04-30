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
    return ultimo_domingo.strftime("%d-%m-%Y")

def penultimo_domingo():
    hoje = datetime.date.today()
    dia_da_semana = hoje.weekday()  # Retorna um número de 0 (segunda-feira) a 6 (domingo)
    if dia_da_semana == 0: #segunda
        dias_para_subtrair = (dia_da_semana + 8) % 7  # Dias a subtrair para chegar ao último sabado
    elif dia_da_semana == 1: #terça
        dias_para_subtrair = (dia_da_semana + 8) % 7  # Dias a subtrair para chegar ao último sabado
    ultimo_domingo = hoje - datetime.timedelta(days=dias_para_subtrair)
    penultimo_domingo = ultimo_domingo - datetime.timedelta(days=7)
    return penultimo_domingo.strftime("%d-%m-%Y")

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

path_aliss = 'Usuario'
# path_Usuarios = 'aliss'
# path_Usuarios = 'Usuario'

def fePublico_FBIG():
    '''
    https://business.facebook.com

    https://business.facebook.com/latest/insights/people?asset_id=146958865328939&ad_account_id=23862053469140633&entity_type=FB_PAGE

    CAMINHO: Insights (barra lateral) >>> Público (menu lateral) >>> 

    Ações: Exportar (dropdown) >>> Exportar como csv
    '''



    idade = pd.read_csv(fr"C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Público.csv", skiprows= 13, encoding='utf-16')

    idade3 = pd.read_csv(fr"C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Público.csv", skiprows= 13, encoding='utf-16')

    idadeIG = idade3.iloc[0:6]

    idade['m_ig'] = idadeIG['Mulheres'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')
    idade['h_ig'] = idadeIG['Homens'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')

    followersIG = pd.read_csv(fr"C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Público.csv", skiprows= 5, encoding='utf-16', delimiter=';')

    IG_followers = followersIG[1:2]

    IG_followers = int(IG_followers['Seguidores do Instagram'][1])

    # Calcula os totais das colunas de homens e mulheres,
    idade['t_h'] = ((IG_followers * idade['h_ig'])) / (+IG_followers)

    idade['t_m'] = ((IG_followers * idade['m_ig'])) / (IG_followers)

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
    fePublico_FBIG_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/fePublico_FBIG.png"
    plt.savefig(fePublico_FBIG_plot_path, bbox_inches="tight")
    
    return fePublico_FBIG_plot_path, IG_followers

def publicoCidades():
    '''
    https://business.facebook.com

    https://business.facebook.com/latest/insights/people?asset_id=146958865328939&ad_account_id=23862053469140633&entity_type=FB_PAGE

    CAMINHO: Insights (barra lateral) >>> Público (menu lateral) >>> 

    Ações: Exportar (dropdown) >>> Exportar como csv
    '''
    cidadesIG = pd.read_csv(fr"C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Público.csv", skiprows=25, encoding='utf-16')

    cidadesIG = cidadesIG.iloc[0:5]

    cidadesIG['Valor'] = cidadesIG['Valor'].apply(lambda x: x.split('%')[-2].replace(',', '.')).astype('float')

    followersIG = pd.read_csv(fr"C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Público.csv", skiprows= 5, encoding='utf-16', delimiter=';')

    IG_followers = followersIG[1:2]

    IG_followers = int(IG_followers['Seguidores do Instagram'][1])

    cidades = pd.DataFrame({
        'cidade': cidadesIG['Principais cidades'],
        'facebook': 0,
        'instagram': cidadesIG['Valor']
    })

    #cidades['instagram'].fillna(np.nan)

    for citys,valor in zip(cidadesIG['Principais cidades'],cidadesIG['Valor']):
        numero_linha = cidadesIG.index[cidadesIG['Principais cidades'] == citys].tolist()[0]
        # cidades['instagram'][numero_linha] = cidadesIG['Valor'][numero_linha]
        cidades.loc[cidades['cidade'] == citys, 'instagram'] = valor

    cidades.loc[len(cidades)] = {'cidade':'Outras', 'facebook': abs(cidades['facebook'].sum()-100), 'instagram': abs(cidades['instagram'].sum()-100)}

    cidades['facebook'] = cidades['facebook']*0/100
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
    # dodge=False serve para colocar mais de uma barra, pois ela "desvia" da outro e ficam mais finas
    sns.barplot(data=pd.melt(cidades, id_vars='cidade'), x='value', y='cidade', hue='variable', dodge=False, palette={  'instagram': '#DF2A77','facebook': '#3b5998' })

    # Adicionar percentuais
    for i, p in enumerate(plt.gca().patches):
        if p.get_width() > 0:
            percentage = 100 * p.get_width() / total
            plt.text(p.get_x() + p.get_width() + 0.02, p.get_y() + p.get_height() / 2, f"{percentage:.2f}%", ha='left', va='center', size=8)

    # Ajustes estéticos
    plt.title('Cidades com mais seguidores da Tribuna do Norte no Facebook e Instagram')
    plt.xlabel('Seguidores')
    plt.ylabel('Cidade')
    plt.xlim(0, 12000)
    plt.legend(title='Plataforma')
    sns.despine(left=True, bottom=True)

    # Exibir gráfico
    #plt.show()
    publicoCidades_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/publicoCidades.png"
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

def seguidoresIG():
    # # SEGUIDORES
    
    inicio_seguidoresIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Seguidores.csv', 'Seguidos no Instagram')

    seguidoresIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Seguidores.csv', skiprows=inicio_seguidoresIG, encoding='utf-16', skip_blank_lines=True)

    seguidoresIG['Data'] = pd.to_datetime(seguidoresIG['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#833AB4", "#E1306C", "#FCAF45"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Data", y="Primary", data=seguidoresIG, label="seguidores", linewidth=2.5, color=cores[0])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Seguidores")
    plt.title("Novos seguidores no IG")

    plt.legend()

    # Exibindo o gráfico
    # plt.show()
    seguidoresIG_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/seguidoresIG.png"
    plt.savefig(seguidoresIG_plot_path, bbox_inches="tight")
    
    return seguidoresIG_plot_path, seguidoresIG

def visitasIG():
    # # VISITAS
    
    inicio_visitasIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Visitas.csv', 'Visitas ao perfil do Instagram')

    visitasIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Visitas.csv', skiprows=inicio_visitasIG, encoding='utf-16', skip_blank_lines=True)

    visitasIG['Data'] = pd.to_datetime(visitasIG['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#833AB4", "#E1306C", "#FCAF45"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Data", y="Primary", data=visitasIG, label="visitas", linewidth=2.5, color=cores[1])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Visitas")
    plt.title("Visitas no perefil do IG")

    plt.legend()
    
    visitasIG_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/visitasIG.png"
    plt.savefig(visitasIG_plot_path, bbox_inches="tight")
    
    return visitasIG_plot_path, visitasIG

def alcanceIG():
    #final_alcanceIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Alcance.csv', 'Alcance no Facebook')
    inicio_alcanceIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Alcance.csv', 'Alcance do Instagram')

    alcanceIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Alcance.csv', skiprows=inicio_alcanceIG, encoding='utf-16', skip_blank_lines=True) #, nrows=final_alcanceIG-5

    alcanceIG['Data'] = pd.to_datetime(alcanceIG['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#833AB4", "#E1306C", "#FCAF45"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Data", y="Primary", data=alcanceIG, label="alcance", linewidth=2.5, color=cores[2])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Alcance")
    plt.title("Alcance do perefil do IG")

    plt.legend()
    
    alcanceIG_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/alcanceIG.png"
    plt.savefig(alcanceIG_plot_path, bbox_inches="tight")
    
    return alcanceIG_plot_path, alcanceIG

def dadosIG(intVisistas, intSeg):
    
    # ALCANCE
    #final_alcanceIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Alcance.csv', 'Alcance no Facebook')
    inicio_alcanceIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Alcance.csv', 'Alcance do Instagram')

    alcanceIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Alcance.csv', skiprows=inicio_alcanceIG, encoding='utf-16', skip_blank_lines=True) #, nrows=final_alcanceIG-5

    alcanceIG['Data'] = pd.to_datetime(alcanceIG['Data']).dt.strftime('%d-%m-%Y')

    # VISITAS
    inicio_visitasIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Visitas.csv', 'Visitas ao perfil do Instagram')

    visitasIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Visitas.csv', skiprows=inicio_visitasIG, encoding='utf-16', skip_blank_lines=True)

    visitasIG['Data'] = pd.to_datetime(visitasIG['Data']).dt.strftime('%d-%m-%Y')

    visitasIG['Primary'] = visitasIG['Primary']*intVisistas

    # SEGUIDORES
    inicio_seguidoresIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Seguidores.csv', 'Seguidos no Instagram')

    final_segIG = encontrar_frase_em_csv_meta(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Seguidores.csv', 'Seguidores')
    print(final_segIG)
    seguidoresIG = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\Seguidores.csv', skiprows=inicio_seguidoresIG, encoding='utf-16', skip_blank_lines=True).dropna()

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
    sns.lineplot(x="Data", y="Primary", data=seguidoresIG, label="seguidores", linewidth=2.5, color=cores[0])

    # Ajustando o intervalo entre as datas no eixo x
    #plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    plt.ylabel("Alcance | Visitas | Seguidores")
    plt.title("Dados do IG")

    plt.yticks([])

    plt.legend()
    
    dadosIG_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/dadosIG.png"
    plt.savefig(dadosIG_plot_path, bbox_inches="tight")
    
    return dadosIG_plot_path

def engajamentoTW():
    tw = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\twitter.csv')

    twFiltrado = tw[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado['Data'] = pd.to_datetime(twFiltrado['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#1DA1F2", "#14171A", "#657786"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Data", y="engajamentos", data=twFiltrado, label="alcance", linewidth=2.5, color=cores[0])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance")
    plt.title("Engajamento do Twitter")

    plt.legend()

    # Exibindo o gráfico
    #plt.show()
    
    engajamentoTW_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/engajamentoTW.png"
    plt.savefig(engajamentoTW_plot_path, bbox_inches="tight")
    
    return engajamentoTW_plot_path

def impressoesTW():
    tw = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\twitter.csv')

    twFiltrado = tw[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado['Data'] = pd.to_datetime(twFiltrado['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="darkgrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#1DA1F2", "#14171A", "#657786"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Data", y="impressões", data=twFiltrado, label="alcance", linewidth=2.5, color=cores[1])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance")
    plt.title("Impressões do Twitter")

    plt.legend()
    
    impressoesTW_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/impressoesTW.png"
    plt.savefig(impressoesTW_plot_path, bbox_inches="tight")
    
    return impressoesTW_plot_path

def seguidoresTW():
    tw = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\twitter.csv')

    twFiltrado = tw[['Data','engajamentos','impressões', 'seguiram']]
    twFiltrado['Data'] = pd.to_datetime(twFiltrado['Data']).dt.strftime('%d-%m-%Y')

    # Configurando o tema do Seaborn
    sns.set_theme(style="whitegrid")

    # Criando o gráfico de linhas
    plt.figure(figsize=(10, 6))  # Definindo o tamanho da figura

    # Definindo a paleta de cores desejada
    cores = ["#1DA1F2", "#14171A", "#657786"]

    # Plotando o gráfico de linhas
    sns.lineplot(x="Data", y="seguiram", data=twFiltrado, label="alcance", linewidth=2.5, color=cores[2])

    # Ajustando o intervalo entre as datas no eixo x
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Intervalo de 1 dia

    plt.xticks(rotation=-90)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel("Data")
    #plt.ylabel("Alcance")
    plt.title("Novos seguidores do Twitter")

    plt.legend()

    seguidoresTW_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/seguidoresTW.png"
    plt.savefig(seguidoresTW_plot_path, bbox_inches="tight")
    
    return seguidoresTW_plot_path

def visualizacoesIdadeYTB():
    ytb_idade_visualizações = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\idadeytb.csv')
    # ytb_idade_visualizações['Visualizações (%)'] = ytb_idade_visualizações['Visualizações (%)'].str.replace(',','.').astype(float)
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
    
    visualizacoesIdadeYTB_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/visualizacoesIdadeYTB.png"
    plt.savefig(visualizacoesIdadeYTB_plot_path, bbox_inches="tight")
    
    return visualizacoesIdadeYTB_plot_path

def horasIdadeYTB():
    ytb_idade_horas = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\idadeytb.csv')
    # ytb_idade_horas['Tempo de exibição (horas) (%)'] = ytb_idade_horas['Tempo de exibição (horas) (%)'].str.replace(',','.').astype(float)
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
    
    horasIdadeYTB_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/horasIdadeYTB.png"
    plt.savefig(horasIdadeYTB_plot_path, bbox_inches="tight")
    
    return horasIdadeYTB_plot_path

def generoYTB():
    generoytb = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\generoytb.csv')
    # generoytb['Visualizações (%)'] = generoytb['Visualizações (%)'].str.replace(',','.').astype(float)
    # Criar um gráfico de pizza usando Matplotlib
    plt.figure(figsize=(8, 8))  # Ajuste o tamanho da figura conforme necessário

    # Plotar o gráfico de pizza usando Matplotlib
    plt.pie(generoytb['Visualizações (%)'], labels=generoytb['Gênero do espectador'], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("light:#787878"))

    # Adicionar título
    plt.title('Sexo dos usuários do YouTube')
    
    generoYTB_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/generoYTB.png"
    plt.savefig(generoYTB_plot_path, bbox_inches="tight")
    
    return generoYTB_plot_path

def visualizacoesCidadeYTB():
    ytb_cidades_visualizacoes = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\cidadesytb.csv')

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

    visualizacoesCidadeYTB_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/visualizacoesCidadeYTB.png"
    plt.savefig(visualizacoesCidadeYTB_plot_path, bbox_inches="tight")
    
    return visualizacoesCidadeYTB_plot_path

def conteudoYTB():
    conteudo = pd.read_csv(fr'C:\Users\{path_aliss}\Documents\Repositórios\csv\JPNsemanal\conteudoYTB.csv')
    conteudo=conteudo.dropna()
    # Função para agrupar os usuários por mídia
    def agrupar_por_midia(row):
        if '🔴' in row['Título do vídeo']:
            return 'Transmissão de Jogo'
        elif 'JORNAL DA MANHÃ' in row['Título do vídeo']:
            return 'Jornal da Manhã'
        # elif 'Jornal da Manhã' in row['Título do vídeo']:
        #     return 'Jornal da Manhã'
        elif 'TRIBUNA ESPORTE' in row['Título do vídeo']:
            return 'Tribuna Esporte'
        # elif 'Tribuna Esporte' in row['Título do vídeo']:
        #     return 'Tribuna Esporte'
        elif 'TRIBUNA LIVRE' in row['Título do vídeo']:
            return 'Tribuna Livre'
        # elif 'Tribuna Livre' in row['Título do vídeo']:
        #     return 'Tribuna Livre'
        elif 'BATE PRONTO' in row['Título do vídeo']:
            return 'Bate Pronto'
        # elif 'Bate Pronto' in row['Título do vídeo']:
        #     return 'Bate Pronto'
    conteudo['Midia'] = conteudo.apply(agrupar_por_midia, axis=1)

    agrupado = conteudo.groupby('Midia')['Visualizações'].sum().reset_index().sort_values(by='Visualizações',ascending=False)
    # agrupado['Visualizações'] = agrupado['Visualizações'].astype(int)
    # agrupado.sort_values(by='Visualizações',ascending=False)
    sns.set_theme(style="whitegrid")

    # Criar o gráfico de barras com a paleta "magma"
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x='Visualizações', y='Midia', data=agrupado, palette="blend:#77BAB5,#7794BA,#77AABB,#77BA9F,#777FBA")#"blend:#7AB,#EDA"

    # Adicionar rótulos diretamente acima de cada barra
    # for p in ax.patches:
    #     ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
    #                 ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
    #                 textcoords='offset points')

    # Adicionar percentuais
    for i, p in enumerate(plt.gca().patches):
        percentage = p.get_width()
        plt.text(p.get_x() + p.get_width() + 0.02, p.get_y() + p.get_height() / 2, f"{percentage:.0f}", ha='left', va='center', size=10)

    # Adicionar rótulos e título
    plt.xlabel('Conteúdo')
    plt.ylabel('Visualizações')
    plt.title('Conteudos com mais visualizações')


    # Ajustar os rótulos do eixo Y para valores correspondentes
    #plt.yticks(range(0, max(visualizacoes)+100000, 200000))

    # Desativar a notação científica no eixo Y
    plt.ticklabel_format(axis='x', style='plain')
    
    conteudoYTB_plot_path = fr"C:/Users/{path_aliss}/Documents/Repositórios/Imagens/JPN/conteudoYTB.png"
    plt.savefig(conteudoYTB_plot_path, bbox_inches="tight")
    
    return conteudoYTB_plot_path