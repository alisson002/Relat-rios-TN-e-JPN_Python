from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage, Math
from pylatex.utils import bold
import graficosRelatorio as GR
import pandas as pd
import rpy2.robjects as robjects
import numpy as np


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
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "lmargin": "2.5cm", "landscape": True}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório das Redes Sociais")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Anual de 2024")))
        doc.append(LineBreak())

# f'{p.get_height():.1f}%'
GR.path_aliss
GR.path_Usuarios


ig_seg_2023 = [1240,8640,22600,6150,3514,5242,6672,5785,7315,6451,6106,5683]
ig_seg_2023_perdeu = [0,0,0,0,2794,4279,5165,4624,4585,4906,4988,4763]
ig_alcance_2023 = [669864,642671,715617,569749,541961,533116,570764,530776,515617,571695,543975,582262]
ig_vivitas_2023 = [205736,245144,739332,162899,156869,128295,142502,147638,143376,132933,135058,129676]
ig_visu_2023 = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]

ig_seg_2024 = [6931,5816,5835,7843,6717,5573,5369,6072,5521,6905,6104,6217]
ig_seg_2024_perdeu = [5485,4945,4587,4885,4649,4326,4987,6082,4603,7306,4592,4469]
ig_alcance_2024 = [542064,658917,633648,847362,941640,930258,1008296,1158467,922259,1345111,1125447,1439711]
ig_vivitas_2024 = [151885,144742,131296,162036,133497,117925,110346,135437,109653,202369,142333,116139]
ig_visu_2024 = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,12978952,36267275,34238435,41592552,30634077,34713177]
ig_seg_2024_total = [529865,530797,532444,535373,537733,538756,539028,538982,539983,539659,541103,542851]

fb_seg_2023 = [524,401,1316,362,386,273,293,223,172,186,248,455]
fb_seg_2023_perdeu = [97,72,102,54,50,42,63,53,44,73,146,152]
fb_alcance_2023 = [506283,459876,655223,310292,338973,250577,333882,258987,259921,336781,389143,492038]
fb_vivitas_2023 = [30707,24425,81866,36040,34809,29306,26755,27793,26507,25099,29348,29167]
fb_visu_2023 = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]

fb_seg_2024 = [628,389,188,295,254,251,265,516,230,253,151,215]
fb_seg_2024_perdeu = [162,162,176,171,158,132,160,213,203,295,184,96]
fb_alcance_2024 = [467889,390008,197628,292192,257199,254134,266380,675762,205619,222416,163290,226351]
fb_vivitas_2024 = [32152,31459,31499,31612,29294,22864,24050,26171,21062,26441,22817,22690]
fb_visu_2024 = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,1161433,4074241,3169345,3441949]

fb_seg_2024_total = [332603,332614,332419,332336,332214,332133,332006,332122,331921,331641,331426,331545]

# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection('Resultados anuais/2024', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Instagram'), GR.formataNumero((ig_seg_2024_total[-1]-(ig_seg_2024_total[0]-ig_seg_2024[0]+ig_seg_2024_perdeu[0]))), GR.formataNumero(sum(ig_alcance_2024)), GR.formataNumero(sum(ig_vivitas_2024)), GR.formataNumero(sum(ig_visu_2024[6:]))))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil', 'visualizações'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Facebook'), GR.formataNumero(119), GR.formataNumero(sum(fb_alcance_2024)), GR.formataNumero(sum(fb_vivitas_2024)), GR.formataNumero(sum(fb_visu_2024[8:]))))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil', 'visualizações'))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Twitter'), '-', '-', '-'))
                # table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                # table.add_hline()
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item(f"Ao todo, as redes sociais da Tribuna do Norte entregaram seu conteúdo para, aproximadamente, {GR.formataNumero((ig_seg_2024_total[-1]-(ig_seg_2024_total[0]-ig_seg_2024[0]+ig_seg_2024_perdeu[0]))+(fb_seg_2024_total[-1]-(fb_seg_2024_total[0]-fb_seg_2024[0]+fb_seg_2024_perdeu[0])))} novas contas, entre Instagram e Facebook")
            #+(tw_seg_2024_total[-1]-tw_seg_2024_total[-2])
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(ig_seg_2024_total[-1])}. Total de seguidores no final do ano anterior: {GR.formataNumero(ig_seg_2024_total[0]-ig_seg_2024[0]+ig_seg_2024_perdeu[0])}")
                # sublist.add_item(f"Seguidores adquiridos no ano: {GR.formataNumero(ig_seg_2024_total[-1]-(ig_seg_2024_total[0]-ig_seg_2024[0]+ig_seg_2024_perdeu[0]))}. Deixaram de seguir: {GR.formataNumero(sum(ig_seg_2024_perdeu)-445)}.")
                sublist.add_item(f"Seguidores adquiridos no ano: {GR.formataNumero(sum(ig_seg_2024))}. Deixaram de seguir: {GR.formataNumero(sum(ig_seg_2024_perdeu)-445)}. Com um saldo de seguidores positivo de 14.432.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(sum(ig_seg_2024),sum(ig_seg_2024_perdeu)-445)}")
                sublist.add_item(f"Obs.: número de visualizações disponibilizados a partir de Jul/2024.")
                # sublist.add_item(f"Obs.: diferente do relatório semanal onde o instagram voltou a subir o número de seguidores após algumas quedas, no saldo total do mês o número total de seguidores ficou abaixo de Julho.")
            itemize.add_item(Command('textbf', arguments='Facebook'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(fb_seg_2024_total[-1])}. Total de seguidores no final do ano anterior: {GR.formataNumero(fb_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos no ano: {GR.formataNumero(sum(fb_seg_2024))}. Deixaram de seguir: {GR.formataNumero(sum(fb_seg_2024)-119)}. com um saldo positivo de 119.")
                # sublist.add_item(f"Seguidores adquiridos no ano: {GR.formataNumero(fb_seg_2024_total[-1]-(fb_seg_2024_total[0]-fb_seg_2024[0]+fb_seg_2024_perdeu[0]))}. Deixaram de seguir: {GR.formataNumero(sum(fb_seg_2024_perdeu))}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(sum(fb_seg_2024),sum(fb_seg_2024)-119)}")
                # sublist.add_item(f"Obs.: nesse caso, a taxa de fixação negatíva se trata de uma diferença relmente baixa, visto que tanto 'Seguidores adquiridos na semana' quanto 'Deixaram de seguir' são números positivos.")
                sublist.add_item(f"Obs.: número de visualizações disponibilizados a partir de Set/2024.")
            # itemize.add_item(Command('textbf', arguments='Twitter'))
            # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
            #     sublist.add_item("Total de seguidores atual: -. Total de seguidores no mês anterior: -")
            #     sublist.add_item("Seguidores adquiridos no mês: -. Deixaram de seguir: -.")
            #     sublist.add_item("Taxa de fixação: -")
            #     sublist.add_item("AVISO: Rede social bloqueada")

doc.append(NewPage())


doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{float}'))

with doc.create(Subsection('Análise mensal - 2024', numbering=False)):
    with doc.create(Subsubsection('Instagram', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas', 'Visualizações'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '6,7 mil', '542 mil', '152 mil', GR.numeroPorExtensso(ig_visu_2024[0])))
                table.add_row(('', FootnoteText('+21,8% | -'), FootnoteText('-7% | -19%'), FootnoteText('+17,2% | -26,2%'), FootnoteText(f'{GR.crescimento(ig_visu_2024[0],ig_visu_2023[11])} | {GR.crescimento(ig_visu_2024[0],ig_visu_2023[0])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(ig_seg_2024[1]), GR.numeroPorExtensso(ig_alcance_2024[1]), GR.numeroPorExtensso(ig_vivitas_2024[1]), GR.numeroPorExtensso(ig_visu_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[1],ig_seg_2024[0])} | {GR.crescimento(ig_seg_2024[1],ig_seg_2023[1])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[1],ig_alcance_2024[0])} | {GR.crescimento(ig_alcance_2024[1],ig_alcance_2023[1])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[1],ig_vivitas_2024[0])} | {GR.crescimento(ig_vivitas_2024[1],ig_vivitas_2023[1])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[1],ig_visu_2024[0])} | {GR.crescimento(ig_visu_2024[1],ig_visu_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(ig_seg_2024[2]), GR.numeroPorExtensso(ig_alcance_2024[2]), GR.numeroPorExtensso(ig_vivitas_2024[2]), GR.numeroPorExtensso(ig_visu_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[2],ig_seg_2024[1])} | {GR.crescimento(ig_seg_2024[2],ig_seg_2023[2])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[2],ig_alcance_2024[1])} | {GR.crescimento(ig_alcance_2024[2],ig_alcance_2023[2])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[2],ig_vivitas_2024[1])} | {GR.crescimento(ig_vivitas_2024[2],ig_vivitas_2023[2])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[2],ig_visu_2024[1])} | {GR.crescimento(ig_visu_2024[2],ig_visu_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(ig_seg_2024[3]), GR.numeroPorExtensso(ig_alcance_2024[3]), GR.numeroPorExtensso(ig_vivitas_2024[3]), GR.numeroPorExtensso(ig_visu_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[3],ig_seg_2024[2])} | {GR.crescimento(ig_seg_2024[3],ig_seg_2023[3])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[3],ig_alcance_2024[2])} | {GR.crescimento(ig_alcance_2024[3],ig_alcance_2023[3])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[3],ig_vivitas_2024[2])} | {GR.crescimento(ig_vivitas_2024[3],ig_vivitas_2023[3])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[3],ig_visu_2024[2])} | {GR.crescimento(ig_visu_2024[3],ig_visu_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(ig_seg_2024[4]), GR.numeroPorExtensso(ig_alcance_2024[4]), GR.numeroPorExtensso(ig_vivitas_2024[4]), GR.numeroPorExtensso(ig_visu_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[4],ig_seg_2024[3])} | {GR.crescimento(ig_seg_2024[4],ig_seg_2023[4])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[4],ig_alcance_2024[3])} | {GR.crescimento(ig_alcance_2024[4],ig_alcance_2023[4])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[4],ig_vivitas_2024[3])} | {GR.crescimento(ig_vivitas_2024[4],ig_vivitas_2023[4])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[4],ig_visu_2024[3])} | {GR.crescimento(ig_visu_2024[4],ig_visu_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(ig_seg_2024[5]), GR.numeroPorExtensso(ig_alcance_2024[5]), GR.numeroPorExtensso(ig_vivitas_2024[5]), GR.numeroPorExtensso(ig_visu_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[5],ig_seg_2024[4])} | {GR.crescimento(ig_seg_2024[5],ig_seg_2023[5])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[5],ig_alcance_2024[4])} | {GR.crescimento(ig_alcance_2024[5],ig_alcance_2023[5])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[5],ig_vivitas_2024[4])} | {GR.crescimento(ig_vivitas_2024[5],ig_vivitas_2023[5])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[5],ig_visu_2024[4])} | {GR.crescimento(ig_visu_2024[5],ig_visu_2023[5])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(ig_seg_2024[6]), GR.numeroPorExtensso(ig_alcance_2024[6]), GR.numeroPorExtensso(ig_vivitas_2024[6]), GR.numeroPorExtensso(ig_visu_2024[6])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[6],ig_seg_2024[5])} | {GR.crescimento(ig_seg_2024[6],ig_seg_2023[6])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[6],ig_alcance_2024[5])} | {GR.crescimento(ig_alcance_2024[6],ig_alcance_2023[6])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[6],ig_vivitas_2024[5])} | {GR.crescimento(ig_vivitas_2024[6],ig_vivitas_2023[6])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[6],ig_visu_2024[5])} | {GR.crescimento(ig_visu_2024[6],ig_visu_2023[6])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(ig_seg_2024[7]), GR.numeroPorExtensso(ig_alcance_2024[7]), GR.numeroPorExtensso(ig_vivitas_2024[7]), GR.numeroPorExtensso(ig_visu_2024[7])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[7],ig_seg_2024[6])} | {GR.crescimento(ig_seg_2024[7],ig_seg_2023[7])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[7],ig_alcance_2024[6])} | {GR.crescimento(ig_alcance_2024[7],ig_alcance_2023[7])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[7],ig_vivitas_2024[6])} | {GR.crescimento(ig_vivitas_2024[7],ig_vivitas_2023[7])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[7],ig_visu_2024[6])} | {GR.crescimento(ig_visu_2024[7],ig_visu_2023[7])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(ig_seg_2024[8]), GR.numeroPorExtensso(ig_alcance_2024[8]), GR.numeroPorExtensso(ig_vivitas_2024[8]), GR.numeroPorExtensso(ig_visu_2024[8])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[8],ig_seg_2024[7])} | {GR.crescimento(ig_seg_2024[8],ig_seg_2023[8])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[8],ig_alcance_2024[7])} | {GR.crescimento(ig_alcance_2024[8],ig_alcance_2023[8])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[8],ig_vivitas_2024[7])} | {GR.crescimento(ig_vivitas_2024[8],ig_vivitas_2023[8])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[8],ig_visu_2024[7])} | {GR.crescimento(ig_visu_2024[8],ig_visu_2023[8])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(ig_seg_2024[9]), GR.numeroPorExtensso(ig_alcance_2024[9]), GR.numeroPorExtensso(ig_vivitas_2024[9]), GR.numeroPorExtensso(ig_visu_2024[9])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[9],ig_seg_2024[8])} | {GR.crescimento(ig_seg_2024[9],ig_seg_2023[9])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[9],ig_alcance_2024[8])} | {GR.crescimento(ig_alcance_2024[9],ig_alcance_2023[9])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[9],ig_vivitas_2024[8])} | {GR.crescimento(ig_vivitas_2024[9],ig_vivitas_2023[9])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[9],ig_visu_2024[8])} | {GR.crescimento(ig_visu_2024[9],ig_visu_2023[9])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(ig_seg_2024[10]), GR.numeroPorExtensso(ig_alcance_2024[10]), GR.numeroPorExtensso(ig_vivitas_2024[10]), GR.numeroPorExtensso(ig_visu_2024[10])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[10],ig_seg_2024[9])} | {GR.crescimento(ig_seg_2024[10],ig_seg_2023[10])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[10],ig_alcance_2024[9])} | {GR.crescimento(ig_alcance_2024[10],ig_alcance_2023[10])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[10],ig_vivitas_2024[9])} | {GR.crescimento(ig_vivitas_2024[10],ig_vivitas_2023[10])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[10],ig_visu_2024[9])} | {GR.crescimento(ig_visu_2024[10],ig_visu_2023[10])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(ig_seg_2024[11]), GR.numeroPorExtensso(ig_alcance_2024[11]), GR.numeroPorExtensso(ig_vivitas_2024[11]), GR.numeroPorExtensso(ig_visu_2024[11])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[11],ig_seg_2024[10])} | {GR.crescimento(ig_seg_2024[11],ig_seg_2023[11])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[11],ig_alcance_2024[10])} | {GR.crescimento(ig_alcance_2024[11],ig_alcance_2023[11])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[11],ig_vivitas_2024[10])} | {GR.crescimento(ig_vivitas_2024[11],ig_vivitas_2023[11])}'), FootnoteText(f'{GR.crescimento(ig_visu_2024[11],ig_visu_2024[10])} | {GR.crescimento(ig_visu_2024[11],ig_visu_2023[11])}')))

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
        sublist.add_item(NoEscape(r"\textbf{Abril} foi o melhor mês em \textbf{novos seguidores}."))
        sublist.add_item(NoEscape(r"\textbf{Outubro} foi o segundo melhor mês em \textbf{alcance} e o melhor em \textbf{visitas e visualizações}."))
        sublist.add_item(NoEscape(r"\textbf{Outubro} teve o segundo melhor número em \textbf{novos seguidores}."))
        sublist.add_item(NoEscape(r"\textbf{Janeiro} teve os números mais baixos em alcance. \textbf{Julho e setembro} teveram os menores números de \textbf{novos seguidores e visitas}, respectivamente."))
        sublist.add_item(NoEscape(r"\textbf{Novembro} tem números semelhantes aos de \textbf{agosto} em \textbf{novos seguidores e alcance}."))
        sublist.add_item(NoEscape(r"\textbf{Dezembro} foi o melhor mês em \textbf{alcance} e o terceiro em \textbf{visualizações}."))
        
doc.append(NewPage())

seguidoresIG_plot_path = GR.seguidorIG(ig_seg_2023, ig_seg_2024)
visitasIG_plot_path = GR.visitaIG(ig_vivitas_2023, ig_vivitas_2024)
alcanceIG_plot_path = GR.alcanceIG(ig_alcance_2023, ig_alcance_2024)
visualizacoes_plot_path = GR.visualizacoesIG(ig_visu_2023, ig_visu_2024)

with doc.create(Subsection('', numbering=False)):
    doc.append("Instagram (MENSAL): Seguidores, visitas, alcance e visualizações")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(seguidoresIG_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(alcanceIG_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visitasIG_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visualizacoes_plot_path, width=NoEscape(r'1\textwidth'))

doc.append(NewPage())

# doc.append(NewPage())

# recebendo camiho da imagem do gráfico e o total de seguidores do fb e ig
# fePublico_FBIG_plot_path, FB_followers, IG_followers = GR.fePublico_FBIG()

with doc.create(Subsection('Análise anual - 2024', numbering=False)):
    with doc.create(Subsubsection('Instagram', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas', 'Visualizações'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('Ano anterior'), FootnoteText('Ano anterior'), FootnoteText('Ano anterior'), FootnoteText('Ano anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data='2024'), GR.numeroPorExtensso(sum(ig_seg_2024)), GR.numeroPorExtensso(sum(ig_alcance_2024)), GR.numeroPorExtensso(sum(ig_vivitas_2024)), GR.numeroPorExtensso(sum(ig_visu_2024[6:]))))
                table.add_row(('', FootnoteText(f'{GR.crescimento(sum(ig_seg_2024),sum(ig_seg_2023))}'), FootnoteText(f'{GR.crescimento(sum(ig_alcance_2024),sum(ig_alcance_2023))}'), FootnoteText(f'{GR.crescimento(sum(ig_vivitas_2024),sum(ig_vivitas_2023))}'), FootnoteText(f'{GR.crescimento(sum(ig_visu_2024[6:]),sum(ig_visu_2023))}')))
                # table.add_hline()

doc.append(NewPage())

seguidoresIG_plot_path_ANUAL = GR.seguidorIG_ANUAL(sum(ig_seg_2023), sum(ig_seg_2024))
visitasIG_plot_path_ANUAL = GR.visitaIG_ANUAL(sum(ig_vivitas_2023), sum(ig_vivitas_2024))
alcanceIG_plot_path_ANUAL = GR.alcanceIG_ANUAL(sum(ig_alcance_2023), sum(ig_alcance_2024))
visualizacoes_plot_path_ANUAL = GR.visualizacoesIG_ANUAL(sum(ig_visu_2023), sum(ig_visu_2024[6:]))

with doc.create(Subsection('', numbering=False)):
    doc.append("Instagram (ANUAL): Seguidores, visitas, alcance e visualizações")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(seguidoresIG_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(alcanceIG_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visitasIG_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visualizacoes_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Instagram - Análise Anual:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"Em 2023 tivemos um ganho maior de seguidores. Apesar disso, os dois anos terminaram com saldo positivos de seguidores, ou seja, o ano de 2024 mesmo com um ganho menor foi finalizado com mais seguidores do que começou."))
        sublist.add_item(NoEscape(r"O alcance em 2024 foi superior ao ano anterior. Além do conteúdo entregado pelo Jornal Tribuna do Norte no Instagram, isso também pode ser justificado pelo saldo positivo de seguidores ao longo do ano."))
        sublist.add_item(NoEscape(r"O número de visitas em 2024 ficou abaixo em relação a 2023, isso pode ser uma das influências para o menor ganhor de seguidores."))

doc.append(NewPage())

with doc.create(Subsection('Análise mensal - 2024', numbering=False)):
    with doc.create(Subsubsection('Facebook', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas', 'Visualizações'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '628', '468 mil', '32 mil', GR.numeroPorExtensso(fb_visu_2024[0])))
                table.add_row(('', FootnoteText('+38% | +20%'), FootnoteText('-5% | -7,5%'), FootnoteText('+9,6% | +4,2%'), FootnoteText(f'{GR.crescimento(fb_visu_2024[0],fb_visu_2023[11])} | {GR.crescimento(fb_visu_2024[0],fb_visu_2023[0])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), GR.numeroPorExtensso(fb_seg_2024[1]), GR.numeroPorExtensso(fb_alcance_2024[1]), GR.numeroPorExtensso(fb_vivitas_2024[1]), GR.numeroPorExtensso(fb_visu_2024[1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[1],fb_seg_2024[0])} | {GR.crescimento(fb_seg_2024[1],fb_seg_2023[1])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[1],fb_alcance_2024[0])} | {GR.crescimento(fb_alcance_2024[1],fb_alcance_2023[1])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[1],fb_vivitas_2024[0])} | {GR.crescimento(fb_vivitas_2024[1],fb_vivitas_2023[1])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[1],fb_visu_2024[0])} | {GR.crescimento(fb_visu_2024[1],fb_visu_2023[1])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(fb_seg_2024[2]), GR.numeroPorExtensso(fb_alcance_2024[2]), GR.numeroPorExtensso(fb_vivitas_2024[2]), GR.numeroPorExtensso(fb_visu_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[2],fb_seg_2024[1])} | {GR.crescimento(fb_seg_2024[2],fb_seg_2023[2])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[2],fb_alcance_2024[1])} | {GR.crescimento(fb_alcance_2024[2],fb_alcance_2023[2])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[2],fb_vivitas_2024[1])} | {GR.crescimento(fb_vivitas_2024[2],fb_vivitas_2023[2])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[2],fb_visu_2024[1])} | {GR.crescimento(fb_visu_2024[2],fb_visu_2023[2])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(fb_seg_2024[3]), GR.numeroPorExtensso(fb_alcance_2024[3]), GR.numeroPorExtensso(fb_vivitas_2024[3]), GR.numeroPorExtensso(fb_visu_2024[3])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[3],fb_seg_2024[2])} | {GR.crescimento(fb_seg_2024[3],fb_seg_2023[3])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[3],fb_alcance_2024[2])} | {GR.crescimento(fb_alcance_2024[3],fb_alcance_2023[3])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[3],fb_vivitas_2024[2])} | {GR.crescimento(fb_vivitas_2024[3],fb_vivitas_2023[3])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[3],fb_visu_2024[2])} | {GR.crescimento(fb_visu_2024[3],fb_visu_2023[3])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(fb_seg_2024[4]), GR.numeroPorExtensso(fb_alcance_2024[4]), GR.numeroPorExtensso(fb_vivitas_2024[4]), GR.numeroPorExtensso(fb_visu_2024[4])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[4],fb_seg_2024[3])} | {GR.crescimento(fb_seg_2024[4],fb_seg_2023[4])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[4],fb_alcance_2024[3])} | {GR.crescimento(fb_alcance_2024[4],fb_alcance_2023[4])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[4],fb_vivitas_2024[3])} | {GR.crescimento(fb_vivitas_2024[4],fb_vivitas_2023[4])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[4],fb_visu_2024[3])} | {GR.crescimento(fb_visu_2024[4],fb_visu_2023[4])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(fb_seg_2024[5]), GR.numeroPorExtensso(fb_alcance_2024[5]), GR.numeroPorExtensso(fb_vivitas_2024[5]), GR.numeroPorExtensso(fb_visu_2024[5])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[5],fb_seg_2024[4])} | {GR.crescimento(fb_seg_2024[5],fb_seg_2023[5])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[5],fb_alcance_2024[4])} | {GR.crescimento(fb_alcance_2024[5],fb_alcance_2023[5])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[5],fb_vivitas_2024[4])} | {GR.crescimento(fb_vivitas_2024[5],fb_vivitas_2023[5])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[5],fb_visu_2024[4])} | {GR.crescimento(fb_visu_2024[5],fb_visu_2023[5])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Julho'), GR.numeroPorExtensso(fb_seg_2024[6]), GR.numeroPorExtensso(fb_alcance_2024[6]), GR.numeroPorExtensso(fb_vivitas_2024[6]), GR.numeroPorExtensso(fb_visu_2024[6])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[6],fb_seg_2024[5])} | {GR.crescimento(fb_seg_2024[6],fb_seg_2023[6])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[6],fb_alcance_2024[5])} | {GR.crescimento(fb_alcance_2024[6],fb_alcance_2023[6])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[6],fb_vivitas_2024[5])} | {GR.crescimento(fb_vivitas_2024[6],fb_vivitas_2023[6])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[6],fb_visu_2024[5])} | {GR.crescimento(fb_visu_2024[6],fb_visu_2023[6])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Agosto'), GR.numeroPorExtensso(fb_seg_2024[7]), GR.numeroPorExtensso(fb_alcance_2024[7]), GR.numeroPorExtensso(fb_vivitas_2024[7]), GR.numeroPorExtensso(fb_visu_2024[7])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[7],fb_seg_2024[6])} | {GR.crescimento(fb_seg_2024[7],fb_seg_2023[7])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[7],fb_alcance_2024[6])} | {GR.crescimento(fb_alcance_2024[7],fb_alcance_2023[7])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[7],fb_vivitas_2024[6])} | {GR.crescimento(fb_vivitas_2024[7],fb_vivitas_2023[7])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[7],fb_visu_2024[6])} | {GR.crescimento(fb_visu_2024[7],fb_visu_2023[7])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Setembro'), GR.numeroPorExtensso(fb_seg_2024[8]), GR.numeroPorExtensso(fb_alcance_2024[8]), GR.numeroPorExtensso(fb_vivitas_2024[8]), GR.numeroPorExtensso(fb_visu_2024[8])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[8],fb_seg_2024[7])} | {GR.crescimento(fb_seg_2024[8],fb_seg_2023[8])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[8],fb_alcance_2024[7])} | {GR.crescimento(fb_alcance_2024[8],fb_alcance_2023[8])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[8],fb_vivitas_2024[7])} | {GR.crescimento(fb_vivitas_2024[8],fb_vivitas_2023[8])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[8],fb_visu_2024[7])} | {GR.crescimento(fb_visu_2024[8],fb_visu_2023[8])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Outubro'), GR.numeroPorExtensso(fb_seg_2024[9]), GR.numeroPorExtensso(fb_alcance_2024[9]), GR.numeroPorExtensso(fb_vivitas_2024[9]), GR.numeroPorExtensso(fb_visu_2024[9])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[9],fb_seg_2024[8])} | {GR.crescimento(fb_seg_2024[9],fb_seg_2023[9])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[9],fb_alcance_2024[8])} | {GR.crescimento(fb_alcance_2024[9],fb_alcance_2023[9])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[9],fb_vivitas_2024[8])} | {GR.crescimento(fb_vivitas_2024[9],fb_vivitas_2023[9])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[9],fb_visu_2024[8])} | {GR.crescimento(fb_visu_2024[9],fb_visu_2023[9])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Novembro'), GR.numeroPorExtensso(fb_seg_2024[10]), GR.numeroPorExtensso(fb_alcance_2024[10]), GR.numeroPorExtensso(fb_vivitas_2024[10]), GR.numeroPorExtensso(fb_visu_2024[10])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[10],fb_seg_2024[9])} | {GR.crescimento(fb_seg_2024[10],fb_seg_2023[10])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[10],fb_alcance_2024[9])} | {GR.crescimento(fb_alcance_2024[10],fb_alcance_2023[10])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[10],fb_vivitas_2024[9])} | {GR.crescimento(fb_vivitas_2024[10],fb_vivitas_2023[10])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[10],fb_visu_2024[9])} | {GR.crescimento(fb_visu_2024[10],fb_visu_2023[10])}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Dezembro'), GR.numeroPorExtensso(fb_seg_2024[11]), GR.numeroPorExtensso(fb_alcance_2024[11]), GR.numeroPorExtensso(fb_vivitas_2024[11]), GR.numeroPorExtensso(fb_visu_2024[11])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[11],fb_seg_2024[10])} | {GR.crescimento(fb_seg_2024[11],fb_seg_2023[11])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[11],fb_alcance_2024[10])} | {GR.crescimento(fb_alcance_2024[11],fb_alcance_2023[11])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[11],fb_vivitas_2024[10])} | {GR.crescimento(fb_vivitas_2024[11],fb_vivitas_2023[11])}'), FootnoteText(f'{GR.crescimento(fb_visu_2024[11],fb_visu_2024[10])} | {GR.crescimento(fb_visu_2024[11],fb_visu_2023[11])}')))

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
        sublist.add_item(NoEscape(r"\textbf{Janeiro} foi o melhor mês em \textbf{novos seguidores e visitas}. Também teve o melhor crescimento em visitas."))
        sublist.add_item(NoEscape(r"Em \textbf{janeiro}, apesar da queda no alcance as outras métricas ainda cresceram."))
        sublist.add_item(NoEscape(r"\textbf{Agosto} teve o maior alcance."))
        sublist.add_item(NoEscape(r"\textbf{Setembro} está entre os meses com os menores números em todas as métricas, ficando acima apenas de \textbf{março e novembro} em \textbf{novos seguidores e alcance} e de \textbf{dezembro} em \textbf{alcance}."))
        sublist.add_item(NoEscape(r"\textbf{Novembro} tem números mais baixos em \textbf{novos seguidores e alcance}."))
        sublist.add_item(NoEscape(r"\textbf{Dezembro} só não tem números mais baixos em \textbf{visitas} do que \textbf{setembro}. Tembém foi o mês com o segundo maior número de \textbf{visualizações}."))
        sublist.add_item(NoEscape(r"\textbf{Outubro} foi o mês com o maior número de \textbf{visualizações}."))

