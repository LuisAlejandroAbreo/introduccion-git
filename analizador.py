def contar_palabras(texto):
    """Cuenta las palabras en un texto."""
    return len(texto.split())
 
def contar_lineas(texto):
    """Cuenta las lineas en un texto."""
    return len(texto.splitlines())
 
if __name__ == "__main__":
    texto = "Hola mundo desde Git"
    print(f"Palabras: {contar_palabras(texto)}")
    print(f"Lineas: {contar_lineas(texto)}")