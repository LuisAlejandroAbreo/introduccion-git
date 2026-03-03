# sistema de gestion de biblioteca
# version : 0.2
# autor : grupo C3 - Campus Lands

libros = []

def buscar_libro(criterio):
    """Busca libros por título o autor"""
    criterio = criterio.lower()
    resultados = []

    for libro in libros:
        titulo_coincide = criterio in libro['titulo'].lower()
        autor_coincide = criterio in libro['autor'].lower()

        if titulo_coincide or autor_coincide:
            resultados.append(libro)

    if not resultados:
        print(f"No se encontraron libros con '{criterio}'")
        return resultados

    print(f"\n=== Resultados para '{criterio}' ===")
    for libro in resultados:
        estado = "Disponible" if libro['disponible'] else "Prestado"
        print(f"- {libro['titulo']} por {libro['autor']} [{estado}]")

    return resultados


def agregar_libro(titulo, autor, isbn):
    """Agrega un libro a la biblioteca"""
    libro = {
        'titulo': titulo,
        'autor': autor,
        'isbn': isbn,
        'disponible': True
    }
    libros.append(libro)
    print(f"✓ Libro '{titulo}' agregado exitosamente")


def listar_libros():
    """Lista todos los libros"""
    if not libros:
        print("No hay libros en la biblioteca")
        return

    print("\n=== Libros en la Biblioteca ===")
    for i, libro in enumerate(libros, 1):
        estado = "Disponible" if libro['disponible'] else "Prestado"
        print(f"{i}. {libro['titulo']} - {libro['autor']} [{estado}]")


# Programa principal
if __name__ == "__main__":
    # Agregar algunos libros de ejemplo
    agregar_libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728")
    agregar_libro("1984", "George Orwell", "978-0451524935")
    agregar_libro("El Quijote", "Miguel de Cervantes", "978-8424936464")

 # Buscar libros
    buscar_libro("garcía")
    buscar_libro("1984")
    buscar_libro("python")  # No existe

    # Listar libros
    listar_libros()
