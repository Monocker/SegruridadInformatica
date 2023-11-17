import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define los límites
theta = np.linspace(0, 2*np.pi, 100)
z = np.linspace(-5, 4, 100)
Theta, Z = np.meshgrid(theta, z)
R = 4  # El radio del cilindro
X = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Crear la figura y el eje
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibuja el cilindro
ax.plot_surface(X, Y, Z, color='blue', alpha=0.3)

# Dibuja las tapas del cilindro
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(16 - X**2 - Y**2)
Z[Z > 0] = np.nan  # Solo nos interesan los valores reales para el círculo
ax.plot_surface(X, Y, -5*np.ones_like(Z), color='green', alpha=0.3)  # Tapa inferior
ax.plot_surface(X, Y, 4*np.ones_like(Z), color='red', alpha=0.3)     # Tapa superior

# Configurar límites y etiquetas
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-6, 5])
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Mostrar la gráfica
plt.show()
