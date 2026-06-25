class Validador(type):
    def __new__(cls, nombre, bases, atributos):
        if nombre != "Validador" and "mostrar_info" not in atributos:
            print(f"Ojo: la clase {nombre} no tiene mostrar_info")
        return super().__new__(cls, nombre, bases, atributos)