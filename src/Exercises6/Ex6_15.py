def calculoIMC(d):
    for i in d.values():
        i["IMC"] = round(i["peso"]/(i["altura"]**2),2)



def main():
    dic = {123456789:{"altura":1.83,"peso":63.0}, 987654321:{"altura":1.75, "peso":60}}
    calculoIMC(dic)
    print(dic)


if __name__ == '__main__':
    main()