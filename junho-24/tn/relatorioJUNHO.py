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
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "lmargin": "2.5cm"}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório das Redes Sociais e Portal")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Junho de 2024")))
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

portal_usuariosUnicos_2024Table = [1633738,1440822,1360093,1686858,1523523,1409476]
portal_usuariosRescorrentes_2024Table = [723672,551399,610932,713143,695163,628876]

portal_usuariosUnicos_2024Analytics = [1100000,970000,872000,1100000,985000,936000]
portal_usuariosRescorrentes_2024Analytics = [279000,248000,233000,267000,263000,244000]

portal_visualizacoes_2024 = [3503660,2645684,3109309,3569089,3274745,3006463] # mesmo valor na tabela e no analytics
portal_novosUsuarios_2024 = [819084,778346,726313,910001,812300,764468] # mesmo valor na tabela e no analytics

ig_seg_2023 = [1240,8640,22600,6150,3514,5242,6672,5785,7315,6451,6106,5683]
ig_seg_2023_perdeu = [0,0,0,0,2794,4279,5165,4624,4585,4906,4988,4763]
ig_alcance_2023 = [669864,642671,715617,569749,541961,533116,570764,530776,515617,571695,543975,582262]
ig_vivitas_2023 = [205736,245144,739332,162899,156869,128295,142502,147638,143376,132933,135058,129676]

ig_seg_2024 = [6931,5816,5835,7843,6717,5573]
ig_seg_2024_perdeu = [5485,4945,4587,4885,4649,4326]
ig_alcance_2024 = [542064,658917,633648,847362,941640,930258]
ig_vivitas_2024 = [151885,144742,131296,162036,133497,117925]

ig_seg_2024_total = [529865,530797,532444,535373,537733,538756]

fb_seg_2023 = [524,401,1316,362,386,273,293,223,172,186,248,455]
fb_seg_2023_perdeu = [97,72,102,54,50,42,63,53,44,73,146,152]
fb_alcance_2023 = [506283,459876,655223,310292,338973,250577,333882,258987,259921,336781,389143,492038]
fb_vivitas_2023 = [30707,24425,81866,36040,34809,29306,26755,27793,26507,25099,29348,29167]

fb_seg_2024 = [628,389,188,295,254,251]
fb_seg_2024_perdeu = [162,162,176,171,158,132]
fb_alcance_2024 = [467889,390008,197628,292192,257199,254134]
fb_vivitas_2024 = [32152,31459,31499,31612,29294,22864]

fb_seg_2024_total = [332603,332614,332419,332336,332214,332133]

tw_seg_2023 = [1649,863,2823,2825,392,347,519,997,1454,1864,2169,2599]
#tw_seg_2023_perdeu = []
tw_impressões_2023 = [0,578375,1305007,1196504,1043859,1029266,782790,587558,285029,354720,391759,429655]
tw_engajamentos_2023 = [0,11089,31977,20510,20347,19405,16967,13004,8337,8112,9825,10816]

tw_seg_2024 = [2867,2002,2084,3679,6005]
tw_impressões_2024 = [455800,421287,420268,439319,378514]
tw_engajamentos_2024 = [13186,11223,12340,14842,14386]

tw_seg_2024_total = [311129,312006,312146,312900,317307]
tw_seg_2024_perdeu = [890,tw_seg_2024[1]-(tw_seg_2024_total[1]-tw_seg_2024_total[0]),tw_seg_2024[2]-(tw_seg_2024_total[2]-tw_seg_2024_total[1]),tw_seg_2024[3]-(tw_seg_2024_total[3]-tw_seg_2024_total[2]),tw_seg_2024[4]-(tw_seg_2024_total[4]-tw_seg_2024_total[3])] #sabe a quantidade que perdeu de acordo com a diferença de seguidores entre um mês e outro e o ganho total de seguidores no mês

yb_inc_2023 = [147,222,467,257,277,287,343,323,240,275,277,310]
yb_inc_2023_perdeu = [48,68,81,42,56,61,65,64,55,46,63,62]
yb_visualizacoes_2023 = [34722,72406,102836,64296,66046,69167,83169,73401,53691,53629,78371,66752]
yb_horas_2023 = [844.7,1415.3,2890.7,1938.2,2018.3,2290.2,2405.9,1759.1,1389.1,1420.0,1690.8,1553.0]

yb_inc_2024 = [415,614,1506,1235,536,439]
yb_inc_2024_perdeu = [85,84,110,97,83,76]
yb_visualizacoes_2024 = [132377,137318,371375,339297,139698,94934]
yb_horas_2024 = [2339,4194,5135,5316,3288,2302]

yb_inc_2024_total = [34000,34500,35940,37092,37544,37922]

# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection('Resultados de junho/2024', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Portal'), GR.formataNumero(portal_novosUsuarios_2024[-1]), GR.formataNumero(portal_visualizacoes_2024[-1]), GR.formataNumero(portal_usuariosRescorrentes_2024Analytics[-1])))
                table.add_row(('', 'novos usuários', 'visualizações', 'usuários recorrentes'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Instagram'), GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]), GR.formataNumero(ig_alcance_2024[-1]), GR.formataNumero(ig_vivitas_2024[-1])))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Facebook'), GR.formataNumero(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]), GR.formataNumero(fb_alcance_2024[-1]), GR.formataNumero(fb_vivitas_2024[-1])))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Twitter'), '-', '-', '-'))
                table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]), GR.formataNumero(yb_visualizacoes_2024[-1]), GR.formataNumero(yb_horas_2024[-1])))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item(f"Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, {GR.formataNumero(portal_novosUsuarios_2024[1]+(ig_seg_2024_total[-1]-ig_seg_2024_total[-2])+(fb_seg_2024_total[-1]-fb_seg_2024_total[-2])+(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]))} novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube.")
            #+(tw_seg_2024_total[-1]-tw_seg_2024_total[-2])
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(ig_seg_2024_total[-1])}. Total de seguidores no mês anterior: {GR.formataNumero(ig_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos no mês: {GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]+ig_seg_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(ig_seg_2024_perdeu[-1])}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]+ig_seg_2024_perdeu[-1],ig_seg_2024_perdeu[-1])}")
            itemize.add_item(Command('textbf', arguments='Facebook'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(fb_seg_2024_total[-1])}. Total de seguidores no mês anterior: {GR.formataNumero(fb_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos no mês: {GR.formataNumero(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]+fb_seg_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(fb_seg_2024_perdeu[-1])}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]+fb_seg_2024_perdeu[-1],fb_seg_2024_perdeu[-1])}")
                sublist.add_item(f"Obs.: nesse caso, a taxa de fixação negatíva se trata de uma diferença relmente baixa, visto que tanto 'Seguidores adquiridos na semana' quanto 'Deixaram de seguir' são números positivos.")
            itemize.add_item(Command('textbf', arguments='Twitter'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("Total de seguidores atual: -. Total de seguidores no mês anterior: -")
                sublist.add_item("Seguidores adquiridos no mês: -. Deixaram de seguir: -.")
                sublist.add_item("Taxa de fixação: -")
            itemize.add_item(Command('textbf', arguments='YouTube'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(yb_inc_2024_total[-1])}. Total de seguidores no mês anterior: {GR.formataNumero(yb_inc_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos no mês: {GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]+yb_inc_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(yb_inc_2024_perdeu[-1])}")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]+yb_inc_2024_perdeu[-1],yb_inc_2024_perdeu[-1])}")

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Portal', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos usuários', 'Visualizações', 'Usuários recorrentes'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '819 mil', '3,5 milhões', '279 mil'))
                table.add_row(('', FootnoteText('+2% | +29%'), FootnoteText('+13% | -30%'), FootnoteText('-3,5% | +37,4%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[1]), GR.numeroPorExtensso(portal_visualizacoes_2024[1]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[1],portal_novosUsuarios_2024[0])} | {GR.crescimento(portal_novosUsuarios_2024[1],portal_novosUsuarios_2023[1])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[1],portal_visualizacoes_2024[0])} | {GR.crescimento(portal_visualizacoes_2024[1],portal_visualizacoes_2023[1])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[1],portal_usuariosRescorrentes_2024Analytics[0])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[1],portal_usuariosRescorrentes_2023Analytics[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(portal_novosUsuarios_2024[2]), GR.numeroPorExtensso(portal_visualizacoes_2024[2]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[2],portal_novosUsuarios_2024[1])} | {GR.crescimento(portal_novosUsuarios_2024[2],portal_novosUsuarios_2023[2])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[2],portal_visualizacoes_2024[1])} | {GR.crescimento(portal_visualizacoes_2024[2],portal_visualizacoes_2023[2])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[2],portal_usuariosRescorrentes_2024Analytics[1])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[2],portal_usuariosRescorrentes_2023Analytics[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(portal_novosUsuarios_2024[3]), GR.numeroPorExtensso(portal_visualizacoes_2024[3]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[3],portal_novosUsuarios_2024[2])} | {GR.crescimento(portal_novosUsuarios_2024[3],portal_novosUsuarios_2023[3])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[3],portal_visualizacoes_2024[2])} | {GR.crescimento(portal_visualizacoes_2024[3],portal_visualizacoes_2023[3])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[3],portal_usuariosRescorrentes_2024Analytics[2])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[3],portal_usuariosRescorrentes_2023Analytics[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(portal_novosUsuarios_2024[4]), GR.numeroPorExtensso(portal_visualizacoes_2024[4]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[4],portal_novosUsuarios_2024[3])} | {GR.crescimento(portal_novosUsuarios_2024[4],portal_novosUsuarios_2023[4])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[4],portal_visualizacoes_2024[3])} | {GR.crescimento(portal_visualizacoes_2024[4],portal_visualizacoes_2023[4])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[4],portal_usuariosRescorrentes_2024Analytics[3])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[4],portal_usuariosRescorrentes_2023Analytics[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(portal_novosUsuarios_2024[5]), GR.numeroPorExtensso(portal_visualizacoes_2024[5]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[5],portal_novosUsuarios_2024[4])} | {GR.crescimento(portal_novosUsuarios_2024[5],portal_novosUsuarios_2023[5])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[5],portal_visualizacoes_2024[4])} | {GR.crescimento(portal_visualizacoes_2024[5],portal_visualizacoes_2023[5])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[5],portal_usuariosRescorrentes_2024Analytics[4])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[5],portal_usuariosRescorrentes_2023Analytics[5])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(portal_novosUsuarios_2024[6]), GR.numeroPorExtensso(portal_visualizacoes_2024[6]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[6])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[6],portal_novosUsuarios_2024[5])} | {GR.crescimento(portal_novosUsuarios_2024[6],portal_novosUsuarios_2023[6])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[6],portal_visualizacoes_2024[5])} | {GR.crescimento(portal_visualizacoes_2024[6],portal_visualizacoes_2023[6])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[6],portal_usuariosRescorrentes_2024Analytics[5])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[6],portal_usuariosRescorrentes_2023Analytics[6])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(portal_novosUsuarios_2024[7]), GR.numeroPorExtensso(portal_visualizacoes_2024[7]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[7],portal_novosUsuarios_2024[6])} | {GR.crescimento(portal_novosUsuarios_2024[7],portal_novosUsuarios_2023[7])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[7],portal_visualizacoes_2024[6])} | {GR.crescimento(portal_visualizacoes_2024[7],portal_visualizacoes_2023[7])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[7],portal_usuariosRescorrentes_2024Analytics[6])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[7],portal_usuariosRescorrentes_2023Analytics[7])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[8]), GR.numeroPorExtensso(portal_visualizacoes_2024[8]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[8])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[8],portal_novosUsuarios_2024[7])} | {GR.crescimento(portal_novosUsuarios_2024[8],portal_novosUsuarios_2023[8])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[8],portal_visualizacoes_2024[7])} | {GR.crescimento(portal_visualizacoes_2024[8],portal_visualizacoes_2023[8])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[8],portal_usuariosRescorrentes_2024Analytics[7])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[8],portal_usuariosRescorrentes_2023Analytics[8])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[9]), GR.numeroPorExtensso(portal_visualizacoes_2024[9]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[9])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[9],portal_novosUsuarios_2024[8])} | {GR.crescimento(portal_novosUsuarios_2024[9],portal_novosUsuarios_2023[9])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[9],portal_visualizacoes_2024[8])} | {GR.crescimento(portal_visualizacoes_2024[9],portal_visualizacoes_2023[9])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[9],portal_usuariosRescorrentes_2024Analytics[8])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[9],portal_usuariosRescorrentes_2023Analytics[9])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[10]), GR.numeroPorExtensso(portal_visualizacoes_2024[10]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[10])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[10],portal_novosUsuarios_2024[9])} | {GR.crescimento(portal_novosUsuarios_2024[10],portal_novosUsuarios_2023[10])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[10],portal_visualizacoes_2024[9])} | {GR.crescimento(portal_visualizacoes_2024[10],portal_visualizacoes_2023[10])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[10],portal_usuariosRescorrentes_2024Analytics[9])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[10],portal_usuariosRescorrentes_2023Analytics[10])}')))
                # # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[11]), GR.numeroPorExtensso(portal_visualizacoes_2024[11]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[11])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[11],portal_novosUsuarios_2024[10])} | {GR.crescimento(portal_novosUsuarios_2024[11],portal_novosUsuarios_2023[11])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[11],portal_visualizacoes_2024[10])} | {GR.crescimento(portal_visualizacoes_2024[11],portal_visualizacoes_2023[11])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[11],portal_usuariosRescorrentes_2024Analytics[10])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[11],portal_usuariosRescorrentes_2023Analytics[11])}')))

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
        sublist.add_item(NoEscape(r"Em geral, \textbf{abril} foi o melhor mês até o momento. Esse foi o mês com o maior número de novos usuários e visualizações e o segundo maior número de usuários recorrentes,tendo o maior crescimento percentual em duas dessas métricas e o segundo maior em visualizações."))
        sublist.add_item(NoEscape(r"Apesar de ter o maior crecimento percentual nas visualizações, \textbf{março} não é o melhor mês como foi em foi 2023. Além disso, tem os menores números de novos usuários e recorrentes até o momento, sendo também o mês com a maior e segunda maior quedas percentuais nessas métricas, respectivamente."))
        sublist.add_item(NoEscape(r"\textbf{Janeiro} é o segundo melhor mês até o momento."))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mesmo mês em 2023:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"\textbf{Janeiro} e \textbf{junho} tiveram os maiores crescimentos percentuais em usuários recorrentes."))
        sublist.add_item(NoEscape(r"\textbf{Abril} e \textbf{junho} tiveram os maiores crescimentos percentuais em novos usuários."))
        sublist.add_item(NoEscape(r"A maioria dos meses tem grandes quedas nas visualizações, com \textbf{março} e \textbf{maio} sendo os maiores."))


doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{float}'))

doc.append(NewPage())

# # ORIGEM PORTAL
# GR.origemPortal()       
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: origem dos usuários")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha

#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.origem_plot_path, width=NoEscape(r'1\textwidth'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item('O acesso direto representa os usuários que digitaram a URL da Tribuna do Norte diretamente no navegador,adicionaram o site aos favoritos ou clicaram diretamente em um link compartilhado, desta forma, indo diretamente para o site sem precisar pesquisa-lo.')
#             itemize.add_item('As outras informações representam o acesso através da plataforma indicada pelo título da respectiva barra.')

# doc.append(NewPage())

# # TOP10 PORTAL
# GR.top10()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: 10 notícias mais vistas")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha

#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.top10_plot_path, width=NoEscape(r'0.9\textwidth'))
        
# # TOP15 PORTAL
# GR.top15()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: 15 notícias mais pesquisadas")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.top15_plot_path, width=NoEscape(r'0.9\textwidth'))

# # TOP15 PORTAL
# GR.top15cliques()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: 15 notícias com mais cliques pelo google")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.top15cliques_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# # VISUALIZAÇÕES E USUÁRIOS PORTAL
# GR.visualizacoesUsuarios()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: comparativo de visualizações e acessos de usuários")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.visualizacoesUsuarios_plot_path, width=NoEscape(r'0.8\textwidth'))
#         # plot.add_caption(NoEscape(r'\small{Este gráfico mostra a semelhança de compatamento entre diferentes dados ao longo do período analisado.}'))  # Adiciona a legenda
# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\small{Este gráfico mostra a semelhança de compatamento entre diferentes dados do portal ao longo do período analisado.}'))


# doc.append(NewPage())

# # VISUALIZAÇÕES POR FE PORTAL
# GR.faixaEtaria()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: visualizações por faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.faixaEtaria_plot_path, width=NoEscape(r'0.8\textwidth'))

# GR.faixaEtaria_desconhecidaAndTotal()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("Portal: visualizações por faixa etária (desconhecida e total)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.faixaEtaria_desconhecidaAndTotal_plot_path, width=NoEscape(r'0.8\textwidth'))

# doc.append(NewPage())

