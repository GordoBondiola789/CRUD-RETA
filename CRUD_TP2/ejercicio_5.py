def registrar_nuevo_alumno():

    # Pedimos los datos de texto del alumno
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")

    # Intentamos convertir DNI y edad a números
    try:
        dni = int(input("Ingrese el DNI: "))
        edad = int(input("Ingrese la edad: "))

    # Si se ingresan letras en lugar de números,
    # mostramos un mensaje de error
    except ValueError:
        print("Error: el DNI y la edad deben ser números.")
        return

    # Pedimos el promedio del alumno
    promedio = float(input("Ingrese el promedio: "))

    # Creamos el diccionario con todos los datos
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad,
        "promedio": promedio
    }

    # Abrimos el archivo en modo agregar
    # para conservar los alumnos registrados anteriormente
    with open("alumnos.txt", "a", encoding="utf-8") as archivo:

        # Guardamos los datos del alumno en el archivo
        archivo.write(str(alumno) + "\n")

    # Mostramos un mensaje confirmando el registro
    print("\nAlumno registrado correctamente.")

    # Informamos dónde se guardaron los datos
    print("Los datos fueron guardados en alumnos.txt")


# Llamamos a la función para comenzar el registro
registrar_nuevo_alumno()