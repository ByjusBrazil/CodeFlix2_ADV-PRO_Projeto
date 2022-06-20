from helpers import clear_screen


# Constante com as opções do menu
MENU_OPTIONS = """
1. Adicionar tarefa
2. Remover tarefa
3. SAIR

"""


# Variável para armazenar a lista de tarefas
tasks = []


def print_tasks():
    # Função para imprimir as tarefas no console

    clear_screen()
    print("\n------------------------- TAREFAS -------------------------")

    for task in tasks:
        print(task)

    print("-----------------------------------------------------------")


def add_task():
    # Função para adicionar uma tarefa

    task = input("\nAdicionar tarefa: ")
    tasks.append(task)


def remove_task():
    # Função para remover uma tarefa

    task = input("\nRemover tarefa: ")

    if task in tasks:
        tasks.remove(task)


def menu():
    # Função principal do programa

    while True:
        print_tasks()

        option = input(MENU_OPTIONS)

        print_tasks()

        if option == "1":
            add_task()

        elif option == "2":
            remove_task()

        elif option == "3":
            break


# Executa a função principal
menu()
