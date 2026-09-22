from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_dni(self):
        return self.__dni
    @abstractmethod
    def mostrar_datos(self):
        pass
class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, curso, promedio):
        super().__init__(nombre, apellido, dni)
        self.__curso = curso
        self.__promedio = promedio
    def get_curso(self):
        return self.__curso
    def get_promedio(self):
        return self.__promedio
    def mostrar_datos(self):
        print("Nombre:", self.get_nombre())
        print("Apellido:", self.get_apellido())
        print("DNI:", self.get_dni())
        print("Curso:", self.get_curso())
        print("Promedio:", self.get_promedio())
class GestorAcademico:
    def __init__(self):
        self.__base_datos_alumnos = []
    def registrar_nuevo_alumno(self, alumno):
        for alumno_existente in self.__base_datos_alumnos:
            if alumno_existente.get_dni() == alumno.get_dni():
                print("ALERTA: El DNI ya se encuentra registrado.")
                return False
        self.__base_datos_alumnos.append(alumno)
        print("Alumno registrado correctamente.")
        return True

    def mostrar_alumnos(self):
        print("\n===== ALUMNOS REGISTRADOS =====")

        for alumno in self.__base_datos_alumnos:
            alumno.mostrar_datos()
            print()


# Prueba
gestor = GestorAcademico()

alumno1 = Alumno("Juan", "Pérez", "45123456", "5°A", 8.5)
alumno2 = Alumno("María", "Gómez", "46234567", "5°B", 9.2)
alumno3 = Alumno("Pedro", "Rodríguez", "45123456", "5°C", 7.8)

gestor.registrar_nuevo_alumno(alumno1)
gestor.registrar_nuevo_alumno(alumno2)
gestor.registrar_nuevo_alumno(alumno3)

gestor.mostrar_alumnos()
