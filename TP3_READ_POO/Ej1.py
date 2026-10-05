class TicketSoporte:
    def __init__(self, numero, usuario, sector, problema, prioridad, estado):
        self.numero = numero
        self.usuario = usuario
        self.sector = sector
        self.problema = problema
        self.prioridad = prioridad
        self.estado = estado

    def mostrar_datos(self):
        print("\n--- DATOS DEL TICKET ---")
        print("Número:", self.numero)
        print("Usuario:", self.usuario)
        print("Sector:", self.sector)
        print("Problema:", self.problema)
        print("Prioridad:", self.prioridad)
        print("Estado:", self.estado)


tickets = [
    TicketSoporte(101, "Ana", "Administración", "No imprime", "Alta", "Pendiente"),
    TicketSoporte(102, "Luis", "Biblioteca", "PC lenta", "Media", "Resuelto"),
    TicketSoporte(103, "Marta", "Dirección", "Sin internet", "Alta", "Pendiente"),
    TicketSoporte(104, "Pedro", "Alumnos", "Teclado no funciona", "Baja", "Resuelto"),
    TicketSoporte(105, "Sofía", "Laboratorio", "Error de Windows", "Alta", "Pendiente"),
    TicketSoporte(106, "Juan", "Secretaría", "No inicia sesión", "Media", "Pendiente"),
    TicketSoporte(107, "Carla", "Biblioteca", "Problema con impresora", "Media", "Resuelto"),
    TicketSoporte(108, "Diego", "Laboratorio", "Monitor sin señal", "Alta", "Pendiente")
]


def buscar_ticket(numero):
    for ticket in tickets:
        if ticket.numero == numero:
            return ticket

    return None


numero = int(input("Ingrese el número de ticket: "))

ticket_encontrado = buscar_ticket(numero)

if ticket_encontrado is not None:
    ticket_encontrado.mostrar_datos()
else:
    print("Ticket no encontrado")


print("\n--- TICKETS PENDIENTES ---")

cantidad_pendientes = 0

for ticket in tickets:
    if ticket.estado.lower() == "pendiente":
        ticket.mostrar_datos()
        cantidad_pendientes += 1

print("\nCantidad de tickets pendientes:", cantidad_pendientes)