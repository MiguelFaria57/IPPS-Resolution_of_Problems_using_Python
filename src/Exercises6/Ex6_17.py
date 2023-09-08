def inverteDic(d):
    dic = {}
    for i, j in d.items():
        if j in dic.keys():
            dic[j] += [i]
        else:
            dic[j] = [i]
    return dic



def main():
    dic = {"joao":10, "pedro":18, "tiago":13, "luis":18}
    print(inverteDic(dic))


if __name__ == '__main__':
    main()