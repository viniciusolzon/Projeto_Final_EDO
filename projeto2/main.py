# Método de Euler e Runge-kutta de quarta ordem para
# resolver uma PVI para um sistema de duas equações 
# diferenciais de primeira ordem.

import matplotlib.pyplot as plt

class Euler():
    def __init__(self, y10, y20, xi, h, iters):
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
            y1i = self.get_y1i() + self.get_h() *f1(xi, self.get_y1i(), self.get_y2i())
            y2i = self.get_y2i() + self.get_h() *f2(xi, self.get_y1i(), self.get_y2i())
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

        plt.title('Euler')
        plt.show()


class RK4():
    def __init__(self, y10, y20, xi, h, iters):
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
            k11 = f1(self.get_xi(), self.get_y1i(), self.get_y2i())
            k12 = f2(self.get_xi(), self.get_y1i(), self.get_y2i())
            k21 = f1(self.get_xi() + self.get_h()/2, self.get_y1i() + self.get_h()/2 * k11, self.get_y2i() + self.get_h()/2 * k12)
            k22 = f2(self.get_xi() + self.get_h()/2, self.get_y1i() + self.get_h()/2 * k11, self.get_y2i() + self.get_h()/2 * k12)
            k31 = f1(self.get_xi() + self.get_h()/2, self.get_y1i() + self.get_h()/2 * k21, self.get_y2i() + self.get_h()/2 * k22)
            k32 = f2(self.get_xi() + self.get_h()/2, self.get_y1i() + self.get_h()/2 * k21, self.get_y2i() + self.get_h()/2 * k22)
            k41 = f1(self.get_xi() + self.get_h(), self.get_y1i() + self.get_h() *k31, self.get_y2i() +self.get_h() * k32)
            k42 = f2(self.get_xi() + self.get_h(), self.get_y1i() + self.get_h() *k31, self.get_y2i() +self.get_h() * k32)
    
            print(f"  - K11 = {k11:.4f}")
            print(f"  - K12 = {k12:.4f}")
            print(f"  - K21 = {k21:.4f}")
            print(f"  - K22 = {k22:.4f}")
            print(f"  - K31 = {k31:.4f}")
            print(f"  - K32 = {k32:.4f}")
            print(f"  - K41 = {k41:.4f}")
            print(f"  - K42 = {k42:.4f}")
                                                        
            # Calculando Y1 e Y2
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


def f1(xi, y1i, y2i):
    f = 2*y1i*y2i
    return f

def f2(xi, y1i, y2i):
    f = -y1i
    return f

def verificaEscolha():
    choice = int(input("\nQual será o método de resolução da EDO?\n* Euler (1)\n* RK4 (2)\n-> "))
    while(choice != int(1) and choice != int(2)):
        choice = int(input("Seleção inválida por favor tente novamente:\n* Euler (1)\n* RK4 (2)\n-> "))
    return choice

def main():
    #y10 = 1
    #y20 = 1
    #xi = 0
    #h = 0.2
    #iters = 2
    
    print("\nInforme as condições iniciais:")
    y10 = input("Valor inicial de y1 = ")
    y20 = input("Valor inicial de y2 = ")
    xi = input("Valor inicial de x = ")
    h = float(input("Valor de h = "))
    iters = int(input("Número de iterações = "))
    
    choice = verificaEscolha()
    if(choice == 1):
        euler = Euler(y10, y20, xi, h, iters)
        euler.solve()
        euler.plotGraph()
    else:
        rk4 = RK4(y10, y20, xi, h, iters)
        rk4.solve()
        rk4.plotGraph()
    
    

if __name__ == "__main__":
    main()