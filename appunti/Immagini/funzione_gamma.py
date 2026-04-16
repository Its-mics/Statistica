import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Impostazioni stile per allinearsi al font di LaTeX (Serif)
plt.rcParams.update({
    # "text.usetex": True, # De-commenta sul tuo PC per usare il motore LaTeX reale per i font
    "font.family": "serif",
    "axes.labelsize": 12,
    "font.size": 12,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
})

# Creazione dell'asse x
x = np.linspace(0, 15, 1000)

# Parametri da variare (forma alpha, tenendo la scala beta = 1)
alpha_values = [0.5, 1, 2, 5, 9]
beta_val = 1.0

# Creazione della figura
plt.figure(figsize=(8, 5))

# Loop per graficare le diverse forme della Gamma
for alpha_val in alpha_values:
    # Nota tecnica: in scipy.stats.gamma, 'a' è il parametro di forma (alpha)
    # Il parametro 'scale' di scipy corrisponde in realtà a (1/beta).
    # Poiché nel nostro esempio beta = 1.0, anche scale = 1.0. 
    # Se volessi beta = 2.0, dovresti passare scale = 1/2.0
    y = gamma.pdf(x, a=alpha_val, scale=1/beta_val)
    plt.plot(x, y, lw=2, label=f'$\\alpha={alpha_val}, \\beta={beta_val}$')

# Dettagli del grafico con sintassi LaTeX
plt.title('Distribuzione Gamma al variare del parametro di forma $\\alpha$')
plt.xlabel('$x$')
plt.ylabel('Densità di Probabilità $f(x)$')
plt.ylim(0, 0.6)
plt.xlim(0, 15)
plt.legend()
plt.grid(True, alpha=0.3)

# Salvataggio dell'immagine ad alta risoluzione (300 dpi) senza margini bianchi
plt.savefig('gamma_shapes_alpha_beta.png', dpi=300, bbox_inches='tight')
plt.show()