def verificaNumerosFicheiro(nomeFich):
    f = open(nomeFich, 'r')
    a = f.read()
    f.close()
    for i in range(len(a)):
        if a[i] is 0: ####
            s=0



def main():
    verificaNumerosFicheiro("Ex7_4_VerificaNum")


if __name__ == '__main__':
    main()