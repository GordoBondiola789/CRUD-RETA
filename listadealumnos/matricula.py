alumnos = []  # Creamos una lista vacía para guardar los alumnos

while True:  # Creamos un bucle que se repetirá indefinidamente

    nombre = input("Ingrese el nombre del alumno (o escriba 'salir' para terminar): ")  # Pedimos un nombre

    if nombre == "salir":  # Comprobamos si el usuario escribió salir
        break  # Terminamos el bucle

    alumno = {  # Creamos un diccionario para representar al alumno
        "nombre": nombre  # Guardamos el nombre dentro del diccionario
    }

    alumnos.append(alumno)  # Agregamos el alumno a la lista

print("Cantidad de alumnos creados:", len(alumnos))  # Mostramos cuántos alumnos se crearon
print(alumnos)  # Mostramos la lista completa de alumnos