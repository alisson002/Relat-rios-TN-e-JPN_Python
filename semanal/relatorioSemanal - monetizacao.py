from pylatex import Document, Section, Subsection, Command, Tabular, Itemize, Enumerate, LineBreak, LargeText, MiniPage, MediumText, MultiRow, NewPage, Subsubsection, SmallText, FootnoteText, NoEscape, Figure, MiniPage, Math
from pylatex.utils import bold
import graficosRelatorioSemanal as GR
import pandas as pd
import rpy2.robjects as robjects
import numpy

# Cria um novo documento LaTeX
geometry_options = {"tmargin": "2.5cm", "rmargin": "2.5cm", "lmargin": "2cm", "landscape": True}
doc = Document(geometry_options=geometry_options)
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

with doc.create(MiniPage(align='c')):
        doc.append(LargeText(("Relatório de Monetização")))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText((f"Relatório semanal {GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}")))
        doc.append(LineBreak())

#YOUTUBE - TN: MONETIZAÇÃO
impressoes_yb_TN=[16429,182696,85235,7141,45266,22621,24240,17580,22039,4936,5452,5090,4705,4982]
visuMonetizadas_yb_TN=[15531,173212,85466,6561,45111,21762,23742,15037,21404,4285,4601,4339,4384,4343]
receitaBruta_yb_TN=[73,1050,573,36,296,130,156,96,138,26,29,36,29,27]
premium_yb_TN=[1,16,6,0,3,2,1,1,1,1,1,1,1,1]
AdSense_yb_TN=[40,578,315,20,163,72,86,53,76,14,16,20,16,15]

#YOUTUBE - JPN: MONETIZAÇÃO
impressoes_yb_JPN=[39593,16737,42079,154350,109270,43500,574953,161484,15444,15701,26664,79852,23895]
visuMonetizadas_yb_JPN=[33296,13781,36523,137373,93411,35514,488003,143579,12635,12359,22254,65113,19436]
receitaBruta_yb_JPN=[185,90,147,515,430,215,2039,443,87,97,157,450,129] #receita de anuncios do ytb
premium_yb_JPN=[7,6,6,31,16,11,75,11,65,7,24,7]
AdSense_yb_JPN=[102,49,81,284,237,119,1123,244,48,53,86,249,71] #receita estimada GADS

# Adiciona a seção para os resultados
with doc.create(Section('YouTube: Monetização', numbering=False)):
    with doc.create(Subsection(f'{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados
            with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
                
                table.add_row((MultiRow(2, data='YouTube - TN'), GR.formataNumero(impressoes_yb_TN[-1]), GR.formataNumero(visuMonetizadas_yb_TN[-1]), GR.formataNumero(receitaBruta_yb_TN[-1]), GR.formataNumero(premium_yb_TN[-1]), GR.formataNumero(AdSense_yb_TN[-1])))
                table.add_row(('', 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta (R$)', 'YTB Premium (R$)', 'Receita estimada (AdSense) (R$)'))
                table.add_hline()
                table.add_row((MultiRow(2, data='YouTube - JPNews'), GR.formataNumero(impressoes_yb_JPN[-1]), GR.formataNumero(visuMonetizadas_yb_JPN[-1]), GR.formataNumero(receitaBruta_yb_JPN[-1]), GR.formataNumero(premium_yb_JPN[-1]), GR.formataNumero(AdSense_yb_JPN[-1])))
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

with doc.create(Subsection('Análise semanal', numbering=False)):
    with doc.create(Subsubsection('YouTube - TN: Monetização', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados            
            with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
            
                table.add_row((MultiRow(5, data='Semana'), 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta (R$)', 'YTB Premium (R$)', 'Receita estimada (AdSense) (R$)'))
                table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
                table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data='-'), GR.numeroPorExtensso(impressoes_yb_TN[-1]), GR.numeroPorExtensso(visuMonetizadas_yb_TN[-1]), GR.numeroPorExtensso(receitaBruta_yb_TN[-1]), GR.numeroPorExtensso(premium_yb_TN[-1]), GR.numeroPorExtensso(AdSense_yb_TN[-1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_TN[-1],impressoes_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_TN[-1],visuMonetizadas_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_TN[-1],receitaBruta_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(premium_yb_TN[-1],premium_yb_TN[-2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_TN[-1],AdSense_yb_TN[-2])}')))

with doc.create(Subsection('Análise semanal', numbering=False)):
    with doc.create(Subsubsection('YouTube - JPN: Monetização', numbering=False)):
        with doc.create(MiniPage(align='c')):
            # Adiciona a tabela de resultados            
            with doc.create(Tabular('|c|c|c|c|c|c|', booktabs =True)) as table:
            
                table.add_row((MultiRow(5, data='Semana'), 'Impressões de anúncios', 'Visualizações monetizadas', 'Receita bruta (R$)', 'YTB Premium (R$)', 'Receita estimada (AdSense) (R$)'))
                table.add_row(('', FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a'), FootnoteText('variação em relação a')))
                table.add_row(('', FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior'), FootnoteText('semana anterior')))
                table.add_hline()
                table.add_row((MultiRow(2, data='-'), GR.numeroPorExtensso(impressoes_yb_JPN[-1]), GR.numeroPorExtensso(visuMonetizadas_yb_JPN[-1]), GR.numeroPorExtensso(receitaBruta_yb_JPN[-1]), GR.numeroPorExtensso(premium_yb_JPN[-1]), GR.numeroPorExtensso(AdSense_yb_JPN[-1])))
                table.add_row(('', FootnoteText(f'{GR.crescimento(impressoes_yb_JPN[-1],impressoes_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(visuMonetizadas_yb_JPN[-1],visuMonetizadas_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(receitaBruta_yb_JPN[-1],receitaBruta_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(premium_yb_JPN[-1],premium_yb_JPN[-2])}'), FootnoteText(f'{GR.crescimento(AdSense_yb_JPN[-1],AdSense_yb_JPN[-2])}')))

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
doc.generate_pdf(fr'C:\Users\{GR.path_Usuarios}\Documents\Repositórios\Relatórios\TNsemanal\RelatórioSemanal-Monetizacao_{GR.penultimo_domingo().strftime("%d-%m-%Y")} a {GR.ultimo_sabado().strftime("%d-%m-%Y")}', clean_tex=True)

print("Relatório em LaTeX gerado com sucesso!")
