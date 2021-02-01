roll=int(input('Enter the dice number you would like to roll: '))   # Type of dice.
while roll <= 1:    # While input is 1 or less, the program will loop the roll input.
    print('Please enter an integer higher than 1.')
    roll=int(input('Enter the dice number you would like to roll: '))
else:
    print('Dice input: d', roll)

import random   # Randomizes roll from 1 to x
min = 1
max = roll

mod = int(input('Enter character modifier.'))   # Modifier to the roll (e.g. d20 + 3)
while roll < -4:    # While input is 1 or less, the program will loop the mod input.
    print('Please enter an integer higher than or equal to -4.')
    mod = int(input('Enter character modifier.'))
else:
    print('Modifier: ', mod)

result = random.randint(1,(roll))   # Result calculation.
modres = result + mod   # Original result plus modifier

if result >= 1:
    print('Result:', result)
    print('d%i + %i, ' % (roll, mod), '\nFinal Result:', modres)
else:
    print('Result: 1')