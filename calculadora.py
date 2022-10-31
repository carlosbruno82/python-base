#!/usr/bin/env python3

"""Tabuada de multiplicação

Tabuada do numero 1
1
2
3
...
------------------

Tabuado do numero 2
2
6
8
...
"""
__version__ = "1.0.0"
__author__ = "Carlos Bruno"
__license__ = "Unlicense"



numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do número", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("-" * 15)
