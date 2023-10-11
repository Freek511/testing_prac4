#  you functions here
import math


# def create_string_equation(s, coef, step):
#     if step == 0:
#         s += coef
#     elif step == 1:
#         if int(coef) > 0:
#             s = s + "+" + coef + "*x"
#         else:
#             s = s + coef + "*x"
#     else:
#         if int(coef) > 0:
#             s = s + "+" + coef + "*x**" + str(step)
#         else:
#             s = s + coef + "*x**" + str(step)
#
#     return s

def calc_func(coeffs, x):
    ans = coeffs[0]
    for i in range(1, len(coeffs)):
        ans += coeffs[i] * x ** i

    return ans


def equation_solver(coeffs, power, a=1.7e+308, b=2.2e-308, eps=2.2e-16):
    if power == 1:
        if coeffs[1] != 0 and coeffs[0] != 0:
            return -coeffs[0]/coeffs[1]
        elif coeffs[1] == 0 and coeffs[0] == 0:
            return 'Any number'
        else:
            return 'No answers'
    elif power == 2:
        D = coeffs[1]**2 - 4 * coeffs[0]*coeffs[2]
        if D < 0:
            return 'No answers'
        elif D == 0:
            return -coeffs[1]/(2*coeffs[2])
        else:
            x1 = (-coeffs[1] + math.sqrt(D))/(2*coeffs[2])
            x2 = (-coeffs[1] - math.sqrt(D)) / (2 * coeffs[2])
            return x1, x2
    else:
        while math.fabs(b - a) > eps:
            a = a - (b - a) * calc_func(coeffs, a) / (calc_func(coeffs, b) - calc_func(coeffs, a))
            b = b - (a - b) * calc_func(coeffs, b) / (calc_func(coeffs, a) - calc_func(coeffs, b))
        return b


def create_string_equation(s, coef, step):
    if step == 0:
        s += coef
    elif step == 1:
        if int(coef) > 0:
            s = s + "+" + coef + "*x"
        else:
            s = s + coef + "*x"
    else:
        if int(coef) > 0:
            s = s + "+" + coef + "*x**" + str(step)
        else:
            s = s + coef + "*x**" + str(step)

    return s


def simpson_integration(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(x[i]) for i in range(n + 1)]
    s = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2])
    return h * s / 3


def numerical_diff(f, x, h=1e-6):
    """
    Вычисляет численную производную функции f в точке x с шагом h.
    """
    return (f(x + h) - f(x - h)) / (2 * h)