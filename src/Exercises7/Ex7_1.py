def criarFicheiro(nomeFich, texto):
    f = open(nomeFich, 'w')
    f.write(texto)
    f.close()



def main():
    criarFicheiro("primeiro.txt", "Acabei de criar o meu primeiro ficheiro em Python.\n")


if __name__ == '__main__':
    main()