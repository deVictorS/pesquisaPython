from inicializar_arquivo import arquivo_dados


def inserir_dado():
    print("=== INSERÇÃO DE DADOS ===")
    dado = input("Digite a nova informação a ser inserida: ")
    with open(arquivo_dados, 'w', encoding='utf-8') as f:
        f.write(dado + "\n")
    print("=== INFORMAÇÃO CADASTRADA ===")    