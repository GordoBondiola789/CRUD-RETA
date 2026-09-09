# Pedimos los datos del alumno
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")

# Convertimos el DNI a número entero
dni = int(input("Ingrese el DNI: "))

# Convertimos el promedio a número decimal
promedio = float(input("Ingrese el promedio: "))

# Creamos un diccionario con los datos del alumno
alumno = {
    "nombre": nombre,
    "apellido": apellido,
    "dni": dni,
    "promedio": promedio
}

# Mostramos los datos del alumno por pantalla
print("\nDatos del alumno:")
print(alumno)