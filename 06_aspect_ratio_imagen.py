"""""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

"""


def invertir_cadena(texto):
    cadena_invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        cadena_invertida += texto[i]
    return cadena_invertida

if __name__ == '__main__':
    texto = "Hola mundo"
    resultado = invertir_cadena(texto)
    print(f"Cadena original: {texto}")
    print(f"Cadena invertida: {resultado}")



