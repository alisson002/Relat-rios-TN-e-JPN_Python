from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage, Math
from pylatex.utils import bold
import graficosRelatorio as GR
import pandas as pd
import rpy2.robjects as robjects
import matplotlib.pyplot as plt


# Cria um novo documento LaTeX
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "lmargin": "1.5cm", "landscape": True}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
# doc.preamble.append(NoEscape(r'\usepackage{geometry}[landscape,margin=1in]'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório da Monetização")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Dezembro de 2024")))
        doc.append(LineBreak())

# f'{p.get_height():.1f}%'
GR.path_aliss
GR.path_Usuarios

#YOUTUBE - TN: MONETIZAÇÃO
impressoes_yb_TN_2023=[4692,10791,21297,13152,10314,11387,15399,17774,15042,18358,34544,29052]
visuMonetizadas_yb_TN_2023=[3921,9057,18849,11768,8969,9497,13558,16086,13704,16520,32073,26873]
receitaBruta_yb_TN_2023=[30,60,107,67,63,71,92,95,68,88,195,128]
premium_yb_TN_2023=[1,1,2,1,2,2,1,2,2,2,3,1]
AdSense_yb_TN_2023=[16,32,59,37,34,39,51,52,38,48,107,71]

impressoes_yb_TN_2024=[26580,68705,106582,50724,49123,35649,80455,263738,343942,111380,40372,75515]
visuMonetizadas_yb_TN_2024=[24539,64181,99340,48892,45513,32464,77698,262329,333255,107118,37255,69009]
receitaBruta_yb_TN_2024=[114,313,746,274,257,202,458,1609,2077,677,249,286]
premium_yb_TN_2024=[2,4,4,3,4,2,6,13,25,7,3,2]
AdSense_yb_TN_2024=[62,138,410,151,141,111,252,885,1144,373,138,158]

visualizacoes_tn = [255163]

def plot_stacked_bar_with_custom_colors(values):
    # Configuração dos dados para o gráfico
    categorias = ['Visualizações x Impressões de Anúncios', 'Visualizações x Visualizações Monetizadas']
    valores_grupo1 = [values[0], values[1]]
    valores_grupo2 = [values[2], values[3]]

    # Criar gráfico de barras empilhadas com largura ajustada
    fig, ax = plt.subplots(figsize=(10, 6))  # Aumentar espaço para visualização

    # Plotar as barras com largura reduzida e maior separação
    bar_width = 0.4
    bar1 = ax.bar(categorias[0], valores_grupo1[0], width=bar_width, label='Visualizações', color='#EE7B12')
    bar2 = ax.bar(categorias[0], valores_grupo1[1], width=bar_width, label='Visualizações monetizadas', color='#355424')

    bar3 = ax.bar(categorias[1], valores_grupo2[0], width=bar_width, label='Visualizações',color='#EE7B12')
    bar4 = ax.bar(categorias[1], valores_grupo2[1], width=bar_width, label='Impressões de anúncios', color='#9EC274')

    # Adicionar os valores no topo das barras
    for bar, value in zip([bar1, bar2, bar3, bar4], values):
        ax.text(bar[0].get_x() + bar[0].get_width() / 2, 
                value + 0.01 * max(values), 
                f'{value}', 
                ha='center', va='bottom')

    # Adicionar porcentagem na frente das barras mais baixas em relação às maiores
    percentages = [
        valores_grupo1[1] / valores_grupo1[0] * 100,
        valores_grupo2[1] / valores_grupo2[0] * 100
    ]

    for i, (bar, percentage) in enumerate(zip([bar2, bar4], percentages)):
        ax.text(bar[0].get_x() + bar[0].get_width() / 2, 
                bar[0].get_height() / 2, 
                f'{percentage:.1f}%', 
                ha='center', va='center', color='white', fontsize=10)

    # Ajustar espaçamento das legendas
    ax.set_title('Comparativo de Visualizações, Impressões e Monetização - TN.')
    ax.set_ylabel('Valores')
    ax.legend(['Visualizações', 'Impressões de anúncios', 'Visualizações', 'Visualizações monetizadas'], loc='upper center', bbox_to_anchor=(0.5, 1))

    # plt.tight_layout()
    visitasIG_plot_path = r"C:/Users/aliss/Documents/Repositórios/Imagens/TN/monetizacao.png"
    plt.savefig(visitasIG_plot_path)
    
    return visitasIG_plot_path


