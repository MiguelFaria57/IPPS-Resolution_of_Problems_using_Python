def calculoPolinomio(x):
    return x**4+x**3+2*x**2-x


def main():
    x = int(input("Indique um valor x: "))
    print("O valor do polinómio é %d." %(calculoPolinomio(x)))



if __name__ == "__main__":
    main()