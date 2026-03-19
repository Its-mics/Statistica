import matplotlib.pyplot as plt
import numpy as np

# 1. Definisco la formula della campana
def f(x, m, s):
    return (1.0/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

# 2. Imposto i valori
m = 0; s_start = 2; s_stop = 0.2
s_values = np.linspace(s_start, s_stop, 30)
x = np.linspace(m - 3*s_start, m + 3*s_start, 1000)

# 3. PREPARO IL GRAFICO (Il pezzo che mancava)
fig, ax = plt.subplots()
y_iniziale = f(x, m, s_start)
lines = ax.plot(x, y_iniziale) # Disegno la prima curva
ax.set_ylim(0, 2.5) # Fisso l'altezza massima del grafico per vedere bene l'animazione

# 4. FACCIO PARTIRE L'ANIMAZIONE
for s in s_values:
    y = f(x, m, s)           # Calcolo la nuova curva
    lines[0].set_ydata(y)    # Aggiorno il disegno
    plt.draw()               # Ridisegno
    plt.pause(0.1)           # Aspetto un decimo di secondo

plt.show() # Mantengo la finestra aperta alla fine dell'animazione
