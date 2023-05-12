# Método de Euler e Runge-kutta de quarta ordem para
# resolver uma PVI composto para equação diferencial
# de primeira ordem.

import matplotlib.pyplot as plt

def verificaEscolha():
    choice = int(input("Qual será o método de resolução da EDO?\n* Euler (1)\n* RK4 (2)\n-> "))
    while(choice != int(1) and choice != int(2)):
        choice = int(input("Seleção inválida por favor tente novamente:\n* Euler (1)\n* RK4 (2)\n-> "))
    return choice

def verificaFuncao():
    pass

def verificaCI():
    print("Informe as condições iniciais:")
    yi = input("Valor inicial de y = ")
    h = input("Valor de h = ")
    iters = input("Número de iterações = ")

class Euler():
    pass

class RK4():
    def __init__(self, y0, xi, h, iters):
        self.yi = y0
        self.xi = xi
        self.h = h
        self.iters = iters

    def get_yi(self):
        return float(self.yi)

    def set_yi(self, yi):
        self.yi = yi

    def get_xi(self):
        return float(self.xi)

    def get_h(self):
        return float(self.h)

    def get_iters(self):
        return int(self.iters)

    def solve(self):
        print("\nSolution:")
        # Solving the problem
        for i in range(self.get_iters()):
            print(f"Iteração {i}")
            xi = int(i) * self.get_h()
            print(f"* X{i} = {xi}")

            # Calculando K1, K2, K3 e K4
            k1 = f(xi, self.get_yi())
            k2 = f(xi + self.get_h()/2, self.get_yi() + self.get_h()/2 * k1, + self.get_h()/2 * k1)
            k3 = f(xi + self.get_h()/2, self.get_yi() + self.get_h()/2 * k2, + self.get_h()/2 * k2)
            k4 = f(xi + self.get_h(), self.get_yi() + self.get_h() *k3, +self.get_h() * k3)
    
            print(f"  - K1 = {k1:.4f}")
            print(f"  - K2 = {k2:.4f}")
            print(f"  - K3 = {k3:.4f}")
            print(f"  - K4 = {k4:.4f}")
                                                        
            # Calculando Y
            yi = self.get_yi() + self.get_h()/6 *(k1 + 2*(k2 + k3) + k4)

            print(f"* y{i} = {yi:.4f}")
            self.set_yi(yi)


    def showGraph(self):
        plt.plot(self.get_xi() ,self.get_yi())
        plt.title('RK4')
        plt.ylabel('y(x)')
        plt.xlabel('x')
        plt.show()
    

def f(xi, yi):
    f = 2*yi
    return f

def main():
    choice = verificaEscolha()
    yi = 1
    xi = 0
    h = 0.2
    iters = 2
    
    # print("\nInforme as condições iniciais:")
    # yi = input("Valor inicial de y = ")
    # h = float(input("Valor de h = "))
    # iters = int(input("Número de iterações = "))
    
    if(choice == 1):
        euler = Euler(yi, xi, h, iters)
        euler.solve()
        euler.showGraph()
    else:
        rk4 = RK4(yi, xi, h, iters)
        rk4.solve()
        rk4.showGraph()
    
    

if __name__ == "__main__":
    main()