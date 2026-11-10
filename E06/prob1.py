import numpy as np
import scipy 
import matplotlib.pyplot as plt
import random
import random
import numpy as np
import matplotlib.pyplot as plt

def prob(x):

    return (3 / 1000) * (x ** 2)
  

def hit_or_miss(estrazioni=1):
    x_val = np.random.uniform(0, 10, estrazioni)
    y_val = np.random.uniform(0, 0.3, estrazioni)
    mask = y_val < prob(x_val)

    return x_val[mask]

valori = hit_or_miss(9000)

plt.figure(figsize=(8, 5))
plt.hist(valori, bins=30, density= True, color='red', label='Campioni Hit-or-Miss')
plt.title('Metodo Hit-or-Miss')
plt.xlabel('x')
plt.ylabel('Densità di probabilità')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
plt.show()

def cumulativa(n=1):
    z = np.random.uniform(0, 1, n)
    x = (1000*z)**(1/3)
    return x


estratti = cumulativa(9000)
plt.figure()
plt.hist(estratti, bins=30, color='orange', label='Campioni con la Cumulativa')
plt.show()
