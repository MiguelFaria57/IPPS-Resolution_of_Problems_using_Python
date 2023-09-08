def comportamentoIgual(a, b):
    try:
        print(a.index(b))
    except ValueError:
        print(-1)



def main():
    comportamentoIgual('abcde', 'f')


if __name__ == '__main__':
    main()