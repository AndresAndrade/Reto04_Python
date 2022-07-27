def ordenes(rutinaContable):
    from functools import reduce
    totales = list(map(lambda x: [x[0]] + list(map(lambda y: y[1] * y[2], x[1:])), rutinaContable))
    print(totales)
    totales1 = list(map(lambda x: [x[0]] + [reduce(lambda y, z: y + z, x[1:])], totales))
    print(totales1)
    totales2 = list(map(lambda x: x if x[1] >= 600000 else [x[0]] + [x[1] + 25000], totales1))
    print(totales2)

    print('------------------------ Inicio Registro diario ---------------------------------')
    for i in totales2:
        print(f"La factura {i[0]} tiene un total en pesos de {i[1]:,.2f}")
    print('-------------------------- Fin Registro diario ----------------------------------')

rutinaContable = [
    [1201, ("5464", 4, 25842.99), ("7854", 18, 23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58), ("1112", 18, 2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20), ("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 390.95)]
]

ordenes(rutinaContable)
