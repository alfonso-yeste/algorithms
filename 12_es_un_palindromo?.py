"""""
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
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

