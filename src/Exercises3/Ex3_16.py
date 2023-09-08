def sufixosCadeia(texto):
    t = ''
    for i in range(len(texto)-1, -1, -1):
        t += texto[i:len(texto)] + '\n'

    return t



def main():
    print(sufixosCadeia('Monty Python'))


if __name__ == '__main__':
    main()