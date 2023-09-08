def serSimetrico(rel):
    for (x,y) in rel:
        print((x,y))
        if (y,x) not in rel:
            print((x,y))
            return False
    return True
    '''
    for k,v in rel:
        if v not in rel:
            return False
    return True
    '''



def main():
    relacao = {(3,1):(2,2), (1,2):(3,1), (2,1):(1,1), (1,3):(1,2)}
    print(serSimetrico(relacao))


if __name__ == '__main__':
    main()