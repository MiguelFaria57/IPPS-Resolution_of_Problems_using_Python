import turtle as t


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



def main():
    t.speed(0)
    grelha(8,8,50)
    t.hideturtle()
    t.done()


if __name__ == '__main__':
    main()