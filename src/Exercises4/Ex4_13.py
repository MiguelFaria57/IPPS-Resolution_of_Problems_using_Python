def milhasQuilometros(limI, limS):
    c = 1.609
    print("Milhas    Quilómetros")
    print('-'*22)
    for i in range(limI, limS+1):
        print("%.2f     %.2f" %(i, i*c))



def main():
    milhasQuilometros(10, 20)


if __name__ == '__main__':
    main()