# ---------- Foto exsIPRP.png

def conta_digitos_letras(texto):
    d = 0
    l = 0
    for i in texto:
        if i.isdigit():
            d += 1
        if i.isalpha():
            l += 1
    print("DIGITOS: %d\nLETRAS: %d" %(d,l))
    return d,l

# o resto está feito nos testes seguintes


# ---------- Teste 2 2018 TP4/8/9

# EX 1

def auxiliar(lista):
    temp = []
    for i in range(len(lista) -1, -1, -1):
        temp.append(lista[i])
    return temp

def misterio(matriz):
    for i in range(len(matriz)):
        matriz[i] = auxiliar(matriz[i])
    return matriz

def ex1_2018tp489():
    print(misterio([[-1, -10, 0], [8, -1, 10]]))

# EX 2

def remove_elementos(l1, l2):
    if len(l1) != len(l2):
        print("Listas não têm o mesmo comprimento")
    else:
        l = []
        for i in range(len(l1)):
            if l2[i] == 1:
                l += [l1[i]]
        return l

def ex2_2018tp489():
    print(remove_elementos ([1,2,3,4,5], [0,1,0,1,0]))

# EX 3

def leituraDados(input_f):
    with open(input_f, 'r') as i:
        d = {}
        for l in i:
            for c in l.strip():
                if c != ' ':
                    if c in d.keys():
                        d[c] += 1
                    else:
                        d[c] = 1
        return d

def escritaHistograma(dic, output_f):
    with open(output_f, 'w') as o:
        for k, v in dic.items():
            print(k + " | " + v*'*')
            o.write(k + " | " + v*'*' + "\n")


def ex3_2018tp489():
    escritaHistograma(leituraDados("input2018TP489.txt"), "output2018TP489.txt")


# ---------- Teste 2 2018 TP4/2

# EX 1

def mais_primeiros(l):
    d = {}
    for i in l:
        for j in range(len(i)):
            if i[j] == 1:
                if j not in d:
                    d[j] = 1
                else:
                    d[j] += 1
    p = (-1, -1)
    for k,v in d.items():
        if v > p[1]:
            p = (k, v)
    print(p[0])

def ex1_2018tp42():
    mais_primeiros([(3,1,2,4), (2,1,3,4), (1,2,3,4), (2,1,4,3)])

# EX 2

def reciprocas(d):
    l = []
    for k,v in d.items():
        for i in v:
            if i in d:
                if k in d[i]:
                    if (i, k) not in l:
                        l += [(k, i)]
    print(l)


def ex2_2018tp42():
    reciprocas({'Joana':['Pedro','Tania','Joao'], 'Joao':['Pedro','Joana','Sofia','Tania'] , 'Tania':['Pedro','Ines','Joao']})

# EX 3

def lerFicheiro(f_i):
    with open(f_i, 'r') as fi:
        t = fi.readlines()
        return t

def escreverFicheiro(f_o, t):
    maxL = 0
    for i in t:
        if len(i)-1 > maxL:
            maxL = len(i)
    with open(f_o, 'w') as fo:
        for i in t:
            fo.write(i.strip() + (maxL-len(i))*'-' + '\n')

def ex3_2018tp42():
    escreverFicheiro("output2018TP42.txt", lerFicheiro("input2018TP42.txt"))


# ---------- Teste 2 2019 TP2/5/9

# EX 2

def removeElementos(d, n):
    newd = {}
    delKeys = []
    for k,v in d.items():
        if n not in v:
            newd[k] = v
        else:
            delKeys += [k]
    return newd, delKeys

def ex2_2019tp259():
    newd, delKeys = removeElementos({1:[1, 5, 2], 2:[3, 1, 4], 3:[9, 3, 5]}, 5)
    print(newd)
    print(delKeys)

# EX 3

def lerMatriz(f_i):
    with open(f_i, 'r') as fi:
        t = fi.readlines()
    return t

