lista = [{'nombre': 'Alba', 'fecha_nac': '1996-03-02'},
         {'nombre': 'Vicente', 'fecha_nac': '1995-01-04'},
         {'nombre': 'Borja', 'fecha_nac': '1997-09-13'}]


def orden1():
    lista.sort(key=lambda x: x['nombre'])
    # print("Ordenado por fecha nombre", str(lista))
    return str(lista)


def orden2():
    lista.sort(key=lambda x: x['fecha_nac'])
    # print("Ordenado por fecha nacimiento", str(lista))
    return str(lista)


def orden3():
    return "1"



