# Método de Euler:
# -> Y1(i+1) = Y1(i) + h * f2(Xi, Y1(i, Y2(i)))
# -> Y2(i+1) = Y2(i) + h * f2(Xi, Y1(i, Y2(i)))

# Método de Runke-kutta:
# -> K11 = f1(Xi, Y1(i), Y2(i))
# -> K12 = f2(Xi, Y1(i), Y2(i))
# -> K21 = f1(Xi + h/2, Y1(i) + h/2*K11, Y2(i) + h/2*K12)
# -> K22 = f2(Xi + h/2, Y1(i) + h/2*K11, Y2(i) + h/2*K12)
# -> K31 = f1(Xi + h/2, Y1(i) + h/2*K21, Y2(i) + h/2*K22)
# -> K32 = f2(Xi + h/2, Y1(i) + h/2*K21, Y2(i) + h/2*K22)
# -> K41 = f1(Xi + h, Y1(i) + h*K31, Y2(i) + h*K32)
# -> K42 = f2(Xi + h, Y1(i) + h*K31, Y2(i) + h*K32)

# -> Y1(i+1) = Y1(i) + h/6 * (K11 + 2*(K21 + K31) + K41)
# -> Y2(i+1) = Y2(i) + h/6 * (K12 + 2*(K22 + K32) + K42)

# precisamos das condições iniciais para os algoritmos:
# y1'/f1 = ?
# y2'/f2 = ?
# Y1(0) = ?
# Y2(0) = ?
# h = ?
# iterações = ?