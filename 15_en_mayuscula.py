"""""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

def capitalizar_primera_letra(texto):
    resultado = ""
    nueva_palabra = True

    for char in texto:
        if char == " ":
            resultado += char
            nueva_palabra = True
        elif nueva_palabra:
            resultado += char.upper()
            nueva_palabra = False
        else:
            resultado += char

    return resultado

if __name__ == '__main__':
    texto = "este es un ejemplo de cadena"
    resultado = capitalizar_primera_letra(texto)
    print(f"Texto original: '{texto}'")
    print(f"Texto capitalizado: '{resultado}'")





