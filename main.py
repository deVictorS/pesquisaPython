##PESQUISADOR DE DADOS##
from inserir_dado import inserir_dado
from buscar_dado import buscar_dado

import re
import os

def menu():
    while True:
        print("=== MENU ===")
        print("1 - Inserir novo dado")
        print("2 - Buscar por dados")
        print("0 - Sair")
        escolha = input("Digite uma opção: ")

        if escolha == "1":
            inserir_dado()

        elif escolha == "2":
            buscar_dado()

        elif escolha == "0":
            print("=== FINANLIZANDO PROGRAMA ===")
            break        

        else:
            print("OPÇÃO INVÁLIDA")

if __name__ == "__main__":
    menu()                    