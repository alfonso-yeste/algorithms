"""""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""


def esta_balanceada(expresion):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for char in expresion:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila:
                return False
            ultimo = pila.pop()
            if pares[char] != ultimo:
                return False

    return len(pila) == 0


if __name__ == '__main__':
    expresion_1 = "{ [ a * ( c + d ) ] - 5 }"
    expresion_2 = "{ a * ( c + d ) ] - 5 }"

    print(f"La expresión '{expresion_1}' está balanceada: {esta_balanceada(expresion_1)}")
    print(f"La expresión '{expresion_2}' está balanceada: {esta_balanceada(expresion_2)}")





