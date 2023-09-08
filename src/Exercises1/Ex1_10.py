def converterTemperatura(temperatura):
    return (9/5)*temperatura+32


def main():
    temp = float(input("Indique a temperatura: "))
    print("%.2f graus Celsius são %.2f Fahrenheit." %(temp, converterTemperatura(temp)))



if __name__ == "__main__":
    main()