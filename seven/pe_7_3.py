studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def mean(list):
    """
    Takes a list of numbers as input and returns the mean average of them.
    """
    total = 0

    for item in list:
        total += item

    return total / len(list)


def gemiddelde_per_student(studentencijfers):
    """
    Neemt een tweedimentionale lijst als invoer. berekent het gemiddelde per kind-lijst en returnt een lijst met de
    gemiddeldes.
    """
    gemiddeldes = []
    for cijferlijst in studentencijfers:
        gemiddeldes.append(mean(cijferlijst))
    return gemiddeldes

def gemiddelde_van_alle_studenten(studentencijfers):
    """
    Neemt een tweedimentionale lijst als invoer. Berekent het gemiddelde per kindlijst. Berekent en retoeneert het
    gemiddelde van de moederlijst.
    """
    return mean(gemiddelde_per_student(studentencijfers))

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))