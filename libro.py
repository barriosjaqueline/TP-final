class Libro:
    def __init__(self, titulo, autor, isbn, año, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año = año
        self.paginas = paginas
        self.disponible = True  

    def prestar(self):
        if not self.disponible:
            print("Este libro ya esta prestado")
            return False
        self.disponible = False
        return True

    def devolver(self):
        self.disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"{self.titulo} - {self.autor} ({self.año}) - ISBN: {self.isbn} - {estado}")

    def __str__(self):
        return f"{self.titulo} de {self.autor}"
