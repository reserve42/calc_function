import matplotlib.pyplot as plt
import numpy as np

# Definindo a função quadrática
def f(x):
    return 2*x**2 + 4*x - 3

# Criando um array de valores de x
x = np.linspace(-7, 3, 400)
y = f(x)

# Determinando o vértice
x_v = -4 / (2 * 2)
y_v = f(x_v)

# Plotando a parábola
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = 2x^2 + 4x - 3', color='b')
plt.scatter([-5, x_v], [f(-5), y_v], color='r')  # Pontos x = -5 e o vértice
plt.text(-5, f(-5), ' (-5, 27)', horizontalalignment='right')
plt.text(x_v, y_v, f' ({x_v:.2f}, {y_v})', horizontalalignment='left')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Gráfico da função quadrática f(x) = 2x^2 + 4x - 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
