from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage, Math
from pylatex.utils import bold
import graficosRelatorio as GR
import pandas as pd
import rpy2.robjects as robjects


# robjects.r('''
#     library(data.table)
#     library(reshape2)
#     library(ggthemes)
#     library(ggplot2)
#     library(dplyr)
#     library(readr)
#     library(knitr)
#     library(reticulate)
#     options(scipen=100)
#     cor_fb <- "#3b5998"
#     cor_ig <- "#d62976"
# ''')

# Cria um novo documento LaTeX
geometry_options = {"tmargin": "2cm", "rmargin": "0cm", "lmargin": "0cm"}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório da Monetização")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Setembro de 2024")))
        doc.append(LineBreak())

# f'{p.get_height():.1f}%'
GR.path_aliss
GR.path_Usuarios

#YOUTUBE - TN: MONETIZAÇÃO
impressoes_yb_TN_2023=[]
visuMonetizadas_yb_TN_2023=[]
receitaBruta_yb_TN_2023=[]
premium_yb_TN_2023=[]
AdSense_yb_TN_2023=[]

impressoes_yb_TN_2024=[]
visuMonetizadas_yb_TN_2024=[]
receitaBruta_yb_TN_2024=[]
premium_yb_TN_2024=[]
AdSense_yb_TN_2024=[]

#YOUTUBE - JPN: MONETIZAÇÃO
impressoes_yb_JPN_2023=[]
visuMonetizadas_yb_JPN_2023=[]
receitaBruta_yb_JPN_2023=[]
premium_yb_JPN_2023=[]
AdSense_yb_JPN_2023=[]

