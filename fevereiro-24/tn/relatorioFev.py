from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage
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
        doc.append(LargeText(("Relatório de Redes Sociais e Portal")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Fevereiro de 2024")))
        doc.append(LineBreak())

# f'{p.get_height():.1f}%'

portal_usuariosUnicos_2023Table = [1310190,1436050,1795250,1313645,1296524,1043117,1214210,1250648,1201899,1586565,1433565,1479161]
portal_usuariosRescorrentes_2023Table = [610947,505622,904008,604270,617390,539523,582611,606820,558692,627700,655389,686461]

portal_usuariosUnicos_2023Analytics = [820000,1000000,1100000,839000,813000,604000,758000,775000,760000,1100000,963000,1000000]
portal_usuariosRescorrentes_2023Analytics = [203000,220000,302000,205000,192000,169000,175000,194000,186000,250000,270000,289000]

portal_visualizacoes_2023 = [5043133,2880374,9257203,5981878,6426837,5382596,6110187,6056062
,5531690,4401142,2948640,3120290] # mesmo valor na tabela e no analytics
portal_novosUsuarios_2023 = [635446,629702,837845,629077,639599,436361,586337,606078,573317,956925,747908,803205] # mesmo valor na tabela e no analytics

portal_usuariosUnicos_2024Table = [1633738,0]
portal_usuariosRescorrentes_2024Table = [723672,0]
portal_usuariosUnicos_2024Analytics = [1100000,0]
portal_usuariosRescorrentes_2024Analytics = [279000,0]
portal_visualizacoes_2024 = [3503660,0] # mesmo valor na tabela e no analytics
portal_novosUsuarios_2024 = [819084,0] # mesmo valor na tabela e no analytics

ig_seg_2023 = [1240,8640,22600,6150,3514,5242,6672,5785,7315,6451,6106,5683]
ig_seg_2023_perdeu = [0,0,0,0,2794,4279,5165,4624,4585,4906,4988,4763]
ig_alcance_2023 = [669864,642671,715617,569749,541961,533116,570764,530776,515617,571695,543975,582262]
ig_vivitas_2023 = [205736,245144,739332,162899,156869,128295,142502,147638,143376,132933,135058,129676]

ig_seg_2024 = [6931,0]
ig_seg_2024_perdeu = [5485,0]
ig_alcance_2024 = [542064,0]
ig_vivitas_2024 = [151885,0]

ig_seg_2024_total = [529865,0]

fb_seg_2023 = [524,401,1316,362,386,273,293,223,172,186,248,455]
fb_seg_2023_perdeu = [97,72,102,54,50,42,63,53,44,73,146,152]
fb_alcance_2023 = [506283,459876,655223,310292,338973,250577,333882,258987,259921,336781,389143,492038]
fb_vivitas_2023 = [30707,24425,81866,36040,34809,29306,26755,27793,26507,25099,29348,29167]

fb_seg_2024 = [628,0]
fb_seg_2024_perdeu = [162,0]
fb_alcance_2024 = [467889,0]
fb_vivitas_2024 = [32152,0]

fb_seg_2024_total = [332603,0]

tw_seg_2023 = [1649,863,2823,2825,392,347,519,997,1454,1864,2169,2599]
#tw_seg_2023_perdeu = []
tw_impressões_2023 = [0,578375,1305007,1196504,1043859,1029266,782790,587558,285029,354720,391759,429655]
tw_engajamentos_2023 = [0,11089,31977,20510,20347,19405,16967,13004,8337,8112,9825,10816]

tw_seg_2024 = [2867,0]
tw_seg_2024_perdeu = [890,0] #sabe a quantidade que perdeu de acordo com a diferença de seguidores entre um mês e outro e o ganho total de seguidores no mês
tw_impressões_2024 = [455800,0]
tw_engajamentos_2024 = [13186,0]

tw_seg_2024_total = [311129,0]

yb_inc_2023 = [147,222,467,257,277,287,343,323,240,275,277,310]
yb_inc_2023_perdeu = [48,68,81,42,56,61,65,64,55,46,63,62]
yb_visualizacoes_2023 = [34722,72406,102836,64296,66046,69167,83169,73401,53691,53629,78371,66752]
yb_horas_2023 = [844.7,1415.3,2890.7,1938.2,2018.3,2290.2,2405.9,1759.1,1389.1,1420.0,1690.8,1553.0]

yb_inc_2024 = [415,0]
yb_inc_2024_perdeu = [85,0]
yb_visualizacoes_2024 = [132377,0]
yb_horas_2024 = [2338.8,0]

yb_inc_2024_total = [34000,0]

# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection('Resultados de janeiro/2024', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Portal'), GR.formataNumero(portal_novosUsuarios_2024[-1]), GR.formataNumero(portal_visualizacoes_2024[-1]), GR.formataNumero(portal_usuariosRescorrentes_2024Analytics[-1])))
                table.add_row(('', 'novos usuários', 'visualizações', 'usuários recorrentes'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Instagram'), GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]), GR.formataNumero(ig_alcance_2024[-1]), GR.formataNumero(ig_vivitas_2024[-2])))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Facebook'), GR.formataNumero(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]), GR.formataNumero(fb_alcance_2024[-1]), GR.formataNumero(fb_vivitas_2024[-1])))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Twitter'), GR.formataNumero(tw_seg_2024_total[-1]-tw_seg_2024_total[-2]), GR.formataNumero(tw_impressões_2024[-1]), GR.formataNumero(tw_engajamentos_2024[-1])))
                table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]), GR.formataNumero(yb_visualizacoes_2024[-1]), GR.formataNumero(yb_horas_2024[-1])))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item("Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, 829.760 novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube.")
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
            itemize.add_item(Command('textbf', arguments='Twitter'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(tw_seg_2024_total[-1])}. Total de seguidores no mês anterior: {GR.formataNumero(tw_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos no mês: {GR.formataNumero(tw_seg_2024_total[-1]-tw_seg_2024_total[-2]+tw_seg_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(tw_seg_2024_perdeu[-1])}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(tw_seg_2024_total[-1]-tw_seg_2024_total[-2]+tw_seg_2024_perdeu[-1],tw_seg_2024_perdeu[-1])}")
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
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(portal_novosUsuarios_2024[]), GR.numeroPorExtensso(portal_visualizacoes_2024[]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2024[])} | {GR.crescimento(portal_novosUsuarios_2024[],portal_novosUsuarios_2023[])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2024[])} | {GR.crescimento(portal_visualizacoes_2024[],portal_visualizacoes_2023[])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2024Analytics[])} | {GR.crescimento(portal_usuariosRescorrentes_2024Analytics[],portal_usuariosRescorrentes_2023Analytics[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(), GR.numeroPorExtensso(), GR.numeroPorExtensso()))
                # table.add_row(('', FootnoteText(f'{GR.crescimento()} | {GR.crescimento()}'), FootnoteText(f'{GR.crescimento()} | {GR.crescimento()}'), FootnoteText(f'{GR.crescimento()} | {GR.crescimento()}')))

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
        plot.add_image(GR.top10_plot_path, width=NoEscape(r'0.8\textwidth'))
        
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

doc.append(NewPage())

GR.faixaEtaria_desconhecidaAndTotal()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("Portal: visualizações por faixa etária (desconhecida e total)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(GR.faixaEtaria_desconhecidaAndTotal_plot_path, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

# recebendo camiho da imagem do gráfico e o total de seguidores do fb e ig
fePublico_FBIG_plot_path, FB_followers, IG_followers = GR.fePublico_FBIG()

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
                table.add_row(('', FootnoteText('+21,8% | +440,3%'), FootnoteText('-7% | -19%'), FootnoteText('+17,2% | -26,2%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(ig_seg_2024[1]), GR.numeroPorExtensso(ig_alcance_2024[1]), GR.numeroPorExtensso(ig_vivitas_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[1],ig_seg_2024[0])} | {GR.crescimento(ig_seg_2024[1],ig_seg_2023[1])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[1],ig_alcance_2024[0])} | {GR.crescimento(ig_alcance_2024[1],ig_alcance_2023[1])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[1],ig_vivitas_2024[0])} | {GR.crescimento(ig_vivitas_2024[1],ig_vivitas_2023[1])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(ig_seg_2024[]), GR.numeroPorExtensso(ig_alcance_2024[]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[])} | {GR.crescimento(ig_seg_2024[],ig_seg_2023[])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[],ig_alcance_2024[])} | {GR.crescimento(ig_alcance_2024[],ig_alcance_2023[])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[],ig_vivitas_2024[])} | {GR.crescimento(ig_vivitas_2024[],ig_vivitas_2023[])}')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     # itemize.add_item(Command('textbf', arguments='Legenda'))
        #     # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #     #     sublist.add_item(str(Command('textbf', arguments='Alcance: '))+"Esta métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram, incluindo publicações e stories que foram turbinados. O alcance só é calculado uma vez se ocorrer por meio da distribuição orgânica e paga;")
        #     #     sublist.add_item(str(Command('textbf', arguments='Visitas: '))+"número de vezes que usuários visitaram seu perfil.")
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

# doc.append(NewPage())

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
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                # table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                # table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                # table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                # table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                # table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                # table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                # table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                # table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                # table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                # table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                # table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
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

doc.append(NewPage())

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("FB e IG: audiência por sexo e faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(fePublico_FBIG_plot_path, width=NoEscape(r'0.8\textwidth'))

publicoCidades_plot_path = GR.publicoCidades()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("FB e IG: audiência por cidades")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(publicoCidades_plot_path, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

# curtidasFB_plot_path = GR.curtidasFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: curtidas ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(curtidasFB_plot_path, width=NoEscape(r'0.45\textwidth'))

visitasFB_plot_path = GR.visitasFB()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("FB: visitas ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visitasFB_plot_path, width=NoEscape(r'0.75\textwidth'))

alcanceFB_plot_path = GR.alcanceFB()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("FB: alcance ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(alcanceFB_plot_path, width=NoEscape(r'0.75\textwidth'))

seguidoresIG_plot_path, seguidoresIG = GR.seguidoresIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: ganho de seguidores ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(seguidoresIG_plot_path, width=NoEscape(r'0.45\textwidth'))

visitasIG_plot_path, visitasIG = GR.visitasIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: visitas ao perfil ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visitasIG_plot_path, width=NoEscape(r'0.45\textwidth'))

alcanceIG_plot_path, alcanceIG = GR.alcanceIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: alcance do perfil ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(alcanceIG_plot_path, width=NoEscape(r'0.45\textwidth'))

doc.append(NewPage())

dadosIG_plot_path = GR.dadosIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: comparativo de seguidores, visitas e alcance. (Obs.: dados fora de escala para uma melhor visualização)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(dadosIG_plot_path, width=NoEscape(r'1\textwidth'))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal', numbering=False)):
    with doc.create(Subsubsection('Twitter', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Impressões', 'Engajamento'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '2,9 mil', '455,8 mil', '13,2 mil'))
                table.add_row(('', FootnoteText('+81,3% | +75,8%'), FootnoteText('+6% | -59%'), FootnoteText('+22,2% | -26,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                # table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                # table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                # table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                # table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                # table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                # table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                # table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                # table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                # table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                # table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                # table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
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

doc.append(NewPage())

engajamentoTW_plot_path = GR.engajamentoTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: engajamento do twitter")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(engajamentoTW_plot_path, width=NoEscape(r'0.45\textwidth'))

impressoesTW_plot_path = GR.impressoesTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: impressões do twitter")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(impressoesTW_plot_path, width=NoEscape(r'0.45\textwidth'))

seguidoresTW_plot_path = GR.seguidoresTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: ganho de seguidores no twitter ao logo do mês. (Esses dados levam em consideração apenas os ganhos)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(seguidoresTW_plot_path, width=NoEscape(r'0.45\textwidth'))

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
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Fevereiro'), '805 mil', '5 milhões', '220 mil'))
                # table.add_row(('', FootnoteText('+26,8% | %'), FootnoteText('-20% | %'), FootnoteText('+8,4% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Março'), '838 mil', '9,3 milhões', '302 mil'))
                # table.add_row(('', FootnoteText('+4,1% | %'), FootnoteText('+132,5% | %'), FootnoteText('+37,3% | %')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), '649 mil', '6,1 milhões', '205 mil'))
                # table.add_row(('', FootnoteText('-22,6% | +102%'), FootnoteText('-34,4% | +165,2%'), FootnoteText('-32,1% | +184,7%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), '640 mil', '6,4 milhões', '192 mil'))
                # table.add_row(('', FootnoteText('-1,4% | -5%'), FootnoteText('+5% | -8,6%'), FootnoteText('-6,3% | +28,8%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), '447 mil', '5,6 milhões', '169 mil'))
                # table.add_row(('', FootnoteText('-30% | -17%'), FootnoteText('-12,5% | 0%'), FootnoteText('-12% | 0,6%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Julho'), '586 mil', '6,1 milhões', '175 mil'))
                # table.add_row(('', FootnoteText('+31,1% | -41,4%'), FootnoteText('+9% | -22,8%'), FootnoteText('+3,5% | -30,5%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Agosto'), '606 mil', '6,1 milhões', '194 mil'))
                # table.add_row(('', FootnoteText('+3,4% | -6,6%'), FootnoteText('0% | -16,44%'), FootnoteText('+10,8% | -17,1%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Setembro'), '586 mil', '5,6 milhões', '186 mil'))
                # table.add_row(('', FootnoteText('-3,3% | -41,4%'), FootnoteText('-8,2% | -30%'), FootnoteText('-4% | -44,3%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Outubro'), '957 mil', '4,4 milhões', '250 mil'))
                # table.add_row(('', FootnoteText('+63,3% | -13%'), FootnoteText('-21,4% | -39,7%'), FootnoteText('+34% | -26%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Novembro'), '776 mil', '3,1 milhões', '270 mil'))
                # table.add_row(('', FootnoteText('-19% | +58,7%'), FootnoteText('-29,5% | -22,5%'), FootnoteText('+8% | +33%')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Dezembro'), '', '', ''))
                # table.add_row(('', FootnoteText(''), FootnoteText(''), FootnoteText('')))

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

visualizacoesIdadeYTB_plot_path = GR.visualizacoesIdadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: visualizações por faixa etári a")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visualizacoesIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))

doc.append(NewPage())

horasIdadeYTB_plot_path = GR.horasIdadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: horas de exibição por faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(horasIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))
        
generoYTB_plot_path = GR.generoYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: sexo do público")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(generoYTB_plot_path, width=NoEscape(r'0.6\textwidth'))
        
visualizacoesCidadeYTB_plot_path = GR.visualizacoesCidadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: visualizações por cidade")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visualizacoesCidadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))


doc.append(NewPage())

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Funcionamento dos algoritmos:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Facebook:} O algoritmo do Facebook prioriza os conteúdos que geram mais interações, como curtidas, comentários e compartilhamentos. Ele também considera o grau de relacionamento entre os usuários e as contas que eles seguem, mostrando mais publicações de amigos e familiares do que de páginas. Além disso, o Facebook leva em conta a relevância e a atualidade dos conteúdos, dando mais destaque para as notícias e os assuntos do momento;'))
                sublist.add_item(NoEscape(r'\textbf{Instagram:} O algoritmo do Instagram também se baseia no engajamento, no relacionamento e na temporalidade dos conteúdos. Ele mostra primeiro as postagens e as histórias das contas com as quais o usuário mais interage, seja por meio de curtidas, comentários, mensagens diretas ou buscas. Ele também valoriza os conteúdos mais recentes e mais relevantes para o usuário, de acordo com os seus interesses e hábitos;'))
                sublist.add_item(NoEscape(r'\textbf{Twitter:} O algoritmo do Twitter tem duas formas de exibir os conteúdos: o modo cronológico e o modo destacado. No modo cronológico, o usuário vê os tweets mais recentes em ordem de publicação. No modo destacado, o usuário vê os tweets mais relevantes para ele, de acordo com o seu perfil, as suas interações e os assuntos do momento. O Twitter também mostra os tweets mais populares e mais comentados na seção “O que está acontecendo”;'))
                sublist.add_item(NoEscape(r'\textbf{YouTube:} O algoritmo do YouTube tem como objetivo aumentar o tempo de permanência dos usuários na plataforma, recomendando os vídeos que eles têm mais chances de assistir e se engajar. Para isso, ele considera fatores como o histórico de visualização, as preferências, as inscrições, a localização e o feedback dos usuários. Ele também leva em conta a qualidade e a relevância dos vídeos, analisando aspectos como o título, descrição, tags, miniaturas e os metadados.'))

# with doc.create(MiniPage(width=r'\textwidth', pos='t!')) as page:
#     page.append(NoEscape(r'\hspace{4em}-'))
#     page.append(Command('textbf', arguments='Facebook: '))
#     page.append(NoEscape(' O algoritmo do Facebook prioriza os conteúdos que geram mais interações, como curtidas, comentários e compartilhamentos. Ele também considera o grau de relacionamento entre os usuários e as contas que eles seguem, mostrando mais publicações de amigos e familiares do que de páginas. Além disso, o Facebook leva em conta a relevância e a atualidade dos conteúdos, dando mais destaque para as notícias e os assuntos do momento.'))
                    
# Gera o arquivo LaTeX
doc.generate_pdf('Relatório-TN_Fev-2024', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
