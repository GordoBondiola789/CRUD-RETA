class RecursoDigital:
    def __init__(self, codigo, titulo, categoria, autor, anio, disponible):
        self.codigo = codigo
        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.anio = anio
        self.disponible = disponible

    def mostrar_resumen(self):
        if self.disponible:
            disponibilidad = "Disponible"
        else:
            disponibilidad = "No disponible"

        print("\nCódigo:", self.codigo)
        print("Título:", self.titulo)
        print("Categoría:", self.categoria)
        print("Disponibilidad:", disponibilidad)


recursos = [
    RecursoDigital("R01", "Python desde cero", "Libro digital", "A. Pérez", 2024, True),
    RecursoDigital("R02", "Python avanzado", "Tutorial", "M. López", 2023, False),
    RecursoDigital("R03", "Manual de redes", "Manual", "J. Gómez", 2022, True),
    RecursoDigital("R04", "Introducción a HTML", "Libro digital", "L. Díaz", 2024, True),
    RecursoDigital("R05", "Python para principiantes", "Video educativo", "C. Ruiz", 2025, True),
    RecursoDigital("R06", "Revista de tecnología", "Revista", "Editorial Tec", 2025, False),
    RecursoDigital("R07", "JavaScript básico", "Tutorial", "S. Torres", 2023, True),
    RecursoDigital("R08", "Manual de bases de datos", "Manual", "F. Silva", 2024, False),
    RecursoDigital("R09", "Python y POO", "Video educativo", "D. Fernández", 2025, True),
    RecursoDigital("R10", "Sistemas digitales", "Libro digital", "R. Castro", 2022, True)
]


busqueda = input("Ingrese una palabra o parte del título: ")

busqueda = busqueda.lower()

cantidad_coincidencias = 0
cantidad_disponibles = 0

print("\n--- RESULTADOS ---")

for recurso in recursos:

    if busqueda in recurso.titulo.lower():

        recurso.mostrar_resumen()

        cantidad_coincidencias += 1

        if recurso.disponible:
            cantidad_disponibles += 1


if cantidad_coincidencias == 0:
    print("No se encontraron coincidencias.")
else:
    print("\nCantidad de coincidencias:", cantidad_coincidencias)
    print("Cantidad disponibles:", cantidad_disponibles)