# recebendo camiho da imagem do gráfico e o total de seguidores do fb e ig
# fePublico_FBIG_plot_path, FB_followers, IG_followers = GR.fePublico_FBIG()

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Instagram', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '6,7 mil', '542 mil', '152 mil'))
                table.add_row(('', FootnoteText('+21,8% | -'), FootnoteText('-7% | -19%'), FootnoteText('+17,2% | -26,2%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(ig_seg_2024[1]), GR.numeroPorExtensso(ig_alcance_2024[1]), GR.numeroPorExtensso(ig_vivitas_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[1],ig_seg_2024[0])} | {GR.crescimento(ig_seg_2024[1],ig_seg_2023[1])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[1],ig_alcance_2024[0])} | {GR.crescimento(ig_alcance_2024[1],ig_alcance_2023[1])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[1],ig_vivitas_2024[0])} | {GR.crescimento(ig_vivitas_2024[1],ig_vivitas_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(ig_seg_2024[2]), GR.numeroPorExtensso(ig_alcance_2024[2]), GR.numeroPorExtensso(ig_vivitas_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[2],ig_seg_2024[1])} | {GR.crescimento(ig_seg_2024[2],ig_seg_2023[2])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[2],ig_alcance_2024[1])} | {GR.crescimento(ig_alcance_2024[2],ig_alcance_2023[2])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[2],ig_vivitas_2024[1])} | {GR.crescimento(ig_vivitas_2024[2],ig_vivitas_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(ig_seg_2024[3]), GR.numeroPorExtensso(ig_alcance_2024[3]), GR.numeroPorExtensso(ig_vivitas_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[3],ig_seg_2024[2])} | {GR.crescimento(ig_seg_2024[3],ig_seg_2023[3])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[3],ig_alcance_2024[2])} | {GR.crescimento(ig_alcance_2024[3],ig_alcance_2023[3])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[3],ig_vivitas_2024[2])} | {GR.crescimento(ig_vivitas_2024[3],ig_vivitas_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(ig_seg_2024[4]), GR.numeroPorExtensso(ig_alcance_2024[4]), GR.numeroPorExtensso(ig_vivitas_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[4],ig_seg_2024[3])} | {GR.crescimento(ig_seg_2024[4],ig_seg_2023[4])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[4],ig_alcance_2024[3])} | {GR.crescimento(ig_alcance_2024[4],ig_alcance_2023[4])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[4],ig_vivitas_2024[3])} | {GR.crescimento(ig_vivitas_2024[4],ig_vivitas_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(ig_seg_2024[5]), GR.numeroPorExtensso(ig_alcance_2024[5]), GR.numeroPorExtensso(ig_vivitas_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[5],ig_seg_2024[4])} | {GR.crescimento(ig_seg_2024[5],ig_seg_2023[5])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[5],ig_alcance_2024[4])} | {GR.crescimento(ig_alcance_2024[5],ig_alcance_2023[5])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[5],ig_vivitas_2024[4])} | {GR.crescimento(ig_vivitas_2024[5],ig_vivitas_2023[5])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(ig_seg_2024[6]), GR.numeroPorExtensso(ig_alcance_2024[6]), GR.numeroPorExtensso(ig_vivitas_2024[6])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[6],ig_seg_2024[5])} | {GR.crescimento(ig_seg_2024[6],ig_seg_2023[6])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[6],ig_alcance_2024[5])} | {GR.crescimento(ig_alcance_2024[6],ig_alcance_2023[6])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[6],ig_vivitas_2024[5])} | {GR.crescimento(ig_vivitas_2024[6],ig_vivitas_2023[6])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(ig_seg_2024[7]), GR.numeroPorExtensso(ig_alcance_2024[7]), GR.numeroPorExtensso(ig_vivitas_2024[7])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[7],ig_seg_2024[6])} | {GR.crescimento(ig_seg_2024[7],ig_seg_2023[7])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[7],ig_alcance_2024[6])} | {GR.crescimento(ig_alcance_2024[7],ig_alcance_2023[7])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[7],ig_vivitas_2024[6])} | {GR.crescimento(ig_vivitas_2024[7],ig_vivitas_2023[7])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(ig_seg_2024[8]), GR.numeroPorExtensso(ig_alcance_2024[8]), GR.numeroPorExtensso(ig_vivitas_2024[8])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[8],ig_seg_2024[7])} | {GR.crescimento(ig_seg_2024[8],ig_seg_2023[8])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[8],ig_alcance_2024[7])} | {GR.crescimento(ig_alcance_2024[8],ig_alcance_2023[8])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[8],ig_vivitas_2024[7])} | {GR.crescimento(ig_vivitas_2024[8],ig_vivitas_2023[8])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(ig_seg_2024[9]), GR.numeroPorExtensso(ig_alcance_2024[9]), GR.numeroPorExtensso(ig_vivitas_2024[9])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[9],ig_seg_2024[8])} | {GR.crescimento(ig_seg_2024[9],ig_seg_2023[9])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[9],ig_alcance_2024[8])} | {GR.crescimento(ig_alcance_2024[9],ig_alcance_2023[9])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[9],ig_vivitas_2024[8])} | {GR.crescimento(ig_vivitas_2024[9],ig_vivitas_2023[9])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(ig_seg_2024[10]), GR.numeroPorExtensso(ig_alcance_2024[10]), GR.numeroPorExtensso(ig_vivitas_2024[10])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[10],ig_seg_2024[9])} | {GR.crescimento(ig_seg_2024[10],ig_seg_2023[10])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[10],ig_alcance_2024[9])} | {GR.crescimento(ig_alcance_2024[10],ig_alcance_2023[10])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[10],ig_vivitas_2024[9])} | {GR.crescimento(ig_vivitas_2024[10],ig_vivitas_2023[10])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(ig_seg_2024[11]), GR.numeroPorExtensso(ig_alcance_2024[11]), GR.numeroPorExtensso(ig_vivitas_2024[11])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[11],ig_seg_2024[10])} | {GR.crescimento(ig_seg_2024[11],ig_seg_2023[11])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[11],ig_alcance_2024[10])} | {GR.crescimento(ig_alcance_2024[11],ig_alcance_2023[11])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[11],ig_vivitas_2024[10])} | {GR.crescimento(ig_vivitas_2024[11],ig_vivitas_2023[11])}')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Legenda:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Alcance:} Essa métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram e/ou Facebook, incluindo publicações e stories que foram turbinados. Também pode ser interpretada como a quantidade de contas atingidas;'))
                sublist.add_item(NoEscape(r'\textbf{Visitas:} número de vezes que usuários visitaram seu perfil.'))
        # with doc.create(Itemize()) as itemize:
        #     itemize.add_item(Command('textbf', arguments='Legenda'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item(str(Command('textbf', arguments='Alcance: '))+"Esta métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram, incluindo publicações e stories que foram turbinados. O alcance só é calculado uma vez se ocorrer por meio da distribuição orgânica e paga;")
        #         sublist.add_item(str(Command('textbf', arguments='Visitas: '))+"número de vezes que usuários visitaram seu perfil.")
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
        sublist.add_item(NoEscape(r"\textbf{Abril} foi o melhor mês até o momento. Tem os maiores números de novos seguidores e visitas, está entre os três maiores em alcance e tem os maiores crecimentos pencentuais."))
        sublist.add_item(NoEscape(r"\textbf{Janeiro} teve os segundos melhores números e crescimentos em novos seguidores(junto de \textbf{março}) e visitas."))
        sublist.add_item(NoEscape(r"\textbf{Março} teve os números mais baixos em alcance e o segundo em visitas e quedas nessas métricas. \textbf{Junho} teve o menor número de visitas e novos seguidores."))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mesmo mês em 2023:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"\textbf{Março} teve a maior queda em visitas, \textbf{janeiro} em alcance e \textbf{fevereiro} em novos seguidores."))
        sublist.add_item(NoEscape(r"\textbf{Maio} foi o mês que mais cresceu em novos seguidores e \textbf{junho} em alcance."))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Facebook', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '628', '468 mil', '32 mil'))
                table.add_row(('', FootnoteText('+38% | +20%'), FootnoteText('-5% | -7,5%'), FootnoteText('+9,6% | +4,2%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(fb_seg_2024[1]), GR.numeroPorExtensso(fb_alcance_2024[1]), GR.numeroPorExtensso(fb_vivitas_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[1],fb_seg_2024[0])} | {GR.crescimento(fb_seg_2024[1],fb_seg_2023[1])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[1],fb_alcance_2024[0])} | {GR.crescimento(fb_alcance_2024[1],fb_alcance_2023[1])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[1],fb_vivitas_2024[0])} | {GR.crescimento(fb_vivitas_2024[1],fb_vivitas_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(fb_seg_2024[2]), GR.numeroPorExtensso(fb_alcance_2024[2]), GR.numeroPorExtensso(fb_vivitas_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[2],fb_seg_2024[1])} | {GR.crescimento(fb_seg_2024[2],fb_seg_2023[2])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[2],fb_alcance_2024[1])} | {GR.crescimento(fb_alcance_2024[2],fb_alcance_2023[2])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[2],fb_vivitas_2024[1])} | {GR.crescimento(fb_vivitas_2024[2],fb_vivitas_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(fb_seg_2024[3]), GR.numeroPorExtensso(fb_alcance_2024[3]), GR.numeroPorExtensso(fb_vivitas_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[3],fb_seg_2024[2])} | {GR.crescimento(fb_seg_2024[3],fb_seg_2023[3])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[3],fb_alcance_2024[2])} | {GR.crescimento(fb_alcance_2024[3],fb_alcance_2023[3])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[3],fb_vivitas_2024[2])} | {GR.crescimento(fb_vivitas_2024[3],fb_vivitas_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(fb_seg_2024[4]), GR.numeroPorExtensso(fb_alcance_2024[4]), GR.numeroPorExtensso(fb_vivitas_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[4],fb_seg_2024[3])} | {GR.crescimento(fb_seg_2024[4],fb_seg_2023[4])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[4],fb_alcance_2024[3])} | {GR.crescimento(fb_vivitas_2024[4],fb_alcance_2023[4])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[4],fb_vivitas_2024[3])} | {GR.crescimento(fb_vivitas_2024[4],fb_vivitas_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(fb_seg_2024[5]), GR.numeroPorExtensso(fb_alcance_2024[5]), GR.numeroPorExtensso(fb_vivitas_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[5],fb_seg_2024[4])} | {GR.crescimento(fb_seg_2024[5],fb_seg_2023[5])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[5],fb_alcance_2024[4])} | {GR.crescimento(fb_vivitas_2024[5],fb_alcance_2023[5])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[5],fb_vivitas_2024[4])} | {GR.crescimento(fb_vivitas_2024[5],fb_vivitas_2023[5])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(fb_seg_2024[6]), GR.numeroPorExtensso(fb_alcance_2024[6]), GR.numeroPorExtensso(fb_vivitas_2024[6])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[6],fb_seg_2024[5])} | {GR.crescimento(fb_seg_2024[6],fb_seg_2023[6])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[6],fb_alcance_2024[5])} | {GR.crescimento(fb_vivitas_2024[6],fb_alcance_2023[6])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[6],fb_vivitas_2024[5])} | {GR.crescimento(fb_vivitas_2024[6],fb_vivitas_2023[6])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(fb_seg_2024[7]), GR.numeroPorExtensso(fb_alcance_2024[7]), GR.numeroPorExtensso(fb_vivitas_2024[7])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[7],fb_seg_2024[6])} | {GR.crescimento(fb_seg_2024[7],fb_seg_2023[7])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[7],fb_alcance_2024[6])} | {GR.crescimento(fb_vivitas_2024[7],fb_alcance_2023[7])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[7],fb_vivitas_2024[6])} | {GR.crescimento(fb_vivitas_2024[7],fb_vivitas_2023[7])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(fb_seg_2024[8]), GR.numeroPorExtensso(fb_alcance_2024[8]), GR.numeroPorExtensso(fb_vivitas_2024[8])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[8],fb_seg_2024[7])} | {GR.crescimento(fb_seg_2024[8],fb_seg_2023[8])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[8],fb_alcance_2024[7])} | {GR.crescimento(fb_vivitas_2024[8],fb_alcance_2023[8])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[8],fb_vivitas_2024[7])} | {GR.crescimento(fb_vivitas_2024[8],fb_vivitas_2023[8])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(fb_seg_2024[9]), GR.numeroPorExtensso(fb_alcance_2024[9]), GR.numeroPorExtensso(fb_vivitas_2024[9])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[9],fb_seg_2024[8])} | {GR.crescimento(fb_seg_2024[9],fb_seg_2023[9])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[9],fb_alcance_2024[8])} | {GR.crescimento(fb_vivitas_2024[9],fb_alcance_2023[9])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[9],fb_vivitas_2024[8])} | {GR.crescimento(fb_vivitas_2024[9],fb_vivitas_2023[9])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(fb_seg_2024[10]), GR.numeroPorExtensso(fb_alcance_2024[10]), GR.numeroPorExtensso(fb_vivitas_2024[10])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[10],fb_seg_2024[9])} | {GR.crescimento(fb_seg_2024[10],fb_seg_2023[10])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[10],fb_alcance_2024[9])} | {GR.crescimento(fb_vivitas_2024[10],fb_alcance_2023[10])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[10],fb_vivitas_2024[9])} | {GR.crescimento(fb_vivitas_2024[10],fb_vivitas_2023[10])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(fb_seg_2024[11]), GR.numeroPorExtensso(fb_alcance_2024[11]), GR.numeroPorExtensso(fb_vivitas_2024[11])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[11],fb_seg_2024[10])} | {GR.crescimento(fb_seg_2024[11],fb_seg_2023[11])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[11],fb_alcance_2024[10])} | {GR.crescimento(fb_vivitas_2024[11],fb_alcance_2023[11])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[11],fb_vivitas_2024[10])} | {GR.crescimento(fb_vivitas_2024[11],fb_vivitas_2023[11])}')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Legenda:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Alcance:} Essa métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram e/ou Facebook, incluindo publicações e stories que foram turbinados. Também pode ser interpretada como a quantidade de contas atingidas;'))
                sublist.add_item(NoEscape(r'\textbf{Visitas:} número de vezes que usuários visitaram seu perfil.'))
        # with doc.create(Itemize()) as itemize:
        #     # itemize.add_item(Command('textbf', arguments='Legenda'))
        #     # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #     #     sublist.add_item(str(Command('textbf', arguments='Alcance: '))+"Esta métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram, incluindo publicações e stories que foram turbinados. O alcance só é calculado uma vez se ocorrer por meio da distribuição orgânica e paga;")
        #     #     sublist.add_item(str(Command('textbf', arguments='Visitas: '))+"número de vezes que usuários visitaram seu perfil ou página.")
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
        sublist.add_item(NoEscape(r"\textbf{Janeiro} foi o melhor mês até o momento, pois tem os maiores números. Também teve o segundo melhore crecimento em novos seguidores e o melhor em visitas."))
        sublist.add_item(NoEscape(r"Em \textbf{janeiro}, apesar da queda no alcance as outras métricas ainda cresceram."))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mesmo mês em 2023:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"\textbf{Março} teve a maior queda em novos seguidores, \textbf{maio} e \textbf{junho} em alcance, e \textbf{abril} e \textbf{março} em visitas."))
        

