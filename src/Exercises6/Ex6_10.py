def alteracoesDicionario(d):
    d["tudo"] = "MF"
    print(d)
    d["python"] = "Guido van Rossum"
    print(d)
    d.pop("xpto")
    #del d["xpto"]
    print(d)
    print(len(d))
    print(d.get("c++"))



def main():
    autor = {"php":"Rasmus Lerdorf","perl":"Larry Wall","tcl":"John Ousterhout",
             "awk":"Brian Kernighan","java":"James Gosling","parrot":"Simon Cozens",
             "python":"GuidovanRossum","xpto":"zxcv"}
    alteracoesDicionario(autor)


if __name__ == '__main__':
    main()