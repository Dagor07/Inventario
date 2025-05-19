import datetime
import json

libros = []
contador_id = 1
prestamos_por_persona = {}

def generate_id():
    global contador_id
    nuevo_id = contador_id
    contador_id += 1
    return nuevo_id

def validate_entry(texto, tipo=int, condiciones=None):
    while True:
        valor = input(texto)
        if not valor.strip():
            print("El campo no puede estar vacío.")
            continue
        try:
            if tipo == int:
                valor = int(valor)
            if condiciones and not condiciones(valor):
                print("Valor fuera de rango o inválido.")
                continue
            return valor
        except:
            print("Formato inválido.")

def register_book():
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    año = validate_entry("Año de publicación: ", int, lambda x: 1500 <= x <= datetime.date.today().year)
    categoria = input("Categoría (Ficción, No Ficción, Infantil, Educativo): ").strip()
    if categoria not in ['Ficción', 'No Ficción', 'Infantil', 'Educativo']:
        print("Categoría inválida.")
        return
    libro = {
        "id": generate_id(),
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "categoria": categoria,
        "estado": "Disponible"
    }
    libros.append(libro)
    print(" Libro registrado correctamente.")



def lend_book():
    id_libro = validate_entry("ID del libro a prestar: ")
    libro = next((l for l in libros if l["id"] == id_libro), None)
    if not libro:
        print("Libro no encontrado.")
        return
    if libro["estado"] == "Prestado":
        print("El libro ya está prestado.")
        return
    nombre = input("Nombre de quien presta: ").strip()
    if prestamos_por_persona.get(nombre, 0) >= 3:
        print("No puede prestar más de 3 libros.")
        return
    libro["estado"] = "Prestado"
    libro["prestamo"] = {
        "nombre": nombre,
        "fecha": str(datetime.date.today())
    }
    prestamos_por_persona[nombre] = prestamos_por_persona.get(nombre, 0) + 1
    print(" Libro prestado correctamente.")
