def rodarImagem(lista):
    novaLista = []
    for l in range(len(lista)):
        novaLista += [lista[l][:]]
    for l in range(len(lista)):
        for c in range(len(lista[l])):
            novaLista[c][len(lista)-1-l] = lista[l][c]
    print(lista)
    print(novaLista)
    return novaLista



def main():
    rodarImagem([[1,1,1],[0,1,0],[0,1,0]])


if __name__ == '__main__':
    main()