class Reparacion:
    def __init__(self, orden, cliente, equipo, falla, estado, tecnico, costo_estimado):
        self.orden = orden
        self.cliente = cliente
        self.equipo = equipo
        self.falla = falla
        self.estado = estado
        self.tecnico = tecnico
        self.costo_estimado = costo_estimado

    def mostrar_datos(self):
        print("\n--- DATOS DE LA REPARACIÓN ---")
        print("Orden:", self.orden)
        print("Cliente:", self.cliente)
        print("Equipo:", self.equipo)
        print("Falla:", self.falla)
        print("Estado:", self.estado)
        print("Técnico:", self.tecnico)
        print("Costo estimado: $", self.costo_estimado)


reparaciones = [
    Reparacion(1001, "Ana", "Notebook", "No enciende", "Pendiente", "Carlos", 45000),
    Reparacion(1002, "Luis", "PC", "Pantalla azul", "En reparación", "María", 30000),
    Reparacion(1003, "Sofía", "Notebook", "Teclado dañado", "Finalizada", "Carlos", 22000),
    Reparacion(1004, "Juan", "PC", "No tiene internet", "Pendiente", "Pedro", 18000),
    Reparacion(1005, "Marta", "Notebook", "Batería defectuosa", "En reparación", "María", 50000),
    Reparacion(1006, "Diego", "PC", "Limpieza", "Finalizada", "Pedro", 12000),
    Reparacion(1007, "Carla", "Notebook", "Disco dañado", "Pendiente", "Carlos", 65000),
    Reparacion(1008, "Pablo", "PC", "Fuente defectuosa", "En reparación", "Pedro", 40000),
    Reparacion(1009, "Laura", "Notebook", "Sistema lento", "Finalizada", "María", 15000),
    Reparacion(1010, "Nicolás", "PC", "RAM defectuosa", "Pendiente", "Carlos", 28000)
]


def buscar_por_orden(numero):

    for reparacion in reparaciones:

        if reparacion.orden == numero:
            return reparacion

    return None


def filtrar_por_estado(estado):

    encontrados = 0

    for reparacion in reparaciones:

        if reparacion.estado.lower() == estado.lower():

            reparacion.mostrar_datos()
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron reparaciones con ese estado.")


def filtrar_por_tecnico(tecnico):

    encontrados = 0

    for reparacion in reparaciones:

        if reparacion.tecnico.lower() == tecnico.lower():

            reparacion.mostrar_datos()
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron reparaciones para ese técnico.")


def filtrar_por_costo(limite):

    encontrados = 0

    for reparacion in reparaciones:

        if reparacion.costo_estimado <= limite:

            reparacion.mostrar_datos()
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron reparaciones dentro de ese costo.")


while True:

    print("\n===== SERVICIO TÉCNICO =====")
    print("1) Mostrar todas")
    print("2) Buscar por orden")
    print("3) Filtrar por estado")
    print("4) Filtrar por técnico")
    print("5) Filtrar por costo")
    print("6) Salir")

    opcion = input("Seleccione una opción: ")


    if opcion == "1":

        for reparacion in reparaciones:
            reparacion.mostrar_datos()


    elif opcion == "2":

        numero = int(input("Ingrese el número de orden: "))

        reparacion = buscar_por_orden(numero)

        if reparacion is not None:
            reparacion.mostrar_datos()
        else:
            print("Reparación no encontrada.")


    elif opcion == "3":

        estado = input("Ingrese el estado: ")

        filtrar_por_estado(estado)


    elif opcion == "4":

        tecnico = input("Ingrese el nombre del técnico: ")

        filtrar_por_tecnico(tecnico)


    elif opcion == "5":

        limite = float(input("Ingrese el costo máximo: "))

        filtrar_por_costo(limite)


    elif opcion == "6":

        print("Programa finalizado.")
        break


    else:

        print("Opción inválida.")