impressoes_yb_JPN_2024=[]
visuMonetizadas_yb_JPN_2024=[]
receitaBruta_yb_JPN_2024=[]
premium_yb_JPN_2024=[]
AdSense_yb_JPN_2024=[]

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('YouTube - TN: Monetização', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(5, data='Mês'), 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta ', 'YTB Premium', 'Receita estimada (AdSense)'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), GR.numeroPorExtensso(impressoes_yb_TN_2024[0]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[0]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[0]), GR.numeroPorExtensso(premium_yb_TN_2024[0]), GR.numeroPorExtensso(AdSense_yb_TN_2024[0])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[0],impressoes_yb_TN_2023[11])} | {GR.crescimento(impressoes_yb_TN_2024[0],impressoes_yb_TN_2023[0])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[0],visuMonetizadas_yb_TN_2023[11])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[0],visuMonetizadas_yb_TN_2023[0])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[0],receitaBruta_yb_TN_2023[11])} | {GR.crescimento(receitaBruta_yb_TN_2024[0],receitaBruta_yb_TN_2023[0])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[0],premium_yb_TN_2023[11])} | {GR.crescimento(premium_yb_TN_2024[0],premium_yb_TN_2023[0])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[0],AdSense_yb_TN_2023[11])} | {GR.crescimento(AdSense_yb_TN_2024[0],AdSense_yb_TN_2023[0])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(impressoes_yb_TN_2024[1]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[1]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[1]), GR.numeroPorExtensso(premium_yb_TN_2024[1]), GR.numeroPorExtensso(AdSense_yb_TN_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[1],impressoes_yb_TN_2024[0])} | {GR.crescimento(impressoes_yb_TN_2024[1],impressoes_yb_TN_2023[1])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[1],visuMonetizadas_yb_TN_2024[0])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[1],visuMonetizadas_yb_TN_2023[1])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[1],receitaBruta_yb_TN_2024[0])} | {GR.crescimento(receitaBruta_yb_TN_2024[1],receitaBruta_yb_TN_2023[1])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[1],premium_yb_TN_2024[0])} | {GR.crescimento(premium_yb_TN_2024[1],premium_yb_TN_2023[1])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[1],AdSense_yb_TN_2024[0])} | {GR.crescimento(AdSense_yb_TN_2024[1],AdSense_yb_TN_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(impressoes_yb_TN_2024[2]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[2]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[2],impressoes_yb_TN_2024[1])} | {GR.crescimento(impressoes_yb_TN_2024[2],impressoes_yb_TN_2023[2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[2],visuMonetizadas_yb_TN_2024[1])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[2],visuMonetizadas_yb_TN_2023[2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[2],receitaBruta_yb_TN_2024[1])} | {GR.crescimento(receitaBruta_yb_TN_2024[2],receitaBruta_yb_TN_2023[2])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[2],premium_yb_TN_2024[1])} | {GR.crescimento(premium_yb_TN_2024[2],premium_yb_TN_2023[2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[2],AdSense_yb_TN_2024[1])} | {GR.crescimento(AdSense_yb_TN_2024[2],AdSense_yb_TN_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(impressoes_yb_TN_2024[3]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[3]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[3],impressoes_yb_TN_2024[2])} | {GR.crescimento(impressoes_yb_TN_2024[3],impressoes_yb_TN_2023[3])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[3],visuMonetizadas_yb_TN_2024[2])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[3],visuMonetizadas_yb_TN_2023[3])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[3],receitaBruta_yb_TN_2024[2])} | {GR.crescimento(receitaBruta_yb_TN_2024[3],receitaBruta_yb_TN_2023[3])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[3],premium_yb_TN_2024[2])} | {GR.crescimento(premium_yb_TN_2024[3],premium_yb_TN_2023[3])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[3],AdSense_yb_TN_2024[2])} | {GR.crescimento(AdSense_yb_TN_2024[3],AdSense_yb_TN_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(impressoes_yb_TN_2024[4]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[4]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[4],impressoes_yb_TN_2024[3])} | {GR.crescimento(impressoes_yb_TN_2024[4],impressoes_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[4],visuMonetizadas_yb_TN_2024[3])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[4],visuMonetizadas_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[4],receitaBruta_yb_TN_2024[3])} | {GR.crescimento(receitaBruta_yb_TN_2024[4],receitaBruta_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[4],premium_yb_TN_2024[3])} | {GR.crescimento(premium_yb_TN_2024[4],premium_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[4],AdSense_yb_TN_2024[3])} | {GR.crescimento(AdSense_yb_TN_2024[4],AdSense_yb_TN_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(impressoes_yb_TN_2024[5]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[5]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[5],impressoes_yb_TN_2024[4])} | {GR.crescimento(impressoes_yb_TN_2024[5],impressoes_yb_TN_2023[5])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[5],visuMonetizadas_yb_TN_2024[4])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[5],visuMonetizadas_yb_TN_2023[5])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[5],receitaBruta_yb_TN_2024[4])} | {GR.crescimento(receitaBruta_yb_TN_2024[5],receitaBruta_yb_TN_2023[4])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[5],premium_yb_TN_2024[4])} | {GR.crescimento(premium_yb_TN_2024[5],premium_yb_TN_2023[5])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[5],AdSense_yb_TN_2024[4])} | {GR.crescimento(AdSense_yb_TN_2024[5],AdSense_yb_TN_2023[5])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(impressoes_yb_TN_2024[6]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[6]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[6])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[6],impressoes_yb_TN_2024[5])} | {GR.crescimento(impressoes_yb_TN_2024[6],impressoes_yb_TN_2023[6])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[6],visuMonetizadas_yb_TN_2024[5])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[6],visuMonetizadas_yb_TN_2023[6])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[6],receitaBruta_yb_TN_2024[5])} | {GR.crescimento(receitaBruta_yb_TN_2024[6],receitaBruta_yb_TN_2023[6])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[6],premium_yb_TN_2024[5])} | {GR.crescimento(premium_yb_TN_2024[6],premium_yb_TN_2023[6])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[6],AdSense_yb_TN_2024[5])} | {GR.crescimento(AdSense_yb_TN_2024[6],AdSense_yb_TN_2023[6])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(impressoes_yb_TN_2024[7]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[7]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[7])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[7],impressoes_yb_TN_2024[6])} | {GR.crescimento(impressoes_yb_TN_2024[7],impressoes_yb_TN_2023[7])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[7],visuMonetizadas_yb_TN_2024[6])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[7],visuMonetizadas_yb_TN_2023[7])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[7],receitaBruta_yb_TN_2024[6])} | {GR.crescimento(receitaBruta_yb_TN_2024[7],receitaBruta_yb_TN_2023[7])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[7],premium_yb_TN_2024[6])} | {GR.crescimento(premium_yb_TN_2024[7],premium_yb_TN_2023[7])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[7],AdSense_yb_TN_2024[6])} | {GR.crescimento(AdSense_yb_TN_2024[7],AdSense_yb_TN_2023[7])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(impressoes_yb_TN_2024[8]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[8]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[8])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[8],impressoes_yb_TN_2024[7])} | {GR.crescimento(impressoes_yb_TN_2024[8],impressoes_yb_TN_2023[8])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[8],visuMonetizadas_yb_TN_2024[7])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[8],visuMonetizadas_yb_TN_2023[8])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[8],receitaBruta_yb_TN_2024[7])} | {GR.crescimento(receitaBruta_yb_TN_2024[8],receitaBruta_yb_TN_2023[8])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[8],premium_yb_TN_2024[7])} | {GR.crescimento(premium_yb_TN_2024[8],premium_yb_TN_2023[8])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[8],AdSense_yb_TN_2024[7])} | {GR.crescimento(AdSense_yb_TN_2024[8],AdSense_yb_TN_2023[8])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(impressoes_yb_TN_2024[9]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[9]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[9])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[9],impressoes_yb_TN_2024[8])} | {GR.crescimento(impressoes_yb_TN_2024[9],impressoes_yb_TN_2023[9])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[9],visuMonetizadas_yb_TN_2024[8])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[9],visuMonetizadas_yb_TN_2023[9])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[9],receitaBruta_yb_TN_2024[8])} | {GR.crescimento(receitaBruta_yb_TN_2024[9],receitaBruta_yb_TN_2023[9])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[9],premium_yb_TN_2024[8])} | {GR.crescimento(premium_yb_TN_2024[9],premium_yb_TN_2023[9])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[9],AdSense_yb_TN_2024[8])} | {GR.crescimento(AdSense_yb_TN_2024[9],AdSense_yb_TN_2023[9])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(impressoes_yb_TN_2024[10]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[10]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[10])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[10],impressoes_yb_TN_2024[9])} | {GR.crescimento(impressoes_yb_TN_2024[10],impressoes_yb_TN_2023[10])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[10],visuMonetizadas_yb_TN_2024[9])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[10],visuMonetizadas_yb_TN_2023[10])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[10],receitaBruta_yb_TN_2024[9])} | {GR.crescimento(receitaBruta_yb_TN_2024[10],receitaBruta_yb_TN_2023[10])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[10],premium_yb_TN_2024[9])} | {GR.crescimento(premium_yb_TN_2024[10],premium_yb_TN_2023[10])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[10],AdSense_yb_TN_2024[9])} | {GR.crescimento(AdSense_yb_TN_2024[10],AdSense_yb_TN_2023[10])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(impressoes_yb_TN_2024[11]), GR.numeroPorExtensso(visuMonetizadas_yb_TN_2024[11]), GR.numeroPorExtensso(receitaBruta_yb_TN_2024[11])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN_2024[11],impressoes_yb_TN_2024[10])} | {GR.crescimento(impressoes_yb_TN_2024[11],impressoes_yb_TN_2023[11])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN_2024[11],visuMonetizadas_yb_TN_2024[10])} | {GR.crescimento(visuMonetizadas_yb_TN_2024[11],visuMonetizadas_yb_TN_2023[11])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN_2024[11],receitaBruta_yb_TN_2024[10])} | {GR.crescimento(receitaBruta_yb_TN_2024[11],receitaBruta_yb_TN_2023[11])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN_2024[11],premium_yb_TN_2024[10])} | {GR.crescimento(premium_yb_TN_2024[11],premium_yb_TN_2023[11])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN_2024[11],AdSense_yb_TN_2024[10])} | {GR.crescimento(AdSense_yb_TN_2024[11],AdSense_yb_TN_2023[11])}')))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mês anterior:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"\textbf{Agosto} "))
        sublist.add_item(NoEscape(r"\textbf{Abril} "))
        sublist.add_item(NoEscape(r""))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mesmo mês em 2023:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r""))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('YouTube - JPN: Monetização', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(5, data='Mês'), 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta ', 'YTB Premium', 'Receita estimada (AdSense)'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '484', '132 mil', '2,3 mil'))
                table.add_row(('', FootnoteText('+95,2% | +389%'), FootnoteText('+95,3% | +288%'), FootnoteText('+48% | +172,2%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[1]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[1]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[1]), GR.numeroPorExtensso(premium_yb_JPN_2024[1]), GR.numeroPorExtensso(AdSense_yb_JPN_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[1],impressoes_yb_JPN_2024[0])} | {GR.crescimento(impressoes_yb_JPN_2024[1],impressoes_yb_JPN_2023[1])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[1],visuMonetizadas_yb_JPN_2024[0])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[1],visuMonetizadas_yb_JPN_2023[1])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[1],receitaBruta_yb_JPN_2024[0])} | {GR.crescimento(receitaBruta_yb_JPN_2024[1],receitaBruta_yb_JPN_2023[1])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[1],premium_yb_JPN_2024[0])} | {GR.crescimento(premium_yb_JPN_2024[1],premium_yb_JPN_2023[1])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[1],AdSense_yb_JPN_2024[0])} | {GR.crescimento(AdSense_yb_JPN_2024[1],AdSense_yb_JPN_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[2]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[2]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[2],impressoes_yb_JPN_2024[1])} | {GR.crescimento(impressoes_yb_JPN_2024[2],impressoes_yb_JPN_2023[2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[2],visuMonetizadas_yb_JPN_2024[1])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[2],visuMonetizadas_yb_JPN_2023[2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[2],receitaBruta_yb_JPN_2024[1])} | {GR.crescimento(receitaBruta_yb_JPN_2024[2],receitaBruta_yb_JPN_2023[2])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[2],premium_yb_JPN_2024[1])} | {GR.crescimento(premium_yb_JPN_2024[2],premium_yb_JPN_2023[2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[2],AdSense_yb_JPN_2024[1])} | {GR.crescimento(AdSense_yb_JPN_2024[2],AdSense_yb_JPN_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[3]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[3]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[3],impressoes_yb_JPN_2024[2])} | {GR.crescimento(impressoes_yb_JPN_2024[3],impressoes_yb_JPN_2023[3])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[3],visuMonetizadas_yb_JPN_2024[2])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[3],visuMonetizadas_yb_JPN_2023[3])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[3],receitaBruta_yb_JPN_2024[2])} | {GR.crescimento(receitaBruta_yb_JPN_2024[3],receitaBruta_yb_JPN_2023[3])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[3],premium_yb_JPN_2024[2])} | {GR.crescimento(premium_yb_JPN_2024[3],premium_yb_JPN_2023[3])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[3],AdSense_yb_JPN_2024[2])} | {GR.crescimento(AdSense_yb_JPN_2024[3],AdSense_yb_JPN_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[4]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[4]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[4],impressoes_yb_JPN_2024[3])} | {GR.crescimento(impressoes_yb_JPN_2024[4],impressoes_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[4],visuMonetizadas_yb_JPN_2024[3])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[4],visuMonetizadas_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[4],receitaBruta_yb_JPN_2024[3])} | {GR.crescimento(receitaBruta_yb_JPN_2024[4],receitaBruta_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[4],premium_yb_JPN_2024[3])} | {GR.crescimento(premium_yb_JPN_2024[4],premium_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[4],AdSense_yb_JPN_2024[3])} | {GR.crescimento(AdSense_yb_JPN_2024[4],AdSense_yb_JPN_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[5]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[5]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[5],impressoes_yb_JPN_2024[4])} | {GR.crescimento(impressoes_yb_JPN_2024[5],impressoes_yb_JPN_2023[5])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[5],visuMonetizadas_yb_JPN_2024[4])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[5],visuMonetizadas_yb_JPN_2023[5])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[5],receitaBruta_yb_JPN_2024[4])} | {GR.crescimento(receitaBruta_yb_JPN_2024[5],receitaBruta_yb_JPN_2023[4])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[5],premium_yb_JPN_2024[4])} | {GR.crescimento(premium_yb_JPN_2024[5],premium_yb_JPN_2023[5])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[5],AdSense_yb_JPN_2024[4])} | {GR.crescimento(AdSense_yb_JPN_2024[5],AdSense_yb_JPN_2023[5])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[6]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[6]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[6])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[6],impressoes_yb_JPN_2024[5])} | {GR.crescimento(impressoes_yb_JPN_2024[6],impressoes_yb_JPN_2023[6])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[6],visuMonetizadas_yb_JPN_2024[5])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[6],visuMonetizadas_yb_JPN_2023[6])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[6],receitaBruta_yb_JPN_2024[5])} | {GR.crescimento(receitaBruta_yb_JPN_2024[6],receitaBruta_yb_JPN_2023[6])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[6],premium_yb_JPN_2024[5])} | {GR.crescimento(premium_yb_JPN_2024[6],premium_yb_JPN_2023[6])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[6],AdSense_yb_JPN_2024[5])} | {GR.crescimento(AdSense_yb_JPN_2024[6],AdSense_yb_JPN_2023[6])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[7]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[7]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[7])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[7],impressoes_yb_JPN_2024[6])} | {GR.crescimento(impressoes_yb_JPN_2024[7],impressoes_yb_JPN_2023[7])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[7],visuMonetizadas_yb_JPN_2024[6])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[7],visuMonetizadas_yb_JPN_2023[7])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[7],receitaBruta_yb_JPN_2024[6])} | {GR.crescimento(receitaBruta_yb_JPN_2024[7],receitaBruta_yb_JPN_2023[7])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[7],premium_yb_JPN_2024[6])} | {GR.crescimento(premium_yb_JPN_2024[7],premium_yb_JPN_2023[7])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[7],AdSense_yb_JPN_2024[6])} | {GR.crescimento(AdSense_yb_JPN_2024[7],AdSense_yb_JPN_2023[7])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[8]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[8]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[8])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[8],impressoes_yb_JPN_2024[7])} | {GR.crescimento(impressoes_yb_JPN_2024[8],impressoes_yb_JPN_2023[8])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[8],visuMonetizadas_yb_JPN_2024[7])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[8],visuMonetizadas_yb_JPN_2023[8])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[8],receitaBruta_yb_JPN_2024[7])} | {GR.crescimento(receitaBruta_yb_JPN_2024[8],receitaBruta_yb_JPN_2023[8])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[8],premium_yb_JPN_2024[7])} | {GR.crescimento(premium_yb_JPN_2024[8],premium_yb_JPN_2023[8])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[8],AdSense_yb_JPN_2024[7])} | {GR.crescimento(AdSense_yb_JPN_2024[8],AdSense_yb_JPN_2023[8])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[9]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[9]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[9])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[9],impressoes_yb_JPN_2024[8])} | {GR.crescimento(impressoes_yb_JPN_2024[9],impressoes_yb_JPN_2023[9])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[9],visuMonetizadas_yb_JPN_2024[8])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[9],visuMonetizadas_yb_JPN_2023[9])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[9],receitaBruta_yb_JPN_2024[8])} | {GR.crescimento(receitaBruta_yb_JPN_2024[9],receitaBruta_yb_JPN_2023[9])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[9],premium_yb_JPN_2024[8])} | {GR.crescimento(premium_yb_JPN_2024[9],premium_yb_JPN_2023[9])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[9],AdSense_yb_JPN_2024[8])} | {GR.crescimento(AdSense_yb_JPN_2024[9],AdSense_yb_JPN_2023[9])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[10]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[10]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[10])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[10],impressoes_yb_JPN_2024[9])} | {GR.crescimento(impressoes_yb_JPN_2024[10],impressoes_yb_JPN_2023[10])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[10],visuMonetizadas_yb_JPN_2024[9])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[10],visuMonetizadas_yb_JPN_2023[10])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[10],receitaBruta_yb_JPN_2024[9])} | {GR.crescimento(receitaBruta_yb_JPN_2024[10],receitaBruta_yb_JPN_2023[10])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[10],premium_yb_JPN_2024[9])} | {GR.crescimento(premium_yb_JPN_2024[10],premium_yb_JPN_2023[10])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[10],AdSense_yb_JPN_2024[9])} | {GR.crescimento(AdSense_yb_JPN_2024[10],AdSense_yb_JPN_2023[10])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(impressoes_yb_JPN_2024[11]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN_2024[11]), GR.numeroPorExtensso(receitaBruta_yb_JPN_2024[11])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN_2024[11],impressoes_yb_JPN_2024[10])} | {GR.crescimento(impressoes_yb_JPN_2024[11],impressoes_yb_JPN_2023[11])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN_2024[11],visuMonetizadas_yb_JPN_2024[10])} | {GR.crescimento(visuMonetizadas_yb_JPN_2024[11],visuMonetizadas_yb_JPN_2023[11])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN_2024[11],receitaBruta_yb_JPN_2024[10])} | {GR.crescimento(receitaBruta_yb_JPN_2024[11],receitaBruta_yb_JPN_2023[11])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN_2024[11],premium_yb_JPN_2024[10])} | {GR.crescimento(premium_yb_JPN_2024[11],premium_yb_JPN_2023[11])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN_2024[11],AdSense_yb_JPN_2024[10])} | {GR.crescimento(AdSense_yb_JPN_2024[11],AdSense_yb_JPN_2023[11])}')))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mês anterior:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"\textbf{Agosto} "))
        sublist.add_item(NoEscape(r"\textbf{Abril} "))
        sublist.add_item(NoEscape(r""))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mesmo mês em 2023:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r""))

