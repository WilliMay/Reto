Sistema de Carrito de Compras
Este programa implementa un sistema de gestión de carrito de compras que permite a los usuarios agregar productos, calcular descuentos y generar tickets de compra. A través de un menú interactivo, los usuarios pueden realizar varias acciones relacionadas con la compra de productos, como agregar productos al carrito, ver el contenido del carrito, eliminar productos, y finalizar la compra.

Funcionalidades
Agregar productos: Los usuarios pueden agregar productos al carrito especificando el nombre, la cantidad y el precio unitario. El sistema valida que los valores sean positivos y calcula el subtotal, los descuentos y el total de cada producto.
Mostrar carrito: Permite ver el contenido del carrito, con detalles de cada producto, los descuentos aplicados y el total a pagar.
Eliminar productos: Los usuarios pueden eliminar productos previamente agregados al carrito.
Generar ticket de compra: El sistema genera un ticket que resume la compra realizada, mostrando los productos adquiridos, los descuentos aplicados y el total a pagar.
Presupuesto límite: El sistema alerta cuando el total de la compra supera un presupuesto límite definido (en este caso, $1000), ofreciendo al usuario la opción de continuar o cancelar la compra.
Estructura del Código
Funciones
validar_numero_positivo(valor): Valida que un valor sea un número positivo.
calcular_descuento(cantidad, subtotal): Calcula el descuento que se aplica según la cantidad de productos. Ofrece descuentos del 5%, 10% o 15%, dependiendo de la cantidad de unidades compradas.
agregar_producto(productos): Permite agregar productos al carrito. Solicita al usuario el nombre, cantidad y precio, y calcula el descuento y el total.
mostrar_carrito(productos): Muestra los detalles de los productos en el carrito y el total a pagar.
eliminar_producto(productos): Permite eliminar productos del carrito, mostrando una lista de los productos actuales y permitiendo al usuario seleccionar cuál eliminar.
generar_ticket(productos): Genera un ticket de compra con los detalles de todos los productos en el carrito, el total de los descuentos y el total final.
menu(): Función principal que gestiona el flujo del programa, mostrando el menú interactivo y permitiendo al usuario seleccionar las acciones a realizar.
Configuración global
PRESUPUESTO_LIMITE: Valor definido como el presupuesto límite para la compra (en este caso, 1000.0). Si el total supera este límite, se muestra una advertencia y se ofrece la opción de continuar o cancelar la compra.
Ejecución del Programa
El usuario selecciona una opción del menú interactivo:

Agregar producto: Ingresa los detalles del producto (nombre, cantidad, precio).
Ver carrito: Muestra los productos agregados y el total.
Eliminar producto: Permite eliminar productos seleccionados del carrito.
Finalizar compra: Genera un ticket con los detalles de la compra.
Salir: Finaliza el programa.
Si el usuario decide generar un ticket, se muestra un resumen de la compra y se ofrece la opción de realizar otra compra o salir del sistema.

Requisitos
Python 3.x: El programa está escrito en Python y requiere una versión moderna (3.x) para funcionar correctamente.
Ejemplo de Uso
El usuario ingresa "1" para agregar un producto:

Nombre del producto: "Laptop"
Cantidad: "2"
Precio unitario: "$500"
El sistema calcula el subtotal, aplica los descuentos (si corresponde) y agrega el producto al carrito.

El usuario ingresa "2" para ver el carrito y el total de la compra.

El usuario ingresa "4" para generar un ticket de compra, que resume todos los productos adquiridos, los descuentos aplicados y el total final.
