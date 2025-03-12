def celsius_fahrenheit(lista_celsius):
    lista_fahrenheit = list(map(lambda temperatura: (temperatura * 9/5) + 32, lista_celsius))
    return lista_fahrenheit
