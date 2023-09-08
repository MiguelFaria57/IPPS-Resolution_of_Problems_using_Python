def dinheiroRender(v, t, a):
    return v*(1+t)**a



def main():
    v = float(input("Indique o valor inicial: "))
    t = float(input("Indique a taxa de juro: "))

    a=0
    while(dinheiroRender(v, t, a) < 2*v):
        a += 1

    print("Cosegue duplicar o seu dinheiro ao fim de %.1f anos." %(a))


if __name__ == '__main__':
    main()