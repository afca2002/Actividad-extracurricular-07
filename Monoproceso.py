import os
import sys


def example_function(a, b):
    print("El valor de a es:", a, "y el valor de b es:", b)
    if a > b:
        print("a es mayor que b")
    else:
        print("b es mayor o igual a a")
    for i in range(0, 5):
        print(i, end=" ")
    print()


example_function(5, 3)
example_function(2, 8)
