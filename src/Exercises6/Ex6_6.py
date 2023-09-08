def somaCumulativa(lista):
    novaLista = []
    for i in range(len(lista)):
        soma = 0
        for j in range(i+1):
            soma += lista[j]
        novaLista += [soma]
    print(novaLista)
    return novaLista



def main():
    somaCumulativa([1,2,3])


if __name__ == '__main__':
    main()