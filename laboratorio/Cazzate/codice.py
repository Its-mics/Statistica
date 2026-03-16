import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse, Circle

# Configurazione della figura e degli assi
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_xlim(-8, 8)
ax.set_ylim(0, 25)
ax.set_aspect('equal')
ax.axis('off')  # Nasconde gli assi

# Parametri e colori
raggio_testicoli = 2.5
raggio_asta = 1.8
base_x = 0
base_y = 3
colore_asta = '#E6C19D'   # Un tono carne/marrone chiaro
colore_glande = '#D0A382'  # Un tono carne leggermente più scuro
colore_testicoli = '#E6C19D' # Stesso colore dell'asta o simile

#--- Inizializzazione degli Elementi Grafici ---

# 1. Testicoli (Circle patches fissi)
testicolo_sx = Circle((base_x - 1.8, base_y), raggio_testicoli, color=colore_testicoli)
testicolo_dx = Circle((base_x + 1.8, base_y), raggio_testicoli, color=colore_testicoli)
ax.add_patch(testicolo_sx)
ax.add_patch(testicolo_dx)

# 2. Asta del pene (linea spessa, il cui punto finale cambierà)
asta, = ax.plot([], [], color=colore_asta, linewidth=60, solid_capstyle='butt') # Usiamo butt per non avere arrotondamenti sulla linea

# 3. Glande (Ellipse patch, che traslerà verso l'alto)
# La larghezza dell'ellisse è leggermente maggiore del diametro dell'asta per l'effetto "cappella"
glande = Ellipse((base_x, base_y + 0.1), width=raggio_asta * 2.2, height=3, color=colore_glande)
ax.add_patch(glande)


def init():
    asta.set_data([], [])
    glande.set_center((base_x, base_y + 0.1)) # Posizione iniziale
    return asta, glande,

def update(frame):
    # Il frame determina la lunghezza corrente (da 0 a 10)
    lunghezza_corrente = frame
    altezza_apice = base_y + lunghezza_corrente

    #--- Aggiornamento Asta ---
    asta_x = [base_x, base_x]
    asta_y = [base_y, altezza_apice]
    asta.set_data(asta_x, asta_y)

    #--- Aggiornamento Glande ---
    # Posizioniamo il centro del glande leggermente sopra l'apice corrente dell'asta
    glande.set_center((base_x, altezza_apice + 1.2))

    return asta, glande,

# Creazione animazione
# frames=np.linspace(0, 15, 80) definisce la lunghezza finale e la fluidità
ani = FuncAnimation(fig, update, frames=np.linspace(0, 15, 80),
                    init_func=init, blit=True)

# Salvataggio in formato GIF
print("Generazione e salvataggio della GIF in corso...")
ani.save('allungamento_anatomico.gif', writer='pillow', fps=20)
print("Fatto. File 'allungamento_anatomico.gif' salvato nella directory corrente.")

plt.show()