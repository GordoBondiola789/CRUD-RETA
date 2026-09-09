# Creamos una lista vacía para guardar los alumnos
alumnos = []

# Preguntamos cuántos alumnos se quieren registrar
cantidad = int(input("¿Cuántos alumnos desea registrar? "))

# Repetimos el proceso según la cantidad indicada
for i in range(cantidad):

    # Mostramos el número de alumno que estamos registrando
    print(f"\nAlumno {i + 1}")

    # Pedimos los datos del alumno
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = int(input("Ingrese el DNI: "))
    promedio = float(input("Ingrese el promedio: "))

    # Creamos el diccionario del alumno
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "promedio": promedio
    }

    # Agregamos el alumno a la lista
    alumnos.append(alumno)

# Mostramos la lista completa al finalizar
print("\nLista completa de alumnos:")
print(alumnos)