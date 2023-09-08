import turtle as t
import random as r


def goto(x, y, h):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.seth(h)


def quadrado(l):
    for i in range(4):
        t.fd(l)
        t.lt(90)


def grelha(l, c, d):
    x = t.xcor()
    y = t.ycor()
    for i in range(l):
        for j in range(c):
            quadrado(d)
            goto(x+(j+1)*d, y+i*d, 0)
        goto(x, y+(i+1)*d, 0)


def passeioAleatorio(n, d, l, c):
    direcoes = ("norte", "este", "sul", "oeste")
    goto(r.randrange(0, c*d, d), r.randrange(0, l*d, d), 0)
    t.pensize(2)
    t.pencolor("red")
    t.fillcolor("red")
    t.dot(10)
    for i in range(n):
        ir = r.choice(direcoes)
        if ir == "norte":
            if t.ycor()+d <= l*d:
                t.seth(90)
                t.fd(d)
            else:
                n += 1
        if ir == "este":
            if t.xcor()+d <= c*d:
                t.seth(0)
                t.fd(d)
            else:
                n += 1
        if ir == "sul":
            if t.ycor()-d >= 0:
                t.seth(-90)
                t.fd(d)
            else:
                n += 1
        if ir == "oeste":
            if t.xcor()-d >= 0:
                t.seth(180)
                t.fd(d)
            else:
                n += 1
    t.stamp()



def main():
    t.speed(0)
    grelha(8, 8, 50)
    passeioAleatorio(100, 50, 8, 8)
    t.hideturtle()
    t.done()


if __name__ == '__main__':
    main()