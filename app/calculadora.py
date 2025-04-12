# app/calculadora.py
"""A collection of basic arithmetic functions"""
def sumar(a, b):
    """returns the sum of two numbers"""
    return a + b


def restar(a, b):
    """returns the difference between two numbers"""
    return a - b


def multiplicar(a, b):
    """returns the product of two numbers"""
    return a * b


def dividir(a, b):
    """divides the first number by the second number"""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
