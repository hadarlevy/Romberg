# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sympy as sp
import math
from sympy.utilities.lambdify import lambdify
x = sp.symbols('x')




def Trapezoidal(f, n, a, b, tf):
    h = (b - a) / n
    if tf:
        print("Error evaluation En = ", round(TrapezError(func(), b, a, h), 6))
    integral = 0.5 * (f(a)*f(b))
    for i in range(n):
        integral += f(a+h*i)
    integral *= h
    return integral


def RombergsMethod(f, n, a, b):

    matrix = [[0 for i in range(n)] for j in range(n)]
    for k in range(0, n):
        matrix[k][0] = Trapezoidal(f, 2**k, a, b, False)
        for j in range(0, k):
            matrix[k][j + 1] = (4 ** (j + 1) * matrix[k][j] - matrix[k - 1][j]) / (4 ** (j + 1) - 1)
            print("R[{0}][{1}] = ".format(k, j+1), round(matrix[k][j+1], 6))
    return matrix


def func():
    return sp.sin(x)


def f(val):
    return lambdify(x, func())(val)


def TrapezError(func, b, a, h):

    xsi = (-1)*(math.pi/2)
    print("ƒ(x): ", func)
    f2 = sp.diff(func, x, 2)
    print("ƒ'': ", f2)
    diff_2 = lambdify(x, f2)
    print("ƒ''(", xsi, ") =", diff_2(xsi))
    return h**2/12*(b-a)*diff_2(xsi)


def Main():

    n = 4
    print("Division into sections n =", n)
    print("Numerical Integration of definite integral in range [0,𝛑] ∫= SIN(X)")
    print("I = ", round(RombergsMethod(f, n, 0, math.pi)[n-1][n-1], 6))


Main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
