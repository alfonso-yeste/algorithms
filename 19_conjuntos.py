"""""
 * CONJUNTOS
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""


def dos_arrays(array1, array2):
    array_resultante = []  # Inicializa el array vacío
    for cada in array1:    # Recorre los elementos del primer array
        if cada in array2: # Comprueba si el elemento está en el segundo array
            array_resultante.append(cada)  # Agrega el elemento común
    return array_resultante  # Devuelve el resultado al final

# Arrays de ejemplo
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

if __name__ == '__main__':
    # Definir dos arrays de ejemplo
    array1 = [1, 2, 3, 4, 5]
    array2 = [3, 4, 5, 6, 7]

    # Ejecutar la función con los arrays y el booleano True (elementos comunes)
    resultado_comunes = dos_arrays(array1, array2)
    print(f"Elementos comunes: {resultado_comunes}")