#YOUTUBE - JPN: MONETIZAÇÃO
impressoes_yb_JPN_2023=[185819,104421,159348,103283,176878,148994,117387,108411,67821,66770,68978,33860]
visuMonetizadas_yb_JPN_2023=[152248,86985,129067,84567,148854,124338,100843,94128,56538,56165,59319,28555]
receitaBruta_yb_JPN_2023=[698,450,738,483,678,604,445,436,293,284,305,199]
premium_yb_JPN_2023=[63,18,30,22,24,24,22,24,18,15,60,16]
AdSense_yb_JPN_2023=[383,246,405,266,372,332,244,240,161,156,167,109]

impressoes_yb_JPN_2024=[119775,100933,152837,86663,95707,151554,161089,147669,136039,728093,385756,115866]
visuMonetizadas_yb_JPN_2024=[101040,83561,123957,70751,79378,120773,134537,124481,116047,616077,339358,94256]
receitaBruta_yb_JPN_2024=[449,354,656,388,434,657,721,674,642,2842,1201,655]
premium_yb_JPN_2024=[21,28,32,28,25,28,30,36,38,131,36,69]
AdSense_yb_JPN_2024=[247,195,360,212,237,361,396,368,362,1562,663,361]

visualizacoes_jpn = [85827]

# Adiciona a seção para os resultados
with doc.create(Section('YouTube: Monetização', numbering=False)):
    with doc.create(Subsection('Dezembro/2024', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='YouTube - TN'), GR.formataNumero(impressoes_yb_TN_2024[-1]), GR.formataNumero(visuMonetizadas_yb_TN_2024[-1]), GR.formataNumero(receitaBruta_yb_TN_2024[-1]), GR.formataNumero(premium_yb_TN_2024[-1]), GR.formataNumero(AdSense_yb_TN_2024[-1])))
                table.add_row(('', 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta (R$)', 'YTB Premium (R$)', 'Receita estimada (AdSense) (R$)'))
                table.add_hline()
                table.add_row((MultiRow(2, data='YouTube - JPNews'), GR.formataNumero(impressoes_yb_JPN_2024[-1]), GR.formataNumero(visuMonetizadas_yb_JPN_2024[-1]), GR.formataNumero(receitaBruta_yb_JPN_2024[-1]), GR.formataNumero(premium_yb_JPN_2024[-1]), GR.formataNumero(AdSense_yb_JPN_2024[-1])))
                table.add_row(('', 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta (R$)', 'YTB Premium (R$)', 'Receita estimada (AdSense) (R$)'))

# # Adiciona a seção para os resultados
# with doc.create(Section('YouTube: Monetização', numbering=False)):
#     with doc.create(Subsection('Setembro/2024', numbering=False)):
#         with doc.create(MiniPage(align='c')):
#             # Adiciona a tabela de resultados
#             with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
                
#                 table.add_row(('-', 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta (R$)', 'YTB Premium (R$)', 'Receita estimada (AdSense) (R$)'))
#                 table.add_hline()
#                 table.add_row(('YouTube - TN', GR.formataNumero(impressoes_yb_TN_2024[-1]), GR.formataNumero(visuMonetizadas_yb_TN_2024[-1]), GR.formataNumero(receitaBruta_yb_TN_2024[-1]), GR.formataNumero(premium_yb_TN_2024[-1]), GR.formataNumero(AdSense_yb_TN_2024[-1])))
#                 table.add_hline()
#                 table.add_row(('YouTube - JPNews', GR.formataNumero(impressoes_yb_JPN_2024[-1]), GR.formataNumero(visuMonetizadas_yb_JPN_2024[-1]), GR.formataNumero(receitaBruta_yb_JPN_2024[-1]), GR.formataNumero(premium_yb_JPN_2024[-1]), GR.formataNumero(AdSense_yb_JPN_2024[-1])))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('YouTube - TN: Monetização', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(5, data='Mês'), 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta (R$)', 'YTB Premium (R$)', 'Receita estimada (AdSense) (R$)'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', (FootnoteText('mês anterior | msm mês em 2023')), FootnoteText('mês anterior | msm mês em 2023'), FootnoteText('mês anterior | msm mês em 2023'), FootnoteText('mês anterior | msm mês em 2023'), FootnoteText('mês anterior | msm mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Jan'), GR.numeroPorExtensso(impressoes_yb_TN_2024[0]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[0]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[0]), GR.numeroPorExtensso(premium_yb_TN_2024[0]), GR.numeroPorExtensso(AdSense_yb_TN_2024[0])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[0],impressoes_yb_TN_2023[11])} | {GR.crescimento(impressoes_yb_TN_2024[0],impressoes_yb_TN_2023[0])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[0],visuMonetizadas_yb_TN_2023[11])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[0],visuMonetizadas_yb_TN_2023[0])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[0],receitaBruta_yb_TN_2023[11])} | {GR.crescimento(receitaBruta_yb_TN_2024[0],receitaBruta_yb_TN_2023[0])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[0],premium_yb_TN_2023[11])} | {GR.crescimento(premium_yb_TN_2024[0],premium_yb_TN_2023[0])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[0],AdSense_yb_TN_2023[11])} | {GR.crescimento(AdSense_yb_TN_2024[0],AdSense_yb_TN_2023[0])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fev'), GR.numeroPorExtensso(impressoes_yb_TN_2024[1]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[1]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[1]), GR.numeroPorExtensso(premium_yb_TN_2024[1]), GR.numeroPorExtensso(AdSense_yb_TN_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[1],impressoes_yb_TN_2024[0])} | {GR.crescimento(impressoes_yb_TN_2024[1],impressoes_yb_TN_2023[1])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[1],visuMonetizadas_yb_TN_2024[0])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[1],visuMonetizadas_yb_TN_2023[1])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[1],receitaBruta_yb_TN_2024[0])} | {GR.crescimento(receitaBruta_yb_TN_2024[1],receitaBruta_yb_TN_2023[1])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[1],premium_yb_TN_2024[0])} | {GR.crescimento(premium_yb_TN_2024[1],premium_yb_TN_2023[1])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[1],AdSense_yb_TN_2024[0])} | {GR.crescimento(AdSense_yb_TN_2024[1],AdSense_yb_TN_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Mar'), GR.numeroPorExtensso(impressoes_yb_TN_2024[2]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[2]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[2]), GR.numeroPorExtensso(premium_yb_TN_2024[2]), GR.numeroPorExtensso(AdSense_yb_TN_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[2],impressoes_yb_TN_2024[1])} | {GR.crescimento(impressoes_yb_TN_2024[2],impressoes_yb_TN_2023[2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[2],visuMonetizadas_yb_TN_2024[1])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[2],visuMonetizadas_yb_TN_2023[2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[2],receitaBruta_yb_TN_2024[1])} | {GR.crescimento(receitaBruta_yb_TN_2024[2],receitaBruta_yb_TN_2023[2])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[2],premium_yb_TN_2024[1])} | {GR.crescimento(premium_yb_TN_2024[2],premium_yb_TN_2023[2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[2],AdSense_yb_TN_2024[1])} | {GR.crescimento(AdSense_yb_TN_2024[2],AdSense_yb_TN_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abr'), GR.numeroPorExtensso(impressoes_yb_TN_2024[3]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[3]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[3]), GR.numeroPorExtensso(premium_yb_TN_2024[3]), GR.numeroPorExtensso(AdSense_yb_TN_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[3],impressoes_yb_TN_2024[2])} | {GR.crescimento(impressoes_yb_TN_2024[3],impressoes_yb_TN_2023[3])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[3],visuMonetizadas_yb_TN_2024[2])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[3],visuMonetizadas_yb_TN_2023[3])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[3],receitaBruta_yb_TN_2024[2])} | {GR.crescimento(receitaBruta_yb_TN_2024[3],receitaBruta_yb_TN_2023[3])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[3],premium_yb_TN_2024[2])} | {GR.crescimento(premium_yb_TN_2024[3],premium_yb_TN_2023[3])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[3],AdSense_yb_TN_2024[2])} | {GR.crescimento(AdSense_yb_TN_2024[3],AdSense_yb_TN_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Mai'), GR.numeroPorExtensso(impressoes_yb_TN_2024[4]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[4]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[4]), GR.numeroPorExtensso(premium_yb_TN_2024[4]), GR.numeroPorExtensso(AdSense_yb_TN_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[4],impressoes_yb_TN_2024[3])} | {GR.crescimento(impressoes_yb_TN_2024[4],impressoes_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[4],visuMonetizadas_yb_TN_2024[3])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[4],visuMonetizadas_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[4],receitaBruta_yb_TN_2024[3])} | {GR.crescimento(receitaBruta_yb_TN_2024[4],receitaBruta_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[4],premium_yb_TN_2024[3])} | {GR.crescimento(premium_yb_TN_2024[4],premium_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[4],AdSense_yb_TN_2024[3])} | {GR.crescimento(AdSense_yb_TN_2024[4],AdSense_yb_TN_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Jun'), GR.numeroPorExtensso(impressoes_yb_TN_2024[5]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[5]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[5]), GR.numeroPorExtensso(premium_yb_TN_2024[5]), GR.numeroPorExtensso(AdSense_yb_TN_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[5],impressoes_yb_TN_2024[4])} | {GR.crescimento(impressoes_yb_TN_2024[5],impressoes_yb_TN_2023[5])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[5],visuMonetizadas_yb_TN_2024[4])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[5],visuMonetizadas_yb_TN_2023[5])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[5],receitaBruta_yb_TN_2024[4])} | {GR.crescimento(receitaBruta_yb_TN_2024[5],receitaBruta_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[5],premium_yb_TN_2024[4])} | {GR.crescimento(premium_yb_TN_2024[5],premium_yb_TN_2023[5])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[5],AdSense_yb_TN_2024[4])} | {GR.crescimento(AdSense_yb_TN_2024[5],AdSense_yb_TN_2023[5])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Jul'), GR.numeroPorExtensso(impressoes_yb_TN_2024[6]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[6]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[6]), GR.numeroPorExtensso(premium_yb_TN_2024[6]), GR.numeroPorExtensso(AdSense_yb_TN_2024[6])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[6],impressoes_yb_TN_2024[5])} | {GR.crescimento(impressoes_yb_TN_2024[6],impressoes_yb_TN_2023[6])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[6],visuMonetizadas_yb_TN_2024[5])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[6],visuMonetizadas_yb_TN_2023[6])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[6],receitaBruta_yb_TN_2024[5])} | {GR.crescimento(receitaBruta_yb_TN_2024[6],receitaBruta_yb_TN_2023[6])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[6],premium_yb_TN_2024[5])} | {GR.crescimento(premium_yb_TN_2024[6],premium_yb_TN_2023[6])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[6],AdSense_yb_TN_2024[5])} | {GR.crescimento(AdSense_yb_TN_2024[6],AdSense_yb_TN_2023[6])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Ago'), GR.numeroPorExtensso(impressoes_yb_TN_2024[7]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[7]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[7]), GR.numeroPorExtensso(premium_yb_TN_2024[7]), GR.numeroPorExtensso(AdSense_yb_TN_2024[7])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[7],impressoes_yb_TN_2024[6])} | {GR.crescimento(impressoes_yb_TN_2024[7],impressoes_yb_TN_2023[7])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[7],visuMonetizadas_yb_TN_2024[6])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[7],visuMonetizadas_yb_TN_2023[7])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[7],receitaBruta_yb_TN_2024[6])} | {GR.crescimento(receitaBruta_yb_TN_2024[7],receitaBruta_yb_TN_2023[7])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[7],premium_yb_TN_2024[6])} | {GR.crescimento(premium_yb_TN_2024[7],premium_yb_TN_2023[7])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[7],AdSense_yb_TN_2024[6])} | {GR.crescimento(AdSense_yb_TN_2024[7],AdSense_yb_TN_2023[7])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Set'), GR.numeroPorExtensso(impressoes_yb_TN_2024[8]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[8]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[8]), GR.numeroPorExtensso(premium_yb_TN_2024[8]), GR.numeroPorExtensso(AdSense_yb_TN_2024[8])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[8],impressoes_yb_TN_2024[7])} | {GR.crescimento(impressoes_yb_TN_2024[8],impressoes_yb_TN_2023[8])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[8],visuMonetizadas_yb_TN_2024[7])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[8],visuMonetizadas_yb_TN_2023[8])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[8],receitaBruta_yb_TN_2024[7])} | {GR.crescimento(receitaBruta_yb_TN_2024[8],receitaBruta_yb_TN_2023[8])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[8],premium_yb_TN_2024[7])} | {GR.crescimento(premium_yb_TN_2024[8],premium_yb_TN_2023[8])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[8],AdSense_yb_TN_2024[7])} | {GR.crescimento(AdSense_yb_TN_2024[8],AdSense_yb_TN_2023[8])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Out'), GR.numeroPorExtensso(impressoes_yb_TN_2024[9]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[9]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[9]), GR.numeroPorExtensso(premium_yb_TN_2024[9]), GR.numeroPorExtensso(AdSense_yb_TN_2024[9])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[9],impressoes_yb_TN_2024[8])} | {GR.crescimento(impressoes_yb_TN_2024[9],impressoes_yb_TN_2023[9])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[9],visuMonetizadas_yb_TN_2024[8])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[9],visuMonetizadas_yb_TN_2023[9])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[9],receitaBruta_yb_TN_2024[8])} | {GR.crescimento(receitaBruta_yb_TN_2024[9],receitaBruta_yb_TN_2023[9])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[9],premium_yb_TN_2024[8])} | {GR.crescimento(premium_yb_TN_2024[9],premium_yb_TN_2023[9])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[9],AdSense_yb_TN_2024[8])} | {GR.crescimento(AdSense_yb_TN_2024[9],AdSense_yb_TN_2023[9])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Nov'), GR.numeroPorExtensso(impressoes_yb_TN_2024[10]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[10]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[10]), GR.numeroPorExtensso(premium_yb_TN_2024[10]), GR.numeroPorExtensso(AdSense_yb_TN_2024[10])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[10],impressoes_yb_TN_2024[9])} | {GR.crescimento(impressoes_yb_TN_2024[10],impressoes_yb_TN_2023[10])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[10],visuMonetizadas_yb_TN_2024[9])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[10],visuMonetizadas_yb_TN_2023[10])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[10],receitaBruta_yb_TN_2024[9])} | {GR.crescimento(receitaBruta_yb_TN_2024[10],receitaBruta_yb_TN_2023[10])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[10],premium_yb_TN_2024[9])} | {GR.crescimento(premium_yb_TN_2024[10],premium_yb_TN_2023[10])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[10],AdSense_yb_TN_2024[9])} | {GR.crescimento(AdSense_yb_TN_2024[10],AdSense_yb_TN_2023[10])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Dez'), GR.numeroPorExtensso(impressoes_yb_TN_2024[11]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[11]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[11]), GR.numeroPorExtensso(premium_yb_TN_2024[11]), GR.numeroPorExtensso(AdSense_yb_TN_2024[11])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[11],impressoes_yb_TN_2024[10])} | {GR.crescimento(impressoes_yb_TN_2024[11],impressoes_yb_TN_2023[11])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[11],visuMonetizadas_yb_TN_2024[10])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[11],visuMonetizadas_yb_TN_2023[11])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[11],receitaBruta_yb_TN_2024[10])} | {GR.crescimento(receitaBruta_yb_TN_2024[11],receitaBruta_yb_TN_2023[11])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[11],premium_yb_TN_2024[10])} | {GR.crescimento(premium_yb_TN_2024[11],premium_yb_TN_2023[11])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[11],AdSense_yb_TN_2024[10])} | {GR.crescimento(AdSense_yb_TN_2024[11],AdSense_yb_TN_2023[11])}')))

path = plot_stacked_bar_with_custom_colors([visualizacoes_tn[-1], impressoes_yb_TN_2024[-1], visualizacoes_tn[-1], visuMonetizadas_yb_TN_2024[-1]])

doc.append(NewPage())
with doc.create(Subsection('', numbering=False)):
    doc.append("Monetização - YTB: Comparativo")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(path, width=NoEscape(r'1\textwidth'))
doc.append(NewPage())

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('YouTube - JPN: Monetização', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(5, data='Mês'), 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta (R$)', 'YTB Premium (R$)', 'Receita estimada (AdSense) (R$)'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | msm mês em 2023'), FootnoteText('mês anterior | msm mês em 2023'), FootnoteText('mês anterior | msm mês em 2023'), FootnoteText('mês anterior | msm mês em 2023'), FootnoteText('mês anterior | msm mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Jan'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[0]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[0]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[0]), GR.numeroPorExtensso(premium_yb_JPN_2024[0]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[0])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[0],impressoes_yb_JPN_2023[11])} | {GR.crescimento(impressoes_yb_JPN_2024[0],impressoes_yb_JPN_2023[0])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[0],visuMonetizadas_yb_JPN_2023[11])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[0],visuMonetizadas_yb_JPN_2023[0])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[0],receitaBruta_yb_JPN_2023[11])} | {GR.crescimento(receitaBruta_yb_JPN_2024[0],receitaBruta_yb_JPN_2023[0])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[0],premium_yb_JPN_2023[11])} | {GR.crescimento(premium_yb_JPN_2024[0],premium_yb_JPN_2023[0])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[0],AdSense_yb_JPN_2023[11])} | {GR.crescimento(AdSense_yb_JPN_2024[0],AdSense_yb_JPN_2023[0])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fev'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[1]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[1]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[1]), GR.numeroPorExtensso(premium_yb_JPN_2024[1]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[1],impressoes_yb_JPN_2024[0])} | {GR.crescimento(impressoes_yb_JPN_2024[1],impressoes_yb_JPN_2023[1])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[1],visuMonetizadas_yb_JPN_2024[0])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[1],visuMonetizadas_yb_JPN_2023[1])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[1],receitaBruta_yb_JPN_2024[0])} | {GR.crescimento(receitaBruta_yb_JPN_2024[1],receitaBruta_yb_JPN_2023[1])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[1],premium_yb_JPN_2024[0])} | {GR.crescimento(premium_yb_JPN_2024[1],premium_yb_JPN_2023[1])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[1],AdSense_yb_JPN_2024[0])} | {GR.crescimento(AdSense_yb_JPN_2024[1],AdSense_yb_JPN_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Mar'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[2]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[2]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[2]), GR.numeroPorExtensso(premium_yb_JPN_2024[2]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[2],impressoes_yb_JPN_2024[1])} | {GR.crescimento(impressoes_yb_JPN_2024[2],impressoes_yb_JPN_2023[2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[2],visuMonetizadas_yb_JPN_2024[1])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[2],visuMonetizadas_yb_JPN_2023[2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[2],receitaBruta_yb_JPN_2024[1])} | {GR.crescimento(receitaBruta_yb_JPN_2024[2],receitaBruta_yb_JPN_2023[2])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[2],premium_yb_JPN_2024[1])} | {GR.crescimento(premium_yb_JPN_2024[2],premium_yb_JPN_2023[2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[2],AdSense_yb_JPN_2024[1])} | {GR.crescimento(AdSense_yb_JPN_2024[2],AdSense_yb_JPN_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abr'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[3]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[3]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[3]), GR.numeroPorExtensso(premium_yb_JPN_2024[3]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[3],impressoes_yb_JPN_2024[2])} | {GR.crescimento(impressoes_yb_JPN_2024[3],impressoes_yb_JPN_2023[3])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[3],visuMonetizadas_yb_JPN_2024[2])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[3],visuMonetizadas_yb_JPN_2023[3])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[3],receitaBruta_yb_JPN_2024[2])} | {GR.crescimento(receitaBruta_yb_JPN_2024[3],receitaBruta_yb_JPN_2023[3])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[3],premium_yb_JPN_2024[2])} | {GR.crescimento(premium_yb_JPN_2024[3],premium_yb_JPN_2023[3])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[3],AdSense_yb_JPN_2024[2])} | {GR.crescimento(AdSense_yb_JPN_2024[3],AdSense_yb_JPN_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Mai'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[4]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[4]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[4]), GR.numeroPorExtensso(premium_yb_JPN_2024[4]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[4],impressoes_yb_JPN_2024[3])} | {GR.crescimento(impressoes_yb_JPN_2024[4],impressoes_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[4],visuMonetizadas_yb_JPN_2024[3])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[4],visuMonetizadas_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[4],receitaBruta_yb_JPN_2024[3])} | {GR.crescimento(receitaBruta_yb_JPN_2024[4],receitaBruta_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[4],premium_yb_JPN_2024[3])} | {GR.crescimento(premium_yb_JPN_2024[4],premium_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[4],AdSense_yb_JPN_2024[3])} | {GR.crescimento(AdSense_yb_JPN_2024[4],AdSense_yb_JPN_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Jun'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[5]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[5]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[5]), GR.numeroPorExtensso(premium_yb_JPN_2024[5]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[5],impressoes_yb_JPN_2024[4])} | {GR.crescimento(impressoes_yb_JPN_2024[5],impressoes_yb_JPN_2023[5])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[5],visuMonetizadas_yb_JPN_2024[4])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[5],visuMonetizadas_yb_JPN_2023[5])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[5],receitaBruta_yb_JPN_2024[4])} | {GR.crescimento(receitaBruta_yb_JPN_2024[5],receitaBruta_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[5],premium_yb_JPN_2024[4])} | {GR.crescimento(premium_yb_JPN_2024[5],premium_yb_JPN_2023[5])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[5],AdSense_yb_JPN_2024[4])} | {GR.crescimento(AdSense_yb_JPN_2024[5],AdSense_yb_JPN_2023[5])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Jul'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[6]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[6]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[6]), GR.numeroPorExtensso(premium_yb_JPN_2024[6]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[6])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[6],impressoes_yb_JPN_2024[5])} | {GR.crescimento(impressoes_yb_JPN_2024[6],impressoes_yb_JPN_2023[6])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[6],visuMonetizadas_yb_JPN_2024[5])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[6],visuMonetizadas_yb_JPN_2023[6])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[6],receitaBruta_yb_JPN_2024[5])} | {GR.crescimento(receitaBruta_yb_JPN_2024[6],receitaBruta_yb_JPN_2023[6])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[6],premium_yb_JPN_2024[5])} | {GR.crescimento(premium_yb_JPN_2024[6],premium_yb_JPN_2023[6])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[6],AdSense_yb_JPN_2024[5])} | {GR.crescimento(AdSense_yb_JPN_2024[6],AdSense_yb_JPN_2023[6])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Ago'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[7]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[7]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[7]), GR.numeroPorExtensso(premium_yb_JPN_2024[7]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[7])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[7],impressoes_yb_JPN_2024[6])} | {GR.crescimento(impressoes_yb_JPN_2024[7],impressoes_yb_JPN_2023[7])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[7],visuMonetizadas_yb_JPN_2024[6])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[7],visuMonetizadas_yb_JPN_2023[7])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[7],receitaBruta_yb_JPN_2024[6])} | {GR.crescimento(receitaBruta_yb_JPN_2024[7],receitaBruta_yb_JPN_2023[7])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[7],premium_yb_JPN_2024[6])} | {GR.crescimento(premium_yb_JPN_2024[7],premium_yb_JPN_2023[7])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[7],AdSense_yb_JPN_2024[6])} | {GR.crescimento(AdSense_yb_JPN_2024[7],AdSense_yb_JPN_2023[7])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Set'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[8]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[8]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[8]), GR.numeroPorExtensso(premium_yb_JPN_2024[8]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[8])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[8],impressoes_yb_JPN_2024[7])} | {GR.crescimento(impressoes_yb_JPN_2024[8],impressoes_yb_JPN_2023[8])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[8],visuMonetizadas_yb_JPN_2024[7])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[8],visuMonetizadas_yb_JPN_2023[8])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[8],receitaBruta_yb_JPN_2024[7])} | {GR.crescimento(receitaBruta_yb_JPN_2024[8],receitaBruta_yb_JPN_2023[8])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[8],premium_yb_JPN_2024[7])} | {GR.crescimento(premium_yb_JPN_2024[8],premium_yb_JPN_2023[8])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[8],AdSense_yb_JPN_2024[7])} | {GR.crescimento(AdSense_yb_JPN_2024[8],AdSense_yb_JPN_2023[8])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Out'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[9]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[9]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[9]), GR.numeroPorExtensso(premium_yb_JPN_2024[9]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[9])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[9],impressoes_yb_JPN_2024[8])} | {GR.crescimento(impressoes_yb_JPN_2024[9],impressoes_yb_JPN_2023[9])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[9],visuMonetizadas_yb_JPN_2024[8])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[9],visuMonetizadas_yb_JPN_2023[9])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[9],receitaBruta_yb_JPN_2024[8])} | {GR.crescimento(receitaBruta_yb_JPN_2024[9],receitaBruta_yb_JPN_2023[9])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[9],premium_yb_JPN_2024[8])} | {GR.crescimento(premium_yb_JPN_2024[9],premium_yb_JPN_2023[9])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[9],AdSense_yb_JPN_2024[8])} | {GR.crescimento(AdSense_yb_JPN_2024[9],AdSense_yb_JPN_2023[9])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Nov'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[10]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[10]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[10]), GR.numeroPorExtensso(premium_yb_JPN_2024[10]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[10])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[10],impressoes_yb_JPN_2024[9])} | {GR.crescimento(impressoes_yb_JPN_2024[10],impressoes_yb_JPN_2023[10])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[10],visuMonetizadas_yb_JPN_2024[9])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[10],visuMonetizadas_yb_JPN_2023[10])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[10],receitaBruta_yb_JPN_2024[9])} | {GR.crescimento(receitaBruta_yb_JPN_2024[10],receitaBruta_yb_JPN_2023[10])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[10],premium_yb_JPN_2024[9])} | {GR.crescimento(premium_yb_JPN_2024[10],premium_yb_JPN_2023[10])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[10],AdSense_yb_JPN_2024[9])} | {GR.crescimento(AdSense_yb_JPN_2024[10],AdSense_yb_JPN_2023[10])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Dez'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[11]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[11]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[11]), GR.numeroPorExtensso(premium_yb_JPN_2024[11]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[11])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[11],impressoes_yb_JPN_2024[10])} | {GR.crescimento(impressoes_yb_JPN_2024[11],impressoes_yb_JPN_2023[11])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[11],visuMonetizadas_yb_JPN_2024[10])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[11],visuMonetizadas_yb_JPN_2023[11])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[11],receitaBruta_yb_JPN_2024[10])} | {GR.crescimento(receitaBruta_yb_JPN_2024[11],receitaBruta_yb_JPN_2023[11])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[11],premium_yb_JPN_2024[10])} | {GR.crescimento(premium_yb_JPN_2024[11],premium_yb_JPN_2023[11])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[11],AdSense_yb_JPN_2024[10])} | {GR.crescimento(AdSense_yb_JPN_2024[11],AdSense_yb_JPN_2023[11])}')))

