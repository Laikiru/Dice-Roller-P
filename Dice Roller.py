print('Enter dice number you would like to roll. (6, 8, 20, etc.)')
roll = int(input()) #d10, d20, d2, etc.
print('d ', roll)

while roll <= 1:
    print('Error. Please enter a number higher than 1.')
    break

import random #randomizes roll from 1 to x
min = 1
max = roll

print('Enter character modifier.')
mod = int(input()) # Modifier to the roll (e.g. d20 + 3)
print('shit ', mod)
result = random.randint(1,(roll)) + mod

if result >= 1:
    print('Result:', result)
else:
    print('Result: 1')


############################
