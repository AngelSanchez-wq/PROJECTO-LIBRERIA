class Persona:
    def _init_(self, nombre, edad, fechadenacimiento, numerodeidentificacion):
        self.nombre = nombre
        self.edad = edad
        self.fechadenacimiento = fechadenacimiento
        self.numerodeidentificacion = numerodeidentificacion

class Cliente(Persona):
    def _init_(self, nombre, edad, fechadenacimiento, numerodeidentificacion, IDdecliente):
        super()._init_(nombre, edad, fechadenacimiento, numerodeidentificacion)
        self.IDdecliente = IDdecliente
        
class libro:
    def _init_(self, titulo, autor, estado):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado
        self.precio = 0.0
        self.unidades = 0  

    def vender(self, precio):
        if self.estado == "disponible" and self.unidades > 0:
            self.precio = precio
            self.unidades -= 1
            print(f"El libro ha sido vendido por ${precio:.2f}")
            print(f"Quedan {self.unidades} unidades disponibles")
            if self.unidades == 0:
                self.estado = "agotado"
            return True
        else:
            print("El libro no está disponible para venta.")
            print(f"Unidades disponibles: {self.unidades}")
            return False

class Libreria():
    def _init_(self):
        self.libros = []
        self.clientes = []  

    def agregar_libro(self, titulo, autor, cantidad, precio):
        nuevo_libro = libro(titulo, autor, "disponible")
        nuevo_libro.unidades = cantidad
        nuevo_libro.precio = precio
        self.libros.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado con {cantidad} unidades a ${precio}")
        return nuevo_libro
    
    def agregar_cliente(self, nombre, edad, fecha_nac, num_id, id_cliente):
        nuevo_cliente = Cliente(nombre, edad, fecha_nac, num_id, id_cliente)
        self.clientes.append(nuevo_cliente)
        print(f"Cliente {nombre} registrado exitosamente")
        return nuevo_cliente


    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.IDdecliente == id_cliente:
                return cliente
        print("Cliente no encontrado")
        return None

    def mostrar_inventario(self):
        print("\nInventario de libros:")
        for libro in self.libros:
            print(f"- {libro.titulo} por {libro.autor}")
            print(f"  Unidades: {libro.unidades}")
            print(f"  Estado: {libro.estado}")
            if libro.precio > 0:
                print(f"  Precio: ${libro.precio:.2f}")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print(f"\nLibro encontrado:")
                print(f"Título: {libro.titulo}")
                print(f"Autor: {libro.autor}")
                print(f"Estado: {libro.estado}")
                print(f"Unidades disponibles: {libro.unidades}")
                if libro.precio > 0:
                    print(f"Precio: ${libro.precio:.2f}")
                return libro
        print("\nLibro no encontrado en el inventario")
        return None