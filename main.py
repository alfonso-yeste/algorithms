

#Idear una programa que encuentre el máximo en una matriz

def max_number(numbers):
    max_value = numbers[0]

    for num in numbers[1:]:
        if num > max_value:
            max_value = num
    return max_value


def min_number(numbers):
    min_value = numbers[0]

    for num in numbers[1:]:
        if num < min_value:
            min_value = num
    return min_value


if __name__ == '__main__':
    print(max_number([1, 2, 5, -7, 13, -9]))

""""" Reto #0
 * EL FAMOSO "FIZZ BUZZ"
 * Fecha publicación enunciado: 27/12/21
 * Fecha publicación resolución: 03/01/22
 * Dificultad: FÁCIL
 * Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100
  (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


def fizz_buzz():
    for index in range(1, 101):
        divisible_for_three = index % 3 == 0
        divisible_for_five = index % 5 == 0

        if divisible_for_three and divisible_for_five:
            print("fizzbuzz")
        elif divisible_for_three:
            print("fizz")
        elif divisible_for_five:
            print("buzz")
        else:
            print(index)


# Ejecutar la función principal
if __name__ == '__main__':
    fizz_buzz()
