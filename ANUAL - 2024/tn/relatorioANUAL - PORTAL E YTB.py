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
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "landscape": True}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório dO Portal e YouTube")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Anual de 2024")))
        doc.append(LineBreak())

# f'{p.get_height():.1f}%'
GR.path_aliss
GR.path_Usuarios

portal_usuariosUnicos_2023Table = [1310190,1436050,1795250,1313645,1296524,1043117,1214210,1250648,1201899,1586565,1433565,1479161]
portal_usuariosRescorrentes_2023Table = [610947,505622,904008,604270,617390,539523,582611,606820,558692,627700,655389,686461]

portal_usuariosUnicos_2023Analytics = [820000,1000000,1100000,839000,813000,604000,758000,775000,760000,1100000,963000,1000000]
portal_usuariosRescorrentes_2023Analytics = [203000,220000,302000,205000,192000,169000,175000,194000,186000,250000,270000,289000]

portal_visualizacoes_2023 = [5043133,2880374,9257203,5981878,6426837,5382596,6110187,6056062
,5531690,4401142,2948640,3120290] # mesmo valor na tabela e no analytics
portal_novosUsuarios_2023 = [635446,629702,837845,629077,639599,436361,586337,606078,573317,956925,747908,803205] # mesmo valor na tabela e no analytics

portal_usuariosUnicos_2024Table = [1633738,1440822,1360093,1686858,1523523,1409476,1753667,1898844,1370851,1902909,1451975,1796994]
portal_usuariosRescorrentes_2024Table = [723672,551399,610932,713143,695163,628876,647637,704678,612918,789103,596089,662969]

portal_usuariosUnicos_2024Analytics = [1100000,970000,872000,1100000,985000,936000,1300000,1400000,926000,1300000,1000000,1300000]
portal_usuariosRescorrentes_2024Analytics = [279000,248000,233000,267000,263000,244000,265000,306000,251000,341000,235000,269000]

portal_visualizacoes_2024 = [3503660,2645684,3109309,3569089,3274745,3006463,3524319,3505334,2813497,3824026,2889428,3274106] # mesmo valor na tabela e no analytics
portal_novosUsuarios_2024 = [819084,778346,726313,910001,812300,764468,1101211,1194579,759312,1119030,854130,1150202] # mesmo valor na tabela e no analytics

yb_inc_2023 = [147,222,467,257,277,287,343,323,240,275,277,310]
yb_inc_2023_perdeu = [48,68,81,42,56,61,65,64,55,46,63,62]
yb_visualizacoes_2023 = [34722,72406,102836,64296,66046,69167,83169,73401,53691,53629,78371,66752]
yb_horas_2023 = [844.7,1415.3,2890.7,1938.2,2018.3,2290.2,2405.9,1759.1,1389.1,1420.0,1690.8,1553.0]

yb_inc_2024 = [415,614,1506,1235,536,439,684,1690,1724,573,384,1025]
yb_inc_2024_perdeu = [85,84,110,97,83,76,100,142,172,111,72,108]
yb_visualizacoes_2024 = [132377,137318,371375,339297,139698,94934,175389,431106,657651,201390,129201,255163]
yb_horas_2024 = [2339,4194,5135,5316,3288,2302,2724,5438,9389,2692,1633,3867]

yb_inc_2024_total = [34000,34500,35940,37092,37544,37922,38507,40032,41578,42052,42354,43271]

# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection('Resultados anuais/2024', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Portal'), GR.formataNumero(sum(portal_novosUsuarios_2024)), GR.formataNumero(sum(portal_visualizacoes_2024)), GR.formataNumero(sum(portal_usuariosRescorrentes_2024Table)), GR.formataNumero(sum(portal_usuariosUnicos_2024Table))))
                table.add_row(('', 'novos usuários', 'visualizações', 'usuários recorrentes', 'usuários únicos'))
                table.add_hline()
                # table.add_row((MultiRow(2, data='Twitter'), '-', '-', '-'))
                # table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                # table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[0]), GR.formataNumero(sum(yb_visualizacoes_2024)), GR.formataNumero(sum(yb_horas_2024)), '-'))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição', '-'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item(f"Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, {GR.formataNumero(sum(portal_novosUsuarios_2024)+(yb_inc_2024_total[-1]-yb_inc_2024_total[0]))} novas contas, entre Portal e YouTube.")
            #+(tw_seg_2024_total[-1]-tw_seg_2024_total[-2])
            itemize.add_item(Command('textbf', arguments='YouTube'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(yb_inc_2024_total[-1])}. Total de seguidores no ano anterior: {GR.formataNumero(yb_inc_2024_total[0]-(yb_inc_2024[0]-yb_inc_2024_perdeu[0]))}")
                sublist.add_item(f"Seguidores adquiridos no ano: {GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[0]+sum(yb_inc_2024_perdeu))}. Deixaram de seguir: {GR.formataNumero(sum(yb_inc_2024_perdeu))}")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(yb_inc_2024_total[-1]-yb_inc_2024_total[0]+sum(yb_inc_2024_perdeu),sum(yb_inc_2024_perdeu))}")

