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
