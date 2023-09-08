import turtle as t

def triangulo(lado):
    for i in range(3):
        t.fd(lado)
        t.lt(120)


def desenhaFigura(lado):
    for i in range(6):
        t.seth(i*60)
        triangulo(lado)



def main():
    t.pensize(2)
    desenhaFigura(100)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()