"""
input(): Nos sirve para obtener un string por la consola otorgado por el usuario
float(): Convierte un valor a un dato de tipo flotante
str(): Convierte un valor a un dato de tipo texto o string
round(): Redondea un flotante con una cantidad de decimales especifico
print(): Nos imprime un valor
"""

menu = '''
Bienvenido al conversor de monedas 💰

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opción:
'''

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input('¿Cuántos pesos méxicanos tienes? '))
    dolar_peso = 20.5
    dolares = str(round((pesos / dolar_peso), 2))
    print('Tienes $' + dolares + ' dólares')
elif opcion == 2:
    pesos = float(input('¿Cuántos pesos colombianos tienes? '))
    dolar_peso = 3900
    dolares = str(round((pesos / dolar_peso), 2))
    print('Tienes $' + dolares + ' dólares')
elif opcion == 3:
    pesos = float(input('¿Cuántos pesos argentinos tienes?'))
    dolar_peso = 100
    dolares = str(round((pesos / dolar_peso), 2))
    print('Tienes $' + dolares + ' dólares')
else:
    print('Ingresa una opcion')
