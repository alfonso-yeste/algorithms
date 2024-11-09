"""""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""



def calcular_area(poligono, *dimensiones):
    if poligono.lower() == "triángulo":
        if len(dimensiones) != 2:
            return "Error: El triángulo requiere base y altura."
        base, altura = dimensiones
        return (base * altura) / 2

    elif poligono.lower() == "cuadrado":
        if len(dimensiones) != 1:
            return "Error: El cuadrado requiere un lado."
        lado = dimensiones[0]
        return lado ** 2

    elif poligono.lower() == "rectángulo":
        if len(dimensiones) != 2:
            return "Error: El rectángulo requiere largo y ancho."
        largo, ancho = dimensiones
        return largo * ancho

    else:
        return "Error: Tipo de polígono no soportado."


# Ejecutar la función para cada tipo de polígono
if __name__ == '__main__':
    # Área de un triángulo con base 5 y altura 3
    print("Área del triángulo:", calcular_area("triángulo", 5, 3))

    # Área de un cuadrado con lado 4
    print("Área del cuadrado:", calcular_area("cuadrado", 4))

    # Área de un rectángulo con largo 6 y ancho 2
    print("Área del rectángulo:", calcular_area("rectángulo", 6, 2))


