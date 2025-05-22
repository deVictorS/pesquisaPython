from inicializar_arquivo import arquivo_dados
from destacar_palavra import destacar_palavra
import os
import curses

def buscar_dado():

    print("=== BUSCA DE DADOS ===")
    termo = input("Digite o termo para buscar: ")
    with open(arquivo_dados, 'r', encoding='utf-8') as f:
        texto = f.read()

    curses.wrapper(exibir_resultado_curses, texto, termo)    

    