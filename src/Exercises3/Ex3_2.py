import math


def areaTriangulo(a, b, c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    

def main():
    a = int(input("Indique o lado a do triângulo: "))
    b = int(input("Indique o lado b do triângulo: "))
    c = int(input("Indique o lado c do triângulo: "))
    if a or b or c <=0:
        print("Erro - valores dos lados do triângulo estão incorretos.")
    else:
        print("A área do triângulo é %.2f u.a." %(areaTriangulo(a, b, c)))


if __name__ == '__main__':
    main()