doc.append(NewPage())

with doc.create(Subsection('Análise anual - 2024', numbering=False)):
    with doc.create(Subsubsection('Portal', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                table.add_row((MultiRow(3, data='Ano'), 'Novos usuários', 'Visualizações', 'Usuários recorrentes', 'Usuários únicos'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('Ano anterior'), FootnoteText('Ano anterior'), FootnoteText('Ano anterior'), FootnoteText('Ano anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data='2024'), GR.numeroPorExtensso(sum(portal_novosUsuarios_2024)), GR.numeroPorExtensso(sum(portal_visualizacoes_2024)), GR.numeroPorExtensso(sum(portal_usuariosRescorrentes_2024Table)), GR.numeroPorExtensso(sum(portal_usuariosUnicos_2024Table))))
                table.add_row(('', FootnoteText(f'{GR.crescimento(sum(portal_novosUsuarios_2024),sum(portal_novosUsuarios_2023))}'), FootnoteText(f'{GR.crescimento(sum(portal_visualizacoes_2024),sum(portal_visualizacoes_2023))}'), FootnoteText(f'{GR.crescimento(sum(portal_usuariosRescorrentes_2024Table),sum(portal_usuariosRescorrentes_2023Table))}'), FootnoteText(f'{GR.crescimento(sum(portal_usuariosUnicos_2024Table),sum(portal_usuariosUnicos_2023Table))}')))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal - 2024', numbering=False)):
    with doc.create(Subsubsection('Portal', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos usuários', 'Visualizações', 'Usuários recorrentes', 'Usuários únicos'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '819 mil', '3,5 milhões', '279 mil', GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[0])))
                table.add_row(('', FootnoteText('+2% | +29%'), FootnoteText('+13% | -30%'), FootnoteText('-3,5% | +37,4%'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[1],portal_usuariosUnicos_2023Table[11])} | {GR.crescimento(portal_usuariosUnicos_2024Table[1],portal_usuariosUnicos_2023Table[1])}'))) 
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[1]), GR.numeroPorExtensso(portal_visualizacoes_2024[1]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[1]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[1],portal_novosUsuarios_2024[0])} | {GR.crescimento(portal_novosUsuarios_2024[1],portal_novosUsuarios_2023[1])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[1],portal_visualizacoes_2024[0])} | {GR.crescimento(portal_visualizacoes_2024[1],portal_visualizacoes_2023[1])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[1],portal_usuariosRescorrentes_2024Table[0])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[1],portal_usuariosRescorrentes_2023Analytics[1])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[1],portal_usuariosUnicos_2024Table[0])} | {GR.crescimento(portal_usuariosUnicos_2024Table[1],portal_usuariosUnicos_2023Table[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(portal_novosUsuarios_2024[2]), GR.numeroPorExtensso(portal_visualizacoes_2024[2]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[2]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[2],portal_novosUsuarios_2024[1])} | {GR.crescimento(portal_novosUsuarios_2024[2],portal_novosUsuarios_2023[2])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[2],portal_visualizacoes_2024[1])} | {GR.crescimento(portal_visualizacoes_2024[2],portal_visualizacoes_2023[2])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[2],portal_usuariosRescorrentes_2024Table[1])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[2],portal_usuariosRescorrentes_2023Analytics[2])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[2],portal_usuariosUnicos_2024Table[1])} | {GR.crescimento(portal_usuariosUnicos_2024Table[2],portal_usuariosUnicos_2023Table[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(portal_novosUsuarios_2024[3]), GR.numeroPorExtensso(portal_visualizacoes_2024[3]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[3]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[3],portal_novosUsuarios_2024[2])} | {GR.crescimento(portal_novosUsuarios_2024[3],portal_novosUsuarios_2023[3])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[3],portal_visualizacoes_2024[2])} | {GR.crescimento(portal_visualizacoes_2024[3],portal_visualizacoes_2023[3])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[3],portal_usuariosRescorrentes_2024Table[2])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[3],portal_usuariosRescorrentes_2023Analytics[3])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[3],portal_usuariosUnicos_2024Table[2])} | {GR.crescimento(portal_usuariosUnicos_2024Table[3],portal_usuariosUnicos_2023Table[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(portal_novosUsuarios_2024[4]), GR.numeroPorExtensso(portal_visualizacoes_2024[4]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[4]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[4],portal_novosUsuarios_2024[3])} | {GR.crescimento(portal_novosUsuarios_2024[4],portal_novosUsuarios_2023[4])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[4],portal_visualizacoes_2024[3])} | {GR.crescimento(portal_visualizacoes_2024[4],portal_visualizacoes_2023[4])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[4],portal_usuariosRescorrentes_2024Table[3])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[4],portal_usuariosRescorrentes_2023Analytics[4])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[4],portal_usuariosUnicos_2024Table[3])} | {GR.crescimento(portal_usuariosUnicos_2024Table[4],portal_usuariosUnicos_2023Table[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(portal_novosUsuarios_2024[5]), GR.numeroPorExtensso(portal_visualizacoes_2024[5]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[5]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[5],portal_novosUsuarios_2024[4])} | {GR.crescimento(portal_novosUsuarios_2024[5],portal_novosUsuarios_2023[5])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[5],portal_visualizacoes_2024[4])} | {GR.crescimento(portal_visualizacoes_2024[5],portal_visualizacoes_2023[5])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[5],portal_usuariosRescorrentes_2024Table[4])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[5],portal_usuariosRescorrentes_2023Analytics[5])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[5],portal_usuariosUnicos_2024Table[4])} | {GR.crescimento(portal_usuariosUnicos_2024Table[5],portal_usuariosUnicos_2023Table[5])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(portal_novosUsuarios_2024[6]), GR.numeroPorExtensso(portal_visualizacoes_2024[6]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[6]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[6])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[6],portal_novosUsuarios_2024[5])} | {GR.crescimento(portal_novosUsuarios_2024[6],portal_novosUsuarios_2023[6])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[6],portal_visualizacoes_2024[5])} | {GR.crescimento(portal_visualizacoes_2024[6],portal_visualizacoes_2023[6])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[6],portal_usuariosRescorrentes_2024Table[5])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[6],portal_usuariosRescorrentes_2023Analytics[6])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[6],portal_usuariosUnicos_2024Table[5])} | {GR.crescimento(portal_usuariosUnicos_2024Table[6],portal_usuariosUnicos_2023Table[6])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(portal_novosUsuarios_2024[7]), GR.numeroPorExtensso(portal_visualizacoes_2024[7]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[7]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[7])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[7],portal_novosUsuarios_2024[6])} | {GR.crescimento(portal_novosUsuarios_2024[7],portal_novosUsuarios_2023[7])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[7],portal_visualizacoes_2024[6])} | {GR.crescimento(portal_visualizacoes_2024[7],portal_visualizacoes_2023[7])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[7],portal_usuariosRescorrentes_2024Table[6])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[7],portal_usuariosRescorrentes_2023Analytics[7])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[7],portal_usuariosUnicos_2024Table[6])} | {GR.crescimento(portal_usuariosUnicos_2024Table[7],portal_usuariosUnicos_2023Table[7])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[8]), GR.numeroPorExtensso(portal_visualizacoes_2024[8]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[8]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[8])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[8],portal_novosUsuarios_2024[7])} | {GR.crescimento(portal_novosUsuarios_2024[8],portal_novosUsuarios_2023[8])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[8],portal_visualizacoes_2024[7])} | {GR.crescimento(portal_visualizacoes_2024[8],portal_visualizacoes_2023[8])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[8],portal_usuariosRescorrentes_2024Table[7])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[8],portal_usuariosRescorrentes_2023Analytics[8])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[8],portal_usuariosUnicos_2024Table[7])} | {GR.crescimento(portal_usuariosUnicos_2024Table[8],portal_usuariosUnicos_2023Table[8])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[9]), GR.numeroPorExtensso(portal_visualizacoes_2024[9]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[9]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[9])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[9],portal_novosUsuarios_2024[8])} | {GR.crescimento(portal_novosUsuarios_2024[9],portal_novosUsuarios_2023[9])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[9],portal_visualizacoes_2024[8])} | {GR.crescimento(portal_visualizacoes_2024[9],portal_visualizacoes_2023[9])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[9],portal_usuariosRescorrentes_2024Table[8])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[9],portal_usuariosRescorrentes_2023Analytics[9])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[9],portal_usuariosUnicos_2024Table[8])} | {GR.crescimento(portal_usuariosUnicos_2024Table[9],portal_usuariosUnicos_2023Table[9])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[10]), GR.numeroPorExtensso(portal_visualizacoes_2024[10]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[10]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[10])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[10],portal_novosUsuarios_2024[9])} | {GR.crescimento(portal_novosUsuarios_2024[10],portal_novosUsuarios_2023[10])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[10],portal_visualizacoes_2024[9])} | {GR.crescimento(portal_visualizacoes_2024[10],portal_visualizacoes_2023[10])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[10],portal_usuariosRescorrentes_2024Table[9])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[10],portal_usuariosRescorrentes_2023Analytics[10])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[10],portal_usuariosUnicos_2024Table[9])} | {GR.crescimento(portal_usuariosUnicos_2024Table[10],portal_usuariosUnicos_2023Table[10])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[11]), GR.numeroPorExtensso(portal_visualizacoes_2024[11]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Table[11]), GR.numeroPorExtensso(portal_usuariosUnicos_2024Table[11])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[11],portal_novosUsuarios_2024[10])} | {GR.crescimento(portal_novosUsuarios_2024[11],portal_novosUsuarios_2023[11])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[11],portal_visualizacoes_2024[10])} | {GR.crescimento(portal_visualizacoes_2024[11],portal_visualizacoes_2023[11])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Table[11],portal_usuariosRescorrentes_2024Table[10])} | {GR.crescimento(portal_usuariosRescorrentes_2024Table[11],portal_usuariosRescorrentes_2023Analytics[11])}'), FootnoteText(f'{GR.crescimento(portal_usuariosUnicos_2024Table[11],portal_usuariosUnicos_2024Table[10])} | {GR.crescimento(portal_usuariosUnicos_2024Table[11],portal_usuariosUnicos_2023Table[11])}')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     itemize.add_item(Command('textbf', arguments='Mês anterior'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")
        #     itemize.add_item(Command('textbf', arguments='Mesmo mês em 2023'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")
        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Legenda:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Usuários únicos:} número de usuários únicos que interagiram com seu site ou app. É qualquer usuário que tenha uma sessão engajada ou quando o Google Analytics coleta o evento "first\_open", que é quando o usuário abre o site pela primeira vez dentro do período especificado;'))
                sublist.add_item(NoEscape(r'\textbf{Novos usuários:} número de novos usuários únicos que visitaram o site ou app pela primeira vez;'))
                sublist.add_item(NoEscape(r'\textbf{Usuários recorrentes:} número de usuários que iniciaram pelo menos uma sessão anterior, independentemente de ter sido ou não uma sessão engajada no período especificado;'))
                sublist.add_item(NoEscape(r'\textbf{Visualizações:} quantas telas do app para dispositivos móveis ou páginas da Web seus usuários acessaram. Exibições repetidas de uma única tela ou página são consideradas. Nesse caso tembém deve ser lavada em consideração a informação de que Jonathas fez alterações em relação as exibições repetidas;'))
                sublist.add_item(NoEscape(r'\textbf{Sessões engajadas:} correspondem ao número de sessões com mais de 10 segundos, que geraram um ou mais eventos de conversão ou tiveram duas ou mais visualizações de página/tela. Vá para a ultima página para saber a definição de uma sessão de acordo com o Google Analytics.'))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mês anterior:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"\textbf{Agosto} foi o melhor mês em \textbf{novos usuários}."))
        sublist.add_item(NoEscape(r"\textbf{Outubro} foi o melhor mês em \textbf{visualizações e usuários recorrentes}. \textbf{Agosto} também teve bons números nessa métricas, assim como \textbf{abril e julho}."))
        sublist.add_item(NoEscape(r"Apesar de ter o maior crecimento percentual nas visualizações, \textbf{março} não é o melhor mês como foi em foi 2023. Além disso, tem os menores números de \textbf{novos usuários}."))
        sublist.add_item(NoEscape(r"\textbf{Outubro} é o melhor mês em geral e muito disso é por conta das eleições."))
        sublist.add_item(NoEscape(r"\textbf{Setembro} tem queda em relação a agosto, que foi um bom mês, e fica abaixo da maioria dos outros meses em todas as métricas."))
        sublist.add_item(NoEscape(r"\textbf{Agosto e outubro} são os meses com mais \textbf{usuários únicos}. \textbf{Dezembro} vem na sequência."))
        
