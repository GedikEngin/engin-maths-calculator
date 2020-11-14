from sympy import *
import numpy as np

def rad_deg():
    answer = float(input('What radian would you like to convert to degrees'))
    print(np.rad2deg(answer))

def deg_rad():
    answer = float(input('What degree would you like to convert to radian'))
    print(np.deg2rad(answer))

def area_shape():
    print('area_shape')

def perimeter_shape():
    print('perimeter_shape')

def find_val():
    print('find_val')

def find_angle():
    print('find_angle')

op_categories = ['conversion', 'shape', 'finding']
conversion_ops = ['Convert radians into degrees','Convert degrees into radians']
shape_ops = ['Finding the area of a shape', 'Finding the perimeter of shape']
finding_ops = ['Finding a missing value', 'Finding the angle']

# getting pi
pi_length = int(input('How many significant figures should pi be taken to <<0 will default to 16>>\t'))


if pi_length == 0:
    pi = pi.evalf(16)
else:
    pi = pi.evalf(pi_length)


print(op_categories)
type0 = input('What do you want to do?:')


if type0 == 'shape':
    for i in range(len(shape_ops)):
        print(shape_ops[i], '[', i, ']')
    type1 = int(input('What do you want to do?:'))
    if type1 == 0:
        area_shape()
    if type1 == 1:
        perimeter_shape()


if type0 == 'conversion':
    for i in range(len(conversion_ops)):
        print(conversion_ops[i], '[', i, ']')
    type1 = int(input('What do you want to do?:'))
    if type1 == 0:
        rad_deg()
    if type1 == 1:
        deg_rad()

if type0 == 'finding':
    for i in range(len(finding_ops)):
        print(finding_ops[i], '[', i, ']')
    type1 = int(input('What do you want to do?:'))
    if type1 == 0:
        find_val()
    if type1 == 1:
        find_angle()

