import random as r

def geraCadeia(tamanho):
    adn = 'ATCG'
    cadeia = ''
    for i in range(tamanho):
        cadeia += adn[r.randint(0,3)]
    return cadeia


def main():
    print(geraCadeia(10))


if __name__ == '__main__':
    main()