# with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
#     itemize.add_item("Mês anterior:")
#     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#         sublist.add_item(NoEscape(r"\textbf{Ago} "))
#         sublist.add_item(NoEscape(r"\textbf{Abr} "))
#         sublist.add_item(NoEscape(r""))

# with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
#     itemize.add_item("msm mês em 2023:")
#     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#         sublist.add_item(NoEscape(r""))

doc.append(NewPage())

# Adiciona informações extras
# Adiciona uma lista com marcadores
with doc.create(Itemize()) as itemize:
    # itemize.add_item('Em geral, Mar vem sendo o melhor mês da Tribuna do Norte nas redes sociais e Set o pior.')
    itemize.add_item('Legenda:')
    #doc.append(NoEscape(r'\newline'))
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r'\textbf{Impressões de anúncios:} quantidade de vezes que o anúncio apareceu na tela dos usuários, ou seja, o anúncio começou a ser carregado no dispositivo do usuário, e em alguns casos pode nem ter sido carregado por completo;'))
        sublist.add_item(NoEscape(r'\textbf{Visualizações monetizadas:} uma reprodução monetizada ocorre quando um espectador assiste um vídeo e pelo menos uma impressão de anúncios é exibida. Esse tipo de reprodução também é contabilizado quando o espectador para de assistir durante o anúncio precedente sem assistir o vídeo;'))
        sublist.add_item(NoEscape(r'\textbf{Receita bruta (R\$):} receita bruta estimada de todas as fontes de publicidade vendidas pelo Google para o período selecionado. Não se deve confundir receita de anúncios do YouTube com receita estimada ou receita líquida que são calculadas em seus contratos de participação nos lucros. ;'))
        sublist.add_item(NoEscape(r'\textbf{YouTube Premium (R\$):} receita estimada do YouTube Premium para o período selecionado;'))
        sublist.add_item(NoEscape(r'\textbf{Receita estimada (AdSense) (R\$):} receita estimada de publicidade vendida pelo Google AdSense para o período selecionado. Esse valor é o que é de direito do propietario do canal, já com os descontos feitos pelo YouTube de acordo com o contrato e o que diz respeito a participação de lucros.'))

# Gera o arquivo LaTeX
doc.generate_pdf(fr'C:\Users\{GR.path_aliss}\Documents\Repositórios\Relatórios\TN\Relatório-TNeJPN_DEZ_ytbMonetizacao-2024', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
