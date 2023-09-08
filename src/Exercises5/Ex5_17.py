def padraoA(n):
    print("Padrão A")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
    print()


def padraoB(n):
    print("Padrão B")
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
    print()


def padraoC(n):
    print("Padrão C")
    for i in range(1, n+1):
        print((n-i)*2*' ', end = '')
        for j in range(1, i+1):
            print(j, end=' ')
        print()
    print()



def main():
    padraoA(5)
    padraoB(5)
    padraoC(5)

if __name__ == '__main__':
    main()