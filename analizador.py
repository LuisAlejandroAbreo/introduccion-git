def contar_palabras(ruta_arch):
    """
    Cuenta las lineas en un texto.
    
    Args:
        texto (str): La cadena de texto a analizar.
        
    Returns:
        int: Número total de líneas.
    """
    try:
        with open(ruta_arch, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return len(contenido.split())
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_arch}' no existe.")
        return 0
 
def contar_lineas(texto):
    """Cuenta las lineas en un texto."""
    return len(texto.splitlines())
 
if __name__ == "__main__":
    texto = "Hola mundo desde Git"
    print(f"Palabras: {contar_palabras(texto)}")
    print(f"Lineas: {contar_lineas(texto)}")