from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage, Math
from pylatex.utils import bold
import graficosRelatorioSemanal as GR
import pandas as pd
import rpy2.robjects as robjects
import numpy

# Cria um novo documento LaTeX
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "lmargin": "2.5cm", "landscape": True}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório das Redes Sociais")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Relatório semanal")))
        doc.append(LineBreak())

#INSTAGRAM
ig_seg_2024 = [1299,2685,1476,1499,2054,1558,1469,358,1693,1584,1323,1317,1130,1181,1143,1128,1310,1245,1395,1333,1334,1528,1468,1290,1236,1366,1246,1604,1400,1541,1243,2170,931,1264,1114,1287,1004,1540,1630,1350,1145,1392]
ig_seg_2024_perdeu = [1040,1165,1080,1114,1228,1094,1070,315,1050,1040,1074,1081,996,963,1161,1126,1134,1209,1616,1732,1137,1140,1274,1080,992,1106,978,1050,2115,1739,1549,930,1162,1064,852,933,879,895,1051,984,1633,1248]
ig_alcance_2024 = [330170,619778,394150,368303,430160,430041,430095,518193,564967,444404,479370,512399,445377,407004,491253,437034,513738,558433,615446,562833,538665,439570,521604,567754,421204,459048,429685,681810,626215,707526,661841,706352,451946,481716,537018,653258,540510,535088,769092,565434,572468,574663]
ig_vivitas_2024 = [24896,53103,28198,27847,49389,28931,29098,31347,33708,38352,26704,26949,20380,21911,22017,24981,29750,25951,39564,29111,21658,32248,29450,22943,24755,27086,27575,59705,48200,44503,37933,58692,29239,25762,21512,22167,24009,28540,27000,29031,26868,23780]
ig_visualizacoes = [8148162,7086305,8576180,8210348,7767102,7377090]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
ig_seg_2024_total = [532444,533616,534049,534392,535150,535716,536047,536508,537733,537993,538290,538507,538756,538846,538864,538830,539051,539028,538783,538412,538630,538982,539191,539421,539673,539945,540385,540796,539941,539600,540800,540586,540879,541103,541504,541548,542193,542772,543138,542650,542794]

#FACEBOOK
fb_seg_2024 = [30,61,71,42,83,80,49,74,40,67,30,36,84,37,62,62,80,62,132,210,68,87,82,46,53,45,27,44,48,110,49,45,32,33,33,42,62,27,55,75,82,46]
fb_seg_2024_perdeu = [34,35,44,35,49,40,31,33,41,32,53,34,36,36,29,35,47,36,36,72,47,43,55,51,39,51,39,49,75,90,79,32,57,43,35,46,53,107,51,38,183,62]
fb_alcance_2024 = [64958,88738,112464,63173,142594,139599,101924,132711,87877,114958,127230,78859,119785,84527,109848,87594,147513,120924,243257,372104,132062,116796,105821,91718,88120,78560,45397,64761,76336,144122,97423,65137,39119,80527,61214,71529,105842,62199,110877,99563,116162,72022]
fb_vivitas_2024 = [6500,7686,8158,6718,6757,7087,7074,5937,6326,5417,5125,3796,5242,5130,5452,5563,5332,5172,6152,6201,5262,6606,5332,4866,4619,5015,4640,6797,5731,6298,5696,6370,4981,4796,5179,4976,4964,5253,5144,5296,4895,4588]
fb_visualizacoes = [973081,685619,742979,814864,698242,576001]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
fb_seg_2024_total = [332419,332392,332389,332334,332339,332314,332287,332176,332214,332210,332186,332136,332133,332086,332086,332049,332035,332006,332075,332140,332099,332122,332085,332018,331995,331941,331858,331821,331755,331724,331611,331532,331482,331426,331372,331658,331578,331582,331619,331518,331502]

