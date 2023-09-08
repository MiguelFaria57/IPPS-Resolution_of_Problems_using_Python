def codifica(texto, num):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    alfabetoM = alfabeto.upper()
    codificado = ''
    for i in texto:
        if i in alfabeto:
            codificado += alfabeto[(alfabeto.find(i)+num) % len(alfabeto)]
        elif i in alfabetoM:
            codificado += alfabetoM[(alfabetoM.find(i)+num) % len(alfabetoM)]
        else:
            codificado += i
    return codificado


def descodifica(texto, num):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabetoM = alfabeto.upper()
    descodificado = ''
    for i in texto:
        if i in alfabeto:
            descodificado += alfabeto[(alfabeto.find(i)-num) % len(alfabeto)]
        elif i in alfabetoM:
            descodificado += alfabetoM[(alfabetoM.find(i)-num) % len(alfabetoM)]
        else:
            descodificado += i
    return descodificado



def main():
    print(codifica("Ola eu sou o Miguel", 12))
    print(descodifica(codifica("Ola eu sou o Miguel", 12), 12))


if __name__ == "__main__":
    main()