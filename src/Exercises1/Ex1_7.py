def areaTriangulo(compLado, distVertice):
    return (compLado*distVertice)/2


def main():
    compLado = float(input("Indique comprimento de um dos lados: "))
    distVertice = float(input("Indique a distância ao vértice oposto medida perpendicularmente: "))
    print("A área do triângulo é", areaTriangulo(compLado,distVertice), "u.m.")


if __name__ == "__main__":
    main()
