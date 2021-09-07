#1.3 statements
#exc 1
a = 6
b = 7
print(a, b)

#exc 2
c = (a + b) / 2
print(c)

#exc 3
voornaam = 'Susan'
tussenvoegsel = ''
achternaam = 'Bruggeling'
print(voornaam, tussenvoegsel, achternaam)

#exc 4
if tussenvoegsel:
    mijnnaam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam
else:
    mijnnaam = voornaam + ' ' + achternaam
print(mijnnaam)

#1.4 boolean expression
#exc 1
print(a > b)

#exc 2
print(len(mijnnaam) == len(voornaam) + len(tussenvoegsel) + len(achternaam))

#exc 3
print(len(mijnnaam) >= c * 5)

#exc 4
print(tussenvoegsel in achternaam)