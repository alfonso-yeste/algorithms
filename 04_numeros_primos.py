"""""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""



def es_primo(n):
    if n <= 1:
        return False
    # Verificar si el número tiene algún divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def imprimir_primos_hasta_100():
    for num in range(1, 101):
        if es_primo(num):
            print(num, end=", ")

# Ejecutar la función principal
if __name__ == '__main__':
    imprimir_primos_hasta_100()



def primo(n):
    if n <= 1:
        return false