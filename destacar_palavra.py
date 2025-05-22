import re
import curses

def destacar_palavra(texto , palavra):
    padrao = re.compile(re.escape(palavra), re.IGNORECASE)
    linhas = texto.split('\n')
    resultado = []
    for linha in linhas:
        if padrao.search(linha):
            linha_destacada = padrao.sub(lambda m: f"\033[4m\033[93m{m.group(0)}\033[0m", linha)
            resultado.append((linha_destacada, linha))

        else:
            resultado.append((linha, None))    

    return resultado        
                                         