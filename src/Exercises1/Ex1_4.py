def calcularSegundos(dias):
    segundosDia = 60*60*24
    segundosPretendidos = segundosDia * dias
    print(segundosPretendidos)

if __name__ == "__main__":
    calcularSegundos(365)