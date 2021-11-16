"""
input(): Nos sirve para obtener un string por la consola otorgado por el usuario
float(): Convierte un valor a un dato de tipo flotante
str(): Convierte un valor a un dato de tipo texto o string
round(): Redondea un flotante con una cantidad de decimales especifico
print(): Nos imprime un valor
"""
pesos = float(input('¿Cuántos pesos méxicanos tienes?'))
dolar_peso = 20.5
dolares = str(round((pesos / dolar_peso), 2))
print('Tienes $' + dolares + ' dólares')

dolares = float(input('¿Cuántos dolares tienes?'))
pesos = str(round((dolares * dolar_peso), 2))
print('Tienes $' + pesos + ' pesos')
