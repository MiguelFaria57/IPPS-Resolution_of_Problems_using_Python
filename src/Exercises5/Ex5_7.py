def palavrasAmigas(p1, p2):
    aux = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            aux += 1
    p = aux/len(p1)
    if p<0.1:
        print("As palavras são amigas.")
    else:
        print("As palavras não são amigas.")


def main():
    palavrasAmigas("abcdefghijk", "abcdefghijz")


if __name__ == "__main__":
    main()