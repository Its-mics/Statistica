import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

# Parametri iniziali
N = 1000
n_bins = 10

# Generazione dati e istogramma
dati = np.random.uniform(0, 1, N)

plt.figure(figsize=(10, 6))
conteggi, bordi, _ = plt.hist(dati, bins=n_bins, range=(0, 1), color='skyblue', alpha=0.6, label='Dati', edgecolor='black')

# Calcoli 
p = 1 / n_bins
mu = N * p
sigma = np.sqrt(N * p * (1 - p))

print(f"Probabilità p: {p}")
print(f"Valore atteso (mu): {mu}")
print(f"Deviazione std (sigma): {sigma:.2f}")

# Linea del valore atteso
plt.axhline(mu, color='red', linestyle='--', label='Valore atteso')
plt.legend()
plt.show()