import math

def volumeCone(raioBase, altura):
    return (math.pi*(raioBase**2)*altura)/3


def main():
    r = float(input("Indique o raio da base do cone: "))
    h = float(input("Indique a altura do cone: "))
    print("A área do cone é %.2f u.m." %(volumeCone(r, h)))



if __name__ == "__main__":
    main()