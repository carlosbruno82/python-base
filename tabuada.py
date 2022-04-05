#! /usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

Tabuada do 1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
...
-------------

Tabuada do 2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
...
-------------
"""

__version__ = "0.1.1"
__autor__ = "Carlos Bruno"

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

for n1 in numeros:
    print()
    print("{:-^20}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^20}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("#" * 20)
    #print("{:#^20}".format(f""))
   
