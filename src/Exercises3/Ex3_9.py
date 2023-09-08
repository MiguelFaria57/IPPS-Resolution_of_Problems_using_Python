def descodifica(textoCod):
    textoPosP = textoCod[len(textoCod)//2:]
    textoPosI = textoCod[:len(textoCod)//2]
    texto = ''
    i=0
    aux1=0
    aux2=0
    while i<(len(textoPosP) + len(textoPosI)):
        if i%2 == 0:
            texto += textoPosP[aux1]
            aux1 += 1
        else:
            texto += textoPosI[aux2]
            aux2 += 1
        i += 1

    return texto



def main():
    t = '1357902468'
    print(descodifica(t))


if __name__ == '__main__':
    main()