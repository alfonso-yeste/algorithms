"""""
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
"""


def diferencia_cadenas(str1,str2):
    out1 = ""
    out2 = ""
    for char in str1:
        if char not in str2:
            out1 += char

    for char in str2:
        if char not in str1:
            out2 += char
    print(f"out1: '{out1}'")
    print(f"out2: '{out2}'")


if __name__ == '__main__':
    cadena1 = "hola"
    cadena2 = "mundo"
    diferencia_cadenas(cadena1, cadena2)

