from fractions import Fraction

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
    print('Term', i, 'is integrated to', new_coeff, 'x ^^', new_pow, ' + c')