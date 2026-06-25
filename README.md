# Sistema de Gestion de Biblioteca Digital

Trabajo Final - Programacion Avanzada
Licenciatura en Ciencia de Datos

## Integrantes del grupo
- Barrios Jaqueline
- Batallanes Rodrigo
- Sosa Adrian
- Lara Levy

## Descripcion del tp

Sistema simple para gestionar libros, usuarios y prestamos de una biblioteca.

## Ejecutar en el main.py
Al iniciar pregunta si queres cargar datos de prueba para probar el sistema rapido.

## Estructura del tp

- libro.py: clase Libro
- usuario.py: clases Persona y Usuario (Usuario hereda de Persona)
- prestamo.py: clase Prestamo, conecta un libro con un usuario
- biblioteca.py: clase principal que maneja todo (patron Singleton)
- decorador.py: decorador que loguea cuando se ejecuta una operacion
- validador.py: metaclase que valida que las clases tengan mostrar_info
- main.py: menu por consola

## Requisitos del tp

- Herencia: Usuario hereda de Persona
- Polimorfismo: mostrar_info() es distinto en Persona y en Usuario
- Composicion: Prestamo no existe sin un Libro y un Usuario
- Agregacion: Biblioteca tiene una lista de libros, usuarios y prestamos
- Decorador propio: log_operacion
- Metaclase: Validador
- Patron de diseño: Singleton en Biblioteca, para que solo haya una biblioteca en todo el sistema
