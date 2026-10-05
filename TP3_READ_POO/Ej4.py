class Videojuego:
    def __init__(self, codigo, titulo, genero, plataforma, anio, horas_estimadas):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.anio = anio
        self.horas_estimadas = horas_estimadas

    def mostrar_datos(self):
        print("\nCódigo:", self.codigo)
        print("Título:", self.titulo)
        print("Género:", self.genero)
        print("Plataforma:", self.plataforma)
        print("Año:", self.anio)
        print("Horas estimadas:", self.horas_estimadas)

    def es_del_genero(self, genero):
        return self.genero.lower() == genero.lower()

    def supera_horas(self, cantidad):
        return self.horas_estimadas > cantidad


videojuegos = [
    Videojuego("V01", "Minecraft", "Sandbox", "PC", 2011, 100),
    Videojuego("V02", "FIFA 25", "Deportes", "PS5", 2024, 80),
    Videojuego("V03", "God of War Ragnarök", "Acción", "PS5", 2022, 30),
    Videojuego("V04", "The Sims 4", "Simulación", "PC", 2014, 200),
    Videojuego("V05", "Forza Horizon 5", "Carreras", "Xbox", 2021, 50),
    Videojuego("V06", "Resident Evil 4", "Terror", "PS5", 2023, 20),
    Videojuego("V07", "EA Sports FC 25", "Deportes", "PC", 2024, 70),
    Videojuego("V08", "Hollow Knight", "Metroidvania", "PC", 2017, 35)
]


def buscar_por_codigo(codigo):

    for juego in videojuegos:

        if juego.codigo.lower() == codigo.lower():
            return juego

    return None


genero = input("Ingrese un género: ")

cantidad_genero = 0

print("\n--- VIDEOJUEGOS DEL GÉNERO ---")

for juego in videojuegos:

    if juego.es_del_genero(genero):

        juego.mostrar_datos()
        cantidad_genero += 1


if cantidad_genero == 0:
    print("No se encontraron videojuegos de ese género.")


horas = float(input("\nIngrese una cantidad de horas: "))

cantidad_horas = 0

print("\n--- VIDEOJUEGOS QUE SUPERAN LAS HORAS ---")

for juego in videojuegos:

    if juego.supera_horas(horas):

        juego.mostrar_datos()
        cantidad_horas += 1


if cantidad_horas == 0:
    print("No hay videojuegos que superen esa duración.")


codigo = input("\nIngrese el código del videojuego: ")

juego_encontrado = buscar_por_codigo(codigo)

if juego_encontrado is not None:

    juego_encontrado.mostrar_datos()

else:

    print("Videojuego no encontrado.")