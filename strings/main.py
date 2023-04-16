# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#part 1
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = f'{scorer_1} {goal_0}, {scorer_2} {goal_1}'
report = f'{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute'

#part 2
player = 'Erwin Koeman'
spatie = player.find(' ')
first_name = player[:spatie]
last_name = player[spatie + 1:]
last_name_len = len(last_name)
name_short = player[:1]+'. '+ last_name
chant = (first_name + '! ') * len(first_name)
chant = chant[:-1]
goodChant = chant[:-1]
space = ' '
good_chant = goodChant != space
print (good_chant)