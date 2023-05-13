# Método de Euler e Runge-kutta de quarta ordem para
# resolver uma PVI para um sistema de duas equações 
# diferenciais de primeira ordem.

import matplotlib.pyplot as plt

class Euler():
    def __init__(self, y0, xi, h, iters):
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

    def solve(self):
        print("\n* Solução *\n")
        # Solving the problem
        for i in range(self.get_iters()):
            print(f"Iteração {i+1}")
            xi = (i+1) * self.get_h()
            self.xlist.append(xi)
            self.set_xi(xi)
            print(f"* x{i+1} = {xi:.2f}")

            # Calculando Y1 e Y2
            yi = self.get_yi() + self.get_h() * f(xi, self.get_yi())
            self.ylist.append(yi)

            print(f"* y{i+1} = {yi:.4f}\n")
            self.set_yi(yi)


    def plotGraph(self):
        plt.plot(self.xlist, self.ylist, 'r-', linewidth=2.0)

        plt.xlabel('x')
        plt.ylabel('y(x)')
        plt.legend(["y"])

        plt.title('Euler')
        plt.show()


class RK4():
    def __init__(self, y0, xi, h, iters):
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

    def solve(self):
        print("\n* Solução *\n")
        # Solving the problem
        for i in range(self.get_iters()):
            print(f"Iteração {i+1}")
            xi = (i+1) * self.get_h()
            self.xlist.append(xi)
            self.set_xi(xi)
            print(f"* x{i+1} = {xi:.2f}")

            # Calculando K1, K2, K3 e K4
            k1 = f(self.get_xi(), self.get_yi())
            k2 = f(self.get_xi() + self.get_h()/2, self.get_yi() + self.get_h()/2 * k1)
            k3 = f(self.get_xi() + self.get_h()/2, self.get_yi() + self.get_h()/2 * k2)
            k4 = f(self.get_xi() + self.get_h(), self.get_yi() + self.get_h() *k3)
    
            print(f"  - k1 = {k1:.4f}")
            print(f"  - K2 = {k2:.4f}")
            print(f"  - K3 = {k3:.4f}")
            print(f"  - K4 = {k4:.4f}")
                                                        
            # Calculando Y1 e Y2
            yi = self.get_yi() + self.get_h()/6 *(k1 + 2*(k2 + k3) + k4)
            self.ylist.append(yi)

            print(f"* y{i+1} = {yi:.4f}\n")
            self.set_yi(yi)


    def plotGraph(self):
        plt.plot(self.xlist, self.ylist, 'r-', linewidth=2.0)

        plt.xlabel('x')
        plt.ylabel('y(x)')
        plt.legend(["y"])

        plt.title('RK4')
        plt.show()


def f(xi, yi):
    f = (-2)*xi*(yi*yi)
    return f

def verificaEscolha():
    choice = int(input("\nQual será o método de resolução da EDO?\n* Euler (1)\n* RK4 (2)\n-> "))
    while(choice != int(1) and choice != int(2)):
        choice = int(input("Seleção inválida por favor tente novamente:\n* Euler (1)\n* RK4 (2)\n-> "))
    return choice

def main():
    #y0 = 1
    #xi = 0
    #h = 0.2
    #iters = 2
    
    print("\nInforme as condições iniciais:")
    y0 = input("Valor inicial de y = ")
    xi = input("Valor inicial de x = ")
    h = float(input("Valor de h = "))
    iters = int(input("Número de iterações = "))
    
    choice = verificaEscolha()
    if(choice == 1):
        euler = Euler(y0, xi, h, iters)
        euler.solve()
        euler.plotGraph()
    else:
        rk4 = RK4(y0, xi, h, iters)
        rk4.solve()
        rk4.plotGraph()
    
    

if __name__ == "__main__":
    main()