def posElemMatriz(matriz):
    for i in range(len(matriz)):
        aux = ''
        for j in range(len(matriz[i])):
            aux += "(%d,%d): %-3d" %(i,j,matriz[i][j])
        print(aux)



def main():
    posElemMatriz([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


if __name__ == '__main__':
    main()