def verNetos(dic, pes):
    if pes in dic:
        netos = []
        filhos = dic[pes]
        for i in filhos:
            netos += dic[i]
        return netos
    else:
        return []



def main():
    arvore = {'pai': ['filho1', 'filho2'], 'mae': ['filho1', 'filho2'], 'filho1': ['neto1', 'neto2'],
              'filho2': ['neto3'], 'neto1': ['bisneto1'], 'neto2': [], 'neto3': ['bisneto2']}
    print(verNetos(arvore, "pai"))


if __name__ == '__main__':
    main()