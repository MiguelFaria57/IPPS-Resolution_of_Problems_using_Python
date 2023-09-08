import math


def mediaBatimentos(idade):
    return 163+1.16*idade-0.018*idade**2



def main():
    idade = int(input("Indique a sua idade: "))
    print("O valor médio do batimento cardíaco máximo é %.2f." %(mediaBatimentos(idade)))


if __name__ == '__main__':
    main()