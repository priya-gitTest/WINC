# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_scorer1 = 'Ruud Gullit'
goal_0 = 32
goal_scorer2 = 'Marco van Basten'
goal_1 = 54
scorers = goal_scorer1 +' '+ str(goal_0) +', ' + goal_scorer2+' '+ str(goal_1)


report = f'{goal_scorer1} scored in the {goal_0}nd minute\n{goal_scorer2} scored in the {goal_1}th minute'
print(report)

player ='Berry van Aerle'
first_name = player[0: player.find(' ')]
print(first_name)
last_name  = player[player.find(' ')+1:]
print(last_name)
last_name_len = len(player[player.find(' ')+1:])
print(last_name_len)
name_short = first_name[0]+'. '+last_name
print(name_short)
chant = ((first_name + '! ' )* len(first_name)).rstrip()
print(chant)
good_chant = chant[-1] !=' '
print(good_chant)

