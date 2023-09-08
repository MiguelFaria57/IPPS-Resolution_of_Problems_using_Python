def fatorial(n):
    aux = 1
    for i in range(n, 0, -1):
        aux *= i
    return aux

def logNatural(precisao):
    aux = 0
    for i in range(precisao):
        aux += 1/fatorial(i)
    return aux



def main():
    x = int(input("Deseja calcular o valor aproximado de 'e' com que precisão: "))
    print("Valor aproximado de 'e': %f" % logNatural(x))


if __name__ == "__main__":
    main()