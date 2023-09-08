def entrelaca(s1, s2):
    a = len(s1)
    b = len(s2)
    c=0
    if a>=b:
        c=a
    else:
        c=b
    nova_s = ""
    for i in range(c):
        if i<=a-1:
            nova_s += s1[i]
        if i<=b-1:
            nova_s += s2[i]
    tam = a+b
    t = (nova_s, tam)
    print(t)
    return t

entrelaca("acegi", "bdfhj")


def processa_dados(lt):
    d={}
    for i in lt:
        a = i[0] + i[1]
        if a not in d:
            d[a] = [1, [i]]
        else:
            d[a][0] += 1
            if i not in d[a][1]:
                d[a][1] += [i]
    print(d)
    return d

processa_dados([(2,2), (2,2), (4,5), (3,1)])


def export_friends(l, ficheiro):
    pessoas = []
    for i in l:
        for j in i:
            if j not in pessoas:
                pessoas += [j]
    with open(ficheiro, "w") as f:
        for p in pessoas:
            f.write(p + ";")
        for a in pessoas:
            f.write("\n")
            for b in pessoas:
                if (a,b) in l or (b,a) in l:
                    f.write("X")
                else:
                    f.write("0")

export_friends([("joao", "maria"), ("maria", "sofia"), ("sofia", "carla")], "exame_p4.txt")