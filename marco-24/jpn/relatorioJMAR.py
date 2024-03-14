from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage
from pylatex.utils import bold
import graficosRelatorio as GR
import pandas as pd
import rpy2.robjects as robjects

# Cria um novo documento LaTeX
geometry_options = {"tmargin": "2cm", "rmargin": "2.5cm", "lmargin": "2.5cm"}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório das Redes Sociais")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText(("Fevereiro de 2024")))
        doc.append(LineBreak())

ig_seg_2023_og = [39,302,2011,237,217,290,258,260,255,178,221,259] #apenas os valores de jun e nov mudaram pela plataforma
ig_seg_2023 = [39,302,2011,237,217,221,258,260,255,178,217,259]
ig_seg_2023_perdeu = [0,0,0,0,0,142,241,202,236,204,194,226]
ig_alcance_2023 = [21733,15091,25147,17005,14844,19697,29758,16139,13015,11219,24345,65525]
ig_vivitas_2023 = [1641,1213,10131,1105,1436,1780,1193,1297,1372,1246,1468,1902]

ig_seg_2024 = [306,265]
ig_seg_2024_perdeu = [230,240]
ig_alcance_2024 = [26399,32188]
ig_vivitas_2024 = [1646,2176]

ig_seg_2024_total = [28290,28326]

tw_seg_2023_og = [151,-30,62,-5,-5,-36,-2,7,1,20-18,6]
tw_impressões_2023_og = [55700,39500,60300,99800,53900,55800,46300,51900,35000,35400,28500,27500]
tw_engajamentos_2023_og = [700,578,927,1303,699,761,663,656,452,394,365,351]

tw_seg_2023 = [151,-30,62,-5,-5,-36,26,87,40,68,51,62] #dados da tabela disponíveis a partir de julho
#tw_seg_2023_perdeu = []
tw_impressões_2023 = [55700,39500,51586,45839,53858,55765,46258,51901,34972,35441,28486,27474]
tw_engajamentos_2023 = [700,578,982,706,848,890,769,847,558,574,473,489]

tw_seg_2024 = [32,60]
tw_impressões_2024 = [35684,28801]
tw_engajamentos_2024 = [589,518]

tw_seg_2024_total = [27820,27808]
tw_seg_2024_perdeu = [58,tw_seg_2024[1]-(tw_seg_2024_total[1]-tw_seg_2024_total[0])] #sabe a quantidade que perdeu de acordo com a diferença de seguidores entre um mês e outro e o ganho total de seguidores no mês

yb_inc_2023 = [948,418,760,356,516,411,371,387,258,259,495,172]
yb_inc_2023_perdeu = [258,152,154,103,139,117,117,123,121,113,111,105]
yb_visualizacoes_2023 = [247874,108139,146070,86068,148727,118942,107559,94221,52970,51953,166181,23359]
yb_horas_2023 = [24389,8349,12020,7839,11011,9419,9362,8893,5907,5131,12228,3396]

yb_inc_2024 = [501,286]
yb_inc_2024_perdeu = [130,111]
yb_visualizacoes_2024 = [97513,81437]
yb_horas_2024 = [7077,6209]

yb_inc_2024_total = [33338,33513]

