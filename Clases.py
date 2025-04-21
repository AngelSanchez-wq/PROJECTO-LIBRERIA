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
