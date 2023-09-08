def subCadeias(texto, comp):
    t = ''
    for i in range(len(texto)-comp+1):
        t += texto[i:i+comp] + '\n'

    return t



def main():
    print(subCadeias('Monty Python', 3))


if __name__ == '__main__':
    main()