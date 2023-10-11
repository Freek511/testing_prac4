import math

def numerical_diff(f, x, h=1e-6):
    """
    Вычисляет численную производную функции f в точке x с шагом h.
    """
    return (f(x + h) - f(x - h)) / (2 * h)