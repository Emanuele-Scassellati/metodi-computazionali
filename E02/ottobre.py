import numpy as np

giorni = ['giovedì', ' venerdì', 'sabato', 'domenica', 'lunedì', 'martedì', 'mercoledì']*4 + ['giovedì', 'venerdì', 'sabato']

numeri = []
i = 1
while i < 32:
	numeri.append(i)
	i = i+1
#print(numeri)

k = 1
ottobre = {}
while k < 32:
	ottobre[k-1] = { numeri[k-1] : giorni[k-1] }
	k = k+1
print(ottobre)

	