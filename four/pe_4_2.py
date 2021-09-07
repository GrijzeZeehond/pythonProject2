# asks user their age and if they possess a dutch passport
age = input('Hoe oud bent u?: ')
paspoort_stat = input('Heeft u een Nederlands paspoort? (Ja/Nee): ')

# prints if the user can vote
if int(age) > 17 and paspoort_stat.capitalize() == 'Ja':
    print('Gefeliciteerd, u mag stemmen!')
else:
    print('Helaas, u kunt niet stemmen.')
    if paspoort_stat.capitalize() != 'Ja':
        print('Omdat u niet in het bezit bent van een nederlands paspoort kunt u niet stemmen. Bezoek\nhttps://ind.nl/'
              'Nederlanderschap/naturalisatie/Paginas/Naturalisatie.aspx om de nederlandse\nnationaliteit aan te vragen'
              ' of vraag informatie aan bij een lokaal gemeentebureau.')
    else:
        print('U bent nog niet oud genoeg.')