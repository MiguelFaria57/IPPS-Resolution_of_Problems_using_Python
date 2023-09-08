import math


def desordem(n, m):
    if (n == 0) or (m == 0):
        return 0
    p1 = n/(n+m)
    p2 = m/(n+m)
    return - p1 * math.log2(p1) - p2 * math.log2(p2)



def main():
    n = int(input("Indique o nº de objetos do 1º tipo: "))
    m = int(input("Indique o nº de objetos do 2º tipo: "))
    print("A desordem do conjunto é %.2f." %(desordem(n, m)))


if __name__ == '__main__':
    main()