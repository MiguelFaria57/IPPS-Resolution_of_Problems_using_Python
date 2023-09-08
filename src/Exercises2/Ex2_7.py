import turtle as t

def goto(posx, posy, heading):
    t.pu()
    t.goto(posx, posy)
    t.pd()
    t.seth(heading)

def circulo(raio, extensao, cor):
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio, extensao)
    t.end_fill()

def smile():
    circulo(150, 360, 'white')
    goto(-60, 200, 0)
    circulo(20, 360, 'black')
    goto(60, 200, 0)
    circulo(20, 360, 'black')
    goto(-80, 60, -30)
    circulo(150, 70, 'white')


def main():
    smile()
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()