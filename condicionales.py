"""
CONDICIONALES
if (Si) Se usa para la condición principal.
elif (Si no) En caso de que la condición principal o anterior no se cumpla,
    se puede usar para agregar otra condición.
else (Sino) En caso de que la(s) condición(es) anterior(s) no se cumplan,
    se ejecuta como alternativa sin condicional.
"""

# Se le pide al usuario su edad y se guarda en "edad" como número entero
edad = int(input('Escribe tu edad: '))
# Si la edad es mayor a 17 entonces imprime que es mayor de edad
if edad > 17:
    print('Eres mayor de edad')
# Si no cumple con lo anterior, entonces imprime que es menor
else:
    print('Eres menor de edad')

numero = int(input('Escribe un número: '))

if numero > 5:
    print('Es mayor a 5')
elif numero == 5:
    print('Es igual a 5')
else:
    print('Es menor a 5')
