
# Lista principal donde se almacenarán todos los productos
inventario = []


# Función: Agregar un producto al inventario
# Solicita datos, valida precio y cantidad, y guarda en diccionario

def agregar_producto():
    # Solicitar nombre del producto
    nombre = input("Ingrese el nombre del producto: ")

    # Validar precio
    while True:
        precio_input = input("Ingrese el precio del producto: ")
        try:
            precio = float(precio_input)
            if precio < 0:
                print("Error: el precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número válido.")

    # Validar cantidad
    while True:
        cantidad_input = input("Ingrese la cantidad del producto: ")
        try:
            cantidad = int(cantidad_input)
            if cantidad < 0:
                print("Error: la cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero válido.")

    # Crear el diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregar el producto a la lista inventario
    inventario.append(producto)

    print("Producto agregado correctamente.")


# Función: Mostrar todo el inventario
# Recorre la lista con un for e imprime cada producto

def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    print("\n--- Inventario Actual ---")
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
   


# Función: Calcular estadísticas del inventario
# Calcula valor total del inventario y cantidad de productos

def calcular_estadisticas():
    """Calcula y muestra el valor total del inventario y la cantidad de productos registrados."""
    if len(inventario) == 0:
        print("No hay productos para calcular estadísticas.")
        return

    valor_total = 0

    # Recorrer el inventario y sumar el valor de cada producto
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]

    cantidad_productos = len(inventario)

    print("\n--- Estadísticas del Inventario ---")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos registrados: {cantidad_productos}")
    

# Función principal con el menú interactivo
# Mantiene el programa activo hasta que el usuario elija salir

def menu():
    while True:
        print("\n========= MENÚ PRINCIPAL =========")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
     

        opcion = input("Seleccione una opción: ")

        # Validación de la opción con condicionales
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



# Ejecución del programa

menu()

