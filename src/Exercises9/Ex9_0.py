# Somatório de números inteiros até N
#    0.1 sem recursividade
#    0.2 com recursividade


def somatorio1(N):
    aux = 0
    for i in range(1, N+1):
        aux += i
    return aux


def somatorio2(N):
    if N==1:
        return 1
    else:
        return N+somatorio2(N-1)



def main():
    print(somatorio1(3))
    print(somatorio2(3))


if __name__ == '__main__':
    main()