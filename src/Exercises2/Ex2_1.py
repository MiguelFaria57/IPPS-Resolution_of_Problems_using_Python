import turtle as t

def desenhaPoligono(numVezes, avanco, rotacao):
    for i in range(numVezes):
        t.fd(avanco)
        t.rt(rotacao)


def main():
    a = int(input("Indique o avanço: "))
    r = int(input("Indique a rotação: "))
    n = int(input("Indique o número de vezes que pretende repetir: "))
    t.pensize(2)
    desenhaPoligono(n, a, r)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()