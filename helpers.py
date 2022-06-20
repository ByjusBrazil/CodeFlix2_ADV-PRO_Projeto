import os


def clear_screen():
    # Função para limpar a tela do console

    if os.name == "nt":  # Verifica se o sistema é Windows
        os.system("cls")

    else:
        os.system("clear")