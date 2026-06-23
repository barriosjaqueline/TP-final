class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def mostrar_info(self):
        print(f"{self.nombre_completo()} - DNI: {self.dni}")


class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido, dni)
        self.email = email
        self.activo = True

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Inactivo"
        print(f"{self.nombre_completo()} - DNI: {self.dni} - Email: {self.email} - {estado}")

    def desactivar(self):
        self.activo = False