#TWITTER
tw_seg_2024 = [359,455,1249,892,801,725,1009,2464,886,2460]
tw_impressões_2024 = [86012,102051,96123,100004,113293,95767,95199,90299,78103,89681]
tw_engajamentos_2024 = [2390,3324,3242,3257,4164,2661,3219,4553,2650,4576]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
tw_seg_2024_total = [312146,312041,312437,312722,312797,313181,314742,315456,317307,319917]
tw_seg_2024_perdeu = [890,tw_seg_2024[1]-(tw_seg_2024_total[1]-tw_seg_2024_total[0]),tw_seg_2024[2]-(tw_seg_2024_total[2]-tw_seg_2024_total[1]),tw_seg_2024[3]-(tw_seg_2024_total[3]-tw_seg_2024_total[2]),tw_seg_2024[4]-(tw_seg_2024_total[4]-tw_seg_2024_total[3]),tw_seg_2024[5]-(tw_seg_2024_total[5]-tw_seg_2024_total[4]),abs(tw_seg_2024[6]-(tw_seg_2024_total[6]-tw_seg_2024_total[5])),tw_seg_2024[7]-(tw_seg_2024_total[7]-tw_seg_2024_total[6]),abs(tw_seg_2024[8]-(tw_seg_2024_total[8]-tw_seg_2024_total[7])),abs(tw_seg_2024[9]-(tw_seg_2024_total[9]-tw_seg_2024_total[8]))] #sabe a quantidade que perdeu de acordo com a diferença de seguidores entre um mês e outro e o ganho total de seguidores no mês


# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection(f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Instagram'), GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]), GR.formataNumero(ig_alcance_2024[-1]), GR.formataNumero(ig_vivitas_2024[-1]), GR.formataNumero(ig_visualizacoes[-1])))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil', 'visualizações'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Facebook'), GR.formataNumero(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]), GR.formataNumero(fb_alcance_2024[-1]), GR.formataNumero(fb_vivitas_2024[-1]), GR.formataNumero(fb_visualizacoes[-1])))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil', 'visualizações'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     itemize.add_item(f"Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, {GR.formataNumero(portal_novosUsuarios_2024[-1]+(ig_seg_2024_total[-1]-ig_seg_2024_total[-2])+(fb_seg_2024_total[-1]-fb_seg_2024_total[-2])+(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]))} novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube.")
        with doc.create(Itemize()) as itemize:
            itemize.add_item(f"Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, {GR.formataNumero((ig_seg_2024[-1])+(fb_seg_2024[-1]))} novas contas, entre Instagram e Facebook.")
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(ig_seg_2024_total[-1])}. Total de seguidores na semana anterior: {GR.formataNumero(ig_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos na semana: {GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]+ig_seg_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(ig_seg_2024_perdeu[-1])}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]+ig_seg_2024_perdeu[-1],ig_seg_2024_perdeu[-1])}")
                #sublist.add_item(f"O Instagram não disponibilizou os dados de ganhos e perda de seguidores da semana passada, portanto temos disponível apenas o saldo de seguidores.")
                #sublist.add_item(f"nan: not a number (não é um número).")
                # sublist.add_item(f"Queda nos seguidores do Instagram.")
            itemize.add_item(Command('textbf', arguments='Facebook'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(fb_seg_2024_total[-1])}. Total de seguidores na semana anterior: {GR.formataNumero(fb_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos na semana: {GR.formataNumero(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]+fb_seg_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(fb_seg_2024_perdeu[-1])}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]+fb_seg_2024_perdeu[-1],fb_seg_2024_perdeu[-1])}")
                sublist.add_item(f"Sem queda nos seguidores do Facebook essa semana.")
                

doc.append(NewPage())

# doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
# doc.preamble.append(NoEscape(r'\usepackage{float}'))

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
#         plot.add_image(GR.top15cliques_plot_path, width=NoEscape(r'1\textwidth'))

# doc.append(NewPage())

# # VISUALIZAÇÕES E USUÁRIOS PORTAL
# GR.visualizacoesUsuarios()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: comparativo de visualizações e acessos de usuários")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.visualizacoesUsuarios_plot_path, width=NoEscape(r'1\textwidth'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\small{Este gráfico mostra a semelhança de compatamento entre diferentes dados do portal ao longo do período analisado.}'))

# doc.append(NewPage())

# # VISUALIZAÇÕES
# GR.visu_cumsum()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: visualizações com valores acumulativos")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.visu_cumsum_plot_path, width=NoEscape(r'0.9\textwidth'))

