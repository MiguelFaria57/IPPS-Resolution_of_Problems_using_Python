import turtle as t
import random as r
import math as m

def goto(x, y, h):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(h)

#####################################################

def trocaCaracter(cadeia):
    novo = ''
    if len(cadeia) % 2 == 0:
        for i in range(len(cadeia)):
            if i%2 != 0:
                novo += cadeia[i] + cadeia[i-1]
    else:
        for i in range(len(cadeia)-1):
            if i%2 != 0:
                novo += cadeia[i] + cadeia[i-1]
        novo += cadeia[len(cadeia)-1]
    print(novo)
#####################################################

def trianguloCor(lado, cor):
    t.pencolor(cor)
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(3):
        t.fd(lado)
        t.rt(120)
    t.end_fill()

def desenhaTriangulos(num, tamMinimo):
    for i in range(num):
        goto(-((num - i) * tamMinimo + 20)/2, -i*20, 0)
        if i%2 == 0:
            trianguloCor((num-i)*tamMinimo + 20, "yellow")
        else:
            trianguloCor((num-i)*tamMinimo + 20, "blue")
    t.hideturtle()
    t.done()
######################################################

def raizes(a, b, c):
    discriminante = b**2 - 4*a*c
    if a == 0 or discriminante < 0:
        print(" Erro ")
    else:
        raiz_disc = m.sqrt(discriminante)
        raiz1 = float((-b + raiz_disc))/(2*a)
        raiz2 = float((-b - raiz_disc))/(2*a)
        if raiz1 == raiz2 :
            print(" Solucao : ", raiz1)
        else :
            print(" Solucoes : ", raiz1, raiz2) #aqui
######################################################

def palavra_aleatoria(palavra):
    novo =''
    for i in range(len(palavra)):
        novo += palavra[r.randint(0,len(palavra)-1)]
    print(novo)
######################################################

def retanguloCor(l, c, cor):
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(2):
        t.fd(l)
        t.lt(90)
        t.fd(c)
        t.lt(90)
    t.end_fill()

def seccaoPiano(ladoTecla):
    aux = t.xcor()
    for i in range(4):
        retanguloCor(ladoTecla, ladoTecla*7, "white")
        goto(t.xcor()+ladoTecla, t.ycor(), 0)
    goto(aux+2*ladoTecla/3, ladoTecla*7/2-ladoTecla*3, 0)
    for i in range(3):
        retanguloCor(ladoTecla-ladoTecla/3, ladoTecla*3, "black")
        goto(t.xcor()+ladoTecla, t.ycor(), 0)

def desenhaPiano(numVezes, ladoTecla):
    t.speed(0)
    goto(-numVezes*ladoTecla*4/2, -ladoTecla*7/2, 0)
    for i in range(numVezes):
        seccaoPiano(ladoTecla)
        goto(-numVezes*ladoTecla*4/2+4*(i+1)*ladoTecla, -ladoTecla*7/2, 0)
    t.hideturtle()
    t.done()
######################################################

def caracteresEntrePos(cad, a, b):
    novo = ''
    for i in cad:
        if a <= i <= b:
            novo += i
    print(novo)
######################################################

def triangulo(lado):
    for i in range(3):
        t.fd(lado)
        t.lt(120)

def teias(x, y, ori, tam):
    t.speed(0)
    espacamentoTeias = 10
    goto(x, y, ori)
    for i in range(tam):
        aux=(i+1)*espacamentoTeias
        for j in range(6):
            triangulo(aux)
            t.lt(60)
    goto(x, y, ori)
    t.turtlesize(0.1*tam)
    t.shape("turtle")
    t.stamp()
    t.hideturtle()
    t.done()
######################################################

def petala(raio, cor):
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio, 90)
    t.lt(90)
    t.circle(raio, 90)
    t.end_fill()

def flor(raio, numP, cor):
    t.speed(0)
    for i in range(numP):
        t.seth(360/numP*i)
        petala(raio, cor)
    t.seth(230)
    t.pensize(10)
    t.circle(3*raio, 60)
    t.hideturtle()
    t.done()
######################################################

def mostra(i):
    print(i[-1]) # a_str não está definido aqui
    #i[ -1] = i[0] 'str' object does not support item assignment
    print(i[-1])

