from libro import Libro
from usuario import Usuario
from prestamo import Prestamo
from decorador import log_operacion


class Biblioteca:
    instancia = None

    def __new__(cls):
        if cls.instancia is None:
            cls.instancia = super().__new__(cls)
            cls.instancia.libros = []
            cls.instancia.usuarios = []
            cls.instancia.prestamos = []
        return cls.instancia

    @log_operacion
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Se agrego el libro: {libro.titulo}")

    @log_operacion
    def eliminar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro is None:
            print("No se encontro ese libro")
            return
        if not libro.disponible:
            print("No se puede eliminar, esta prestado")
            return
        self.libros.remove(libro)
        print(f"Se elimino el libro: {libro.titulo}")

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def listar_libros(self):
        if len(self.libros) == 0:
            print("No hay libros cargados")
            return
        for libro in self.libros:
            libro.mostrar_info()

    @log_operacion
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Se agrego el usuario: {usuario.nombre_completo()}")

    def buscar_usuario(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario
        return None

    def listar_usuarios(self):
        if len(self.usuarios) == 0:
            print("No hay usuarios cargados")
            return
        for usuario in self.usuarios:
            usuario.mostrar_info()

    @log_operacion
    def hacer_prestamo(self, isbn, dni):
        libro = self.buscar_libro(isbn)
        usuario = self.buscar_usuario(dni)

        if libro is None:
            print("No se encontro el libro")
            return
        if usuario is None:
            print("No se encontro el usuario")
            return

        if libro.prestar():
            prestamo = Prestamo(libro, usuario)
            self.prestamos.append(prestamo)
            print(f"Prestamo realizado: {libro.titulo} a {usuario.nombre_completo()}")

    @log_operacion
    def devolver_prestamo(self, id_prestamo):
        for prestamo in self.prestamos:
            if prestamo.id == id_prestamo:
                prestamo.devolver()
                print(f"Se devolvio el libro: {prestamo.libro.titulo}")
                return
        print("No se encontro ese prestamo")

    def listar_prestamos_activos(self):
        activos = [p for p in self.prestamos if p.activo]
        if len(activos) == 0:
            print("No hay prestamos activos")
            return
        for prestamo in activos:
            prestamo.mostrar_info()