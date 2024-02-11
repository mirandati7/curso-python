import csv


def ler_csv():
    arquivo = open('pessoas.csv')

    linhas = csv.reader(arquivo)

    for linha in linhas:
        print(linha)

def ler_csv_dicionario_dados():
    arquivo = open('pessoas.csv')

    pessoas = csv.DictReader(arquivo)

    for pessoa in pessoas:
        print("Nome:", pessoa["nome"], " - Idade:", pessoa["idade"], " - Email:", pessoa["email"])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ler_csv()
    ler_csv_dicionario_dados()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
