# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):

    area = base * altura
    return area

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):

    area = 0.5 * base * altura
    return area

# Función principal
def main():
    # Área del rectángulo
    base_rectangulo = 4
    altura_rectangulo = 6
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    print("Área del rectángulo:", area_rectangulo)

    # Área del triángulo
    base_triangulo = 5
    altura_triangulo = 8
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

if __name__ == "__main__":
    main()
