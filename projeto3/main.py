# Método de diferenças finitas para resolver PVC de
# segunda ordem. Para resolver o sistema resultante
# implemente o Algoritmo de Thomas.

import matplotlib.pyplot as plt

class Method():
    def __init__(self, f1, f2, y10, y20, xi, h, iters):
        self.f1 = f1
        self.f2 = f2
        self.y1i = y10
        self.y2i = y20
        self.xi = xi
        self.h = h
        self.iters = iters
        self.xlist = []
        self.y1list = []
        self.y2list = []

    def get_y1i(self):
        return float(self.y1i)

    def set_y1i(self, y1i):
        self.y1i = y1i

    def get_y2i(self):
        return float(self.y2i)

    def set_y2i(self, y2i):
        self.y2i = y2i

    def get_xi(self):
        return float(self.xi)

    def set_xi(self, xi):
        self.xi = xi

    def get_h(self):
        return float(self.h)

    def get_iters(self):
        return int(self.iters)

class Euler(Method):
    def __init__(self, f1, f2, y10, y20, xi, h, iters):
        Method.__init__(self, f1, f2, y10, y20, xi, h, iters)

    def solve(self):
        print("\n* Solução *\n")
        # Solving the problem
        for i in range(self.get_iters()):
            print(f"Iteração {i+1}")

            # Calculando y1 e y2
            y1i = self.get_y1i() + self.get_h() *self.f1(self.get_xi(), self.get_y1i(), self.get_y2i())
            y2i = self.get_y2i() + self.get_h() *self.f2(self.get_xi(), self.get_y1i(), self.get_y2i())
            self.y1list.append(y1i)
            self.y2list.append(y2i)
            self.set_y1i(y1i)
            self.set_y2i(y2i)

            xi = (i+1) * self.get_h()
            self.xlist.append(xi)
            self.set_xi(xi)
            print(f"* x{i+1} = {xi:.2f}")

            print(f"* y1{i+1} = {y1i:.4f}")
            print(f"* y2{i+1} = {y2i:.4f}\n")

    def plotGraph(self):
        plt.plot(self.xlist, self.y1list, 'r-', linewidth=2.0)
        plt.plot(self.xlist, self.y2list, 'b-', linewidth=2.0)

        plt.xlabel('x')
        plt.ylabel('y(x)')
        plt.legend(["y1","y2"])

        plt.title('Euler')
        plt.show()


class RK4(Method):
    def __init__(self, f1, f2, y10, y20, xi, h, iters):
        Method.__init__(self, f1, f2, y10, y20, xi, h, iters)

    def solve(self):
        print("\n* Solução *\n")
        # Solving the problem
        for i in range(self.get_iters()):
            print(f"Iteração {i+1}")

            # Calculando K1, K2, K3 e K4
            k11 = self.f1(self.get_xi(), self.get_y1i(), self.get_y2i())
            k12 = self.f2(self.get_xi(), self.get_y1i(), self.get_y2i())
            k21 = self.f1(self.get_xi() + self.get_h()/2, self.get_y1i() + self.get_h()/2 * k11, self.get_y2i() + self.get_h()/2 * k12)
            k22 = self.f2(self.get_xi() + self.get_h()/2, self.get_y1i() + self.get_h()/2 * k11, self.get_y2i() + self.get_h()/2 * k12)
            k31 = self.f1(self.get_xi() + self.get_h()/2, self.get_y1i() + self.get_h()/2 * k21, self.get_y2i() + self.get_h()/2 * k22)
            k32 = self.f2(self.get_xi() + self.get_h()/2, self.get_y1i() + self.get_h()/2 * k21, self.get_y2i() + self.get_h()/2 * k22)
            k41 = self.f1(self.get_xi() + self.get_h(), self.get_y1i() + self.get_h() *k31, self.get_y2i() +self.get_h() * k32)
            k42 = self.f2(self.get_xi() + self.get_h(), self.get_y1i() + self.get_h() *k31, self.get_y2i() +self.get_h() * k32)

            xi = (i+1) * self.get_h()
            self.xlist.append(xi)
            self.set_xi(xi)
            print(f"* x{i+1} = {xi:.2f}")

            print(f"  - K11 = {k11:.4f}")
            print(f"  - K12 = {k12:.4f}")
            print(f"  - K21 = {k21:.4f}")
            print(f"  - K22 = {k22:.4f}")
            print(f"  - K31 = {k31:.4f}")
            print(f"  - K32 = {k32:.4f}")
            print(f"  - K41 = {k41:.4f}")
            print(f"  - K42 = {k42:.4f}")

            # Calculando y1 e y2
            y1i = self.get_y1i() + self.get_h()/6 *(k11 + 2*(k21 + k31) + k41)
            y2i = self.get_y2i() + self.get_h()/6 *(k12 + 2*(k22 + k32) + k42)
            self.y1list.append(y1i)
            self.y2list.append(y2i)

            print(f"* y1{i+1} = {y1i:.4f}")
            print(f"* y2{i+1} = {y2i:.4f}\n")
            self.set_y1i(y1i)
            self.set_y2i(y2i)

    def plotGraph(self):
        plt.plot(self.xlist, self.y1list, 'r-', linewidth=2.0)
        plt.plot(self.xlist, self.y2list, 'b-', linewidth=2.0)

        plt.xlabel('x')
        plt.ylabel('y(x)')
        plt.legend(["y1","y2"])

        plt.title('RK4')
        plt.show()


# def f1(xi, y1i, y2i):
#     f = 2*y1i*y2i
#     return f

# def f2(xi, y1i, y2i):
#     f = -y1i
#     return f

def verificaEscolha():
    choice = int(input("\nQual será o método de resolução da EDO?\n* Euler (1)\n* RK4 (2)\n-> "))
    while(choice != int(1) and choice != int(2)):
        choice = int(input("Seleção inválida por favor tente novamente:\n* Euler (1)\n* RK4 (2)\n-> "))
    return choice

def main():
    
    print("\nInforme as condições iniciais:")
    function1 = input("Função 1 (xi,y1i,y2i) = ")
    function2 = input("Função 2 (xi,y1i,y2i) = ")
    y1i = float(input("Valor inicial de y1 = "))
    y2i = float(input("Valor inicial de y2 = "))
    xi = float(input("Valor inicial de x = "))
    h = float(input("Valor de h = "))
    iters = int(input("Número de iterações = "))
    
    f1 = lambda xi, y1i, y2i: eval(function1)
    f2 = lambda xi, y1i, y2i: eval(function2)

    choice = verificaEscolha()
    if(choice == 1):
        euler = Euler(f1, f2, y1i, y2i, xi, h, iters)
        euler.solve()
        euler.plotGraph()
    else:
        rk4 = RK4(f1, f2, y1i, y2i, xi, h, iters)
        rk4.solve()
        rk4.plotGraph()
    
    

if __name__ == "__main__":
    main()