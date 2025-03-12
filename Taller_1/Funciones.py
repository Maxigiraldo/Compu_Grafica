import math

def mrua(h):
    t = ((2*h)/9.81)**0.5
    return t

def conversion(v, u):
    if u == 'km/h':
        m = v * 1000 / 3600
        return m
    elif u == 'm/s':
        k = v * 3600 / 1000
        return k
    else:
        return 'Unidades no validas'
    
def desplazamiento(vo, a, t):
    return vo*t + 0.5*a*t**2

def suma_vectorial(v1, v2):
    if len(v1) == len(v2):
        return [v1[i] + v2[i] for i in range(len(v1))]
    else:
        return 'Los vectores deben tener la misma longitud'
    
def producto_escalar(v1, v2):
    if len(v1) == len(v2):
        return sum([v1[i] * v2[i] for i in range(len(v1))])
    else:
        return 'Los vectores deben tener la misma longitud'

def alcance_maximo(vo, theta):
    angulo = math.radians(theta)
    return (vo**2)*math.sin(2*angulo)/9.81

def altura_maxima(vo, theta):
    angulo = math.radians(theta)
    return ((vo**2)*(math.sin(angulo)**2))/(2*9.81)

def seleccion(op, vo, theta):
    if op == 1:
        return alcance_maximo(vo, theta)
    elif op == 2:
        return altura_maxima(vo, theta)
    else:
        return "Opcion invalida"