import random as r
import turtle as t


def escreveParesFicheiro(numVezes, limMin, limMax):
    f = open("Ex7_7_Pares.txt", 'w')
    texto = ''
    for i in range(numVezes):
        c1 = r.randint(1, 6)
        c2 = r.randint(1, 6)
        f.write("%d %d\n" % (c1, c2))
    f.close()


def desenhaFigura(nomeFichCor):
    f = open(nomeFichCor, 'r')
    linhas = f.readlines()
    f.close()
    t.pensize(2)
    for l in linhas:
        l=l[:-1]
        x,y = l.split(" ")
        t.goto(int(x)*50, int(y)*50)
    t.hideturtle()
    t.done()



def main():
    escreveParesFicheiro(10, 1, 6)
    desenhaFigura("Ex7_7_Pares.txt")


if __name__ == '__main__':
    main()