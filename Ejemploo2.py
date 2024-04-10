def calcular_producto_suma(Multiplicando, Multiplicador, Sumando):

    resultado = Multiplicando * Multiplicador + Sumando
    return resultado


def principal():
    # Definición de las variables con nombres más descriptivos
    primer_numero = 5
    segundo_numero = 3
    tercer_numero = 7

    # Llamada a la función calcular_producto_suma y almacenamiento del resultado
    Resultadototal = calcular_producto_suma(primer_numero, segundo_numero, tercer_numero)

    # Impresión del resultado
    print("El resultado de la operación es:", Resultadototal)


# Llamada a la función principal
if __name__ == "__main__":
    principal()