def produtoEscalar(v1, v2):
    if len(v1) == 0:
        return 0
    else:
        return (v1[0] * v2[0]) + produtoEscalar(v1[1:], v2[1:])

'''
def produtoEscalar(v1, v2, n):
    if n == len(v):
        return 0
    else:
        return v1[n] * v2[0] + produtoEscalar(v, w, n+1)
'''



def main():
    print(produtoEscalar((1,2,3), (4,5,6))) #(4 + 10 + 18) = 32
    #print(produtoEscalar((1,2,3), (4,5,6), 0))


if __name__ == '__main__':
    main()