"""Resistor color."""
col= ['black',
'brown',
'red',
'orange',
'yellow',
'green',
'blue',
'violet',
'grey',
'white']
def color_code(color):
    """
    para: string
    return: int
    """
    return col.index(color)

def colors():
    """
    return: list
    """
    return col
