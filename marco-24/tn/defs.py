# Recebe o valor e retorna uma fstring formatada e arredondada
def valorToString(valor):
    
    if float(valor)/1000 < 1:
        return f'{valor}'
    
    elif float(valor)/1000 > 1 and float(valor)/1000 < 1000:
        return f'{round(float(valor)/1000, 1)} mil'.replace('.',',')
    
    
    elif float(valor)/1000000 >= 1 and float(valor)/1000000 < 2:
        return f'{round(float(valor)/1000000,1)} milhão'.replace('.',',')

    elif float(valor)/1000000 >= 2:
        return f'{round(float(valor)/1000000,1)} milhões'.replace('.',',')

def variacaoPercentual(atual, antigo):
    # if(atual>antigo):
    #     valor_maior_tw = atual
    #     valor_menor_tw = antigo
    # else:
    #     valor_maior_tw = antigo
    #     valor_menor_tw = atual
    
    aumento_percentual = ((atual - antigo) / abs(antigo)) * 100
    
    return aumento_percentual*100

def taxaFixação(seguidores_permaneceram, novos_seguidores_total):
    
    return (seguidores_permaneceram/novos_seguidores_total)*100