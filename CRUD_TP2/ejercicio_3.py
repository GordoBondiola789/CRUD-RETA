# Pedimos los datos del alumno
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
dni = int(input("Ingrese el DNI: "))
edad = int(input("Ingrese la edad: "))
promedio = float(input("Ingrese el promedio: "))

# Verificamos que la edad esté entre 17 y 99 años
if edad >= 17 and edad <= 99:

    # Creamos el diccionario si la edad es válida
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "edad": edad,
        "promedio": promedio
    }

    # Mostramos el alumno registrado
    print("\nAlumno registrado correctamente:")
    print(alumno)

else:

    # Mostramos un mensaje si la edad no es válida
    print("\nError: la edad debe estar entre 17 y 99 anos.")

    # Informamos que el registro no fue guardado
    print("El registro fue descartado.")