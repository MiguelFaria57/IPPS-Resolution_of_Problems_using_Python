def calcularDistanciaKm(distanciaAnoLuz):
    anoLuz = 9.459*(10**12)
    distanciaKm = int(anoLuz * distanciaAnoLuz)
    print(distanciaKm)

if __name__ == "__main__":
    calcularDistanciaKm(2.9)