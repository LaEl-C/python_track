"""Resistor color."""
col= {'black': 0,
'brown': 1,
'red': 2,
'orange': 3,
'yellow': 4,
'green': 5,
'blue': 6,
'violet': 7,
'grey': 8,
'white': 9}
def color_code(color):
    """
    para: string
    return: int
    """
    return col[color]

def colors():
    """
    return: list
    """
    keys=[]
    for key, _ in col.items():
        keys.append(key)
    return keys 