doc.append(NewPage())

NovosUsu_plot_path = GR.novosUsu(portal_novosUsuarios_2023, portal_novosUsuarios_2024)
Recorrentes_plot_path = GR.usuRecorrentes(portal_usuariosRescorrentes_2023Table, portal_usuariosRescorrentes_2024Table)
Visua_plot_path = GR.visualizacoes(portal_visualizacoes_2023, portal_visualizacoes_2024)
Usuunico_plot_path = GR.usuUnicos(portal_usuariosUnicos_2023Table, portal_usuariosUnicos_2024Table)

with doc.create(Subsection('', numbering=False)):
    doc.append("Portal (MENSAL): novos usuários, visualizações, usuários recorrentes e usuários únicos")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(NovosUsu_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(Visua_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(Recorrentes_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(Usuunico_plot_path, width=NoEscape(r'1\textwidth'))

doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{float}'))


doc.append(NewPage())

NovosUsu_plot_path_ANUAL = GR.novosUsu_ANUAL(sum(portal_novosUsuarios_2023), sum(portal_novosUsuarios_2024))
Recorrentes_plot_path_ANUAL = GR.usuRecorrentes_ANUAL(sum(portal_usuariosRescorrentes_2023Table), sum(portal_usuariosRescorrentes_2024Table))
Visua_plot_path_ANUAL = GR.visualizacoes_ANUAL(sum(portal_visualizacoes_2023), sum(portal_visualizacoes_2024))
Usuunico_plot_path_ANUAL = GR.usuUnicos_ANUAL(sum(portal_usuariosUnicos_2023Table), sum(portal_usuariosUnicos_2024Table))

with doc.create(Subsection('', numbering=False)):
    doc.append("Portal (ANUAL): novos usuários, visualizações, usuários recorrentes e usuários únicos")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(NovosUsu_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(Visua_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(Recorrentes_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(Usuunico_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))

doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{float}'))


doc.append(NewPage())

sexoPortal = GR.grafico_de_rosca(50.3, 49.7)

with doc.create(Subsection('', numbering=False)):
    doc.append("Portal (ANUAL): Gênero dos Usuários")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(sexoPortal, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Portal - Análise Anual:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"Em comparação com 2023, 2024 ficou abaixo do ano anterior apenas em \textbf{visualizações} por, aproximadamente, \textbf{38.3\%}."))
        sublist.add_item(NoEscape(r"As métricas do portal, como \textbf{usuários únicos, recorrentes e novos}, apresentaram resultados melhores em 2024 em comparação ao ano anterior. Isso indica um aumento no número total de acessos ao portal. No entanto, como já foi dito, as visualizações foram mais baixas que no ano anterior. Desta forma, podemos dizer que houve uma redução no número médio de páginas visualizadas por sessão, ou seja, os usuários acessaram menos publicações por visita."))
        sublist.add_item(NoEscape(r"Apesar de ter sido ano de eleições municipais, os meses de \textbf{outubro e novembro} tiveram menos \textbf{visualizações} em 2024 e menos \textbf{usuários recorrentes} em \textbf{novembro}."))
        sublist.add_item(NoEscape(r"Em geral, o ano de 2024 foi sim melhor que 2023, pois tivemos mais acessos de usuários no portal."))
        sublist.add_item(NoEscape(r"E diferente de 2023 que o público era de aproximadamente 10\% mais homens, em 2024 foi tivemos um público feminino maior, sendo aproximadamente 0.6\% superior."))

doc.append(NewPage())

with doc.create(Subsection('Análise anual - 2024', numbering=False)):
    with doc.create(Subsubsection('YouTube', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                table.add_row((MultiRow(3, data='Ano'), 'Novos inscritos', 'Visualizações', 'Horas de exibição'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('Ano anterior'), FootnoteText('Ano anterior'), FootnoteText('Ano anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data='2024'), GR.numeroPorExtensso(sum(yb_inc_2024)), GR.numeroPorExtensso(sum(yb_visualizacoes_2024)), GR.numeroPorExtensso(sum(yb_horas_2024))))
                table.add_row(('', FootnoteText(f'{GR.crescimento(sum(yb_inc_2024),sum(yb_inc_2023))}'), FootnoteText(f'{GR.crescimento(sum(yb_visualizacoes_2024),sum(yb_visualizacoes_2023))}'), FootnoteText(f'{GR.crescimento(sum(yb_horas_2024),sum(yb_horas_2023))}')))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("YouTube - Análise Anual:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"O YouTube teve exelentes resultados em todas as métricas analisadas, com 2024 superando 2023 em tudo."))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal - 2024', numbering=False)):
    with doc.create(Subsubsection('YouTube', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos inscritos', 'Visualizações', 'Horas de exibição'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '484', '132 mil', '2,3 mil'))
                table.add_row(('', FootnoteText('+95,2% | +389%'), FootnoteText('+95,3% | +288%'), FootnoteText('+48% | +172,2%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(yb_inc_2024[1]), GR.numeroPorExtensso(yb_visualizacoes_2024[1]), GR.numeroPorExtensso(yb_horas_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[1],yb_inc_2024[0])} | {GR.crescimento(yb_inc_2024[1],yb_inc_2023[1])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[1],yb_visualizacoes_2024[0])} | {GR.crescimento(yb_visualizacoes_2024[1],yb_visualizacoes_2023[1])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[1],yb_horas_2024[0])} | {GR.crescimento(yb_horas_2024[1],yb_horas_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(yb_inc_2024[2]), GR.numeroPorExtensso(yb_visualizacoes_2024[2]), GR.numeroPorExtensso(yb_horas_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[2],yb_inc_2024[1])} | {GR.crescimento(yb_inc_2024[2],yb_inc_2023[2])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[2],yb_visualizacoes_2024[1])} | {GR.crescimento(yb_visualizacoes_2024[2],yb_visualizacoes_2023[2])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[2],yb_horas_2024[1])} | {GR.crescimento(yb_horas_2024[2],yb_horas_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(yb_inc_2024[3]), GR.numeroPorExtensso(yb_visualizacoes_2024[3]), GR.numeroPorExtensso(yb_horas_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[3],yb_inc_2024[2])} | {GR.crescimento(yb_inc_2024[3],yb_inc_2023[3])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[3],yb_visualizacoes_2024[2])} | {GR.crescimento(yb_visualizacoes_2024[3],yb_visualizacoes_2023[3])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[3],yb_horas_2024[2])} | {GR.crescimento(yb_horas_2024[3],yb_horas_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(yb_inc_2024[4]), GR.numeroPorExtensso(yb_visualizacoes_2024[4]), GR.numeroPorExtensso(yb_horas_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[4],yb_inc_2024[3])} | {GR.crescimento(yb_inc_2024[4],yb_inc_2023[4])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[4],yb_visualizacoes_2024[3])} | {GR.crescimento(yb_visualizacoes_2024[4],yb_visualizacoes_2023[4])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[4],yb_horas_2024[3])} | {GR.crescimento(yb_horas_2024[4],yb_horas_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(yb_inc_2024[5]), GR.numeroPorExtensso(yb_visualizacoes_2024[5]), GR.numeroPorExtensso(yb_horas_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[5],yb_inc_2024[4])} | {GR.crescimento(yb_inc_2024[5],yb_inc_2023[5])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[5],yb_visualizacoes_2024[4])} | {GR.crescimento(yb_visualizacoes_2024[5],yb_visualizacoes_2023[5])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[5],yb_horas_2024[4])} | {GR.crescimento(yb_horas_2024[5],yb_horas_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(yb_inc_2024[6]), GR.numeroPorExtensso(yb_visualizacoes_2024[6]), GR.numeroPorExtensso(yb_horas_2024[6])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[6],yb_inc_2024[5])} | {GR.crescimento(yb_inc_2024[6],yb_inc_2023[6])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[6],yb_visualizacoes_2024[5])} | {GR.crescimento(yb_visualizacoes_2024[6],yb_visualizacoes_2023[6])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[6],yb_horas_2024[5])} | {GR.crescimento(yb_horas_2024[6],yb_horas_2023[6])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(yb_inc_2024[7]), GR.numeroPorExtensso(yb_visualizacoes_2024[7]), GR.numeroPorExtensso(yb_horas_2024[7])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[7],yb_inc_2024[6])} | {GR.crescimento(yb_inc_2024[7],yb_inc_2023[7])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[7],yb_visualizacoes_2024[6])} | {GR.crescimento(yb_visualizacoes_2024[7],yb_visualizacoes_2023[7])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[7],yb_horas_2024[6])} | {GR.crescimento(yb_horas_2024[7],yb_horas_2023[7])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(yb_inc_2024[8]), GR.numeroPorExtensso(yb_visualizacoes_2024[8]), GR.numeroPorExtensso(yb_horas_2024[8])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[8],yb_inc_2024[7])} | {GR.crescimento(yb_inc_2024[8],yb_inc_2023[8])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[8],yb_visualizacoes_2024[7])} | {GR.crescimento(yb_visualizacoes_2024[8],yb_visualizacoes_2023[8])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[8],yb_horas_2024[7])} | {GR.crescimento(yb_horas_2024[8],yb_horas_2023[8])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(yb_inc_2024[9]), GR.numeroPorExtensso(yb_visualizacoes_2024[9]), GR.numeroPorExtensso(yb_horas_2024[9])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[9],yb_inc_2024[8])} | {GR.crescimento(yb_inc_2024[9],yb_inc_2023[9])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[9],yb_visualizacoes_2024[8])} | {GR.crescimento(yb_visualizacoes_2024[9],yb_visualizacoes_2023[9])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[9],yb_horas_2024[8])} | {GR.crescimento(yb_horas_2024[9],yb_horas_2023[9])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(yb_inc_2024[10]), GR.numeroPorExtensso(yb_visualizacoes_2024[10]), GR.numeroPorExtensso(yb_horas_2024[10])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[10],yb_inc_2024[9])} | {GR.crescimento(yb_inc_2024[10],yb_inc_2023[10])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[10],yb_visualizacoes_2024[9])} | {GR.crescimento(yb_visualizacoes_2024[10],yb_visualizacoes_2023[10])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[10],yb_horas_2024[9])} | {GR.crescimento(yb_horas_2024[10],yb_horas_2023[10])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(yb_inc_2024[11]), GR.numeroPorExtensso(yb_visualizacoes_2024[11]), GR.numeroPorExtensso(yb_horas_2024[11])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[11],yb_inc_2024[10])} | {GR.crescimento(yb_inc_2024[11],yb_inc_2023[11])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[11],yb_visualizacoes_2024[10])} | {GR.crescimento(yb_visualizacoes_2024[11],yb_visualizacoes_2023[11])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[11],yb_horas_2024[10])} | {GR.crescimento(yb_horas_2024[11],yb_horas_2023[11])}')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     itemize.add_item(Command('textbf', arguments='Mês anterior'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")
        #     itemize.add_item(Command('textbf', arguments='Mesmo mês em 2023'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item("")
        #         sublist.add_item("")
        #         sublist.add_item("")

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mês anterior:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"\textbf{Agosto} foi o 2º melhor mês. \textbf{Março} vem em seguida e ambos possuem bons crecimentos percentuais."))
        sublist.add_item(NoEscape(r"\textbf{Abril} foi o primeiro mês com quedas após uma sequência de crescimento."))
        sublist.add_item(NoEscape(r"De \textbf{abril} a \textbf{junho} as métricas pararam de crescer. A partir de \textbf{julho} as métricas continuaram crescendo até \textbf{setembro}, o que nos mostra um certo pradrão com 3 meses crescendo, seguidos de 3 meses de queda e mais 3 messes de crescimento em sequência. O padrão não segue o ano inteiro pois \textbf{dezembro} não continuou a queda que vinha ocorrendo a partir de \textbf{outubro}."))
        sublist.add_item(NoEscape(r"\textbf{Setembro} é o melhor mês. Importante observar que o mês de \textbf{setembro} no portal, apesar de números altos, ainda ficou abaixo da maioria dos outros meses."))
        sublist.add_item(NoEscape(r"\textbf{Outubro} quabra a sequência de crescimento iniciada em \textbf{julho} e essa queda vai até \textbf{novembro}, quabrando o padrão iniciado onde haviam 3 meses de crescimento e 3 de queda nos números."))
        sublist.add_item(NoEscape(r"\textbf{Novembro} é o mês com o menor número de \textbf{novos inscritos e horas de exibição}. Em \textbf{visualizações} só não está abaixo de \textbf{junho}."))

doc.append(NewPage())

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Funcionamento dos algoritmos:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{YouTube:} O algoritmo do YouTube tem como objetivo aumentar o tempo de permanência dos usuários na plataforma, recomendando os vídeos que eles têm mais chances de assistir e se engajar. Para isso, ele considera fatores como o histórico de visualização, as preferências, as inscrições, a localização e o feedback dos usuários. Ele também leva em conta a qualidade e a relevância dos vídeos, analisando aspectos como o título, descrição, tags, miniaturas e os metadados.'))

doc.append(NewPage())

with doc.create(MiniPage(align='c')):
    doc.append(MediumText(("Observações")))

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Sessões:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(f'Por padrão, a sessão é encerrada após 30 minutos de inatividade, mas é possível ajustar esse limite para que ela dure de alguns segundos a várias horas.'))
            with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
                sublist.add_item(NoEscape('O Google Analytics começa a contar a partir do momento em que um usuário acessa seu site. Se depois de 30 minutos este usuário não fizer uma interação, a sessão é finalizada. No entanto, toda vez que ocorre uma interação com um elemento (como um evento, interação de rede social ou uma nova página), o Google Analytics reinicia o tempo de vencimento adicionando 30 minutos a partir do momento da interação.\n Um único usuário pode abrir várias sessões. Essas sessões podem ocorrer no mesmo dia ou em vários dias, semanas ou meses. Assim que uma sessão termina, existe a oportunidade de iniciar uma nova sessão. Há dois métodos para o encerramento de uma sessão:'))
            with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
                sublist.add_item(NoEscape('Um único usuário pode abrir várias sessões. Essas sessões podem ocorrer no mesmo dia ou em vários dias, semanas ou meses. Assim que uma sessão termina, existe a oportunidade de iniciar uma nova sessão. Há dois métodos para o encerramento de uma sessão:'))
                with sublist.create(Enumerate(enumeration_symbol=r"•")) as subsublist:
                    subsublist.add_item(NoEscape('Vencimento por tempo:'))
                    with subsublist.create(Enumerate(enumeration_symbol=r"•")) as subsubsublist:
                        subsubsublist.add_item(NoEscape('Depois de 30 minutos de inatividade;'))
                        subsubsublist.add_item(NoEscape('À meia-noite.'))
                with sublist.create(Enumerate(enumeration_symbol=r"•")) as subsublist:
                    subsublist.add_item(NoEscape('Mudança de campanha::'))
                    with subsublist.create(Enumerate(enumeration_symbol=r"•")) as subsubsublist:
                        subsubsublist.add_item(NoEscape('Se um usuário entra por uma campanha, sai e depois volta para outra. (Fecha o site e entra novamente, por exemplo).'))
            itemize.add_item('Seguidores:')
            with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
                sublist.add_item(NoEscape(f'É  possível observar que o número de novos seguidores ou inscritos adquiridos nos mês pode diferir um pouco na primeira tabela, na descrição dela e em cada uma das tabelas seguintes das respectivas redes sociais.'))
                sublist.add_item(NoEscape(f'Nas tabelas de cada rede social está a quantidade total de usuários que seguiram ao logo do mês analisado, mas nesse caso é o dado que foi informado diretamente pela rede social em questão. Chamaremos esse dado de "follows" e os que deixaram de seguir de "unfollows", para uma melhor identificação.'))
                sublist.add_item(NoEscape(f'Na primeira tabela do relatório está o númere referente a quantidade de seguidores que realmente continuaram seguindo a(o) página/perfil/canal ao final do mês. Logo abaixo, o dado "Seguidores adquiridos no mês:" é a quantidade total de usuários que seguiram ao logo do mês analisado. Nesses dois casos os valores são obtidos atraves da quantidade total de seguidores no mês atual e anterior e quantos usuários deixaram de seguir no mês atual.'))
                sublist.add_item(NoEscape(f'Por exemplo: se subtrairmos a quantidade total de seguidores do mês atual pela anterior e somarmos isso a quantos deixaram de seguir (atual - anterior + unfollow), teremos a quantidade total de "Seguidores adquiridos no mês:". Esse valor seria o mesmo dado de seguidores adquiridos que está nas tabelas de cada rede social (follows). E a quantidade de usuários que continuaram seguindo a página seria apenas a diferença do total de seguidores do mês atual e anterior (atual - anterior), que deveria dar no mesmo de subtrair "follows" por "unfollows" (follows - unfollows). Para que fique mais claro, a diferença entre "follows" e "unfollows" somada a quantidade total de seguidores do mês anterior deveria ser igual a quantidade total do mês atual (follows - unfollows + total seg. anterior = total seg. atual).'))
                sublist.add_item(NoEscape(f'Todos esses dados são fornecidos pelas próprias plataformas, mas eles podem acabar sendo um pouco diferentes para sua respectiva rede social.'))
                
                
# Gera o arquivo LaTeX
doc.generate_pdf(fr'C:\Users\{GR.path_aliss}\Documents\Repositórios\Relatórios\TN\Relatório-ANUAL_PORTAL E YTB-2024', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")