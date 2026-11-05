"""Resistor color Duo."""
col = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def value(colors):
    """
    para: str
    return: int
    """
    first_col = colors[0]
    second_col = colors[1]
    return col.index(colors[0])*10 + col.index(colors[1])
