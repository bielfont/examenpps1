import alumnes


def test1():
    assert alumnes.orden2() == "[{'nombre': 'Vicente', 'fecha_nac': '1995-01-04'}, {'nombre': 'Alba', 'fecha_nac': '1996-03-02'}, {'nombre': 'Borja', 'fecha_nac': '1997-09-13'}]"

def test2():
    assert alumnes.orden1() == "[{'nombre': 'Alba', 'fecha_nac': '1996-03-02'}, {'nombre': 'Borja', 'fecha_nac': '1997-09-13'}, {'nombre': 'Vicente', 'fecha_nac': '1995-01-04'}]"
