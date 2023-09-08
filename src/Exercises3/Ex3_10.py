def descodifica(texto, chave):
    textoDescodificado = ''
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(texto)):
        if texto[i] in abc:
            textoDescodificado += chave[abc.find(texto[i])]
        else:
            textoDescodificado += ' '

    return textoDescodificado



def main():
    t = 'loz vf hlf l nrtfvo'
    c = 'zyxwvutsrqponmlkjihgfedcba'
    print(descodifica(t, c))


if __name__ == '__main__':
    main()