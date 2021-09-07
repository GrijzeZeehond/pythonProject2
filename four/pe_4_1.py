score  = input('Give score recieved in multiplechoice test: ')

if int(score) > 15:
    print('Gefeliciteerd!')
    print('Met een score van', score, 'ben je geslaagd!')
# else:
#     print('Helaas!')
#     print('Met een score van', score, 'ben je niet geslaagd.')

# Als je het printstatement direct onder het ifstatement zet zonder indent wordt deze tekst altijd geprint, ook wanneer
# het if-statement False is. Als je de tekst volgt met een else statement en je het tweede printstatement niet
# indenteert, komt er een error omdat het eerdere deel van de else statement er niet direct voor wordt gevonden door de
# interperter. (er zit een los statement tussen de if en else)