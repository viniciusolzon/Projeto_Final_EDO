# Método de diferenças finitas para resolver PVC de
# segunda ordem. Para resolver o sistema resultante
# implemente o Algoritmo de Thomas.

import matplotlib.pyplot as plt
import numpy as np

class Method():
    def __init__(self, f, y0, xi, h, iters):
        self.f = f
        self.yi = y0
        self.xi = xi
        self.h = h
        self.iters = iters
        self.xlist = []
        self.ylist = []

    def get_yi(self):
        return float(self.yi)

    def set_yi(self, yi):
        self.yi = yi

    def get_xi(self):
        return float(self.xi)

    def set_xi(self, xi):
        self.xi = xi

    def get_h(self):
        return float(self.h)

    def get_iters(self):
        return int(self.iters)

def DiferencasFinitas(f, y0, xi, h, iters):
    print("\n* Solução *\n")
    # Solving the problem
    matriz = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    print(matriz)
    for i in range(iters):
        print(f"Iteração {i+1}")
        # vai resolver e cair numa matriz para o Algoritmo de Thomas resolver


def AlgoritmoThomas(matrix):
    # executa o algoritmo de Thomas na matriz gerada pelo método das diferencas finitas
    pass

# def f(xi, yi):
#     f = (2*yi)+1
#     return f

def main():

    print("\nInforme as condições iniciais:")
    function = input("Função(xi,yi) = ")
    yi = float(input("Valor inicial de y = "))
    xi = float(input("Valor inicial de x = "))
    h = float(input("Valor de h = "))
    iters = int(input("Número de iterações = "))

    f = lambda xi, yi: eval(function)

    matrix = DiferencasFinitas(f, yi, xi, h, iters)
    result = AlgoritmoThomas(matrix)
    
    # plt.plot(xlist, ylist, 'r-', linewidth=2.0)

    # plt.xlabel('x')
    # plt.ylabel('y(x)')
    # plt.legend(["y"])

    # plt.title('RK4')
    # plt.show()
    

if __name__ == "__main__":
    main()