# # usuariso unicos
# GR.usuUni_cumsum()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: usuários únicos com valores acumulativos")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.usuUni_cumsum_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# # usuariso unicos
# GR.newUsu_cumsum()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: novos usuários com valores acumulativos")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.newUsu_cumsum_plot_path, width=NoEscape(r'0.9\textwidth'))

# # usuariso unicos
# GR.usuRec_cumsum()
# # Adiciona uma seção ao documento
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Portal: usuários recorrente com valores acumulativos")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(GR.usuRec_cumsum_plot_path, width=NoEscape(r'0.9\textwidth'))

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

# # recebendo camiho da imagem do gráfico e o total de seguidores do fb e ig
# fePublico_FBIG_plot_path, FB_followers, IG_followers = GR.fePublico_FBIG()

# with doc.create(Subsection('Análise semanal', numbering=False)):
with doc.create(Subsubsection('Instagram', numbering=False)):
    with doc.create(MiniPage(align='c')):
        # Adiciona a tabela de resultados
        with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
            
            table.add_row((MultiRow(3, data='Semana'), 'Novos seguidores', 'Alcance', 'Visitas','Visualizações'))
            table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
            table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
            table.add_hline()
            table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(ig_seg_2024[-1]), GR.numeroPorExtensso(ig_alcance_2024[-1]), GR.numeroPorExtensso(ig_vivitas_2024[-1]), GR.numeroPorExtensso(ig_visualizacoes[-1])))
            table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[-1],ig_seg_2024[-2])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[-1],ig_alcance_2024[-2])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[-1],ig_vivitas_2024[-2])}'), FootnoteText(f'{GR.crescimento(ig_visualizacoes[-1],ig_visualizacoes[-2])}')))

# doc.append(NewPage())
# pocentoMaior = 93.6
# pocentoMenor = 6.4
# publicacoes = 78.9
# reels = 11.1
# stories = 10
# visualizacoesIG_plot_path = GR.visualizacoesIG(7694872, 8851512,pocentoMaior, pocentoMenor)
# grafico_barras_composto_plot_path = GR.grafico_barras_composto([(publicacoes/100)*pocentoMaior,(publicacoes/100)*pocentoMenor,publicacoes,(reels/100)*pocentoMaior,(reels/100)*pocentoMenor,reels,(stories/100)*pocentoMaior,(stories/100)*pocentoMenor,stories,0,0,0])
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Instagram: Visualizações e público")
#     doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='h')) as plot:
#         plot.add_image(visualizacoesIG_plot_path, width=NoEscape(r'0.5\textwidth'))
#         plot.add_image(grafico_barras_composto_plot_path, width=NoEscape(r'0.5\textwidth'))

doc.append(NewPage())
seguidoresIG_plot_path = GR.seguidorIG()
visitasIG_plot_path = GR.visitaIG()
alcanceIG_plot_path = GR.alcanceeIG()
visualizacoes_plot_path = GR.visualizacoeesIG()
with doc.create(Subsection('', numbering=False)):
    doc.append("Instagram: Seguidores, visitas, alcance e visualizações")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h')) as plot:
        plot.add_image(seguidoresIG_plot_path, width=NoEscape(r'0.5\textwidth'))
        plot.add_image(alcanceIG_plot_path, width=NoEscape(r'0.5\textwidth'))
    with doc.create(Figure(position='h')) as plot:
        plot.add_image(visitasIG_plot_path, width=NoEscape(r'0.5\textwidth'))
        plot.add_image(visualizacoes_plot_path, width=NoEscape(r'0.5\textwidth'))
         

# doc.append(NewPage())
# cidadesIG_plot_path = GR.grafico_cidades(['Natal', 'Parnamirim', 'Mossoró', 'Ceará-Mirim','Macaiba','Caicó','Assu','Currais Novos'],[43.7,11.2,2.5,2.2,1.6,0.9,0.8,0.8])
# FEIG_plot_path = GR.grafico_faixa_etaria(['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'],[0.7,9.3,31.3,31.7,15.4,7.5,3.8])
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Instagram: Cidades e faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='h')) as plot:
#         plot.add_image(cidadesIG_plot_path, width=NoEscape(r'0.5\textwidth'))
#         plot.add_image(FEIG_plot_path, width=NoEscape(r'0.5\textwidth'))

# doc.append(NewPage())
# pocentoMaior2 = 96.9
# pocentoMenor2 = 3.1
# publicacoes2 = 90
# reels2 = 9.7
# stories2 = 0.3
# sexoIG_plot_path = GR.sexoIG(ig_seg_2024_total[-1],ig_seg_2024_total[-2],61.7,38.3)
# interacoesIG_plot_path = GR.interacoesIG(184100,177700,96.9,3.1)
# grafico_barras_composto2_plot_path = GR.grafico_barras_composto2([(publicacoes2/100)*pocentoMaior2,(publicacoes2/100)*pocentoMenor2,publicacoes2,(reels2/100)*pocentoMaior2,(reels2/100)*pocentoMenor2,reels2,(stories2/100)*pocentoMaior2,(stories2/100)*pocentoMenor2,stories2,0,0,0])
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Instagram: interações")
#     with doc.create(Figure(position='h')) as plot:
#         plot.add_image(interacoesIG_plot_path, width=NoEscape(r'0.5\textwidth'))
#         plot.add_image(grafico_barras_composto2_plot_path, width=NoEscape(r'0.5\textwidth'))

doc.append(NewPage())

with doc.create(Subsubsection('Facebook', numbering=False)):
    with doc.create(MiniPage(align='c')):
        # Adiciona a tabela de resultados
        with doc.create(Tabular('|c|c|c|c|c|', booktabs =True)) as table:
            
            table.add_row((MultiRow(3, data='Semana'), 'Novos seguidores', 'Alcance', 'Visitas','Visualizações'))
            table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
            table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
            table.add_hline()
            table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(fb_seg_2024[-1]), GR.numeroPorExtensso(fb_alcance_2024[-1]), GR.numeroPorExtensso(fb_vivitas_2024[-1]), GR.numeroPorExtensso(fb_visualizacoes[-1])))
            table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[-1],fb_seg_2024[-2])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[-1],fb_alcance_2024[-2])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[-1],fb_vivitas_2024[-2])}'), FootnoteText(f'{GR.crescimento(fb_visualizacoes[-1],fb_visualizacoes[-2])}')))


        # # Adiciona informações extras
        # # Adiciona uma lista com marcadores
        # with doc.create(Itemize()) as itemize:
        #     # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
        #     itemize.add_item('Legenda:')
        #     #doc.append(NoEscape(r'\newline'))
        #     with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
        #         sublist.add_item(NoEscape(r'\textbf{Alcance:} Essa métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram e/ou Facebook, incluindo publicações e stories que foram turbinados. Também pode ser interpretada como a quantidade de contas atingidas;'))
        #         sublist.add_item(NoEscape(r'\textbf{Visitas:} número de vezes que usuários visitaram seu perfil.'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\textbf{Os detales demográficos (faixa etária, gênero e cidades) do facebook e instagram estavam indisponíveis.}'))
doc.append(NewPage())
seguidoresFB_plot_path = GR.seguidorFB()
visitasFB_plot_path = GR.visitaFB()
alcanceFB_plot_path = GR.alcanceeFB()
visualizacoesFB_plot_path = GR.visualizacoeesFB()
with doc.create(Subsection('', numbering=False)):
    doc.append("Facebook: Seguidores, visitas, alcance e visualizações")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h')) as plot:
        plot.add_image(seguidoresFB_plot_path, width=NoEscape(r'0.5\textwidth'))
        plot.add_image(alcanceFB_plot_path, width=NoEscape(r'0.5\textwidth'))
    with doc.create(Figure(position='h')) as plot:
        plot.add_image(visitasFB_plot_path, width=NoEscape(r'0.5\textwidth'))
        plot.add_image(visualizacoesFB_plot_path, width=NoEscape(r'0.5\textwidth'))

