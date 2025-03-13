import numpy as np
import matplotlib.pyplot as plt
import math

# Función euler
def exp_serie(x):
    n = 10
    sum = 0
    for i in range(0, n+1):
        sum += (x**i)/math.factorial(i)
    return sum

exp_S = np.vectorize(exp_serie)

# Función seno
def sen_serie(x):
    n = 10
    sum = 0
    for i in range(0, n+1):
        sum += ((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1)
    return sum

sen_S = np.vectorize(sen_serie)

# Función coseno
def cos_serie(x):
    n = 10
    sum = 0
    for i in range(0, n+1):
        sum += ((-1)**i)*(x**(2*i))/math.factorial(2*i)
    return sum

# Función logaritmo natural
def ln_serie(x):
    n = 10
    sum = 0
    for i in range(1, n+1):
        sum += ((-1)**(i-1))*(x**i)/i
    return sum

ln_S = np.vectorize(ln_serie)

# Función arctangente
def atan_serie(x):
    n = 10
    sum = 0
    for i in range(0, n+1):
        sum += ((-1)**i)*(x**(2*i+1))/(2*i+1)
    return sum

atan_S = np.vectorize(atan_serie)

x_euler = np.linspace(0, 10, 50)
y_euler = exp_S(x_euler)

x_seno = np.linspace(-2*np.pi, 2*np.pi, 50)
y_seno = sen_S(x_seno)

x_coseno = np.linspace(-2*np.pi, 2*np.pi, 50)
y_coseno = cos_serie(x_coseno)

x_ln = np.linspace(0.1, 40, 70)
y_ln = ln_S(x_ln)

x_atan = np.linspace(-10, 10, 50)
y_atan = atan_S(x_atan)


plt.subplot(3, 2, 1)
plt.plot(x_euler, y_euler)
plt.title('Serie de Euler')

plt.subplot(3, 2, 2)
plt.plot(x_seno, y_seno)
plt.title('Serie de Seno')

plt.subplot(3, 2, 3)
plt.plot(x_coseno, y_coseno)
plt.title('Serie de Coseno')

plt.subplot(3, 2, 4)
plt.plot(x_ln, y_ln)
plt.title('Serie de Logaritmo Natural')

plt.subplot(3, 2, 5)
plt.plot(x_atan, y_atan)
plt.title('Serie de Arctangente')

plt.show()