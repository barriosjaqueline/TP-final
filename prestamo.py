from datetime import datetime

class Prestamo:
    contador = 0 

    def __init__(self, libro, usuario):
        Prestamo.contador += 1
        self.id = Prestamo.contador
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None
        self.activo = True

    def devolver(self):
        if not self.activo:
            print("Este prestamo ya fue devuelto")
            return
        self.fecha_devolucion = datetime.now()
        self.activo = False
        self.libro.devolver()

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Devuelto"
        fecha = self.fecha_prestamo.strftime("%d/%m/%Y")
        print(f"Prestamo #{self.id} - {self.libro.titulo} - {self.usuario.nombre_completo()} - {fecha} - {estado}")