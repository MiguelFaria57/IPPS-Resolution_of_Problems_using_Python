def adicionaLinhaFicheiro(nomeFich, texto):
    f = open(nomeFich, 'a')
    f.write(texto)
    f.close()



def main():
    adicionaLinhaFicheiro("primeiro.txt", "Linha\n")


if __name__ == '__main__':
    main()