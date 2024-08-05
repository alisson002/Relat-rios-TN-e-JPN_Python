from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage, Math
from pylatex.utils import bold
import graficosRelatorioSemanal as GR
import pandas as pd
import rpy2.robjects as robjects
import numpy

# Cria um novo documento LaTeX
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "lmargin": "2.5cm"}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório das Redes Sociais e Portal")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Relatório semanal")))
        doc.append(LineBreak())

portal_usuariosUnicos_2024Table = [276184,441269,455979,340868,369804,272294,293971,459877,326566,369497,302557,358037,308259,358280,294016,371248,552230,347410]
portal_usuariosRescorrentes_2024Table = [123944,197378,172485,156579,169541,124341,135747,202480,151029,160475,147401,154262,133798,142551,126291,137344,177835,134973]

portal_usuariosUnicos_2024Analytics = [213000,331000,370000,261000,283000,210000,226000,357000,259000,292000,231000,286000,244000,295000,233000,304000,469000,314000]
portal_usuariosRescorrentes_2024Analytics = [73000,113000,105000,92000,100000,73000,79000,122000,93000,98000,88000,93000,80000,90000,75000,83000,115000,85000]

portal_visualizacoes_2024 = [621206,965340,924908,765698,829407,635989,664666,907045,698454,764245,671189,745886,682403,733301,648784,782882,992290,742668] # mesmo valor na tabela e no analytics
portal_novosUsuarios_2024 = [147518,242760,278732,177038,198428,144767,155648,255141,170986,204845,151741,200186,170757,214285,164265,233626,374522,237463] # mesmo valor na tabela e no analytics

#INSTAGRAM
ig_seg_2024 = [1299,2685,1476,1499,2054,1558,1469,358,1693,1584,1323,1317,1130,1181,1143,1128,1310,1245]
ig_seg_2024_perdeu = [1040,1165,1080,1114,1228,1094,1070,315,1050,1040,1074,1081,996,963,1161,1126,1134,1209]
ig_alcance_2024 = [330170,619778,394150,368303,430160,430041,430095,518193,564967,444404,479370,512399,445377,407004,491253,437034,513738,558433]
ig_vivitas_2024 = [24896,53103,28198,27847,49389,28931,29098,31347,33708,38352,26704,26949,20380,21911,22017,24981,29750,25951]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
ig_seg_2024_total = [532444,533616,534049,534392,535150,535716,536047,536508,537733,537993,538290,538507,538756,538846,538864,538830,539051,539028]

#FACEBOOK
fb_seg_2024 = [30,61,71,42,83,80,49,74,40,67,30,36,84,37,62,62,80,62]
fb_seg_2024_perdeu = [34,35,44,35,49,40,31,33,41,32,53,34,36,36,29,35,47,36]
fb_alcance_2024 = [64958,88738,112464,63173,142594,139599,101924,132711,87877,114958,127230,78859,119785,84527,109848,87594,147513,120924]
fb_vivitas_2024 = [6500,7686,8158,6718,6757,7087,7074,5937,6326,5417,5125,3796,5242,5130,5452,5563,5332,5172]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
fb_seg_2024_total = [332419,332392,332389,332334,332339,332314,332287,332176,332214,332210,332186,332136,332133,332086,332086,332049,332035,332006]

#TWITTER
tw_seg_2024 = [359,455,1249,892,801,725,1009,2464,886,2460]
tw_impressões_2024 = [86012,102051,96123,100004,113293,95767,95199,90299,78103,89681]
tw_engajamentos_2024 = [2390,3324,3242,3257,4164,2661,3219,4553,2650,4576]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
tw_seg_2024_total = [312146,312041,312437,312722,312797,313181,314742,315456,317307,319917]
tw_seg_2024_perdeu = [890,tw_seg_2024[1]-(tw_seg_2024_total[1]-tw_seg_2024_total[0]),tw_seg_2024[2]-(tw_seg_2024_total[2]-tw_seg_2024_total[1]),tw_seg_2024[3]-(tw_seg_2024_total[3]-tw_seg_2024_total[2]),tw_seg_2024[4]-(tw_seg_2024_total[4]-tw_seg_2024_total[3]),tw_seg_2024[5]-(tw_seg_2024_total[5]-tw_seg_2024_total[4]),abs(tw_seg_2024[6]-(tw_seg_2024_total[6]-tw_seg_2024_total[5])),tw_seg_2024[7]-(tw_seg_2024_total[7]-tw_seg_2024_total[6]),abs(tw_seg_2024[8]-(tw_seg_2024_total[8]-tw_seg_2024_total[7])),abs(tw_seg_2024[9]-(tw_seg_2024_total[9]-tw_seg_2024_total[8]))] #sabe a quantidade que perdeu de acordo com a diferença de seguidores entre um mês e outro e o ganho total de seguidores no mês