# doc.append(NewPage())
# cidadesFB_plot_path = GR.grafico_cidadesFB(['Natal', 'Parnamirim', 'Mossoró', 'Ceará-Mirim','Macaiba'],[43.5,5.5,2.4,0.9,0.9])
# totalFB = 331654
# fe1824 = (totalFB*(2.5)+totalFB*(2))/totalFB
# fe2534 = (totalFB*(18.4)+totalFB*(14.3))/totalFB
# fe3544 = (totalFB*(18.3)+totalFB*(13.7))/totalFB
# fe4554 = (totalFB*(9.7)+totalFB*(7.1))/totalFB
# fe5564 = (totalFB*(5.3)+totalFB*(3.5))/totalFB
# fe65 = (totalFB*(3.1)+totalFB*(2.1))/totalFB
# FEFB_plot_path = GR.grafico_faixa_etariaFB(['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'],[0,fe1824,fe2534,fe3544,fe4554,fe5564,fe65])
# with doc.create(Subsection('', numbering=False)):
#     doc.append("Instagram: Cidades e faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='h')) as plot:
#         plot.add_image(cidadesFB_plot_path, width=NoEscape(r'0.5\textwidth'))
#         plot.add_image(FEFB_plot_path, width=NoEscape(r'0.5\textwidth'))

# # fePublico_FBIG_plot_path, FB_followers, IG_followers = GR.fePublico_FBIG
# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB e IG: audiência por sexo e faixa etária")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(fePublico_FBIG_plot_path, width=NoEscape(r'0.8\textwidth'))

# doc.append(NewPage())

# publicoCidades_plot_path = GR.publicoCidades()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB e IG: audiência por cidades")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(publicoCidades_plot_path, width=NoEscape(r'1\textwidth'))

doc.append(NewPage())

# curtidasFB_plot_path = GR.curtidasFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: novos seguidores ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(curtidasFB_plot_path, width=NoEscape(r'0.9\textwidth'))

# visitasFB_plot_path = GR.visitasFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: visitas ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visitasFB_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# alcanceFB_plot_path = GR.alcanceFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: alcance ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(alcanceFB_plot_path, width=NoEscape(r'0.9\textwidth'))

# dadosFB_plot_path = GR.dadosFB()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("FB: comparativo de seguidores, visitas e alcance. (Obs.: dados fora de escala para uma melhor visualização)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(dadosFB_plot_path, width=NoEscape(r'0.75\textwidth'))

# doc.append(NewPage())

# # with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
# #             itemize.add_item(NoEscape(r'\textbf{Os dados diários de seguidores do Instagram não foram disponobilizados pela Meta essa semana.}'))
# seguidoresIG_plot_path, seguidoresIG = GR.seguidoresIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: ganho de seguidores ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(seguidoresIG_plot_path, width=NoEscape(r'0.9\textwidth'))

# visitasIG_plot_path, visitasIG = GR.visitasIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: visitas ao perfil ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(visitasIG_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# alcanceIG_plot_path, alcanceIG = GR.alcanceIG()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: alcance do perfil ao longo do mês")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(alcanceIG_plot_path, width=NoEscape(r'0.9\textwidth'))

# doc.append(NewPage())

