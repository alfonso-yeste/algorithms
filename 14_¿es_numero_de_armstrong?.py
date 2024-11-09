"""""
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
"""


def es_numero_armstrong(num):
    digitos = str(num)
    n = len(digitos)
    suma = sum(int(d) ** n for d in digitos)
    return suma == num

# Ejemplo de uso
if __name__ == '__main__':
    numero_armstrong = 153
    print(f"¿El número {numero_armstrong} es un número de Armstrong?: {es_numero_armstrong(numero_armstrong)}")



