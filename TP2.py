import matplotlib.pyplot as plt
# on importe les graphiques et la fonction

import numpy as np
import math

def f(x):
    return np.log(x) - 1 # calcul de base avec la commande log pour ln (et log10 pour log decimal)

# Intervalle et pas
x_values = np.arange(1, 6.5, 0.5)  # on s'arrete à 6.5 pour inclure 6 et on fait 0.05 pas (start,stop,step)
y_values = f(x_values) # f est ma fonction defini

# Tracé de la courbe
plt.plot(x_values, y_values, markersize=1)  # Réduire la taille des marqueurs pour un affichage plus clair
plt.title('Courbe de f(x) = ln(x) - 1 avec un pas de 0.5') # affiche le titre
plt.xlabel('x') 
plt.ylabel('f(x)') 
plt.axhline(0, color='red', linestyle='--')  # on utilise ligne 0 pour référence (utile pour la question 3)
plt.grid() # affiche une grille
plt.show()