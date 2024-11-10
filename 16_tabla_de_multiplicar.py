"""
/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 */
"""

def imprimir_tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ejemplo de uso
if __name__ == '__main__':
    try:
        numero = int(input("Introduce un número para imprimir su tabla de multiplicar: "))
        imprimir_tabla_multiplicar(numero)
    except ValueError:
        print("Por favor, introduce un número entero válido.")

