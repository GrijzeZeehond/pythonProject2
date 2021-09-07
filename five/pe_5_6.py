def wijzig(letterlijst):
    """
    Takes a list as input. Empties the list and fills it with the following elements: 'd', 'e', 'f'
    """
    while letterlijst:
        letterlijst.pop()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)

# Als je de functie de opdracht (letter)lijst = ['d', 'e', 'f'] geeft. veranderd de value vanm lijst binnen het
# construct van de functie, maar niet globaal. Om de lijst globaal te veranderen moet je hem globaal een nieuwe
# waarde geven of de waardes in een functie via list-functies veranderen.

# Mijn functie werkt niet met een string parameter. Dit komt omdat de functie pop op de parameter wordt toegepast, maar
# dit kan niet op een string. Daarom krijg je een attributeError.

# mutabilititeit speelt een rol bij deze vraag. Ik kan deze lijst alleen veranderen omdat hij mutabil is.