
def poly_integration(poly_text):
    poly_text = poly_text.replace('-', '+ -')
    terms = poly_text.split('+')
    result = []
    for term in terms:
        pow_split = term.split('^')
        if len(pow_split) == 2:
            power = pow_split[1]
        else:
            power = '0'

        coef_split = term.split('*')
        if len(coef_split) == 2:
            coef = coef_split[0]
        else:
            coef = '1'

        new_power = power + '-1'
        new_coef = power + '*' + coef
         # todo sort out appearence and use fraction library

        int_term = new_coef + '*x^'  + new_power
        result.append(int_term)

    result = '+'.join(result)

    return result






if __name__ == '__main__':

    res = poly_integration('2*x^2 - 1/4*x^1/3 - 2')
    print(res)
