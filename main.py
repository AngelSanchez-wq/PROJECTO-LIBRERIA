from Clases import Libreria

libreria = Libreria()
#
while True:
    print("\n=== LIBRERÍA ===")
    print("1. Agregar libro")
    print("2. Vender libro")
    print("3. Mostrar inventario")
    print("4. Buscar libro")
    print("5. Registrar cliente")
    print("6. Buscar cliente")
    print("7. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: $"))
        libreria.agregar_libro(titulo, autor, cantidad, precio)

    elif opcion == "2":
        titulo = input("Título del libro: ")
        libro = libreria.buscar_libro(titulo)
        if libro:
            precio = float(input("Precio de venta: $"))
            libro.vender(precio)

    elif opcion == "3":
        libreria.mostrar_inventario()

    elif opcion == "4":
        titulo = input("Título del libro a buscar: ")
        libreria.buscar_libro(titulo)

    elif opcion == "5":
        nombre = input("Nombre del cliente: ")
        edad = int(input("Edad: "))
        fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
        num_id = input("Número de identificación: ")
        id_cliente = input("ID de cliente: ")
        libreria.agregar_cliente(nombre, edad, fecha_nac, num_id, id_cliente)

    elif opcion == "6":
        id_cliente = input("ID del cliente a buscar: ")
        cliente = libreria.buscar_cliente(id_cliente)
        if cliente:
            print(f"\nCliente encontrado:")
            print(f"Nombre: {cliente.nombre}")
            print(f"Edad: {cliente.edad}")
            print(f"Fecha de nacimiento: {cliente.fechadenacimiento}")
            print(f"ID: {cliente.IDdecliente}")

    elif opcion == "7":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida")