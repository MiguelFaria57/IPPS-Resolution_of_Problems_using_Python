def negativo(lista):
    novaLista = []
    for l in range(len(lista)):
        novaLista += [lista[l][:]]
    # podia usar "for l in lista" e "for c in l"
    for l in range(len(lista)):
        for c in range(len(lista[l])):
            if lista[l][c] == 0:
                novaLista[l][c] = 1
            elif lista[l][c] == 1:
                novaLista[l][c] = 0
            else:
                print("Imagem não está a preto e branco.")
                break
    print(lista)
    print(novaLista)
    return novaLista



def main():
    negativo([[0,1,0],[1,1,1],[0,1,0]])


if __name__ == '__main__':
    main()