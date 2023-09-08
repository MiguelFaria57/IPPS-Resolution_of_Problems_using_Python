def verSeSaoIrmaos(dic, pes1, pes2):
    paisPes1=[]
    paisPes2=[]
    for k,v in dic.items():
        if pes1 in v:
            paisPes1 += [k]
        if pes2 in v:
            paisPes2 += [k]
    return paisPes1 == paisPes2



def main():
    arvore = {'pai': ['filho1', 'filho2'], 'mae': ['filho1', 'filho2'], 'filho1': ['neto1', 'neto2'],
              'filho2': ['neto3'], 'neto1': ['bisneto1'], 'neto2': [], 'neto3': ['bisneto2']}
    print(verSeSaoIrmaos(arvore, "filho1", "filho2"))


if __name__ == '__main__':
    main()