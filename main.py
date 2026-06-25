from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario


def menu_libros(bib):
    while True:
        print("\n--- LIBROS ---")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Listar libros")
        print("0. Volver")

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            año = int(input("Año: "))
            paginas = int(input("Paginas: "))
            libro = Libro(titulo, autor, isbn, año, paginas)
            bib.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            bib.eliminar_libro(isbn)

        elif opcion == "3":
            bib.listar_libros()

        elif opcion == "0":
            break

        else:
            print("Opcion invalida")


def menu_usuarios(bib):
    while True:
        print("\n--- USUARIOS ---")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("0. Volver")

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            email = input("Email: ")
            usuario = Usuario(nombre, apellido, dni, email)
            bib.agregar_usuario(usuario)

        elif opcion == "2":
            bib.listar_usuarios()

        elif opcion == "0":
            break

        else:
            print("Opcion invalida")


def menu_prestamos(bib):
    while True:
        print("\n--- PRESTAMOS ---")
        print("1. Hacer prestamo")
        print("2. Devolver prestamo")
        print("3. Ver prestamos activos")
        print("0. Volver")

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            isbn = input("ISBN del libro: ")
            dni = input("DNI del usuario: ")
            bib.hacer_prestamo(isbn, dni)

        elif opcion == "2":
            id_prestamo = int(input("ID del prestamo: "))
            bib.devolver_prestamo(id_prestamo)

        elif opcion == "3":
            bib.listar_prestamos_activos()

        elif opcion == "0":
            break

        else:
            print("Opcion invalida")


def cargar_datos_de_prueba(bib):
    libro1 = Libro("El Principito", "Saint-Exupery", "111", 1943, 96)
    libro2 = Libro("1984", "Orwell", "222", 1949, 328)
    libro3 = Libro("Dune", "Herbert", "333", 1965, 412)

    usuario1 = Usuario("Jaqueline", "Barrios", "30111222", "jaquelinebarrios@mail.com")
    usuario2 = Usuario("Lara", "Levy", "28333444", "laralevy@mail.com")

    bib.agregar_libro(libro1)
    bib.agregar_libro(libro2)
    bib.agregar_libro(libro3)
    bib.agregar_usuario(usuario1)
    bib.agregar_usuario(usuario2)

    print("Datos de prueba cargados")


def main():
    bib = Biblioteca()

    cargar = input("Queres cargar datos de prueba? (s/n): ").strip().lower()
    if cargar in ("s", "si", "sí"):
        cargar_datos_de_prueba(bib)

    while True:
        print("\n===== BIBLIOTECA DIGITAL =====")
        print("1. Gestion de libros")
        print("2. Gestion de usuarios")
        print("3. Gestion de prestamos")
        print("0. Salir")

        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            menu_libros(bib)
        elif opcion == "2":
            menu_usuarios(bib)
        elif opcion == "3":
            menu_prestamos(bib)
        elif opcion == "0":
            print("Chau!")
            break
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()