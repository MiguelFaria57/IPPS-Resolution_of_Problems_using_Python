import turtle as t

def desenhaPoligono(numVezes, avanco, rotacao):
    for i in range(numVezes):
        t.fd(avanco + 10*i)
        t.rt(rotacao)


def main():
    t.pensize(2)
    desenhaPoligono(30, 100, 144)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()