# doc.append(NewPage())

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB e IG: audiência por sexo e faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(fePublico_FBIG_plot_path, width=NoEscape(r'0.8\textwidth'))

# publicoCidades_plot_path = GR.publicoCidades()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB e IG: audiência por cidades")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(publicoCidades_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# curtidasFB_plot_path = GR.curtidasFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: novos seguidores ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(curtidasFB_plot_path, width=NoEscape(r'0.75 \textwidth'))

# visitasFB_plot_path = GR.visitasFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: visitas ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visitasFB_plot_path, width=NoEscape(r'0.75\textwidth'))

# alcanceFB_plot_path = GR.alcanceFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: alcance ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(alcanceFB_plot_path, width=NoEscape(r'0.75\textwidth'))

# doc.append(NewPage())

# seguidoresIG_plot_path, seguidoresIG = GR.seguidoresIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: ganho de seguidores ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(seguidoresIG_plot_path, width=NoEscape(r'0.75\textwidth'))

# visitasIG_plot_path, visitasIG = GR.visitasIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: visitas ao perfil ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visitasIG_plot_path, width=NoEscape(r'0.75\textwidth'))

# alcanceIG_plot_path, alcanceIG = GR.alcanceIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: alcance do perfil ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(alcanceIG_plot_path, width=NoEscape(r'0.75\textwidth'))