#YOUTUBE
yb_inc_2024 = [505,241,552,155,268,162,135,81,82,89,121,123,89,110,103,141,171,186]
yb_inc_2024_perdeu = [30,15,31,17,30,15,19,21,16,22,18,18,16,19,22,22,24,21]
yb_visualizacoes_2024 = [134255,69730,149424,40127,73821,39688,35024,29843,22657,20998,21575,27314,19991,35636,22941,39314,40865,45122]
yb_horas_2024 = [1785,1114,2142,671,1265,632,660,768,715,596,586,555,420,537,553,557,661,630]

#ADICIONAR TOTAL DA SEMANA SEGUINTE
yb_inc_2024_total = [35940,36167,36685,36863,37062,37214,37333,37380,37544,37631,37729,37846,37922,37987,38076,38250,38337,38507]

# Adiciona a seção para os resultados
with doc.create(Section('Tribuna do Norte', numbering=False)):
    with doc.create(Subsection(f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}', numbering=False)):
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
        # with doc.create(Itemize()) as itemize:
        #     itemize.add_item(f"Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, {GR.formataNumero(portal_novosUsuarios_2024[-1]+(ig_seg_2024_total[-1]-ig_seg_2024_total[-2])+(fb_seg_2024_total[-1]-fb_seg_2024_total[-2])+(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]))} novas contas, entre Portal, Instagram, Twitter, Facebook e YouTube.")
        with doc.create(Itemize()) as itemize:
            itemize.add_item(f"Ao todo, a Tribuna do Norte entregou seu conteúdo para, aproximadamente, {GR.formataNumero(portal_novosUsuarios_2024[-1]+(ig_seg_2024[-1])+(fb_seg_2024[-1])+(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]))} novas contas, entre Portal, Instagram, Facebook e YouTube.")
            #+(tw_seg_2024_total[-1]-tw_seg_2024_total[-2])
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(ig_seg_2024_total[-1])}. Total de seguidores na semana anterior: {GR.formataNumero(ig_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos na semana: {GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]+ig_seg_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(ig_seg_2024_perdeu[-1])}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]+ig_seg_2024_perdeu[-1],ig_seg_2024_perdeu[-1])}")
                #sublist.add_item(f"O Instagram não disponibilizou os dados de ganhos e perda de seguidores da semana passada, portanto temos disponível apenas o saldo de seguidores.")
                #sublist.add_item(f"nan: not a number (não é um número).")
                # sublist.add_item(f"Sem queda nos seguidores do Instagram.")
            itemize.add_item(Command('textbf', arguments='Facebook'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(fb_seg_2024_total[-1])}. Total de seguidores na semana anterior: {GR.formataNumero(fb_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos na semana: {GR.formataNumero(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]+fb_seg_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(fb_seg_2024_perdeu[-1])}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(fb_seg_2024_total[-1]-fb_seg_2024_total[-2]+fb_seg_2024_perdeu[-1],fb_seg_2024_perdeu[-1])}")
                #sublist.add_item(f"Obs.: O número de seguidores do Facebook segue apenas em queda.")
                # sublist.add_item(f"Obs.: nesse caso, a taxa de fixação negatíva se trata de uma diferença relmente alta, visto que tanto 'Seguidores adquiridos na semana' quanto 'Deixaram de seguir' são números positivos.")
                # sublist.add_item(f"Obs.: nesse caso, a taxa de fixação negatíva se trata de uma diferença relmente baixa, visto que tanto 'Seguidores adquiridos na semana' quanto 'Deixaram de seguir' são números positivos, potanto, quanto mais distante de zero maior ela seria. Só seria interpretada como maior, quanto mais próximo de zero, e menor, quanto mais distante de zero, em casos onde 'Seguidores adquiridos na semana' é um número negativo, fazendo com que ele seja somado a 'Deixaram de seguir' no calcula da diferença.")
                # sublist.add_item(f"O número de seguidores do Facebook apenas caiu nas ultimas 3 semanas.")
                sublist.add_item(f"Facebook vem numa sequência de queda de seguidores a algum tempo, desde a semana de 26-05-2024 a 01-06-2024 que também já vinha de uma outra sequência de queda de seguidores.")
            itemize.add_item(Command('textbf', arguments='Twitter'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item("Total de seguidores atual: -. Total de seguidores na semana anterior: -")
                sublist.add_item("Seguidores adquiridos na semana: -. Deixaram de seguir: -.")
                sublist.add_item("Taxa de fixação: -")
                sublist.add_item("AVISO: Os dados do Twitter estão indiponíveis pois sua plataforma de Analytics agora faz parte do 'X Premium', portanto, se tornou paga.")
            itemize.add_item(Command('textbf', arguments='YouTube'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(yb_inc_2024_total[-1])}. Total de seguidores na semana anterior: {GR.formataNumero(yb_inc_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos na semana: {GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]+yb_inc_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(yb_inc_2024_perdeu[-1])}")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]+yb_inc_2024_perdeu[-1],yb_inc_2024_perdeu[-1])}")

doc.append(NewPage())

with doc.create(Subsection('Análise semanal', numbering=False)):
    with doc.create(Subsubsection('Portal', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Semana'), 'Novos usuários', 'Visualizações', 'Usuários recorrentes'))
                table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
                table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(portal_novosUsuarios_2024[-1]), GR.numeroPorExtensso(portal_visualizacoes_2024[-1]), GR.numeroPorExtensso(portal_usuariosRescorrentes_2024Analytics[-1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(portal_novosUsuarios_2024[-1],portal_novosUsuarios_2024[-2])}'), FootnoteText(f'{GR.crescimento(portal_visualizacoes_2024[-1],portal_visualizacoes_2024[-2])}'), FootnoteText(f'{GR.crescimento(portal_usuariosRescorrentes_2024Analytics[-1],portal_usuariosRescorrentes_2024Analytics[-2])}')))

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

with doc.create(Subsection('Análise semanal', numbering=False)):
    with doc.create(Subsubsection('Instagram', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Semana'), 'Novos seguidores', 'Alcance', 'Visitas'))
                table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
                table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(ig_seg_2024[-1]), GR.numeroPorExtensso(ig_alcance_2024[-1]), GR.numeroPorExtensso(ig_vivitas_2024[-1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[-1],ig_seg_2024[-2])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[-1],ig_alcance_2024[-2])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[-1],ig_vivitas_2024[-2])}')))
    with doc.create(Subsubsection('Facebook', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Semana'), 'Novos seguidores', 'Alcance', 'Visitas'))
                table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
                table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(fb_seg_2024[-1]), GR.numeroPorExtensso(fb_alcance_2024[-1]), GR.numeroPorExtensso(fb_vivitas_2024[-1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(fb_seg_2024[-1],fb_seg_2024[-2])}'), FootnoteText(f'{GR.crescimento(fb_alcance_2024[-1],fb_alcance_2024[-2])}'), FootnoteText(f'{GR.crescimento(fb_vivitas_2024[-1],fb_vivitas_2024[-2])}')))


        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Legenda:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Alcance:} Essa métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram e/ou Facebook, incluindo publicações e stories que foram turbinados. Também pode ser interpretada como a quantidade de contas atingidas;'))
                sublist.add_item(NoEscape(r'\textbf{Visitas:} número de vezes que usuários visitaram seu perfil.'))

# with doc.create(Enumerate(enumeration_symbol=r"")) as itemize:
#             itemize.add_item(NoEscape(r'\textbf{Os detales demográficos (faixa etária, gênero e cidades) do facebook e instagram estavam indisponíveis.}'))
doc.append(NewPage())

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

with doc.create(Subsection('Análise semanal', numbering=False)):
    with doc.create(Subsubsection('YouTube', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Semana'), 'Novos inscritos', 'Visualizações', 'Horas de exibição'))
                table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
                table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data=f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}'), GR.numeroPorExtensso(yb_inc_2024[-1]), GR.numeroPorExtensso(yb_visualizacoes_2024[-1]), GR.numeroPorExtensso(yb_horas_2024[-1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[-1],yb_inc_2024[-2])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[-1],yb_visualizacoes_2024[-2])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[-1],yb_horas_2024[-2])}')))

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
                    subsublist.add_item(NoEscape('Mudança de campanha:'))
                    with subsublist.create(Enumerate(enumeration_symbol=r"•")) as subsubsublist:
                        subsubsublist.add_item(NoEscape('Se um usuário entra por uma campanha, sai e depois volta para outra. (Fecha o site e entra novamente, por exemplo).'))
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
doc.generate_pdf(fr'C:\Users\{GR.path_Usuarios}\Documents\Repositórios\Relatórios\TNsemanal\RelatórioSemanal-TN_{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
