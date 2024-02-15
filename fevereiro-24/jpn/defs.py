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
