
from datetime import datetime


def orden1(lista):
    lista.sort(key=lambda x: x['nombre'])
    # print("Ordenado por fecha nombre", str(lista))
    return str(lista)


def orden2(lista):
    lista.sort(key=lambda x: x['fecha_nac'])
    # print("Ordenado por fecha nacimiento", str(lista))
    #def naix(element):
    #  return datetime.strptime(element['fecha_nac','%y-%m-%d'])
    #  lista.sort(key=naix)
    return str(lista)





