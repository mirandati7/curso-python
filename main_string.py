# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def seu_nome(name):
    print(name + " Miranda")

def meu_time_favorito(time):
    print("Meu time favorito é " + time)

def usando_while():
    opcao = -1

    while opcao:
        print("0. Sair")
        print("1. Flamengo")
        print("2. Palmeiras")
        print("3. Corinthians")
        print("4. São Paulo ")

        opcao = int(input("Opção: "))

        if (opcao == 1):
            meu_time_favorito("Flamengo")
        if (opcao == 2):
            meu_time_favorito("Palmeiras")
        if (opcao == 3):
            meu_time_favorito("Corinthians")
        if (opcao == 4):
            meu_time_favorito("São Paulo")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    seu_nome("Alex")
    usando_while()