doc.append(NewPage())

# Adiciona informações extras
# Adiciona uma lista com marcadores
with doc.create(Itemize()) as itemize:
    # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
    itemize.add_item('Legenda:')
    #doc.append(NoEscape(r'\newline'))
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r'\textbf{Impressões de anúncios:} quantidade de vezes que o anúncio apareceu na tela dos usuários, ou seja, o anúncio começou a ser carregado no dispositivo do usuário, e em alguns casos pode nem ter sido carregado por completo;'))
        sublist.add_item(NoEscape(r'\textbf{Visualizações monetizadas:} uma reprodução monetizada ocorre quando um espectador assiste um vídeo e pelo menos uma impressão de anúncios é exibida. Esse tipo de reprodução também é contabilizado quando o espectador para de assistir durante o anúncio precedente sem assistir o vídeo;'))
        sublist.add_item(NoEscape(r'\textbf{Receita bruta (R\$):} receita bruta estimada de todas as fontes de publicidade vendidas pelo Google para o período selecionado. Não se deve confundir receita de anúncios do YouTube com receita estimada ou receita líquida que são calculadas em seus contratos de participação nos lucros. ;'))
        sublist.add_item(NoEscape(r'\textbf{YouTube Premium (R\$):} receita estimada do YouTube Premium para o período selecionado;'))
        sublist.add_item(NoEscape(r'\textbf{Receita estimada (AdSense) (R\$):} receita estimada de publicidade vendida pelo Google AdSense para o período selecionado. Esse valor é o que é de direito do propietario do canal, já com os descontos feitos pelo YouTube de acordo com o contrato e o que diz respeito a participação de lucros.'))

# Gera o arquivo LaTeX
doc.generate_pdf(fr'C:\Users\{GR.path_aliss}\Documents\Repositórios\Relatórios\TN\Relatório-TN_SET_ytbMonetizacao-2024', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
