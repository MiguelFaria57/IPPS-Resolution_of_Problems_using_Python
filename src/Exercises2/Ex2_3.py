import turtle as t
import random as r


def passeioAleatorio(numVezes):
    for i in range(numVezes):
        t.colormode(255)
        t.pencolor((r.randint(0,255), r.randint(0,255), r.randint(0,255)))
        t.fd(r.randint(10, 200))
        t.rt(r.randint(0,360))



def main():
    t.pensize(2)
    passeioAleatorio(30)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()