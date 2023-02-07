import matplotlib.pyplot as plt
import math

# Defina a equação de primeira ordem
def f(x, y):
    e = 9.8 - y/5 
    return e

#range com valores de x e y a serem calculados
x_range = [0, 10]
y_range = [40, 60]

plt.xlim(x_range[0], x_range[1])
plt.ylim(y_range[0], y_range[1])

plt.axhline(0, color='black', lw=0.1)
plt.axvline(0, color='black', lw=0.1)

# Plota o campo de direções usando flechas
for i in range(x_range[1]):
    for j in range(y_range[1]):
        x = x_range[0] + i
        y = y_range[0] + j
        angle = math.atan(f(x, y))
        u = math.cos(angle) / 2
        v = math.sin(angle) / 2
        plt.arrow(x, y, u, v, head_width=0.2, head_length=0.2, color='blue', lw=0.3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo de direção')
plt.show()
