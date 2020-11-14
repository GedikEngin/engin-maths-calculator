from sympy import *

def neg_quad(a, b, c):
    temp1 = (b**2)-(4 * a * c)
    temp2 = sqrt(temp1)
    temp3 = (-1 * b) - temp2
    res = temp3 / (2 * a)
    return res

def pos_quad(a, b, c):
    temp1 = (b**2)-(4 * a * c)
    temp2 = sqrt(temp1)
    temp3 = (-1 * b) + temp2
    res = temp3 / (2 * a)
    return res

print('Default quadratic setup:     ax^2 + bx + x')
a = float(input('Enter <a> value:\t'))
b = float(input('Enter <b> value:\t'))
c = float(input('Enter <c> value:\t'))

neg_res = neg_quad(a, b, c)
pos_res = pos_quad(a, b, c)
neg_res = round(neg_res, 4)
pos_res = round(pos_res, 4)

print('x =', neg_res)
print('x =',pos_res)
print(a, 'x^2 +',b , 'x +', c)

