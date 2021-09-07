def convert(degrees_celcius):
    """
    takes the temperature in degrees celcius as input. returns the degrees in Fahrenheit.
    """
    return degrees_celcius * 1.8 + 32

print(convert(25))
def table():
    """
    prints a table that shows -30 degrees through 40 degrees and their fahrenheit counterparts.
    """
    table = ('     F      C   ')
    for C in [x for x in range(-30, 41, 10)]:
        table += ('\n{:7}{:7}'.format(convert(C), C))
    return table

print(table())