def escreverEsta(f_o, t):
    t2 =[]
    for i in t:
        i = i.strip()
        a = i.split(" ")
        t2 += [a]
    print(t2)
    s = 0
    for i in t2:
        for j in i:
            s += int(j)
    mean = s/(len(t2)*len(t2[0]))
    nl = len(t2)
    nc = len(t2[0])
    print("nl = %d\nnc = %d\nmean = %f" %(nl, nc, mean))
    with open(f_o, 'w') as fo:
        fo.write("nl = %d\nnc = %d\nmean = %f" %(nl, nc, mean))


def ex3_2019tp259():
    escreverEsta("output2019TP259.txt", lerMatriz("input2019TP259.txt"))


# ---------- Teste 2 2019 TP3/6

# EX 1

def ex1_2019tp36():
    return {"aluno":{"disciplina":"classificacao"}}

# EX 2

def find(file, cad):
    with open(file, 'r') as fi:
        t = fi.readlines()
    l = ()
    for i in range(len(t)):
        if cad in t[i]:
            l += (i,)
    return l

def escreverNumL(f_o, l):
    if l != ():
        with open(f_o, 'w') as fo:
            for i in l:
                fo.write(str(i) + " ")
    else:
        print("A cadeia não foi encontrada")

def ex2_2019tp36():
    escreverNumL("output2019TP36.txt", find("input2019TP36.txt", "abc"))

# EX 3

def cria_dicionario(d):
    nd = {}
    for k,v in d.items():
        if v[0] not in nd:
            nd[v[0]] = 1
        else:
            nd[v[0]] += 1
    for c in nd.keys():
        ano = 2020
        for i,j in d.items():
            if c == j[0]:
                if j[1]<ano:
                    ano = j[1]
        nd[c] = (nd[c], 2020-ano)
    print(nd)

def ex3_2019tp36():
    cria_dicionario({10:(3,2000), 20:(4,1998), 21:(4,1987), 11:(3,1990)})


# ---------- Teste 2 2019 TP3/6

# EX 2

def extrai_info(l):
    print(mediaCor(l, 'x'))
    print(mediaCor(l, 'y'))
    print(mediaCor(l, 'z'))
    print(contagemOcorr(l))

def mediaCor(l, c):
    cor = "xyz"
    if c in cor:
        aux = cor.index(c)
        s = 0
        for i in l:
            s += i[aux]
        return s/len(l)
    else:
        print("Parâmetro inválido")

def contagemOcorr(l):
    d = {}
    for i in l:
        c = 0
        for j in l:
            if i == j:
                c += 1
        d[i] = c
    return d

def ex2_2019tp7():
    extrai_info([(1,2,3), (2,8,6), (1,2,3), (8,5,6)])

# EX 3

def repeticaoLetras(f_i, f_o):
    escreverFich(f_o, lerFich(f_i))

def lerFich(f_i):
    with open(f_i, 'r') as fi:
        t = ''
        for l in fi:
            l = l.strip()
            l = l.split('-')
            t += int(l[0])*l[1]
        return t

def escreverFich(f_o, t):
    with open(f_o, 'w') as fo:
        fo.write(t)

def ex3_2019tp7():
    repeticaoLetras("input2019TP7.txt", "output2019TP7.txt")



# ---------- MAIN

if __name__ == '__main__':
    #conta_digitos_letras("hello world! 123")
    #extrai_info([(1,2,3), (2,8,6), (1,2,3), (8,5,6)])
    #repeticaoLetras("input2019TP7.txt", "outputExsImg1.txt")
    #cria_dicionario({10:(3,2000), 20:(4,1998), 21:(4,1987), 11:(3,1990)})
    #ex1_2018tp489()
    #ex2_2018tp489()
    #ex3_2018tp489()
    #ex1_2018tp42()
    #ex2_2018tp42()
    #ex3_2018tp42()
    #ex2_2019tp259()
    ex3_2019tp259()
    #ex2_2019tp36()
    #ex3_2019tp36()
    #ex2_2019tp7()
    #ex3_2019tp7()