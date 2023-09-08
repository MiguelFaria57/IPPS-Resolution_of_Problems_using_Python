import turtle as t

def goto(posx, posy, heading):
    t.pu()
    t.goto(posx, posy)
    t.pd()
    t.seth(heading)

def retangulo(comp, larg, corPen, corFill):
    t.pensize(2)
    t.pencolor(corPen)
    t.fillcolor(corFill)
    t.begin_fill()
    for i in range(2):
        t.fd(comp)
        t.lt(90)
        t.fd(larg)
        t.lt(90)
    t.end_fill()

def setorCircular(raio, extensao, corPen, corFill):
    t.pensize(1)
    t.pencolor(corPen)
    t.fillcolor(corFill)
    t.begin_fill()
    t.fd(raio)
    t.lt(90)
    t.circle(raio, extensao)
    t.home()
    t.end_fill()

def desenhaFigura(tam):
    goto(-tam/2,-tam/2, 0)
    retangulo(tam, tam, 'black', 'yellow')
    angulo = 0
    for i in range(3):
        goto(0,0,angulo)
        setorCircular(0.4*tam, 60, 'black', 'black')
        angulo += 120
    goto(0, -0.075*tam, 0)
    t.pensize(2)
    t.pencolor('yellow')
    t.fillcolor('black')
    t.begin_fill()
    t.circle(0.075*tam)
    t.end_fill()


def main():
    desenhaFigura(400)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()