# doc.append(NewPage())

# dadosIG_plot_path = GR.dadosIG(10,450)

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: comparativo de seguidores, visitas e alcance. (Obs.: dados fora de escala para uma melhor visualização)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(dadosIG_plot_path, width=NoEscape(r'1\textwidth'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\small{Este gráfico mostra a semelhança de compatamento entre os dados do Instagram ao longo do período analisado.}'))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Twitter', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Impressões', 'Engajamentos'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '2,9 mil', '455,8 mil', '13,2 mil'))
                table.add_row(('', FootnoteText('+81,3% | +75,8%'), FootnoteText('+6% | -59%'), FootnoteText('+22,2% | -26,7%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(tw_seg_2024[1]), GR.numeroPorExtensso(tw_impressões_2024[1]), GR.numeroPorExtensso(tw_engajamentos_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[1],tw_seg_2024[0])} | {GR.crescimento(tw_seg_2024[1],tw_seg_2023[1])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[1],tw_impressões_2024[0])} | {GR.crescimento(tw_impressões_2024[1],tw_impressões_2023[1])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[1],tw_engajamentos_2024[0])} | {GR.crescimento(tw_engajamentos_2024[1],tw_engajamentos_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(tw_seg_2024[2]), GR.numeroPorExtensso(tw_impressões_2024[2]), GR.numeroPorExtensso(tw_engajamentos_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[2],tw_seg_2024[1])} | {GR.crescimento(tw_seg_2024[2],tw_seg_2023[2])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[2],tw_impressões_2024[1])} | {GR.crescimento(tw_impressões_2024[2],tw_impressões_2023[2])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[2],tw_engajamentos_2024[1])} | {GR.crescimento(tw_engajamentos_2024[2],tw_engajamentos_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(tw_seg_2024[3]), GR.numeroPorExtensso(tw_impressões_2024[3]), GR.numeroPorExtensso(tw_engajamentos_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[3],tw_seg_2024[2])} | {GR.crescimento(tw_seg_2024[3],tw_seg_2023[3])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[3],tw_impressões_2024[2])} | {GR.crescimento(tw_impressões_2024[3],tw_impressões_2023[3])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[3],tw_engajamentos_2024[2])} | {GR.crescimento(tw_engajamentos_2024[3],tw_engajamentos_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(tw_seg_2024[4]), GR.numeroPorExtensso(tw_impressões_2024[4]), GR.numeroPorExtensso(tw_engajamentos_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[4],tw_seg_2024[3])} | {GR.crescimento(tw_seg_2024[4],tw_seg_2023[4])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[4],tw_impressões_2024[3])} | {GR.crescimento(tw_impressões_2024[4],tw_impressões_2023[4])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[4],tw_engajamentos_2024[3])} | {GR.crescimento(tw_engajamentos_2024[4],tw_engajamentos_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), '-', '-', '-'))
                table.add_row(('', FootnoteText('- | -'), FootnoteText('- | -'), FootnoteText('- | -')))
                # table.add_hline()
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(tw_seg_2024[6]), GR.numeroPorExtensso(tw_impressões_2024[6]), GR.numeroPorExtensso(tw_engajamentos_2024[6])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[6],tw_seg_2024[5])} | {GR.crescimento(tw_seg_2024[6],tw_seg_2023[6])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[6],tw_impressões_2024[5])} | {GR.crescimento(tw_impressões_2024[6],tw_impressões_2023[6])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[6],tw_engajamentos_2024[5])} | {GR.crescimento(tw_engajamentos_2024[6],tw_engajamentos_2023[6])}')))
                # table.add_hline()
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(tw_seg_2024[7]), GR.numeroPorExtensso(tw_impressões_2024[7]), GR.numeroPorExtensso(tw_engajamentos_2024[7])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[7],tw_seg_2024[6])} | {GR.crescimento(tw_seg_2024[7],tw_seg_2023[7])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[7],tw_impressões_2024[6])} | {GR.crescimento(tw_impressões_2024[7],tw_impressões_2023[7])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[7],tw_engajamentos_2024[6])} | {GR.crescimento(tw_engajamentos_2024[7],tw_engajamentos_2023[7])}')))
                # table.add_hline()
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(tw_seg_2024[8]), GR.numeroPorExtensso(tw_impressões_2024[8]), GR.numeroPorExtensso(tw_engajamentos_2024[8])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[8],tw_seg_2024[7])} | {GR.crescimento(tw_seg_2024[8],tw_seg_2023[8])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[8],tw_impressões_2024[7])} | {GR.crescimento(tw_impressões_2024[8],tw_impressões_2023[8])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[8],tw_engajamentos_2024[7])} | {GR.crescimento(tw_engajamentos_2024[8],tw_engajamentos_2023[8])}')))
                # table.add_hline()
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(tw_seg_2024[9]), GR.numeroPorExtensso(tw_impressões_2024[9]), GR.numeroPorExtensso(tw_engajamentos_2024[9])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[9],tw_seg_2024[8])} | {GR.crescimento(tw_seg_2024[9],tw_seg_2023[9])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[9],tw_impressões_2024[8])} | {GR.crescimento(tw_impressões_2024[9],tw_impressões_2023[9])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[9],tw_engajamentos_2024[8])} | {GR.crescimento(tw_engajamentos_2024[9],tw_engajamentos_2023[9])}')))
                # table.add_hline()
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(tw_seg_2024[10]), GR.numeroPorExtensso(tw_impressões_2024[10]), GR.numeroPorExtensso(tw_engajamentos_2024[10])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[10],tw_seg_2024[9])} | {GR.crescimento(tw_seg_2024[10],tw_seg_2023[10])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[10],tw_impressões_2024[9])} | {GR.crescimento(tw_impressões_2024[10],tw_impressões_2023[10])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[10],tw_engajamentos_2024[9])} | {GR.crescimento(tw_engajamentos_2024[10],tw_engajamentos_2023[10])}')))
                # table.add_hline()
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(tw_seg_2024[11]), GR.numeroPorExtensso(tw_impressões_2024[11]), GR.numeroPorExtensso(tw_engajamentos_2024[11])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[11],tw_seg_2024[10])} | {GR.crescimento(tw_seg_2024[11],tw_seg_2023[11])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[11],tw_impressões_2024[10])} | {GR.crescimento(tw_impressões_2024[11],tw_impressões_2023[11])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[11],tw_engajamentos_2024[10])} | {GR.crescimento(tw_engajamentos_2024[11],tw_engajamentos_2023[11])}')))
                # table.add_hline()

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Legenda:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Impressões:} número de vezes que os usuários viram o(s) Tweet(s);'))
                sublist.add_item(NoEscape(r'\textbf{Engajamentos:} número total de vezes que um usuário interagiu com o(s) Tweet(s). Isso inclui todos os cliques em qualquer lugar no Tweet como: hashtags, links, avatar, nome de usuário e expansão do Tweet, Retweets, respostas e favoritos.'))
        # with doc.create(Itemize()) as itemize:
        #     # itemize.add_item(Command('textbf', arguments='Legenda'))
        #     # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #     #     sublist.add_item(str(Command('textbf', arguments='Impressões: '))+"número de vezes que usuários viram o(s) Tweet(s);")
        #     #     sublist.add_item(str(Command('textbf', arguments='Engajamentos: '))+"número total de vezes que um usuário interagiu com o(s) Tweet(s). Isso inclui todos os cliques em qualquer lugar no Tweet como: hashtags, links, avatar, nome de usuário e expansão do Tweet, Retweets, respostas e favoritos.")
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
        sublist.add_item(NoEscape(r"\textbf{Maio} foi o melhor mês até em novos seguidores e engajamentos. \textbf{Janeiro} e \textbf{abril} ainda o superam em impressões e nos crescimentos percentuais em todas as métricas."))
        sublist.add_item(NoEscape(r"\textbf{Fevereiro} teve as maiores quedas, com \textbf{maio} o suerando apenas em impressões."))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mesmo mês em 2023:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"Com exeção de \textbf{fevereiro}, que teve um pequeno crescimento em engajamentos, tanto impresssões quanto engajamentos tiveram apenas quedas."))
        sublist.add_item(NoEscape(r"Apenas \textbf{março} teve queda em novos seguidores e \textbf{Maio} teve o maior crescimento."))

