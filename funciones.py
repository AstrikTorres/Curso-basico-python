"""
Funciones: codigo que puedes reutilizar.

Las funciones se construyen de la siguiente manera:

def nombre_funcion():
    desarrollo de la funcion.

Los nombres de las funciones se escriben siempre en minusculas,
nunca con numeros y siempre se separan con guion bajo.

Parametros: variables que voy a tener disponibles para usarla dentro de la función.
"""


def imprimir_mensaje():
    print('Mensaje especial: ')
    print('¡Estoy aprendiendo a usar funciones!')


imprimir_mensaje()


def conversacion(mensaje):
    print('Hola')
    print('¿Cómo estás?')
    print(mensaje)
    print('Adios')


opcion = int(input('Elige una opción (1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la opción 1')
elif opcion == 2:
    conversacion('Elegiste la opción 2')
elif opcion == 3:
    conversacion('Elegiste la opción 3')
else:
    print('Escribe una opción valida')


# return es un operador que se utiliza para aprovechar el valor o resultado
# que nos devuelve una función para poder utilizarlo en el código más adelante.
def suma(a, b):
    return a + b


valor_suma = suma(1, 4)
print(valor_suma)
