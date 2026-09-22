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
        return (
            f"Nombre: {self.get_nombre()}\n"
            f"Apellido: {self.get_apellido()}\n"
            f"DNI: {self.get_dni()}\n"
            f"Curso: {self.get_curso()}\n"
            f"Promedio: {self.get_promedio()}"
        )
class EstrategiaGuardado(ABC):
    @abstractmethod
    def guardar(self, datos):
        pass
class GuardadoMemoria(EstrategiaGuardado):
    def guardar(self, datos):
        print("Alumno guardado temporalmente en memoria RAM.")
class GuardadoArchivoTXT(EstrategiaGuardado):
    def guardar(self, datos):
        with open("registro_alumnos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(datos)
            archivo.write("\n")
            archivo.write("-" * 40)
            archivo.write("\n")
        print("Alumno guardado en registro_alumnos.txt.")
class GestorAcademico:
    def __init__(self, estrategia_guardado):
        self.__base_datos_alumnos = []
        self.__estrategia_guardado = estrategia_guardado
    def registrar_nuevo_alumno(self, alumno):
        for alumno_existente in self.__base_datos_alumnos:
            if alumno_existente.get_dni() == alumno.get_dni():
                print("ALERTA: El DNI ya se encuentra registrado.")
                return False
        self.__base_datos_alumnos.append(alumno)
        datos = alumno.mostrar_datos()
        self.__estrategia_guardado.guardar(datos)
        print("CREATE realizado correctamente.")
        return True
    def mostrar_alumnos(self):
        print("\n===== BASE DE DATOS DE ALUMNOS =====")
        for alumno in self.__base_datos_alumnos:
            print(alumno.mostrar_datos())
            print("-" * 40)
# Prueba con guardado en archivo
estrategia = GuardadoArchivoTXT()
gestor = GestorAcademico(estrategia)
alumno1 = Alumno("Juan", "Pérez", "45123456", "5°A", 8.5)
alumno2 = Alumno("María", "Gómez", "46234567", "5°B", 9.2)
alumno3 = Alumno("Pedro", "Rodríguez", "45123456", "5°C", 7.8)
gestor.registrar_nuevo_alumno(alumno1)
gestor.registrar_nuevo_alumno(alumno2)
gestor.registrar_nuevo_alumno(alumno3)
gestor.mostrar_alumnos()
