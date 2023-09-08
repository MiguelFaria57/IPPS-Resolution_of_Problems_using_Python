def prefixosCadeia(texto):
    t = ''
    for i in range(1,len(texto)+1):
        t += texto[0:i] + '\n'

    return t



def main():
    print(prefixosCadeia('Monty Python'))


if __name__ == '__main__':
    main()