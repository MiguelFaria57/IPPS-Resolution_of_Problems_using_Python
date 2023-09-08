def posicoesVogais(texto):
    vogais = "aeiouAEIOU"
    dic = {}
    for i in range(len(texto)):
        if texto[i] in vogais:
            #dic[texto[i]] = dic.get(texto[i],[]) + [i]
            if texto[i] in dic.keys():
                dic[texto[i]] += [i]
            else:
                dic[texto[i]] = [i]
    print(dic)
    return dic


def main():
    posicoesVogais("agora e que vao ser elas, Ai, Ai!")


if __name__ == '__main__':
    main()