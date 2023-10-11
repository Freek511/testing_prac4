#  you functions here
import math


def simpson_integration(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(x[i]) for i in range(n + 1)]
    s = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2])
    return h * s / 3