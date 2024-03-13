from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure
from pylatex.utils import bold
import rpy2.robjects as robjects
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.patches import Patch
# import seaborn as sns
# import defs
import graficosRelatorio as GR


robjects.r('''
    library(data.table)
    library(reshape2)
    library(ggthemes)
    library(ggplot2)
    library(dplyr)
    library(readr)
    library(knitr)
    library(reticulate)
    options(scipen=100)
    cor_fb <- "#3b5998"
    cor_ig <- "#d62976"
''')

# Cria um novo documento LaTeX
geometry_options = {"tmargin": "3cm", "rmargin": "2.5cm", "lmargin": "2.5cm"}
doc = Document(geometry_options=geometry_options)
#doc = Document()

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório de Redes Sociais e Portal")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Janeiro-Dezembro de 2023")))
        doc.append(LineBreak())

# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection('Resultados de dezembro/2023', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Portal'), '2,3 milhões', '18 milhões', '544 mil'))
                table.add_row(('', 'novos usuários', 'visualizações', 'usuários recorrentes'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Instagram'), '33,5 mil', '1,2 milhões', '1,2 milhões'))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Facebook'), '2,2 mil', '991 mil', '137 mil'))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Twitter'), '5,34 mil', '3,2 milhões', '57,3 mil'))
                table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), '639', '210 mil', '5,2 mil'))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item("Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, 1.722.122 novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube. Esse número representa uma queda de 26,4\\% com relação ao primeiro trimestre de 2023;")
            itemize.add_item(Command('textbf', arguments='Portal'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("O ganho de novos usuários cresceu 11,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 26\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("As visualizações cresceram 15,1\\% em relação ao mesmo período do ano anterior, tendo também queda de 1,9\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("Os usuários recorrentes cresceram 27,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 23,4\\% em relação ao primeiro trimestre de 2023.")
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='Facebook'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='Twitter'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='YouTube'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Portal', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos usuários', 'Visualizações', 'Usuários recorrentes'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2022'), FootnoteText('mês anterior | mesmo mês em 2022'), FootnoteText('mês anterior | mesmo mês em 2022')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '635 mil', '5 milhões', '203 mil'))
                table.add_row(('', FootnoteText('+35,7% | %'), FootnoteText('-7,4% | %'), FootnoteText('+18% | %')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item(Command('textbf', arguments='Mês anterior'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("O ganho de novos usuários cresceu 11,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 26\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("As visualizações cresceram 15,1\\% em relação ao mesmo período do ano anterior, tendo também queda de 1,9\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("Os usuários recorrentes cresceram 27,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 23,4\\% em relação ao primeiro trimestre de 2023.")
            itemize.add_item(Command('textbf', arguments='Mesmo mês em 2022'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("O ganho de novos usuários cresceu 11,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 26\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("As visualizações cresceram 15,1\\% em relação ao mesmo período do ano anterior, tendo também queda de 1,9\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("Os usuários recorrentes cresceram 27,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 23,4\\% em relação ao primeiro trimestre de 2023.")

# # Lê o arquivo CSV
# idade = pd.read_csv("idadeOut23.txt")

# # Calcula os totais das colunas de homens e mulheres,
# idade['t_h'] = ((0 * idade['h_fb']) + (28147 * idade['h_ig'])) / 28147
# idade['t_m'] = ((0 * idade['m_fb']) + (28147 * idade['m_ig'])) / 28147
# melted_data = pd.melt(idade, id_vars=['Idade'], value_vars=['t_m', 't_h'])
# sns.set(style="darkgrid") # Define o estilo do seaborn
# plt.figure(figsize=(10,6)) # Cria nova figura com o tamanho especificado
# sns.barplot(x='Idade', y='value', hue='variable', data=melted_data, palette=["#8700f9", "#00c4aa"]) # Cria o gráfico de barras. Recebe o que vai ficar em cada eixo.

# # Add rótulos e títulos ao gráfico
# plt.xlabel('Idade')
# plt.ylabel('Valor')
# plt.title('Audiência por faixa etária e gênero')

# for p in plt.gca().patches:
#     if p.get_height() > 0:
#         plt.gca().annotate(f'{p.get_height():.2f}%',  # Adiciona rótulo formatado com a altura da barra
#                             (p.get_x() + p.get_width() / 2., p.get_height()),
#                             ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=8)
        

# # Cria elementos de linha personalizados para a legenda
# legend_elements = [Patch(facecolor="#8700f9", edgecolor='w', label='Mulheres'),
#                     Patch(facecolor="#00c4aa", edgecolor='w', label='Homens')]

# # Exibição do gráfico com a legenda personalizada
# plt.legend(title="Gênero", handles=legend_elements)
# temp_plot_path = "C:/Users/Usuario/Desktop/Nova pasta/temp_plot.png"
# plt.savefig(temp_plot_path, bbox_inches="tight")
# plt.close()



doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{float}'))

# ORIGEM PORTAL
GR.origemPortal()       
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: origem dos usuários")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha

    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.origem_plot_path, width=NoEscape(r'1\textwidth'))

doc.append(NewPage())

# TOP10 PORTAL
GR.top10()
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: 10 notícias mais vistas")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha

    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.top10_plot_path, width=NoEscape(r'0.9\textwidth'))
        
# TOP15 PORTAL
GR.top15()
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: 15 notícias mais pesquisadas")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.top15_plot_path, width=NoEscape(r'0.9\textwidth'))

# VISUALIZAÇÕES E USUÁRIOS PORTAL
GR.visualizacoesUsuarios()
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: comparativo de visualizações e acessos de usuários")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.visualizacoesUsuarios_plot_path, width=NoEscape(r'0.8\textwidth'))
        
# VISUALIZAÇÕES POR FE PORTAL
GR.faixaEtaria()
# Adiciona uma seção ao documento
with doc.create(Subsection('', numbering=False)):
    doc.append("Portal: visualizações por faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.faixaEtaria_plot_path, width=NoEscape(r'0.8\textwidth'))

GR.faixaEtaria_desconhecidaAndTotal()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("Portal: visualizações por faixa etária (desconhecida e total)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.faixaEtaria_desconhecidaAndTotal_plot_path, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

with doc.create(Subsection('Resultados do 2º semestre/2023', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Portal'), '2,3 milhões', '18 milhões', '544 mil'))
                table.add_row(('', 'novos usuários', 'visualizações', 'usuários recorrentes'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Instagram'), '33,5 mil', '1,2 milhões', '1,2 milhões'))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Facebook'), '2,2 mil', '991 mil', '137 mil'))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Twitter'), '5,34 mil', '3,2 milhões', '57,3 mil'))
                table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), '639', '210 mil', '5,2 mil'))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item("Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, 1.722.122 novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube. Esse número representa uma queda de 26,4\\% com relação ao primeiro trimestre de 2023;")
            itemize.add_item(Command('textbf', arguments='Portal'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("O ganho de novos usuários cresceu 11,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 26\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("As visualizações cresceram 15,1\\% em relação ao mesmo período do ano anterior, tendo também queda de 1,9\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("Os usuários recorrentes cresceram 27,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 23,4\\% em relação ao primeiro trimestre de 2023.")
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='Facebook'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='Twitter'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='YouTube'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")

doc.append(NewPage())

with doc.create(Subsection('Resultado geral de 2023', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Portal'), '2,3 milhões', '18 milhões', '544 mil'))
                table.add_row(('', 'novos usuários', 'visualizações', 'usuários recorrentes'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Instagram'), '33,5 mil', '1,2 milhões', '1,2 milhões'))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Facebook'), '2,2 mil', '991 mil', '137 mil'))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Twitter'), '5,34 mil', '3,2 milhões', '57,3 mil'))
                table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), '639', '210 mil', '5,2 mil'))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item("Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, 1.722.122 novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube. Esse número representa uma queda de 26,4\\% com relação ao primeiro trimestre de 2023;")
            itemize.add_item(Command('textbf', arguments='Portal'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("O ganho de novos usuários cresceu 11,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 26\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("As visualizações cresceram 15,1\\% em relação ao mesmo período do ano anterior, tendo também queda de 1,9\\% em relação ao primeiro trimestre de 2023;")
                sublist.add_item("Os usuários recorrentes cresceram 27,8\\% em relação ao mesmo período do ano anterior, tendo também queda de 23,4\\% em relação ao primeiro trimestre de 2023.")
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='Facebook'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='Twitter'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")
            itemize.add_item(Command('textbf', arguments='YouTube'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("")
                sublist.add_item("")
                sublist.add_item("")

doc.append(NewPage())

# Gera o arquivo LaTeX
doc.generate_pdf('relatorio_redes_sociais', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
