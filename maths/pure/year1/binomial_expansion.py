def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# display function
def series(a, b, n):
    # calculating n factorial
    factorial_n = factorial(n)

    # display loop series
    for i in range(0, n + 1):
        # For calculating the value of n choose r (nCr)
        factorial_ni = factorial(n - i)
        factorial_i = factorial(i)

        # calculating the value of a to the power k and b to the power k
        power_a = pow(a, n - i)
        power_b = pow(b, i)

        # display the series
        print((int((factorial_n * power_a * power_b) / (factorial_ni * factorial_i))), 'x^',i)

    # Driver Code

print('Traditional format: (a+b)^n')

a = int(input('What is the a value:\t'))
b = int(input('What is the b value:\t'))
n = int(input('What is the n value:\t'))

series(a, b, n)

