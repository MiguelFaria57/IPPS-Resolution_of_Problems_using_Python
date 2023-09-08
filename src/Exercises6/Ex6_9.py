import turtle as t
import random as r


def geraComandos(n):
    comandos = []
    for i in range(n):
        comandos += r.choice(('A', 'R', 'E', 'D'))
    return comandos


def navega(c):
    t.dot(20, 'green')
    for i in c:
        if i == 'A':
            t.fd(50)
        elif i == 'R':
            t.bk(50)
        elif i == 'E':
            t.lt(90)
            t.fd(50)
        elif i == 'D':
            t.rt(90)
            t.fd(50)
    t.dot(20, 'red')



def main():
    navega(geraComandos(20))
    t.hideturtle()
    t.done()


if __name__ == '__main__':
    main()