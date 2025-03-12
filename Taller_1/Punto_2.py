def conversion(v, u):
    if u == 'km/h':
        m = v * 1000 / 3600
        return m
    elif u == 'm/s':
        k = v * 3600 / 1000
        return k
    else:
        return 'Unidades no validas'
