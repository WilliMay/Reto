"""
Sistema de Carrito de Compras
Este programa implementa un sistema de gestión de carrito de compras que permite
a los usuarios agregar productos, calcular descuentos y generar tickets de compra.
"""

def validar_numero_positivo(valor):
    """
    Valida que un valor ingresado sea un número positivo.
    Args:
        valor: El valor a validar
    Returns:
        bool: True si es un número positivo, False en caso contrario
    """
    try:
        numero = float(valor)
        return numero > 0
    except ValueError:
        return False

def calcular_descuento(cantidad, subtotal):
    """
    Calcula el descuento basado en la cantidad de productos.
    Args:
        cantidad: Número de unidades del producto
        subtotal: Monto total sin descuento
    Returns:
        float: Monto del descuento aplicado
    """
    if cantidad >= 10:
        return subtotal * 0.15  # 15% descuento
    elif cantidad >= 5:
        return subtotal * 0.10  # 10% descuento
    elif cantidad >= 3:
        return subtotal * 0.05  # 5% descuento
    return 0

def agregar_producto(productos):
    """
    Agrega un nuevo producto al carrito.
    Solicita nombre, cantidad y precio, valida los datos y calcula descuentos.
    Args:
        productos: Lista de productos en el carrito
    """
    nombre = input("Nombre del producto: ")
    while True:
        cantidad = input("Cantidad: ")
        if not validar_numero_positivo(cantidad):
            print("La cantidad debe ser un número positivo")
            continue
        cantidad = int(cantidad)
        
        precio = input("Precio unitario: $")
        if not validar_numero_positivo(precio):
            print("El precio debe ser un número positivo")
            continue
        precio = float(precio)
        break

    subtotal = cantidad * precio
    descuento = calcular_descuento(cantidad, subtotal)
    total = subtotal - descuento
    
    if total > PRESUPUESTO_LIMITE:
        print(f"¡Advertencia! El total supera el presupuesto límite de ${PRESUPUESTO_LIMITE:.2f}")
        if input("¿Desea continuar? (s/n): ").lower() != 's':
            return

    productos.append({
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio,
        'subtotal': subtotal,
        'descuento': descuento,
        'total': total
    })
    print("Producto agregado exitosamente")

def mostrar_carrito(productos):
    """
    Muestra el contenido actual del carrito.
    Incluye detalles de cada producto y el total a pagar.
    Args:
        productos: Lista de productos en el carrito
    """
    if not productos:
        print("\nEl carrito está vacío")
        return

    print("\n=== PRODUCTOS EN CARRITO ===")
    for i, producto in enumerate(productos, 1):
        print(f"\n{i}. Producto: {producto['nombre']}")
        print(f"   Cantidad: {producto['cantidad']}")
        print(f"   Precio unitario: ${producto['precio']:.2f}")
        print(f"   Subtotal: ${producto['subtotal']:.2f}")
        print(f"   Descuento: ${producto['descuento']:.2f}")
        print(f"   Total: ${producto['total']:.2f}")
    
    total_compra = sum(producto['total'] for producto in productos)
    print(f"\nTotal a pagar: ${total_compra:.2f}")

def eliminar_producto(productos):
    """
    Elimina un producto del carrito.
    Muestra la lista de productos y permite seleccionar cuál eliminar.
    Args:
        productos: Lista de productos en el carrito
    """
    if not productos:
        print("\nNo hay productos para eliminar")
        return

    mostrar_carrito(productos)
    while True:
        try:
            indice = int(input("\nIngrese el número del producto a eliminar (0 para cancelar): ")) - 1
            if indice == -1:
                return
            if 0 <= indice < len(productos):
                producto = productos.pop(indice)
                print(f"Producto '{producto['nombre']}' eliminado exitosamente")
                return
            print("Número de producto inválido")
        except ValueError:
            print("Por favor, ingrese un número válido")

def generar_ticket(productos):
    """
    Genera un ticket de compra con el resumen del pedido.
    Args:
        productos: Lista de productos en el carrito
    Returns:
        str: Ticket formateado con los detalles de la compra
    """
    if not productos:
        return "No hay productos en el carrito"

    total_compra = sum(producto['total'] for producto in productos)
    total_descuento = sum(producto['descuento'] for producto in productos)

    ticket = "\n====== TICKET DE COMPRA ======\n"
    for i, producto in enumerate(productos, 1):
        ticket += f"\n{i}. {producto['nombre']}"
        ticket += f"\n   Cantidad: {producto['cantidad']}"
        ticket += f"\n   Precio unitario: ${producto['precio']:.2f}"
        ticket += f"\n   Subtotal: ${producto['subtotal']:.2f}"
        ticket += f"\n   Descuento: ${producto['descuento']:.2f}"
        ticket += f"\n   Total: ${producto['total']:.2f}"
        ticket += "\n-------------------------"

    ticket += f"\n\nTotal descuentos: ${total_descuento:.2f}"
    ticket += f"\nTotal a pagar: ${total_compra:.2f}"
    ticket += "\n\n¡Gracias por su compra!"
    return ticket

def menu():
    """
    Función principal que muestra el menú interactivo y maneja las opciones del usuario.
    Permite agregar, ver, eliminar productos y finalizar la compra.
    """
    productos = []
    while True:
        print("\n=== MENÚ CARRITO DE COMPRAS ===")
        print("1. Agregar producto al carrito")
        print("2. Ver carrito y total a pagar")
        print("3. Eliminar producto del carrito")
        print("4. Finalizar compra (generar ticket)")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_carrito(productos)
        elif opcion == "3":
            eliminar_producto(productos)
        elif opcion == "4":
            print(generar_ticket(productos))
            if input("\n¿Desea realizar otra compra? (s/n): ").lower() != 's':
                print("¡Gracias por su compra!")
                break
            productos = []
        elif opcion == "5":
            print("¡Gracias por usar nuestro sistema!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Configuración global
PRESUPUESTO_LIMITE = 1000.0

if __name__ == "__main__":
    menu()
