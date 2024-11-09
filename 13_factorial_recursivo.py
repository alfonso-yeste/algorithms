"""""
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
"""


def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
if __name__ == '__main__':
    numero = 5
    print(f"El factorial de {numero} es: {factorial(numero)}")



