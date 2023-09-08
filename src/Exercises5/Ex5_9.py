import random as r

def lancamentoDado(num):
    aux = 0
    for i in range(num):
        if r.randint(1, 6) % 2 == 0:
            aux += 1
    return aux/num * 100


def main():
    x = int(input("Deseja lançar o dado quantas vezes: "))
    print("Saiu número par %d%% das vezes." %lancamentoDado(x))


if __name__ == "__main__":
    main()