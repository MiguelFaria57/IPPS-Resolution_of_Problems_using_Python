def multiplicaletras(cad, l, v):
    nova=''
    for i in cad:
        if i==l:
            nova += i*v
        else:
            nova += i
    print(nova)
    return nova

#multiplicaletras("ola", "a", 4)
#multiplicaletras("teste", "e", 3)

import turtle as t


def goto(x, y, h):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.seth(h)

def quadrado(lado):
    for i in range(4):
        t.fd(lado)
        t.lt(90)

def grelha(linhas, colunas, lado):
    x=t.xcor()
    y=t.ycor()
    for i in range(linhas):
        for j in range(colunas):
            quadrado(lado)
            goto(t.xcor()+lado, t.ycor(), 0)
        y-=lado
        goto(x, y, 0)

def pintaQuadrado(linha, coluna, lado, cor):
    goto((coluna-1)*lado, -(linha-1)*lado, 0)
    t.fillcolor(cor)
    t.begin_fill()
    quadrado(lado)
    t.end_fill()

def figura():
    t.speed(0)
    grelha(6, 5, 50)
    pintaQuadrado(2, 2, 50, "black")
    pintaQuadrado(4, 3, 50, "black")
    pintaQuadrado(6, 1, 50, "black")
    t.hideturtle()
    t.done()

figura()