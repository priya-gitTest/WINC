# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order(list_of_films):
    list_of_films.sort()
    return list_of_films

def won_golden_globe(film):
    ggWinners = ['Jaws','Star Wars: Episode IV – A New Hope','E.T. the Extra-Terrestrial','Memoirs of a Geisha']
    ggWinners = [element.lower() for element in ggWinners]
    if film.lower() in ggWinners:
        return True
    else:
        return False
     
print(won_golden_globe('Jaws'))

def remove_toto_albums(dirty_list):
    Joseph_Toto_albums=['Fahrenheit','The Seventh One','Toto XX','Falling in Between','Toto XIV','Old Is New']
    tidy_list = [x for x in dirty_list if x not in Joseph_Toto_albums]
    return tidy_list

print(remove_toto_albums(['aa','Toto XIV','cc']))