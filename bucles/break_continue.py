def run():
    # Imprime los números pares
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)
    # Imprime los numeors del 0 al 5678
    for i in range(10000):
        print(i)
        if i == 5678:
            break
    # Recorre el string hasta que tenga una 'o'
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
