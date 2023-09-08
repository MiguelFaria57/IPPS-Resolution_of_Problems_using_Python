def dadosPopulacionais(populacaoInicial, anos):
    n = int(input("Frequência de nascimentos (minutos): "))
    f = int(input("Frequência de falecimentos (minutos): "))
    e = int(input("Frequência de emigração (minutos): "))
    print("Resumo dos dados:\n" + "-"*17)
    print("Frequência de nascimentos: %d" %(n))
    print("Frequência de falecimentos: %d" % (f))
    print("Frequência de emigrantes: %d" % (e))
    print("População Inicial: %d" % (populacaoInicial))
    print("Estimativa:\n" + "-"*11)
    novaPopulacao = populacaoInicial + ((anos*365*24)/(n/60)) - ((anos*365*24)/(f/60)) - ((anos*365*24)/(e/60))
    print("A população ao fim de %d ano(s): %d" %(anos, novaPopulacao))



def main():
    dadosPopulacionais(10000000, 1)


if __name__ == '__main__':
    main()