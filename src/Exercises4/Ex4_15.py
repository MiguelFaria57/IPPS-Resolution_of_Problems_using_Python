def acronimo(cadeia):
    a = ''
    palavras = cadeia.split()
    for i in palavras:
        a += i[0].upper()

    return a


def main():
    print(acronimo("Random Access Memory"))


if __name__ == '__main__':
    main()