import math

def converteCoordenadas(cor_x, cor_y):
    r = math.sqrt(cor_x**2 + cor_y**2)
    t = math.degrees(math.atan(cor_y/cor_x))
    return r, t


def main():
    x = int(input("Indique o valor x: "))
    y = int(input("Indique o valor y: "))
    print("Coordenadas Cartesianas: (%d, %d)\nCoordenadas polares: (%d, %.2f)"
          %(x, y, converteCoordenadas(x, y)[0], converteCoordenadas(x, y)[1]))



if __name__ == "__main__":
    main()