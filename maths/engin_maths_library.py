# Engin Maths Library
from fractions import Fraction
import numpy as np
import maths as math

## binomial expansion

def binomial_series():
    print('GUI: Traditional format: (a+b)^n')
    a = int(input('GUI: What is the a value:\t'))
    b = int(input('GUI: What is the b value:\t'))
    n = int(input('GUI: What is the n value:\t'))
    # calculating n factorial
    def factorial(n):
        f = 1
        for i in range(2, n + 1):
            f *= i
        return f
    factorial_n = factorial(n)

    # display loop series
    for i in range(0, n + 1):
        # for calculating the value of n choose r (nCr)
        factorial_ni = factorial(n - i)
        factorial_i = factorial(i)

        # calculate a and b to the power k
        power_a = pow(a, n - i)
        power_b = pow(b, i)

        # display string
        print((int((factorial_n * power_a * power_b) / (factorial_ni * factorial_i))), 'x^',i)


## integration
def integration():
    variables_array = []
    num_terms = int(input('How many terms will be integrated:'))

    for i in range(num_terms):
        print('Term', i)
        print()
        if input('Is the co-efficient a fraction? <<Y/N>>') == 'Y':
            co_eff = Fraction(int(input('Enter the numerator of the co-efficient:')),
                              int(input('Enter the denominator of the co-efficient:')))
        else:
            co_eff = float(input('[Float] What is the co-efficient of the term <<x.y>>:'))

        if input('Is the power a fraction? <<Y/N>>:') == 'Y':
            power = Fraction(int(input('Enter the numerator of the power:')),
                              int(input('Enter the denominator of the power:')))
        else:
            power = float(input('[Float] What is the power of the term <<x.y>>:'))

        term_data = [co_eff, power]
        variables_array.append(term_data)

    for i in range(len(variables_array)):
        new_coeff = variables_array[i][0] / variables_array[i][1]
        new_pow = variables_array[i][1] + 1
        print('GUI: Term', i, 'is integrated to', new_coeff, 'x ^^', new_pow, ' + c')

if __name__ == '__main__':
    # binomial_series()
    integration()