# doc.append(NewPage())

# engajamentoTW_plot_path = GR.engajamentoTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: engajamento do twitter")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(engajamentoTW_plot_path, width=NoEscape(r'0.75\textwidth'))

# impressoesTW_plot_path = GR.impressoesTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: impressões do twitter")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(impressoesTW_plot_path, width=NoEscape(r'0.75\textwidth'))

# seguidoresTW_plot_path = GR.seguidoresTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: ganho de seguidores no twitter ao logo do mês. (Esses dados levam em consideração apenas os ganhos)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(seguidoresTW_plot_path, width=NoEscape(r'0.75\textwidth'))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
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
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(yb_inc_2024[6]), GR.numeroPorExtensso(yb_visualizacoes_2024[6]), GR.numeroPorExtensso(yb_horas_2024[6])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[6],yb_inc_2024[5])} | {GR.crescimento(yb_inc_2024[6],yb_inc_2023[6])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[6],yb_visualizacoes_2024[5])} | {GR.crescimento(yb_visualizacoes_2024[6],yb_visualizacoes_2023[6])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[6],yb_horas_2024[5])} | {GR.crescimento(yb_horas_2024[6],yb_horas_2023[6])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(yb_inc_2024[7]), GR.numeroPorExtensso(yb_visualizacoes_2024[7]), GR.numeroPorExtensso(yb_horas_2024[7])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[7],yb_inc_2024[6])} | {GR.crescimento(yb_inc_2024[7],yb_inc_2023[7])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[7],yb_visualizacoes_2024[6])} | {GR.crescimento(yb_visualizacoes_2024[7],yb_visualizacoes_2023[7])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[7],yb_horas_2024[6])} | {GR.crescimento(yb_horas_2024[7],yb_horas_2023[7])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(yb_inc_2024[8]), GR.numeroPorExtensso(yb_visualizacoes_2024[8]), GR.numeroPorExtensso(yb_horas_2024[8])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[8],yb_inc_2024[7])} | {GR.crescimento(yb_inc_2024[8],yb_inc_2023[8])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[8],yb_visualizacoes_2024[7])} | {GR.crescimento(yb_visualizacoes_2024[8],yb_visualizacoes_2023[8])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[8],yb_horas_2024[7])} | {GR.crescimento(yb_horas_2024[8],yb_horas_2023[8])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(yb_inc_2024[9]), GR.numeroPorExtensso(yb_visualizacoes_2024[9]), GR.numeroPorExtensso(yb_horas_2024[9])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[9],yb_inc_2024[8])} | {GR.crescimento(yb_inc_2024[9],yb_inc_2023[9])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[9],yb_visualizacoes_2024[8])} | {GR.crescimento(yb_visualizacoes_2024[9],yb_visualizacoes_2023[9])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[9],yb_horas_2024[8])} | {GR.crescimento(yb_horas_2024[9],yb_horas_2023[9])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(yb_inc_2024[10]), GR.numeroPorExtensso(yb_visualizacoes_2024[10]), GR.numeroPorExtensso(yb_horas_2024[10])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[10],yb_inc_2024[9])} | {GR.crescimento(yb_inc_2024[10],yb_inc_2023[10])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[10],yb_visualizacoes_2024[9])} | {GR.crescimento(yb_visualizacoes_2024[10],yb_visualizacoes_2023[10])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[10],yb_horas_2024[9])} | {GR.crescimento(yb_horas_2024[10],yb_horas_2023[10])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(yb_inc_2024[11]), GR.numeroPorExtensso(yb_visualizacoes_2024[11]), GR.numeroPorExtensso(yb_horas_2024[11])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[11],yb_inc_2024[10])} | {GR.crescimento(yb_inc_2024[11],yb_inc_2023[11])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[11],yb_visualizacoes_2024[10])} | {GR.crescimento(yb_visualizacoes_2024[11],yb_visualizacoes_2023[11])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[11],yb_horas_2024[10])} | {GR.crescimento(yb_horas_2024[11],yb_horas_2023[11])}')))

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
        sublist.add_item(NoEscape(r"\textbf{Março} foi o melhor mês até o momento."))
        sublist.add_item(NoEscape(r"\textbf{Abril} foi o primeiro mês com quedas após uma sequência de crescimento. Também foi o mês com mais horas de exibição."))
        sublist.add_item(NoEscape(r"Desde \textbf{abril} a métricas pararam de crescer."))

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Mesmo mês em 2023:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"Até \textbf{junho} todas as métricas tiveram bons crescimentos em todos os meses em relação ao ano passado. O que significa que até o momento o consumo do YouTube aumentou."))
        
