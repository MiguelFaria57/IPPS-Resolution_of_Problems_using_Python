def mostrarSequenciaCar(nomeFich, numCar, posRef):
    f = open(nomeFich, 'r')
    a = f.read()
    f.close()
    print(a[posRef:posRef+numCar])



def main():
    mostrarSequenciaCar("primeiro.txt", 7, 7)


if __name__ == '__main__':
    main()