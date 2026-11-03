import numpy as np
import math

def somma_naturali( n ):
    somma = 0
    prodotto = 1
    i = 1
    while i <=n:
        somma = somma+(i-1)
        prodotto = prodotto*i
        i = i+1
    return somma, prodotto

def somma_radici(n):
    somma=0
    i=0
    while i<=n:
        somma = somma + math.sqrt(i)
        i = i+1
    return somma

def somma_potenza( n, alfa=1):
    somma = 0
    i = 0
    while i <=n:
        somma = somma + (i**(alfa))
        i = i+1
    return somma



    