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
    t.seth(-60)
    for i in range(numVezes):
        quadrado(lado)
        lado += 10
        t.seth(t.heading()+10)



def main():
    t.speed(10)
    desenhaFigura(20, 20)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()