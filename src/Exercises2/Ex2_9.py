import turtle as t

def desenhaFigura(corFundo, corTartaruga, vezes, tamanho, aumento, angulo):
    t.bgcolor(corFundo)
    t.shape('turtle')
    t.color(corTartaruga)
    t.pu()
    for i in range(vezes):
        t.stamp()
        tamanho += aumento
        t.forward(tamanho)
        t.right(angulo)



def main():
    desenhaFigura('blue', 'red', 40, 10, 3, 25)
    t.hideturtle()
    t.done()


if __name__ == "__main__":
    main()