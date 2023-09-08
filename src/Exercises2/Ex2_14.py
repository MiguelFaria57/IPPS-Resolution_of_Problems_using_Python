import turtle as t


def goto(posx, posy, heading):
    t.pu()
    t.goto(posx, posy)
    t.pd()
    t.seth(heading)


def quadrado(lado):
    for i in range(4):
        t.fd(lado)
        t.lt(90)


def desenhaFigura(numVezes, lado):
    for i in range(numVezes):
        goto(-(lado/2), -(lado/2), 0)
        quadrado(lado)
        lado += 20



def main():
    t.pensize(2)
    desenhaFigura(5, 100)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()