class Componente:
    def __init__(self, codigo, nombre, tipo, marca, stock, ubicacion):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.stock = stock
        self.ubicacion = ubicacion

    def hay_stock(self):
        return self.stock > 0

    def mostrar_datos(self):
        print("\nCódigo:", self.codigo)
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo)
        print("Marca:", self.marca)
        print("Stock:", self.stock)
        print("Ubicación:", self.ubicacion)


componentes = [
    Componente("C01", "Resistencia 220Ω", "Resistencia", "Vishay", 50, "A1"),
    Componente("C02", "LED rojo", "LED", "Osram", 120, "A2"),
    Componente("C03", "Arduino Uno", "Placa", "Arduino", 15, "B1"),
    Componente("C04", "Resistencia 1kΩ", "Resistencia", "Yageo", 80, "A1"),
    Componente("C05", "Capacitor 100uF", "Capacitor", "Nichicon", 30, "A3"),
    Componente("C06", "LED verde", "LED", "Osram", 90, "A2"),
    Componente("C07", "Protoboard", "Placa", "MB-102", 20, "B2"),
    Componente("C08", "Capacitor 10uF", "Capacitor", "Nichicon", 45, "A3"),
    Componente("C09", "Arduino Nano", "Placa", "Arduino", 8, "B1"),
    Componente("C10", "Resistencia 10kΩ", "Resistencia", "Yageo", 65, "A1")
]


tipo_buscado = input("Ingrese el tipo de componente: ")
stock_minimo = int(input("Ingrese el stock mínimo: "))

cantidad = 0
mayor_stock = None

print("\n--- COMPONENTES ENCONTRADOS ---")

for componente in componentes:

    if componente.tipo.lower() == tipo_buscado.lower() and componente.stock >= stock_minimo:

        componente.mostrar_datos()

        cantidad += 1

        if mayor_stock is None or componente.stock > mayor_stock.stock:
            mayor_stock = componente


if cantidad == 0:

    print("No hay componentes que cumplan ambas condiciones.")

else:

    print("\nCantidad de componentes encontrados:", cantidad)

    print("\nComponente con mayor stock:")
    mayor_stock.mostrar_datos()