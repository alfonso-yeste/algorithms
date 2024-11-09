"""""
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */
"""

from datetime import datetime

def dias_entre_fechas(fecha1, fecha2):
    try:
        formato = "%d/%m/%Y"
        fecha1_obj = datetime.strptime(fecha1, formato)
        fecha2_obj = datetime.strptime(fecha2, formato)

        diferencia = abs((fecha2_obj - fecha1_obj).days)
        return diferencia

if __name__ == '__main__':
    fecha1 = "10/11/2024"
    fecha2 = "04/11/2024"
    try:
        dias_diferencia = dias_entre_fechas(fecha1, fecha2)
        print(f"La diferencia en días entre {fecha1} y {fecha2} es: {dias_diferencia} días.")




