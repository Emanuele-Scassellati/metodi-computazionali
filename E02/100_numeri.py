#sommare i primi 100 numeri interi
import numpy as np

i = 0
somma = 0
n = input('Immetti un numero intero')
while i <= float(n):
	somma = somma + i
	i = i+1
print(somma)

if somma == (float(n))*(float(n)+1)*0.5:
	print("sei un grande")
	