"""""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""



def son_anagramas(palabra1,palabra2):
    if palabra1 == palabra2:
        return False
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)


if __name__ == '__main__':
    # Probar la función son_anagramas con algunos ejemplos
    print(son_anagramas("amor", "roma"))
    print(son_anagramas("amor", "amro"))
    print(son_anagramas("amor", "amor"))
    print(son_anagramas("amor", "rama"))