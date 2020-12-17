import math
from fractions import Fraction


print('Projectiles')
print('Select Question Type:')
print('Time it takes for object to hit the ground <0>')
print('The height of the object at a given time in relation to launch height <1>')
print('The time it takes to reach the highest point <2>')
print('The highest point in relation to projection <3>')
print('The horizontal distance travelled until object is the same height as'
      'the starting height <4>')
choice = int(input('What type of question <<0, 1, 2, 3, 4>>'))

if choice == 2:
    if input('Is u a fraction? <Y/N>') == 'Y':
        u = Fraction(int(input('Enter the numerator:')),
                          int(input('Enter the denominator:')))
    else:
        u = float(input('What is u'))

    if input('Is the angle of projection a fraction? <Y/N>') == 'Y':
        angle = Fraction(int(input('Enter the numerator:')),
                          int(input('Enter the denominator:')))
    else:
        angle = float(input('What is the angle of projection?:'))

