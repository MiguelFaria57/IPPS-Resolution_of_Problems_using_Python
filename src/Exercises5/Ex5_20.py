def fibonacci(v):
    n = ()
    for i in range(v):
        if i==0 or i==1:
            n += (1,)
        else:
            aux = n[i-2] + n[i-1]
            n += (aux,)
    return n


def pertencerFibonacci(n):
    if n<=0:
        print("Não pertence.")
    else:
        aux=2
        t=(1, 1)
        while t[aux-2]+t[aux-1] <= n:
            t += (t[aux-2]+t[aux-1],)
            aux += 1
        print(t)
        if n in t:
            print("Pertence.")
        else:
            print("Não pertence.")


def main():
    #print(fibonacci(8))
    pertencerFibonacci(580)


if __name__ == '__main__':
    main()