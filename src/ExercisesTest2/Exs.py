def calcula_mais_pedido(d):
    newd = {}
    for i in d.values():
        for j in i:
            if j not in newd:
                newd[j] = 1
            else:
                newd[j] += 1
    #print(newd)
    brinquedo = ''
    mais_pedido = -1
    for k,v in newd.items():
        if v > mais_pedido:
            mais_pedido = v
            brinquedo = k
    print(brinquedo)
    return brinquedo


calcula_mais_pedido({'João Santos':['Barbie', 'Nenuco'], 'Ana Gonçalves':['Bola de futebol'], 'Gonçalo Almeida':['Nenuco']})


def lerChats(f_i):
    d = {}
    with open(f_i, 'r') as fi:
        for i in fi:
            a=i.strip()
            a=a.split(',')
            #print(a)
            if (a[0],a[1]) not in d and (a[1],a[0]) not in d:
                d[(a[0],a[1])] = [(a[0],a[2])]
            else:
                if (a[0],a[1]) in d:
                    d[(a[0], a[1])] += [(a[0],a[2])]
                if (a[1],a[0]) in d:
                    d[(a[1], a[0])] += [(a[0],a[2])]
        print(d)
    return d

def escreverFichChat(d):
    for k,v in d.items():
        nomeFich = k[0]+"-"+k[1]+".txt"
        with open(nomeFich, 'w') as f:
            for i in v:
                f.write(i[0]+":"+i[1]+'\n')

#lerChats("chats.txt")
escreverFichChat(lerChats("chats.txt"))