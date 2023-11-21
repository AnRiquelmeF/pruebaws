class Producto:
    def __init__(self, id, nombre, autor, precio, genero):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.precio = precio
        self.genero = genero

# Lista temporal para almacenar productos
catalogo = []

def create_product(catalogo):
    try:
        nombre = input("Por favor, introduce el nombre del producto: ")
        precio = float(input("Por favor, introduce el precio del producto: "))

        # Validate that the price is positive
        if precio <= 0:
            print("El precio debe ser un valor positivo.")
            return

        tipo = input("Por favor, introduce el tipo del producto (1=Libro; 2=Otro): ")

        # Validate that the type is either '1' or '2'
        if tipo not in ['1', '2']:
            print("El tipo debe ser 1 (Libro) o 2 (Otro).")
            return

        if tipo == '1':
            autor = input("Por favor, introduce el nombre del autor: ")
            genero = input("Por favor, introduce el genero del libro: ")
        else:
            autor = ""
            genero = ""

        # Crear un nuevo objeto Producto y agregarlo a la lista
        nuevo_producto = Producto(len(catalogo) + 1, nombre, autor, precio, genero)
        catalogo.append(nuevo_producto)

        print("Producto creado con éxito.")

    except ValueError as ve:
        print(f'Error al crear producto: {str(ve)}')

def read_catalog(catalogo):
    try:
        # Mostrar todos los productos en el catálogo
        for producto in catalogo:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}")

    except Exception as e:
        print(f'Error al leer el catálogo: {str(e)}')

def update_product(catalogo, id_producto, nuevo_precio):
    try:
        # Validate that the product ID exists
        if not any(producto.id == id_producto for producto in catalogo):
            print(f"No se encontró ningún producto con el ID {id_producto}.")
            return

        # Buscar el producto en la lista por ID y actualizar el precio
        for producto in catalogo:
            if producto.id == id_producto:
                producto.precio = nuevo_precio
                print("Producto actualizado con éxito.")
                return

    except ValueError as ve:
        print(f'Error al actualizar producto: {str(ve)}')

def delete_product(catalogo, id_producto):
    try:
        # Validate that the product ID exists
        if not any(producto.id == id_producto for producto in catalogo):
            print(f"No se encontró ningún producto con el ID {id_producto}.")
            return

        # Eliminar el producto de la lista por ID
        catalogo = [producto for producto in catalogo if producto.id != id_producto]
        print("Producto eliminado con éxito.")

    except ValueError as ve:
        print(f'Error al eliminar producto: {str(ve)}')

if __name__ == "__main__":
    while True:
        print("\nPor favor, seleccione una opción:\n"
              "1: Ver Catálogo\n"
              "2: Crear Producto\n"
              "3: Actualizar Producto\n"
              "4: Eliminar Producto\n"
              "5: Salir")

        option = input("Seleccione: ")

        if option == '1':
            read_catalog(catalogo)
        elif option == '2':
            create_product(catalogo)
        elif option == '3':
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            update_product(catalogo, id_producto, nuevo_precio)
        elif option == '4':
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            delete_product(catalogo, id_producto)
        elif option == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
