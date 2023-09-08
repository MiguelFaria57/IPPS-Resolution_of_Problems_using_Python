def contaMenores(num, lista):
    aux = 0
    for i in lista:
        if i<num:
            aux += 1
    print(aux)
    return aux



def main():
    contaMenores(5, [2,8,6,5,3,2])


if __name__ == '__main__':
    main()