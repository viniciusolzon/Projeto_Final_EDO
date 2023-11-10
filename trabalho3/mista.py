import numpy as np
import matplotlib.pyplot as plt

def thomas_algorithm(a, b, c, d):
    n = len(d)
    c_ = np.zeros(n)
    d_ = np.zeros(n)
    x = np.zeros(n)
    c_[0] = c[0] / a[0]
    d_[0] = d[0] / a[0]
    for i in range(1, n):
        c_[i] = c[i] / (a[i] - b[i] * c_[i-1])
        d_[i] = (d[i] - b[i] * d_[i-1]) / (a[i] - b[i] * c_[i-1])

    x[n-1] = d_[n-1]
    for i in range(n-2, -1, -1):
        x[i] = d_[i] - c_[i] * x[i+1]

    return x

y0 = 0
yf = 0
x0 = 0
xf = 1

def p(x): # Coeficiente que multiplica y'
    return 0

def q(x): # Coeficiente que multiplica y
    return -1

def r(x): # Coeficiente que não acompanha y
    return x

def diferenca_finita_mista(x0, y0, xf, yf):
    h = 0.25 # passo h
    n = int((xf-x0)/h)

    vetor_x = np.linspace(x0 + h, xf - h, n-1) # Número de pontos
    dim = n - 1 # Dimensão da matriz

    A = np.zeros((dim, dim))
    d = np.zeros(dim)

    for i in range(dim):
        x = vetor_x[i]
        for j in range(dim):
            if i == j:
                A[i][j] = 2 + q(x)*pow(h, 2)
            elif i == (j+1):
                A[i][j] = -1 - p(x)*h/2
            elif i == (j-1):
                A[i][j] = -1 + p(x)*h/2
            else:
                A[i][j] = 0

    for i in range(dim):
        x = vetor_x[i]
        d[i] = -r(x)*pow(h, 2)

    A[0][0] += p(x0)*h/2
    d[0] += (1 + p(x0)*h/2)*y0

    A[dim-1][dim-1] += -p(xf)*h/2
    d[dim-1] += (1 - p(xf)*h/2)*yf

    a = np.zeros(len(A))
    b = np.zeros(len(A))
    c = np.zeros(len(A))

    for i in range(len(A)):
        a[i] = A[i,i]
        if i != 0:
            b[i] = A[i,i-1]
        if i != len(A)-1:
            c[i] = A[i,i+1]

    return a, b, c, d


a, b, c, d = diferenca_finita_mista(x0, y0, xf, yf)

# Adiciona a condição de derivada
h = 0.25
d[0] -= (1 + p(x0)*h/2) * y0

x = thomas_algorithm(a, b, c, d)
h = 0.25
xi = h
y_novo = [y0]
for i in range(len(x)):
    y_novo.append(x[i])
    xi += h
y_novo.append(yf)

xi = np.arange(x0, xf+h, h)

plt.plot(xi, y_novo, color="red", marker="o")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da solução')
plt.grid(True)
plt.show()
