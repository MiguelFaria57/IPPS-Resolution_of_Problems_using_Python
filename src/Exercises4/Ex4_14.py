def tabuada(num):
    print("Tabuada do número %d" %(num))
    print('-'*22)
    for i in range(1, 11):
        print("%d x %3d = %3d" %(num, i, num*i))



def main():
    tabuada(7)


if __name__ == '__main__':
    main()