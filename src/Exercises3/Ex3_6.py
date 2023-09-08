def dinheiroRender(v, t, n, a):
    return v*(1+(t/n))**(n*a)



def main():
    v = float(input("Indique o valor inicial: "))
    t = float(input("Indique a taxa de juro: "))
    a = int(input("Indique os anos decorridos: "))

    print("\nComposição mensal: %.2f\nAcumulação Anual: %.2f\n" %(dinheiroRender(v, t, 12, a), dinheiroRender(v, t, 1, a)))


if __name__ == '__main__':
    main()