doc.append(NewPage())

seguidoresFB_plot_path = GR.seguidorFB(fb_seg_2023, fb_seg_2024)
visitasFB_plot_path = GR.visitaFB(fb_vivitas_2023, fb_vivitas_2024)
alcanceFB_plot_path = GR.alcanceFB(fb_alcance_2023, fb_alcance_2024)
visualizacoesFB_plot_path = GR.visualizacoesFB(fb_visu_2023, fb_visu_2024)

with doc.create(Subsection('', numbering=False)):
    doc.append("Facebook (MENSAL): Seguidores, visitas, alcance e visualizações")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(seguidoresFB_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(alcanceFB_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visitasFB_plot_path, width=NoEscape(r'1\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visualizacoesFB_plot_path, width=NoEscape(r'1\textwidth'))

doc.append(NewPage())

with doc.create(Subsection('Análise anual - 2024', numbering=False)):
    with doc.create(Subsubsection('Facebook', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas', 'Visualizações'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('Ano anterior'), FootnoteText('Ano anterior'), FootnoteText('Ano anterior'), FootnoteText('Ano anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data='2024'), GR.numeroPorExtensso(sum(fb_seg_2024)), GR.numeroPorExtensso(sum(fb_alcance_2024)), GR.numeroPorExtensso(sum(fb_vivitas_2024)), GR.numeroPorExtensso(sum(fb_visu_2024[8:]))))
                table.add_row(('', FootnoteText(f'{GR.crescimento(sum(fb_seg_2024),sum(fb_seg_2023))}'), FootnoteText(f'{GR.crescimento(sum(fb_alcance_2024),sum(fb_alcance_2023))}'), FootnoteText(f'{GR.crescimento(sum(fb_vivitas_2024),sum(fb_vivitas_2023))}'), FootnoteText(f'{GR.crescimento(sum(fb_visu_2024[8:]),sum(fb_visu_2023))}')))
                # table.add_hline()

doc.append(NewPage())

seguidoresFB_plot_path_ANUAL = GR.seguidorFB_ANUAL(sum(fb_seg_2023), sum(fb_seg_2024))
visitasFB_plot_path_ANUAL = GR.visitaFB_ANUAL(sum(fb_vivitas_2023), sum(fb_vivitas_2024))
alcanceFB_plot_path_ANUAL = GR.alcanceFB_ANUAL(sum(fb_alcance_2023), sum(fb_alcance_2024))
visualizacoesFB_plot_path_ANUAL = GR.visualizacoesFB_ANUAL(sum(fb_visu_2023), sum(fb_visu_2024[8:]))

with doc.create(Subsection('', numbering=False)):
    doc.append("Facebook (ANUAL): Seguidores, visitas, alcance e visualizações")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(seguidoresFB_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(alcanceFB_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visitasFB_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))
    with doc.create(Figure(position='H')) as plot:
        plot.add_image(visualizacoesFB_plot_path_ANUAL, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

with doc.create(Enumerate(enumeration_symbol=r"•")) as itemize:     
    itemize.add_item("Facebook - Análise Anual:")
    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        sublist.add_item(NoEscape(r"No ano de 2024 todas as métricas do Facebook foram inferiores em relação a 2023. Ao longo do ano vimos em vários momentos seus seguidores caindo, muitas vezes por várias semanas em sequência. E apesar de que o ano foi finalizado com mais seguidores do que 2023, foram apenas 119 a mais. Para fazer uma comparação, em janeiro de 2024 o Facebook tinha 332.603 seguidores, o que é mais do que em dezembro de 2023 e dezembro de 2024."))

doc.append(NewPage())

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Funcionamento dos algoritmos:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Facebook:} O algoritmo do Facebook prioriza os conteúdos que geram mais interações, como curtidas, comentários e compartilhamentos. Ele também considera o grau de relacionamento entre os usuários e as contas que eles seguem, mostrando mais publicações de amigos e familiares do que de páginas. Além disso, o Facebook leva em conta a relevância e a atualidade dos conteúdos, dando mais destaque para as notícias e os assuntos do momento;'))
                sublist.add_item(NoEscape(r'\textbf{Instagram:} O a lgoritmo do Instagram também se baseia no engajamento, no relacionamento e na temporalidade dos conteúdos. Ele mostra primeiro as postagens e as histórias das contas com as quais o usuário mais interage, seja por meio de curtidas, comentários, mensagens diretas ou buscas. Ele também valoriza os conteúdos mais recentes e mais relevantes para o usuário, de acordo com os seus interesses e hábitos;'))

doc.append(NewPage())

with doc.create(MiniPage(align='c')):
    doc.append(MediumText(("Observações")))

with doc.create(Itemize()) as itemize:
            itemize.add_item('Seguidores:')
            with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
                sublist.add_item(NoEscape(f'É  possível observar que o número de novos seguidores ou inscritos adquiridos nos mês pode diferir um pouco na primeira tabela, na descrição dela e em cada uma das tabelas seguintes das respectivas redes sociais.'))
                sublist.add_item(NoEscape(f'Nas tabelas de cada rede social está a quantidade total de usuários que seguiram ao logo do mês analisado, mas nesse caso é o dado que foi informado diretamente pela rede social em questão. Chamaremos esse dado de "follows" e os que deixaram de seguir de "unfollows", para uma melhor identificação.'))
                sublist.add_item(NoEscape(f'Na primeira tabela do relatório está o númere referente a quantidade de seguidores que realmente continuaram seguindo a(o) página/perfil/canal ao final do mês. Logo abaixo, o dado "Seguidores adquiridos no mês:" é a quantidade total de usuários que seguiram ao logo do mês analisado. Nesses dois casos os valores são obtidos atraves da quantidade total de seguidores no mês atual e anterior e quantos usuários deixaram de seguir no mês atual.'))
                sublist.add_item(NoEscape(f'Por exemplo: se subtrairmos a quantidade total de seguidores do mês atual pela anterior e somarmos isso a quantos deixaram de seguir (atual - anterior + unfollow), teremos a quantidade total de "Seguidores adquiridos no mês:". Esse valor seria o mesmo dado de seguidores adquiridos que está nas tabelas de cada rede social (follows). E a quantidade de usuários que continuaram seguindo a página seria apenas a diferença do total de seguidores do mês atual e anterior (atual - anterior), que deveria dar no mesmo de subtrair "follows" por "unfollows" (follows - unfollows). Para que fique mais claro, a diferença entre "follows" e "unfollows" somada a quantidade total de seguidores do mês anterior deveria ser igual a quantidade total do mês atual (follows - unfollows + total seg. anterior = total seg. atual).'))
                sublist.add_item(NoEscape(f'Todos esses dados são fornecidos pelas próprias plataformas, mas eles podem acabar sendo um pouco diferentes para sua respectiva rede social.'))
            # itemize.add_item('Top15 notícias mais pesquisadas: as impressões são referentes a quantidade de vezes que uma pesquisa sobre determinado assunto foi realizada e foi possível visualizar o link da notícia no portal do TN entre os resultados.')
                        
                
# Gera o arquivo LaTeX
doc.generate_pdf(fr'C:\Users\{GR.path_aliss}\Documents\Repositórios\Relatórios\TN\Relatório-TN_ANUAL - fb e ig', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")