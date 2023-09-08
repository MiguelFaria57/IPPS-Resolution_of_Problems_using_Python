import turtle as t


def simulaCaminho(caminho):
    for i in caminho:
        if i == 'f':
            t.fd(20)
        elif i == 't':
            t.bk(20)
        elif i == 'e':
            t.lt(90)
        elif i == 'd':
            t.rt(-90)


def main():
    simulaCaminho("ffefdtttdfetttteff")
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()