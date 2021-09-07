s_bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}

s_groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

overeenkomst = s_bruin.intersection(s_groen)

verschil = s_bruin.difference(s_groen)

totaal = s_bruin.union(s_groen)

print(overeenkomst, verschil, totaal)