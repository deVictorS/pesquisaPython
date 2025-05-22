import os

arquivo_dados = "dados.txt"

def inicializar_arquivo():
    if not os.path.exists(arquivo_dados):
        with open(arquivo_dados, 'w', encoding='utf-8') as f:
            f.write("")