# Adiciona a seção para os resultados
with doc.create(Section('Jovem Pan News', numbering=False)):
    with doc.create(Subsection('Resultados de fevereiro/2024', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='Instagram'), GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]), GR.formataNumero(ig_alcance_2024[-1]), GR.formataNumero(ig_vivitas_2024[-1])))
                table.add_row(('', 'novos seguidores', 'contas atingidas', 'visitas ao perfil'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Twitter'), GR.formataNumero(tw_seg_2024_total[-1]-tw_seg_2024_total[-2]), GR.formataNumero(tw_impressões_2024[-1]), GR.formataNumero(tw_engajamentos_2024[-1])))
                table.add_row(('', 'novos seguidores', 'impressões', 'engajamentos'))
                table.add_hline()
                table.add_row((MultiRow(2, data='Youtube'), GR.formataNumero(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]), GR.formataNumero(yb_visualizacoes_2024[-1]), '4.194'))
                table.add_row(('', 'novos inscritos', 'visualizações', 'horas de exibição'))
                

        # Adiciona informações extras
        # Adiciona uma lista com marcadores
        with doc.create(Itemize()) as itemize:
            itemize.add_item(f"Ao todo, a JP News entregou seu conteúdo para, aproximadamente, {GR.formataNumero((ig_seg_2024_total[-1]-ig_seg_2024_total[-2])+(tw_seg_2024_total[-1]-tw_seg_2024_total[-2])+(yb_inc_2024_total[-1]-yb_inc_2024_total[-2]))} novos usuários, entre Instagram, Twitter e YouTube.")
            itemize.add_item(Command('textbf', arguments='Instagram'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(f"Total de seguidores atual: {GR.formataNumero(ig_seg_2024_total[-1])}. Total de seguidores no mês anterior: {GR.formataNumero(ig_seg_2024_total[-2])}")
                sublist.add_item(f"Seguidores adquiridos no mês: {GR.formataNumero(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]+ig_seg_2024_perdeu[-1])}. Deixaram de seguir: {GR.formataNumero(ig_seg_2024_perdeu[-1])}.")
                sublist.add_item(f"Taxa de fixação: {GR.fixacao(ig_seg_2024_total[-1]-ig_seg_2024_total[-2]+ig_seg_2024_perdeu[-1],ig_seg_2024_perdeu[-1])}")
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
    with doc.create(Subsubsection('Instagram', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(3, data='Mês'), 'Novos seguidores', 'Alcance', 'Visitas'))
                table.add_row(('', FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao'), FootnoteText('variação em relação ao')))
                table.add_row(('', FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023'), FootnoteText('mês anterior | mesmo mês em 2023')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Janeiro'), '306', '26,4 mil', '1,65 mil'))
                table.add_row(('', FootnoteText('+17% | +677%'), FootnoteText('-57,8% | +20%'), FootnoteText('-13% | +3%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), '265', '32,2 mil', '2,2 mil'))
                table.add_row(('', FootnoteText(f'{GR.crescimento(265,306)} | {GR.crescimento(265,306)}'), FootnoteText(f'{GR.crescimento(32200,26400)} | {GR.crescimento(32200,15100)}'), FootnoteText(f'{GR.crescimento(2200,1650)} | {GR.crescimento(2200,1200)}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(ig_seg_2024[2]), GR.numeroPorExtensso(ig_alcance_2024[2]), GR.numeroPorExtensso(ig_vivitas_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[2],ig_seg_2024[1])} | {GR.crescimento(ig_seg_2024[2],ig_seg_2023[2])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[2],ig_alcance_2024[1])} | {GR.crescimento(ig_alcance_2024[2],ig_alcance_2023[2])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[2],ig_vivitas_2024[1])} | {GR.crescimento(ig_vivitas_2024[2],ig_vivitas_2023[2])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(ig_seg_2024[3]), GR.numeroPorExtensso(ig_alcance_2024[3]), GR.numeroPorExtensso(ig_vivitas_2024[3])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[3],ig_seg_2024[2])} | {GR.crescimento(ig_seg_2024[3],ig_seg_2023[3])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[3],ig_alcance_2024[2])} | {GR.crescimento(ig_alcance_2024[3],ig_alcance_2023[3])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[3],ig_vivitas_2024[2])} | {GR.crescimento(ig_vivitas_2024[3],ig_vivitas_2023[3])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(ig_seg_2024[4]), GR.numeroPorExtensso(ig_alcance_2024[4]), GR.numeroPorExtensso(ig_vivitas_2024[])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[4],ig_seg_2024[3])} | {GR.crescimento(ig_seg_2024[4],ig_seg_2023[4])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[4],ig_alcance_2024[3])} | {GR.crescimento(ig_alcance_2024[4],ig_alcance_2023[4])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[4],ig_vivitas_2024[3])} | {GR.crescimento(ig_vivitas_2024[4],ig_vivitas_2023[4])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(ig_seg_2024[5]), GR.numeroPorExtensso(ig_alcance_2024[5]), GR.numeroPorExtensso(ig_vivitas_2024[5])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(ig_seg_2024[],ig_seg_2024[4])} | {GR.crescimento(ig_seg_2024[5],ig_seg_2023[5])}'), FootnoteText(f'{GR.crescimento(ig_alcance_2024[5],ig_alcance_2024[4])} | {GR.crescimento(ig_alcance_2024[5],ig_alcance_2023[5])}'), FootnoteText(f'{GR.crescimento(ig_vivitas_2024[5],ig_vivitas_2024[4])} | {GR.crescimento(ig_vivitas_2024[5],ig_vivitas_2023[5])}')))
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

        with doc.create(Itemize()) as itemize:
                    # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
                    itemize.add_item('Legenda:')
                    #doc.append(NoEscape(r'\newline'))
                    with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                        sublist.add_item(NoEscape(r'\textbf{Alcance:} Essa métrica calcula o alcance da distribuição orgânica ou paga do seu conteúdo do Instagram e/ou Facebook, incluindo publicações e stories que foram turbinados. Também pode ser interpretada como a quantidade de contas atingidas;'))
                        sublist.add_item(NoEscape(r'\textbf{Visitas:} número de vezes que usuários visitaram seu perfil.'))
                        
# recebendo camiho da imagem do gráfico e o total de seguidores do fb e ig
fePublico_FBIG_plot_path, IG_followers = GR.fePublico_FBIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: audiência por sexo e faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(fePublico_FBIG_plot_path, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

publicoCidades_plot_path = GR.publicoCidades()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: audiência por cidades")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(publicoCidades_plot_path, width=NoEscape(r'0.8\textwidth'))

seguidoresIG_plot_path, seguidoresIG = GR.seguidoresIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: ganho de seguidores ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(seguidoresIG_plot_path, width=NoEscape(r'0.8\textwidth'))

doc.append(NewPage())

visitasIG_plot_path, visitasIG = GR.visitasIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: visitas ao perfil ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(visitasIG_plot_path, width=NoEscape(r'0.7\textwidth'))

alcanceIG_plot_path, alcanceIG = GR.alcanceIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: alcance do perfil ao longo do mês")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(alcanceIG_plot_path, width=NoEscape(r'0.7\textwidth'))

dadosIG_plot_path = GR.dadosIG()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("IG: comparativo de seguidores, visitas e alcance. (Obs.: dados fora de escala para uma melhor visualização)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
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
                table.add_row((MultiRow(2, data='Janeiro'), '32', '35,7 mil', '589'))
                table.add_row(('', FootnoteText('+433,3% | -79%'), FootnoteText('+30% | -36%'), FootnoteText('+68% | -16%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), '60', '28,8 mil', '518'))
                table.add_row(('', FootnoteText(f'{GR.crescimento(60,32)} | {GR.crescimento(60,-30)}'), FootnoteText(f'{GR.crescimento(28801,35700)} | {GR.crescimento(28801,39500)}'), FootnoteText(f'{GR.crescimento(518,589)} | {GR.crescimento(518,578)}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(tw_seg_2024[2]), GR.numeroPorExtensso(tw_impressões_2024[2]), GR.numeroPorExtensso(tw_engajamentos_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[2],tw_seg_2024[1])} | {GR.crescimento(tw_seg_2024[2],tw_seg_2023[2])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[2],tw_impressões_2024[1])} | {GR.crescimento(tw_impressões_2024[2],tw_impressões_2023[2])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[2],tw_engajamentos_2024[1])} | {GR.crescimento(tw_engajamentos_2024[2],tw_engajamentos_2023[2])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(tw_seg_2024[3]), GR.numeroPorExtensso(tw_impressões_2024[3]), GR.numeroPorExtensso(tw_engajamentos_2024[3])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[3],tw_seg_2024[2])} | {GR.crescimento(tw_seg_2024[3],tw_seg_2023[3])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[3],tw_impressões_2024[2])} | {GR.crescimento(tw_impressões_2024[3],tw_impressões_2023[3])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[3],tw_engajamentos_2024[2])} | {GR.crescimento(tw_engajamentos_2024[3],tw_engajamentos_2023[3])}')))
                # table.add_hline()
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(tw_seg_2024[4]), GR.numeroPorExtensso(tw_impressões_2024[4]), GR.numeroPorExtensso(tw_engajamentos_2024[4])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[4],tw_seg_2024[3])} | {GR.crescimento(tw_seg_2024[4],tw_seg_2023[4])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[4],tw_impressões_2024[3])} | {GR.crescimento(tw_impressões_2024[4],tw_impressões_2023[4])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[4],tw_engajamentos_2024[3])} | {GR.crescimento(tw_engajamentos_2024[4],tw_engajamentos_2023[4])}')))
                # table.add_hline()
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(tw_seg_2024[5]), GR.numeroPorExtensso(tw_impressões_2024[5]), GR.numeroPorExtensso(tw_engajamentos_2024[5])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(tw_seg_2024[5],tw_seg_2024[4])} | {GR.crescimento(tw_seg_2024[5],tw_seg_2023[5])}'), FootnoteText(f'{GR.crescimento(tw_impressões_2024[5],tw_impressões_2024[4])} | {GR.crescimento(tw_impressões_2024[5],tw_impressões_2023[5])}'), FootnoteText(f'{GR.crescimento(tw_engajamentos_2024[5],tw_engajamentos_2024[4])} | {GR.crescimento(tw_engajamentos_2024[5],tw_engajamentos_2023[5])}')))
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
                
        with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Legenda:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Impressões:} número de vezes que os usuários viram o(s) Tweet(s);'))
                sublist.add_item(NoEscape(r'\textbf{Engajamentos:} número total de vezes que um usuário interagiu com o(s) Tweet(s). Isso inclui todos os cliques em qualquer lugar no Tweet como: hashtags, links, avatar, nome de usuário e expansão do Tweet, Retweets, respostas e favoritos.'))

engajamentoTW_plot_path = GR.engajamentoTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: engajamento do twitter")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(engajamentoTW_plot_path, width=NoEscape(r'0.7\textwidth'))
doc.append(NewPage())

impressoesTW_plot_path = GR.impressoesTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: impressões do twitter")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(impressoesTW_plot_path, width=NoEscape(r'0.7\textwidth'))

seguidoresTW_plot_path = GR.seguidoresTW()

# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("TW: ganho de seguidores no twitter ao logo do mês. (Esses dados levam em consideração apenas os ganhos)")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(seguidoresTW_plot_path, width=NoEscape(r'0.7\textwidth'))

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
                table.add_row((MultiRow(2, data='Janeiro'), '501', '97,5 mil', '7,1 mil'))
                table.add_row(('', FootnoteText('+191,3% | -47%'), FootnoteText('+317% | -60,7%'), FootnoteText('+109% | -71%')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Fevereiro'), '286', '81,4 mil', '6,2 mil'))
                table.add_row(('', FootnoteText(f'{GR.crescimento(286,501)} | {GR.crescimento(286,418)}'), FootnoteText(f'{GR.crescimento(81400,97513)} | {GR.crescimento(81400,108139)}'), FootnoteText(f'{GR.crescimento(6200,7077)} | {GR.crescimento(6200,8350)}')))
                table.add_hline()
                table.add_row((MultiRow(2, data='Março'), GR.numeroPorExtensso(yb_inc_2024[2]), GR.numeroPorExtensso(yb_visualizacoes_2024[2]), GR.numeroPorExtensso(yb_horas_2024[2])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[2],yb_inc_2024[1])} | {GR.crescimento(yb_inc_2024[2],yb_inc_2023[2])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[2],yb_visualizacoes_2024[1])} | {GR.crescimento(yb_visualizacoes_2024[2],yb_visualizacoes_2023[2])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[2],yb_horas_2024[1])} | {GR.crescimento(yb_horas_2024[2],yb_horas_2023[2])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Abril'), GR.numeroPorExtensso(yb_inc_2024[3]), GR.numeroPorExtensso(yb_visualizacoes_2024[3]), GR.numeroPorExtensso(yb_horas_2024[3])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[3],yb_inc_2024[2])} | {GR.crescimento(yb_inc_2024[3],yb_inc_2023[3])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[3],yb_visualizacoes_2024[2])} | {GR.crescimento(yb_visualizacoes_2024[3],yb_visualizacoes_2023[3])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[3],yb_horas_2024[2])} | {GR.crescimento(yb_horas_2024[3],yb_horas_2023[3])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Maio'), GR.numeroPorExtensso(yb_inc_2024[4]), GR.numeroPorExtensso(yb_visualizacoes_2024[4]), GR.numeroPorExtensso(yb_horas_2024[4])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[4],yb_inc_2024[3])} | {GR.crescimento(yb_inc_2024[4],yb_inc_2023[4])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[4],yb_visualizacoes_2024[3])} | {GR.crescimento(yb_visualizacoes_2024[4],yb_visualizacoes_2023[4])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[4],yb_horas_2024[3])} | {GR.crescimento(yb_horas_2024[4],yb_horas_2023[4])}')))
                # table.add_hline()
                # table.add_row((MultiRow(2, data='Junho'), GR.numeroPorExtensso(yb_inc_2024[5]), GR.numeroPorExtensso(yb_visualizacoes_2024[5]), GR.numeroPorExtensso(yb_horas_2024[5])))
                # table.add_row(('', FootnoteText(f'{GR.crescimento(yb_inc_2024[5],yb_inc_2024[4])} | {GR.crescimento(yb_inc_2024[5],yb_inc_2023[5])}'), FootnoteText(f'{GR.crescimento(yb_visualizacoes_2024[5],yb_visualizacoes_2024[4])} | {GR.crescimento(yb_visualizacoes_2024[5],yb_visualizacoes_2023[5])}'), FootnoteText(f'{GR.crescimento(yb_horas_2024[5],yb_horas_2024[4])} | {GR.crescimento(yb_horas_2024[5],yb_horas_2023[4])}')))
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

visualizacoesIdadeYTB_plot_path = GR.visualizacoesIdadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: visualizações por faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(visualizacoesIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))

doc.append(NewPage())

horasIdadeYTB_plot_path = GR.horasIdadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: horas de exibição por faixa etária")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(horasIdadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))
        
generoYTB_plot_path = GR.generoYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: sexo do público")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(generoYTB_plot_path, width=NoEscape(r'0.6\textwidth'))
        
visualizacoesCidadeYTB_plot_path = GR.visualizacoesCidadeYTB()
# Adiciona uma seção ao documento
with doc.create(Section('', numbering=False)):
    doc.append("YouTube: visualizações por cidade")
    # doc.append(NoEscape(r'\newline'))  # Adiciona uma nova linha
    # Adiciona a figura ao documento
    with doc.create(Figure(position='h!')) as plot:
        plot.add_image(visualizacoesCidadeYTB_plot_path, width=NoEscape(r'0.7\textwidth'))


doc.append(NewPage())

with doc.create(Itemize()) as itemize:
            # itemize.add_item('Em geral, março vem sendo o melhor mês da Tribuna do Norte nas redes sociais e setembro o pior.')
            itemize.add_item('Funcionamento dos algoritmos:')
            #doc.append(NoEscape(r'\newline'))
            with itemize.create(Enumerate(enumeration_symbol=r"-")) as sublist:
                sublist.add_item(NoEscape(r'\textbf{Instagram:} O algoritmo do Instagram também se baseia no engajamento, no relacionamento e na temporalidade dos conteúdos. Ele mostra primeiro as postagens e as histórias das contas com as quais o usuário mais interage, seja por meio de curtidas, comentários, mensagens diretas ou buscas. Ele também valoriza os conteúdos mais recentes e mais relevantes para o usuário, de acordo com os seus interesses e hábitos;'))
                sublist.add_item(NoEscape(r'\textbf{Twitter:} O algoritmo do Twitter tem duas formas de exibir os conteúdos: o modo cronológico e o modo destacado. No modo cronológico, o usuário vê os tweets mais recentes em ordem de publicação. No modo destacado, o usuário vê os tweets mais relevantes para ele, de acordo com o seu perfil, as suas interações e os assuntos do momento. O Twitter também mostra os tweets mais populares e mais comentados na seção “O que está acontecendo”;'))
                sublist.add_item(NoEscape(r'\textbf{YouTube:} O algoritmo do YouTube tem como objetivo aumentar o tempo de permanência dos usuários na plataforma, recomendando os vídeos que eles têm mais chances de assistir e se engajar. Para isso, ele considera fatores como o histórico de visualização, as preferências, as inscrições, a localização e o feedback dos usuários. Ele também leva em conta a qualidade e a relevância dos vídeos, analisando aspectos como o título, descrição, tags, miniaturas e os metadados.'))
                
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

# Gera o arquivo LaTeX
doc.generate_pdf(r'C:\Users\Usuario\Documents\Repositórios\Relatórios\JPN\Relatório-JPNews_Mar-2024', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
