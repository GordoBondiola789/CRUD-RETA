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
        print("----- DATOS DEL ALUMNO -----")
        print("Nombre:", self.get_nombre())
        print("Apellido:", self.get_apellido())
        print("DNI:", self.get_dni())
        print("Curso:", self.get_curso())
        print("Promedio:", self.get_promedio())
# Prueba
alumno1 = Alumno("Juan", "Pérez", "45123456", "5°A", 8.5)
alumno1.mostrar_datos()
