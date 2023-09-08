def AreaRetangulo(largura, comprimento):
    return largura*comprimento


def AreaCirculo(raio):
    return 3.14*(raio**2)


def main():
    larg = float(input("Indique a largura do retângulo: "))
    comp = float(input("Indique o comprimento do retãngulo: "))
    raio = float(input("Indique o raio da circunferencia: "))

    if (AreaRetangulo(larg, comp) == AreaCirculo(raio)):
        print("Não deve reclamar.")
    if (AreaRetangulo(larg, comp) > AreaCirculo(raio)):
        print("Ficou a ganhar.")
    else:
        print("Deve reclamar.")



if __name__ == "__main__":
    main()
