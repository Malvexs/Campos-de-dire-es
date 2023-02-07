import matplotlib.pyplot as plt
import numpy as np
import math

# Define a função de primeira ordem
def f(x, y):
    # Equação da direção do campo
    e = 9.8 - y/5
    return e

# Intervalo de x e y a serem plotados
x_range = [0, 10]
y_range = [40, 60]
# Número de pontos para plotar o campo de direções
num = 20 

# Cria o grid de pontos usando o numpy linspace
x = np.linspace(x_range[0], x_range[1], num)
y = np.linspace(y_range[0], y_range[1], num)
X, Y = np.meshgrid(x, y)

# Define os limites dos eixos x e y
plt.xlim(x_range[0], x_range[1])
plt.ylim(y_range[0], y_range[1])

# Desenha linhas verticais e horizontais
plt.axhline(0, color='black', lw=0.1)
plt.axvline(0, color='black', lw=0.1)

# Plota o campo de direções usando flechas
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        # Calcula o ângulo da direção do campo
        angle = math.atan(f(X[i, j], Y[i, j]))
        # Calcula as componentes x e y da direção do campo 
        u = math.cos(angle) / 4
        v = math.sin(angle) / 4
        # Desenha uma flecha na posição (X[i, j], Y[i, j]) com tamanho (u, v)
        plt.arrow(X[i, j], Y[i, j], u, v, head_width=0, head_length=0, color='blue', lw=0.1)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo de direção')
plt.show()
