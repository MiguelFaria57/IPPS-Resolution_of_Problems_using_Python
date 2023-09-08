import turtle as t

def goto(posx, posy, heading):
    t.pu()
    t.goto(posx, posy)
    t.pd()
    t.seth(heading)

def retangulo(comp, larg, cor):
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(2):
        t.fd(comp)
        t.lt(90)
        t.fd(larg)
        t.lt(90)
    t.end_fill()

def triangulo(lado, cor):
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(3):
        t.fd(lado)
        t.left(120)
    t.end_fill()

def desenhaFigura():
    goto(-50, 0, 0)
    retangulo(100, 100, 'green')
    goto(23, 140, 90)
    retangulo(35, 10, 'black')
    goto(-50, 100, 0)
    triangulo(100, 'red')


def main():
    desenhaFigura()
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()