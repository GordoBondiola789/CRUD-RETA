# Creamos una lista vacía para almacenar los alumnos
alumnos = []

# Iniciamos un bucle que continuará hasta que el usuario escriba SALIR
while True:

    # Pedimos el DNI o la palabra SALIR
    dni = input("\nIngrese el DNI del alumno o escriba SALIR: ")

    # Comprobamos si el usuario quiere terminar
    if dni.upper() == "SALIR":
        break

    # Convertimos el DNI ingresado a número entero
    dni = int(dni)

    # Variable que indica si el DNI ya existe
    existe = False

    # Recorremos la lista para buscar el DNI
    for alumno in alumnos:

        # Comprobamos si el DNI coincide con alguno registrado
        if alumno["dni"] == dni:
            existe = True
            break

    # Si el DNI ya existe, rechazamos el registro
    if existe:
        print("Error: ese DNI ya está registrado.")
        print("No se puede crear el alumno.")

    else:

        # Pedimos el resto de los datos del alumno
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = int(input("Ingrese la edad: "))
        promedio = float(input("Ingrese el promedio: "))

        # Creamos el diccionario del alumno
        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "edad": edad,
            "promedio": promedio
        }

        # Agregamos el alumno a la lista
        alumnos.append(alumno)

        # Informamos que el registro fue exitoso
        print("Alumno registrado correctamente.")

# Mostramos la lista final de alumnos
print("\nLista final de alumnos:")

# Recorremos y mostramos cada alumno
for alumno in alumnos:
    print(alumno)