# dadosIG_plot_path = GR.dadosIG(40,500)

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("IG: comparativo de seguidores, visitas e alcance. (Obs.: dados fora de escala para uma melhor visualização)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(dadosIG_plot_path, width=NoEscape(r'1\textwidth'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\small{Este gráfico mostra a semelhança de compatamento entre diferentes dados do portal ao longo do período analisado.}'))
# doc.append(NewPage())

# with doc.create(Subsection('Análise semanal', numbering=False)):
#     with doc.create(Subsubsection('Twitter', numbering=False)):
#         with doc.create(MiniPage(align='c')):
#             # Adiciona a tabela de resultados
#             with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
#                 table.add_row((MultiRow(3, data='Semana'), 'Novos seguidores', 'Impressões', 'Engajamentos'))
#                 table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#                 table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#                 table.add_hline()
#                 table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(tw_seg_2024[-1]), GR.numeroPorExtensso(tw_impressões_2024[-1]), GR.numeroPorExtensso(tw_engajamentos_2024[-1])))
#                 table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[-1],tw_seg_2024[-2])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[-1],tw_impressões_2024[-2])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[-1],tw_engajamentos_2024[-2])}')))

#         # Adiciona informações extras
#         # Adiciona uma lista com marcadores
#         with doc.create(Itemize()) as itemize:
#             # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
#             itemize.add_item('Legenda:')
#             #doc.append(NoEscape(r'\newline'))
#             with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#                 sublist.add_item(NoEscape(r'\textbf{Impressões:} número de vezes que os usuários viram o(s) Tweet(s);'))
#                 sublist.add_item(NoEscape(r'\textbf{Engajamentos:} número total de vezes que um usuário interagiu com o(s) Tweet(s). Isso inclui todos os cliques em qualquer lugar no Tweet como: hashtags, links, avatar, nome de usuário e expansão do Tweet, Retweets, respostas e favoritos.'))

doc.append(NewPage())

# engajamentoTW_plot_path = GR.engajamentoTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: engajamento do twitter")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(engajamentoTW_plot_path, width=NoEscape(r'0.8\textwidth'))

# impressoesTW_plot_path = GR.impressoesTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: impressões do twitter")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(impressoesTW_plot_path, width=NoEscape(r'0.8\textwidth'))

# doc.append(NewPage())

# seguidoresTW_plot_path = GR.seguidoresTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: ganho de seguidores no twitter ao logo do mês. (Esses dados levam em consideração apenas os ganhos)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(seguidoresTW_plot_path, width=NoEscape(r'0.8\textwidth'))

# dadosTW_plot_path = GR.dadosTW()

# # Adiciona uma seção ao documento
# with doc.create(Section('', numbering=False)):
#     doc.append("TW: comparativo de engajamentos, impressões e seguidores. (Obs.: dados fora de escala para uma melhor visualização)")
#     # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
#     # Adiciona a figura ao documento
#     with doc.create(Figure(position='H')) as plot:
#         plot.add_image(dadosTW_plot_path, width=NoEscape(r'0.8\textwidth'))

# doc.append(NewPage())

# with doc.create(Subsection('Análise semanal', numbering=False)):
#     with doc.create(Subsubsection('YouTube', numbering=False)):
#         with doc.create(MiniPage(align='c')):
#             # Adiciona a tabela de resultados
#             with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
#                 table.add_row((MultiRow(3, data='Semana'), 'Novos inscritos', 'Visualizações', 'Horas de exibição'))
#                 table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#                 table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#                 table.add_hline()
#                 table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(yb_inc_2024[-1]), GR.numeroPorExtensso(yb_visualizacoes_2024[-1]), GR.numeroPorExtensso(yb_horas_2024[-1])))
#                 table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[-1],yb_inc_2024[-2])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[-1],yb_visualizacoes_2024[-2])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[-1],yb_horas_2024[-2])}')))

# with doc.create(Subsection('', numbering=False)):
#     with doc.create(Subsubsection('YouTube - TN: Monetização', numbering=False)):
#         with doc.create(MiniPage(align='c')):
#             # Adiciona a tabela de resultados            
#             with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
            
#                 table.add_row((MultiRow(5, data='Semana'), FootnoteText('Impressões de anúncios'), FootnoteText('Visualizações monetizadas'), FootnoteText('Receita bruta'), FootnoteText('YTB Premium'), FootnoteText('Receita estimada (AdSense)')))
#                 table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#                 table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#                 table.add_hline()
#                 table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(impressoes_yb_TN[-1]), GR.numeroPorExtensso(visuMonetizadas_yb_TN[-1]), GR.numeroPorExtensso(receitaBruta_yb_TN[-1]), GR.numeroPorExtensso(premium_yb_TN[-1]), GR.numeroPorExtensso(AdSense_yb_TN[-1])))
#                 table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN[-1],impressoes_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN[-1],visuMonetizadas_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN[-1],receitaBruta_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN[-1],premium_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN[-1],AdSense_yb_TN[-2])}')))

# with doc.create(Subsection('', numbering=False)):
#     with doc.create(Subsubsection('YouTube - JPN: Monetização', numbering=False)):
#         with doc.create(MiniPage(align='c')):
#             # Adiciona a tabela de resultados            
#             with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
            
#                 table.add_row((MultiRow(5, data='Semana'), 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta', 'YTB Premium', 'Receita estimada (AdSense)'))
#                 table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
#                 table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
#                 table.add_hline()
#                 table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(impressoes_yb_JPN[-1]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN[-1]), GR.numeroPorExtensso(receitaBruta_yb_JPN[-1]), GR.numeroPorExtensso(premium_yb_JPN[-1]), GR.numeroPorExtensso(AdSense_yb_JPN[-1])))
#                 table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN[-1],impressoes_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN[-1],visuMonetizadas_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN[-1],receitaBruta_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN[-1],premium_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN[-1],AdSense_yb_JPN[-2])}')))

#         # Adiciona informações extras
#         # Adiciona uma lista com marcadores
#         with doc.create(Itemize()) as itemize:
#             # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
#             itemize.add_item('Legenda:')
#             #doc.append(NoEscape(r'\newline'))
#             with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
#                 sublist.add_item(NoEscape(r'\textbf{Impressões de anúncios:} quantidade de vezes que o anúncio apareceu na tela dos usuários, ou seja, o anúncio começou a ser carregado no dispositivo do usuário, e em alguns casos pode nem ter sido carregado por completo;'))
#                 sublist.add_item(NoEscape(r'\textbf{Visualizações monetizadas:} uma reprodução monetizada ocorre quando um espectador assiste um vídeo e pelo menos uma impressão de anúncios é exibida. Esse tipo de reprodução também é contabilizado quando o espectador para de assistir durante o anúncio precedente sem assistir o vídeo;'))
#                 sublist.add_item(NoEscape(r'\textbf{Receita bruta:} receita bruta estimada de todas as fontes de publicidade vendidas pelo Google para o período selecionado. Não se deve confundir receita de anúncios do YouTube com receita estimada ou receita líquida que são calculadas em seus contratos de participação nos lucros. ;'))
#                 sublist.add_item(NoEscape(r'\textbf{YouTube Premium:} receita estimada do YouTube Premium para o período selecionado;'))
#                 sublist.add_item(NoEscape(r'\textbf{Receita estimada (AdSense):} receita estimada de publicidade vendida pelo Google AdSense para o período selecionado. Esse valor é o que é de direito do propietario do canal, já com os descontos feitos pelo YouTube de acordo com o contrato e o que diz respeito a participação de lucros.'))
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
                # sublist.add_item(NoEscape(r'\textbf{Twitter:} O algoritmo do Twitter tem duas formas de exibir os conteúdos: o modo cronológico e o modo destacado. No modo cronológico, o usuário vê os tweets mais recentes em ordem de publicação. No modo destacado, o usuário vê os tweets mais relevantes para ele, de acordo com o seu perfil, as suas interações e os assuntos do momento. O Twitter também mostra os tweets mais populares e mais comentados na seção “O que está acontecendo”;'))
                # sublist.add_item(NoEscape(r'\textbf{YouTube:} O algoritmo do YouTube tem como objetivo aumentar o tempo de permanência dos usuários na plataforma, recomendando os vídeos que eles têm mais chances de assistir e se engajar. Para isso, ele considera fatores como o histórico de visualização, as preferências, as inscrições, a localização e o feedback dos usuários. Ele também leva em conta a qualidade e a relevância dos vídeos, analisando aspectos como o título, descrição, tags, miniaturas e os metadados.'))

doc.append(NewPage())

with doc.create(MiniPage(align='c')):
    doc.append(MediumText(("Observações")))

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            # itemize.add_item('Sessões:')
            # #doc.append(NoEscape(r'\newline'))
            # with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
            #     sublist.add_item(NoEscape(f'Por padrão, a sessão é encerrada após 30 minutos de inatividade, mas é possível ajustar esse limite para que ela dure de alguns segundos a várias horas.'))
            # with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
            #     sublist.add_item(NoEscape('O Google Analytics começa a contar a partir do momento em que um usuário acessa seu site. Se depois de 30 minutos este usuário não fizer uma interação, a sessão é finalizada. No entanto, toda vez que ocorre uma interação com um elemento (como um evento, interação de rede social ou uma nova página), o Google Analytics reinicia o tempo de vencimento adicionando 30 minutos a partir do momento da interação.\n Um único usuário pode abrir várias sessões. Essas sessões podem ocorrer no mesmo dia ou em vários dias, semanas ou meses. Assim que uma sessão termina, existe a oportunidade de iniciar uma nova sessão. Há dois métodos para o encerramento de uma sessão:'))
            # with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
            #     sublist.add_item(NoEscape('Um único usuário pode abrir várias sessões. Essas sessões podem ocorrer no mesmo dia ou em vários dias, semanas ou meses. Assim que uma sessão termina, existe a oportunidade de iniciar uma nova sessão. Há dois métodos para o encerramento de uma sessão:'))
            #     with sublist.create(Enumerate(enumeration_symbol=r"•")) as subsublist:
            #         subsublist.add_item(NoEscape('Vencimento por tempo:'))
            #         with subsublist.create(Enumerate(enumeration_symbol=r"•")) as subsubsublist:
            #             subsubsublist.add_item(NoEscape('Depois de 30 minutos de inatividade;'))
            #             subsubsublist.add_item(NoEscape('À meia-noite.'))
            #     with sublist.create(Enumerate(enumeration_symbol=r"•")) as subsublist:
            #         subsublist.add_item(NoEscape('Mudança de campanha:'))
            #         with subsublist.create(Enumerate(enumeration_symbol=r"•")) as subsubsublist:
            #             subsubsublist.add_item(NoEscape('Se um usuário entra por uma campanha, sai e depois volta para outra. (Fecha o site e entra novamente, por exemplo).'))
            itemize.add_item('Seguidores:')
            with itemize.create(Enumerate(enumeration_symbol=r"")) as sublist:
                sublist.add_item(NoEscape(f'É  possível observar que o número de novos seguidores ou inscritos adquiridos nos mês pode diferir um pouco na primeira tabela, na descrição dela e em cada uma das tabelas seguintes das respectivas redes sociais.'))
                sublist.add_item(NoEscape(f'Nas tabelas de cada rede social está a quantidade total de usuários que seguiram ao logo do mês analisado, mas nesse caso é o dado que foi informado diretamente pela rede social em questão. Chamaremos esse dado de "follows" e os que deixaram de seguir de "unfollows", para uma melhor identificação.'))
                sublist.add_item(NoEscape(f'Na primeira tabela do relatório está o númere referente a quantidade de seguidores que realmente continuaram seguindo a(o) página/perfil/canal ao final do mês. Logo abaixo, o dado "Seguidores adquiridos no mês:" é a quantidade total de usuários que seguiram ao logo do mês analisado. Nesses dois casos os valores são obtidos atraves da quantidade total de seguidores no mês atual e anterior e quantos usuários deixaram de seguir no mês atual.'))
                sublist.add_item(NoEscape(f'Por exemplo: se subtrairmos a quantidade total de seguidores do mês atual pela anterior e somarmos isso a quantos deixaram de seguir (atual - anterior + unfollow), teremos a quantidade total de "Seguidores adquiridos no mês:". Esse valor seria o mesmo dado de seguidores adquiridos que está nas tabelas de cada rede social (follows). E a quantidade de usuários que continuaram seguindo a página seria apenas a diferença do total de seguidores do mês atual e anterior (atual - anterior), que deveria dar no mesmo de subtrair "follows" por "unfollows" (follows - unfollows). Para que fique mais claro, a diferença entre "follows" e "unfollows" somada a quantidade total de seguidores do mês anterior deveria ser igual a quantidade total do mês atual (follows - unfollows + total seg. anterior = total seg. atual).'))
                sublist.add_item(NoEscape(f'Todos esses dados são fornecidos pelas próprias plataformas, mas eles podem acabar sendo um pouco diferentes para sua respectiva rede social.'))
            # itemize.add_item('Top15 notícias mais pesquisadas: as impressões são referentes a quantidade de vezes que uma pesquisa sobre determinado assunto foi realizada e foi possível visualizar o link da notícia no portal do TN entre os resultados.')
            
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
doc.generate_pdf(fr'C:\Users\{GR.path_Usuarios}\Documents\Repositórios\Relatórios\TNsemanal\RelatórioSemanal-TN_FB E IG_{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
