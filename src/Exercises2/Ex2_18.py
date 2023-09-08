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

def desenhaFigura(tamanho):
    goto(-tamanho, 0, -90)
    circulo(tamanho, 180, 'black')
    t.seth(90)
    circulo(tamanho, 180, 'white')
    goto(0,0,90)
    circulo(tamanho/2, 180, 'black')
    goto(0, 0, -90)
    circulo(tamanho/2, 180, 'white')
    goto(-(tamanho/2), -(tamanho/9), 0)
    circulo(tamanho/9, 360, 'white')
    goto(tamanho/2, -(tamanho/9), 0)
    circulo(tamanho/9, 360, 'black')



def main():
    desenhaFigura(200)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()