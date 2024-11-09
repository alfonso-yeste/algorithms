"""""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
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

