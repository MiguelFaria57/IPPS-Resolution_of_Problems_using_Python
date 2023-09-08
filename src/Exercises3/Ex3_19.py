import random as r
import turtle as t


def geraPercurso(tamanho):
    direcoes = 'fted'
    percurso = ''
    for i in range(tamanho):
        percurso += direcoes[r.randint(0, 3)]

    return percurso


def simulaCaminho(caminho):
    for i in caminho:
        if i == 'f':
            t.fd(r.randint(10,100))
        elif i == 't':
            t.bk(r.randint(10,100))
        elif i == 'e':
            t.lt(r.randint(0,180))
        elif i == 'd':
            t.rt(-r.randint(0,180))


def main():
    simulaCaminho(geraPercurso(50))
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()