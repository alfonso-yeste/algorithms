"""""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""

def decimal_a_binario(numero):
    if numero == 0:
        return "0"

    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2  # Dividir el número por 2 de forma entera

    return binario

if __name__ == '__main__':
    numero_decimal = 25
    resultado_binario = decimal_a_binario(numero_decimal)
    print(f"El número {numero_decimal} en binario es: {resultado_binario}")




