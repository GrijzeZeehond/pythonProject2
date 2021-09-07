cijferPROJA = 7
cijferPROG = 8
cijferMOD = 7

total = cijferPROJA + cijferPROG + cijferMOD

gemiddelde = total / 3

beloning = '€' + str(total * 30) + '.00'

overzicht = 'Mijn cijfers (gemiddeld een {:1.1f}) leveren een beloning van {} op!'.format(gemiddelde, beloning)

print(overzicht)