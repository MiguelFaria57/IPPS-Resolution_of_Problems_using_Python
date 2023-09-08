def IMC(peso, altura):
    return peso/(altura**2)


def main():
    peso = float(input("Indique o peso (Kg): "))
    altura = float(input("Indique a altura (m): "))
    print("O seu IMC é %.2f" %(IMC(peso, altura)))

if __name__ == "__main__":
    main()