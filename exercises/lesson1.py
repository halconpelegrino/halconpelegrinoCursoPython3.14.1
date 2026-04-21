def saludo(nombre :str)-> str:
    """ Devuelve un saludo personalizado para el nombre dado."""
    return f"Hola, {nombre}! Bienvenido a Python."
if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    nombre = input("Nombre: ")
    print(saludo(nombre))