import random

def generar_contrasena(longitud):
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    caracteres = mayusculas + minusculas + numeros + simbolos
    contrasena = "".join(random.sample(caracteres, longitud))
    return contrasena