class Empleado:

    def __init__(self,nombre,ci,seccion):
        self.nombre = nombre
        self.cedula = ci
        self.seccion = seccion

class Redactor(Empleado):
    def __init__(self,nombre,ci,seccion,articulos):
        super().__init__(nombre,ci,seccion)
        self.articulos = articulos

    def escribir_articulo(self):
        pass

class RedactorJefe(Empleado):
    def __init__(self,nombre,ci,seccion):
        super().__init__(nombre,ci,seccion)

    def supervisar(self):
        pass

    def decidir_articulo(self):
        pass