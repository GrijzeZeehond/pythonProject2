def lang_genoeg(lengte_gebruiker):
    """
    takes the height of the user as input(lengte_gebruiker). returns if the user can ride the attraction.
    """
    if int(lengte_gebruiker) >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'

print(lang_genoeg(120))