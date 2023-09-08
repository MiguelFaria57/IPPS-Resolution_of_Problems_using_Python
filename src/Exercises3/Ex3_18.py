import random as r
import turtle as t


def simulaCaminho(caminho):
    for i in caminho:
        if i == 'f':
            t.fd(50)
        elif i == 't':
            t.bk(50)
        elif i == 'e':
            t.lt(r.randint(0,180))
        elif i == 'd':
            t.rt(-r.randint(0,180))



def main():
    simulaCaminho("ffefdtttdfetttteff")
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()