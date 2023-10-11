# our main here
from functions import *

def since_calc():
    print('Welcome to Since Calculator by Matveev, Gribchenko, Merenkov\n'
          'You can do:\n1) Solving equation\n2) Solving integrals\n3) Solving matrix problems')
    sw = input('Please enter a number from 1 to 3 to continue: ')

    if int(sw) == 1:
        power = input('Enter a power of the equation: ')
        coeffs = []
        equation = ''

        for i in range(int(power) + 1):
            coef = input("Enter coefficient a{0}: ".format(i))
            coeffs.append(int(coef))
            equation = create_string_equation(equation, coef, i)

        print("Your equation is: " + equation + " = 0")
        if power == 1 or power == 2:
            ans = equation_solver(coeffs, power)
        else:
            a = float(input("Set left end: "))
            b = float(input("Set right end: "))
            eps = float(input("Set precise: "))
            ans = equation_solver(coeffs, power, a, b, eps)
        print("Your answer is:" + str(ans))



    elif sw == 2:
        ...
    elif sw == 3:
        ...
    else:
        ...


since_calc()
