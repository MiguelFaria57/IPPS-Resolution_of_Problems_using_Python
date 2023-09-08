def conversorDatas(dicDS, dicMA, data):
    aux = data.split("/")
    print("%s, %s de %s de %s" %(dicDS[int(aux[0])], aux[1], dicMA[int(aux[2])], aux[3]))
    return "%s, %s de %s de %s" %(dicDS[int(aux[0])], aux[1], dicMA[int(aux[2])], aux[3])



def main():
    diasSemana = {1:"Domingo", 2:"Segunda-Feira", 3:"Terça-feira", 4:"Quarta-Feira",
                   5:"Quinta-Feira", 6:"Sexta-Feira", 7:"Sábado"}
    mesesAno = {1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho",
                8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}
    conversorDatas(diasSemana, mesesAno, "4/5/6/2006")

if __name__ == '__main__':
    main()