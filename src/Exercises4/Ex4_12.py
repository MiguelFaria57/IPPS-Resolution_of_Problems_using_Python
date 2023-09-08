def tabela():
    print("Número   Quadrado")
    for i in range(5):
        print("%6d   %8d" %(i+1, (i+1)**2))



def main():
    tabela()


if __name__ == '__main__':
    main()