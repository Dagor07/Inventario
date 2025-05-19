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
    año = validar_entrada("Año de publicación: ", int, lambda x: 1500 <= x <= datetime.date.today().year)
    categoria = input("Categoría (Ficción, No Ficción, Infantil, Educativo): ").strip()
    if categoria not in ['Ficción', 'No Ficción', 'Infantil', 'Educativo']:
        print("Categoría inválida.")
        return
    libro = {
        "id": generar_id(),
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "categoria": categoria,
        "estado": "Disponible"
    }
    libros.append(libro)
    print(" Libro registrado correctamente.")



def lend_book():
    id_libro = validar_entrada("ID del libro a prestar: ")
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


def show_books(books, filter = None):
    print(f"{"****Listado de libros****"}".rjust(60))
    print("*"*115)
    print(f"\n{"ID".center(10)}|{"Titulo del libro".center(25)}|{"Autor".center(25)}|{"Año de publicacion".center(20)}|{"Categoria".center(15)}|{"Estado".center(15)}")
    print("*"*115)
    found = False
    for book in books:
        if filter is None or book["estado"] == filter:
            found = True

            id = str(book["id"])
            title = str(book["titulo"]).capitalize()
            author = str(book["autor"]).title()
            year = str(book["año"])
            category = str(book["categoria"]).capitalize()
            condition = str(book["estado"]).capitalize()
            print(f"{id.center(10)}|{title.center(25)}|{author.center(25)}|{year.center(20)}|{category.center(15)}|{condition.center(15)}")
            print("-"*115)
    if not found and filter:
        print(f"\nNo se encontraron libros con estado '{filter}'.\n")
    elif not found and filter is None:
         print("No hay libros registrados.")




def search_book(books, search):
    
    print("*"*115)
    print(f"\n{"ID".center(10)}|{"Titulo del libro".center(25)}|{"Autor".center(25)}|{"Año".center(20)}|{"Categoria".center(15)}|{"Estado".center(15)}")
    print("*"*115)
    found  = False
    search = search.lower()
    for book in books:
        title = book["titulo"]
        author = book["autor"]
        category = book["categoria"]
        if search in title or search in author or search in category:
            found  = True
            id = str(book["id"])
            title = str(book["titulo"]).capitalize()
            author = str(book["autor"]).title()
            year = str(book["año"])
            category = str(book["categoria"]).capitalize()
            condition = str(book["estado"]).capitalize()
          
            print(f"{id.center(10)}|{title.center(25)}|{author.center(25)}|{year.center(20)}|{category.center(15)}|{condition.center(15)}")
            print("-"*115)
    if not found:
        print("No se encontraron libros que coincidan con la búsqueda.")
        
