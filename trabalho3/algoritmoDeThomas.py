# Versão utilizando linalg do numpy

# Diferenças finitas e algoritmo de thomas usando PVC
import numpy as np
import matplotlib.pyplot as plt
# primeiro precisamos definir as funções que acompanham os valores

# acompanha y'
def p(x):
    return x/3

# acompanha y
def q(x):
    return -1

# acompanha os termos sem y
def r(x):
    return 6*x - 1

# vai receber as condições de contorno
def diferencasFinitas(x0, y0, xf, yf, N):
    # variáveis iniciais
    delta_X = (xf - x0) / N
    vetor_X = np.linspace(x0 + delta_X, xf - delta_X, N - 1)
    dim_sistema = N - 1
    A = np.zeros((dim_sistema, dim_sistema))
    B =  np.zeros(dim_sistema)

    # montagem da matriz A
    for i in range(dim_sistema):
        x = vetor_X[i]
        for j in range(dim_sistema):
            if i == j:
                A[i][j] = 2 + q(x) * pow(delta_X, 2)
            elif i == (j+1):
                A[i][j] = -1 - p(x)*delta_X/2
            elif i == (j-1):
                A[i][j] = -1 + p(x)*delta_X/2
            else:
                A[i][j] = 0

    # montagem do vetor B

    for i in range(dim_sistema):
        x = vetor_X[i]
        if i == 0:
            B[i] = (1 + p(x) * delta_X/2) * y0 - r(x) * pow(delta_X, 2)
        elif i == (dim_sistema - 1):
            B[i] = (1 - p(x) * delta_X/2) * yf - r(x) * pow(delta_X, 2)
        else:
            B[i] = -r(x) * pow(delta_X, 2)

    # Resolução do sistema linear Ay = b

    y = np.linalg.solve(A, B)
    return y


def calcular_coeficientes(x, delta_X, p, q, r):
    a = p(x) * delta_X / 2
    b = 2 + q(x) * pow(delta_X, 2)
    c = -1 + p(x) * delta_X / 2
    d = -r(x) * pow(delta_X, 2)
    return a, b, c, d


def plotar_grafico(x, y):
    plt.plot(x, y, marker='o', color ="red" )
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y em função de x')
    plt.grid(True)
    plt.show()

# Vetor de valores de x
vetor_X = np.linspace(0 + 1/8, 1 - 1/8, 7)

# Calcula os valores de y utilizando diferencasFinitas
y = diferencasFinitas(0, -1, 1, 0, 8)

print("Utilizando linalg solve numpy")
for i in range(len(y)):
    print(f"y({vetor_X[i]}) = {y[i]}")

# Plota o gráfico
plotar_grafico(vetor_X, y)
