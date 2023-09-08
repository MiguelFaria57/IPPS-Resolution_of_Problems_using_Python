def numPerfeito(n):
    aux = 0
    for i in range(1, n):
        if n%i == 0:
           aux += i
    return aux == n

def numPerfeitoInt(limI, limS):
    t = ()
    for i in range(limI, limS):
        if numPerfeito(i):
            t += (i,)
    return t



def main():
    print(numPerfeitoInt(1, 30))


if __name__ == "__main__":
    main()