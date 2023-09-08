import turtle as t

def goto(posx, posy, heading):
    t.pu()
    t.goto(posx, posy)
    t.pd()
    t.seth(heading)

def circulo(raio, cor):
    t.pencolor(cor)
    t.pensize(4)
    t.circle(raio)

def desenhaFigura():
    cores = ['blue', 'black', 'red', 'yellow', 'green']
    posCima = -110
    posBaixo = -55
    for i in range(5):
        if i<3:
            goto(posCima, 0, 0)
            circulo(50, cores[i])
            posCima += 110
        else:
            goto(posBaixo, -50, 0)
            circulo(50, cores[i])
            posBaixo += 110


def main():
    desenhaFigura()
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()