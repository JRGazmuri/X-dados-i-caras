
import random

x = int(input("Ingrese cantidad de dados a lanzar\n"))
o = int(input("Ingrese un dado entre los tipos:\ndado de 4, 6, 10, 12, 20: "))
for i in range (x):
    print (random.randrange(1, o, 1))
