def cadeiaComplementar(adn):
    comp=''
    for i in range(len(adn)):
        if adn[i] == 'A':
            comp = comp + 'T'
        elif adn[i] == 'T':
            comp = comp + 'A'
        elif adn[i] == 'C':
            comp = comp + 'G'
        elif adn[i] == 'G':
            comp = comp + 'C'
        else:
            comp = "Erro - cadeia inválida"
            break
    return comp


def main():
    print(cadeiaComplementar('ATGGCTACG'))


if __name__ == '__main__':
    main()