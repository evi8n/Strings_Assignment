# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = f'{scorer_1} {goal_0}, {scorer_2} {goal_1}'
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'
player = 'Erwin Koeman'
first_name1 = player.find('Erwin')
first_name = player[:5]
last_name1 = player.find('Koeman')
last_name = player[6:12]
last_name_len = len(last_name)
name_short = player[:1]+'. '+ player[6:12]
chant = 'Erwin! Erwin! Erwin! Erwin! Erwin!'
space = ' '
good_chant = chant[5]!= space
print(chant)