def func():
    a_str = "ola"
    mostra(a_str)
######################################################

def acumula_letras(cad1, cad2):
    novo = ""
    for i in cad1:
        if i in cad2:
            novo += i
    print(novo)
######################################################

def eixos(x,y):
    goto(0,0,90)
    t.fd(y)
    t.stamp()
    goto(0,0,0)
    t.fd(x)
    t.stamp()
    goto(0,0,0)

def graficoLinhas(x, y, L, N):
    t.speed(0)
    eixos(x,y)
    xx=0
    yy=0
    for i in range(L):
        t.pencolor((r.random(), r.random(),r.random()))
        for j in range(N):
            xx = r.randint(xx, x)
            yy = r.randint(yy, y)
            t.goto(xx,yy)
        goto(0,0,0)
        xx=0
        yy=0
    t.hideturtle()
    t.done()
######################################################

def obtem_sub_cadeias(cadeia, char_i, char_f ):
    for i in range(len(cadeia)):
        if cadeia[i] == char_i:
            for j in range(i+1, len(cadeia)):
                if cadeia[j] == char_i:
                    break
                if cadeia[j] == char_f:
                    print(cadeia[i:j+1])
                    break
######################################################

def hexagonoCor(lado, cor):
    t.fillcolor(cor)
    t.begin_fill()
    for i in range(6):
        t.fd(lado)
        t.lt(60)
    t.end_fill()

def desenhaFigura(lado, numLinhas, numColunas):
    t.speed(0)
    x = -(lado * numColunas)
    y = (lado * numLinhas/2)
    for i in range(numColunas):
        goto(x, y, 0)
        for j in range(numLinhas):
            if j%2 != 0:
                hexagonoCor(lado, 'black')
                y=y-2*lado
                goto(x, y, 0)
            else:
                hexagonoCor(lado, 'white')
                y=y-2*lado
                goto(x, y, 0)
        if i%2 == 0:
            x = -(lado*numColunas)+((i+1)*2*lado)
            y = (lado*numLinhas/2)+lado
        else:
            x = -(lado*numColunas)+((i+1)*2*lado)
            y = lado*(numLinhas/2)
    t.hideturtle()
    t.done()
######################################################

def divisores(n):
    d = ()
    for i in range(1, n):
        if n%i == 0:
            d += (i,)
    print(d)
######################################################

def circulo(raio, cor):
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()

def mikey(x, y, tam, cor):
    goto(x, y-tam, 0)
    circulo(tam, cor)
    goto(x,y,45)
    t.fd(tam-2)
    t.seth(-45)
    circulo(tam/3, cor)
    goto(x, y, 135)
    t.fd(tam-2)
    t.seth(45)
    circulo(tam/3, cor)
    t.hideturtle()
    t.done()
######################################################

def areaPR(n):
    return n*m.cos(m.pi/n)*m.sin(m.pi/n)

def maiores_90_circulo(n1, n2):
    print("Polígonos com área maior do que 90% da área do círculo:")
    for i in range(n1, n2+1):
        if areaPR(i)>0.9*m.pi:
            print("Polígono com %d lados" %i)
######################################################

def retangulo(l,c):
    for i in range(2):
        t.fd(l)
        t.lt(90)
        t.fd(c)
        t.lt(90)

def prateleira(aP, cP, nL, lL):
    retangulo(cP, aP)
    goto(0,0,0)
    for i in range(nL):
        retangulo(lL, r.randint(2, aP))
        t.fd(lL)
    t.hideturtle()
    t.done()





######################################################
if __name__ == "__main__":
    #trocaCaracter("poder")
    #desenhaTriangulos(6, 50)
    #raizes(2,6,2)
    #palavra_aleatoria("domino")
    #desenhaPiano(4, 30)
    #caracteresEntrePos("aeiou", "e", "o")
    #teias(0, 0, 45, 50)
    #flor(100, 5, "black")
    #func()
    #acumula_letras("o teste deste exercicio ", "oi")
    #graficoLinhas(300,300,3,5)
    #obtem_sub_cadeias("aaa#aa#aeiou**aaa#abcd*", '#', '*')
    #desenhaFigura(50, 5, 6)
    #divisores(10)
    #mikey(10, -30, 100, "black")
    #maiores_90_circulo(3,10)
    prateleira(80,250,10,20)