# doc.append(NewPage())

# visualizacoesIdadeYTB_plot_path = GR.visualizacoesIdadeYTB()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("YouTube: visualizações por faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visualizacoesIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))

# doc.append(NewPage())

# horasIdadeYTB_plot_path = GR.horasIdadeYTB()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("YouTube: horas de exibição por faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(horasIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))
        
# generoYTB_plot_path = GR.generoYTB()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("YouTube: sexo do público")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(generoYTB_plot_path, width=NoEscape(r'0.6\textwidth'))
        
# visualizacoesCidadeYTB_plot_path = GR.visualizacoesCidadeYTB()
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("YouTube: visualizações por cidade")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visualizacoesCidadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))


doc.append(NewPage())

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Funcionamento dos algoritmos:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Facebook:} O algoritmo do Facebook prioriza os conteúdos que geram mais interações, como curtidas, comentários e compartilhamentos. Ele também considera o grau de relacionamento entre os usuários e as contas que eles seguem, mostrando mais publicações de amigos e familiares do que de páginas. Além disso, o Facebook leva em conta a relevância e a atualidade dos conteúdos, dando mais destaque para as notícias e os assuntos do momento;'))
                sublist.add_item(NoEscape(r'\textbf{Instagram:} O a lgoritmo do Instagram também se baseia no engajamento, no relacionamento e na temporalidade dos conteúdos. Ele mostra primeiro as postagens e as histórias das contas com as quais o usuário mais interage, seja por meio de curtidas, comentários, mensagens diretas ou buscas. Ele também valoriza os conteúdos mais recentes e mais relevantes para o usuário, de acordo com os seus interesses e hábitos;'))
                sublist.add_item(NoEscape(r'\textbf{Twitter:} O algoritmo do Twitter tem duas formas de exibir os conteúdos: o modo cronológico e o modo destacado. No modo cronológico, o usuário vê os tweets mais recentes em ordem de publicação. No modo destacado, o usuário vê os tweets mais relevantes para ele, de acordo com o seu perfil, as suas interações e os assuntos do momento. O Twitter também mostra os tweets mais populares e mais comentados na seção “O que está acontecendo”;'))
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
            itemize.add_item('Top15 notícias mais pesquisadas: as impressões são referentes a quantidade de vezes que uma pesquisa sobre determinado assunto foi realizada e foi possível visualizar o link da notícia no portal do TN entre os resultados.')
            
# with doc.create(Itemize()) as itemize:
#             # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
#             itemize.add_item('Calculos de porcentagem:')
#             #doc.append(NoEscape(r'\newline'))
#             with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#                 sublist.add_item(NoEscape(r'\textbf{Variação:} \Large{\left\(\frac{Mês\ Atual\ -\ Mês\ Anterior}{|Mês\ Anterior|}\right\)}\normalsize * 100.'))
#             with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
#                 sublist.add_item(NoEscape(r'O cálculo é feito dessa forma pois quero saber  qual a diferença, em porcentagem, do valor atual em relação ao anterior, seja esse valor anterior o do mês passado ou o do mesmo mês no ano passado. Em outras palavras, quero saber o quanto o valor do mês atual cresceu ou diminuiu em ralação ao outro.'))
#                 sublist.add_item(NoEscape(r'Caso a variação do mês atual com o anterior seja de +10,6\%, além da constatação óbvia de que é um número 10,6\% maior, também quer dizer que essa porcentagem equivale a 10,6\% do valor do mês anterior. Ou seja, se somarmos o valor equivalente a essa porcentagem ao mês anterior o resultado será o valor do mês atual (ou pelo menos algo MUITO próximo).'))
#                 sublist.add_item(NoEscape(r'Por exemplo: se no mês atual o portal teve 957 novos seguidores e o anterior 586, isso quer dizer que o mês atual teve aumento de,  aproxiamdamente, 63,33\%. E sabendo que 63,33\% de 586 é, aproximadamente, 371, podemos provar que 957 - 371 = 586 ou que 586 + 371 = 957.'))
            
#             with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#                 sublist.add_item(NoEscape(r'\textbf{Taxa de fixação:} \Large{\left\(\frac{Total\ de\ novos\ seg.\ no\ mês\ -\ Total\ de\ seg.\ perdidos\ no\ mês}{Total\ de\ novos\ seg.\ no\ mês}\right\)}\normalsize * 100.'))
#             with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
#                 sublist.add_item(NoEscape(r'Nesse cálculo eu quero saber quantos por cento do total de seguidores ganhos continuaram seguindo a rede social em questão.'))
#                 sublist.add_item(NoEscape(r'É importante obeservar que as pessoas que deixaram de seguir não fazem parte apenas dos mesmos que seguiram durante o mês analisado (caso o cálculo ou o texto passem essa impressão), ou apenas dos usuários que já seguiam antes. E saber de qual grupo faz parte a pessoa que deixou de seguir é um dado que não é possível de se obter.'))
                
                
# Gera o arquivo LaTeX
doc.generate_pdf(fr'C:\Users\{GR.path_aliss}\Documents\Repositórios\Relatórios\TN\Relatório-TN_Junho-2024', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
