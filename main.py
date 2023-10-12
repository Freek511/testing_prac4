# our main here
from functions import *


def since_calc():
    print('Welcome to Since Calculator by Matveev, Gribchenko, Merenkov\n'
          'You can do:\n1) Solving equation\n2) Solving integrals and derivating\n3) Solving matrix problems')
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

    elif int(sw) == 2:
        choise = input('Enter a number from 1 to solve integral 2 to derivate: ')
        if choise == 1:
            func = input("Enter a function: ")
            f = lambda x: eval(func)
            a = int(input("Enter left end: "))
            b = int(input("Enter right end: "))
            n = int(input("Enter n: "))
            print(f"Your answer is: {simpson_integration(f, a, b, n)}")
        elif choise == 2:
            func = input("Enter a function: ")
            f = lambda x: eval(func)
            x = int(input("Enter x: "))
            h = int(input("Enter h: "))
            numerical_diff(f, x, h)
        else:
            print("Incorrect input")
    elif int(sw) == 3:
        choice = int(input('1) Multiply matrices\n2) Transpose matrix\n'
                       'Please enter a number from 1 to 2 to continue: '))
        if choice == 1:
            m1 = eval(input("Enter matrix m1 (example: [[1, 2], [3, 4]]):\n"))
            m2 = eval(input("Enter matrix m2 (example: [[1, 2], [3, 4]]):\n"))
            try:
                print("Result of multiplication of matrices is\n", multiply_matrices(m1, m2))
            except AssertionError as e:
                print("Incorrect input")
        elif choice == 2:
            m = eval(input("Enter matrix (example: [[1, 2], [3, 4]]):\n"))
            try:
                print("Transposed matrix\n", transpose_matrix(m))
            except AssertionError as e:
                print("Incorrect input")
        else:
            print("Incorrect input")
    else:
        exit(1)


since_calc()
