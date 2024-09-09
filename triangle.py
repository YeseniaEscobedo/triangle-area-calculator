def calculate_triangle_area(base, height):
    """
    Calcula el área de un triángulo dado la base y la altura.
    Fórmula: (base * altura) / 2
    """
    if base <= 0 or height <= 0:
        raise ValueError("La base y la altura deben ser mayores que 0")
    return (base * height) / 2
