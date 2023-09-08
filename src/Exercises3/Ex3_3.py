import math


def compEscada(alt, ang):
    ang = (math.pi/180)*ang
    return alt/math.sin(ang)



def main():
    alt = int(input("Indique a altura: "))
    ang = int(input("Indique o ângulo: "))
    print("O comprimento da escada será %.2f u.m." %(compEscada(alt, ang)))


if __name__ == '__main__':
    main()