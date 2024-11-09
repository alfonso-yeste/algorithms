"""""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.

"""

def contar_palabras(texto):
    signos_puntuacion = ".,;:!?()\"'"

    texto = texto.lower()

    texto_limpio = ""
    for char in texto:
        if char not in signos_puntuacion:
            texto_limpio += char

    # Dividir el texto en palabras
    palabras = []
    palabra_actual = ""
    for char in texto_limpio:
        if char == " ":
            if palabra_actual != "":
                palabras.append(palabra_actual)
                palabra_actual = ""
        else:
            palabra_actual += char
    if palabra_actual != "":
        palabras.append(palabra_actual)

    contador_palabras = {}
    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1
        else:
            contador_palabras[palabra] = 1

    for palabra, cuenta in contador_palabras.items():
        print(f"'{palabra}': {cuenta}")

# Ejemplo de uso
if __name__ == '__main__':
    texto_ejemplo = "Hola, hola! ¿Qué tal? Hola mundo. Mundo tal y como es."
    contar_palabras(texto_ejemplo)




