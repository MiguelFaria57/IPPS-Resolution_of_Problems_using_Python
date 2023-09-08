def copiaFicheiro(fichOrigem, fichDestino):
    fIn = open(fichOrigem, 'r')
    a = fIn.read()
    fIn.close()
    fOut = open(fichDestino, 'w')
    fOut.write(a)
    fOut.close()



def main():
    ficheiroOrigem = input("Indique o nome do ficheiro de origem: ")
    ficheiroDestino = input("Indique o nome do ficheiro de destino: ")
    copiaFicheiro(ficheiroOrigem, ficheiroDestino)


if __name__ == '__main__':
    main()