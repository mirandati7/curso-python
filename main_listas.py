def funcao_lista():
    lista = ['impostos', 'salarios', 'altos', 'baixos']
    print(lista[0])
    print(len(lista))


def funcao_lista_for():
    impostos = ['MEI', 'Simples']
    for imposto in impostos:
        print(imposto)

# Pulando interação com break
def funcao_lista_for_continue():
    impostos = ['MEI', 'Simples']
    for imposto in impostos:
        if imposto.startswith("M"):
             continue
        print(imposto)


if __name__ == '__main__':
    funcao_lista()
    funcao_lista_for()
    funcao_lista_for_continue()