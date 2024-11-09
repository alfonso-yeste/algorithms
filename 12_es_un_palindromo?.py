"""""
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""


import unidecode

def es_palindromo(texto):
    texto = texto.lower()

    texto = unidecode.unidecode(texto)

    caracteres_validos = "abcdefghijklmnopqrstuvwxyz0123456789"
    texto_limpio = ""
    for char in texto:
        if char in caracteres_validos:
            texto_limpio += char

    return texto_limpio == texto_limpio[::-1]

if __name__ == '__main__':
    ejemplo_1 = "Ana lleva al oso la avellana."
    ejemplo_2 = "Este no es un palíndromo."

    print(f"'{ejemplo_1}' es palíndromo: {es_palindromo(ejemplo_1)}")
    print(f"'{ejemplo_2}' es palíndromo: {es_palindromo(ejemplo_2)}")


