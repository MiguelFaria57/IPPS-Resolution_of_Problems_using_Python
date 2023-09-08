# n par/ímpar, não x

def exponencial(x, n):
    if n == 0:
        return 1
    else:
        aux = exponencial(x, n//2)
        if n%2 == 0:
            return aux*aux
        else:
            return aux*aux*x



def main():
    print(exponencial(2, 3))


if __name__ == '__main__':
    main()