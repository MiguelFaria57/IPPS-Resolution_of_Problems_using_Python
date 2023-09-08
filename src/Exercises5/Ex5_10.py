import random as r

def probDardo(num):
    aux = 0
    for i in range(num):
        x = r.uniform(0, 2)
        y = r.uniform(0, 2)
        if ((x <= 1) and (y >= 1)) or ((x > 1) and (y <= 1)) or ((x > 1) and (y >= 1) and (y < x)):
            aux += 1
    return aux/num * 100



def main():
    x = int(input("Deseja lançar quantos dardos: "))
    print("Caiu numa região de número ímpar %d%% das vezes." %probDardo(x))



if __name__ == "__main__":
    main()