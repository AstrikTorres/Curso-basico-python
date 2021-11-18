"""
input(): Nos sirve para obtener un string por la consola otorgado por el usuario
float(): Convierte un valor a un dato de tipo flotante
str(): Convierte un valor a un dato de tipo texto o string
round(): Redondea un flotante con una cantidad de decimales especifico
print(): Nos imprime un valor
"""


def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('¿Cuántos pesos ' + tipo_pesos + ' tienes? '))
    dolares = str(round((pesos / valor_dolar), 2))
    print('Tienes $' + dolares + ' dólares')


menu = '''
Bienvenido al conversor de monedas 💰

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opción:
'''

opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos", 20.5)
elif opcion == 2:
    conversor("colombianos", 3900)
elif opcion == 3:
    conversor("argentinos", 100)
else:
    print('Ingresa una opcion')
