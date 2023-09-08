def calcularNumUnidades(dimensoes):
    areaSala = dimensoes[0]*dimensoes[1]
    areaTijoleira = dimensoes[2]*dimensoes[3]

    return int(areaSala//areaTijoleira)


def main():
    dimensoes = []
    dimensoes += [float(input("Indique a largura da sala: "))]
    dimensoes += [float(input("Indique o comprimento da sala: "))]
    dimensoes += [float(input("Indique a largura da tijoleira: "))]
    dimensoes += [float(input("Indique o comprimento da tijoleira: "))]

    print("\nDimensões:", end=' ')
    for i in dimensoes:
        print(i, end = ' ')

    print("\nVai precisar de pelo menos", calcularNumUnidades(dimensoes), "unidades.")



if __name__ == "__main__":
    main()