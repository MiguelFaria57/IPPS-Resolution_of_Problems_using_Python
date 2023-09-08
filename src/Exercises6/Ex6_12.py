def adicionaDicionario(d):
    fruta = input("Indique o tipo de fruta: ")
    dic = {}
    informacoes1 = ("quantidadeComprada", "precoCompra", "quantidadeStock", "precoVenda")
    quantidadeComprada = int(input("Indique a quantidade dessa fruta comprada: "))
    precoCompra = float(input("Indique o preço de compra por quilo dessa fruta: "))
    quantidadeStock = int(input("Indique a quantidade dessa fruta em stock: "))
    precoVenda = float(input("Indique o preço de venda por quilo dessa fruta: "))
    informacoes2 = (quantidadeComprada, precoCompra, quantidadeStock, precoVenda)
    for i in range(len(informacoes1)):
        dic[informacoes1[i]] = informacoes2[i]
    d[fruta] = dic

def lucro(d):
    ganhos = 0
    for i in d.values():
        ganhos += (i["quantidadeComprada"] - i["quantidadeStock"]) * (i["precoVenda"] - i["precoCompra"])
    return ganhos

def maisCara(d):
    frutaMaisCara = ''
    precoMaisCaro = 0
    for i, j in d.items():
        if j["precoVenda"]>precoMaisCaro:
            precoMaisCaro = j["precoVenda"]
            frutaMaisCara = i
    return frutaMaisCara



def main():
    loja = {"maça":{"quantidadeComprada":5,"precoCompra":0.5,"quantidadeStock":3,"precoVenda":2},
            "pêra":{"quantidadeComprada":7,"precoCompra":0.7,"quantidadeStock":1,"precoVenda":2.5},
            "banana":{"quantidadeComprada":10,"precoCompra":0.6,"quantidadeStock":5,"precoVenda":2.7}}
    #adicionaDicionario(loja)
    #print(loja)
    print(lucro(loja))
    print(maisCara(loja))


if __name__ == '__main__':
    main()