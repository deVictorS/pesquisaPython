import curses
from destacar_palavra import destacar_palavra
from inicializar_arquivo import arquivo_dados
import os
import re

def exibir_resultado_curses(ctdsrc, texto, termo):
    curses.curs_set(0)
    stdscr.clear()
    linhas, encontrados = destacar_palavra(texto, termo)
    if not encontrados:
        stdscr