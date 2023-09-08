def substituiVogais(texto):
    textoSubstituido = ''
    for i in texto:
        if i in 'aeiou':
            textoSubstituido += ' '
        else:
            textoSubstituido += i

    return textoSubstituido


def main():
    print(substituiVogais('qaa q qaqqa a q aq'))


if __name__ == '__main__':
    main()