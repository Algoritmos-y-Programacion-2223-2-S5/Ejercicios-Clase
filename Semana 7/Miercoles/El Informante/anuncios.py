class AnuncioComercial:
    def __init__(self,nombre,cedula,sección, título,cuerpo):
        self.nombre = nombre
        self.cedula = cedula
        self.sección = sección
        self.título = título
        self.cuerpo = cuerpo

class AnuncioClasificado:
    def __init__(self,precio, fecha_de_publicación, cantidad_de_días, tipo):
        self.precio = precio
        self.fecha_de_publicación = fecha_de_publicación
        self.cantidad_de_días = cantidad_de_días
        self.tipo = tipo

class AnuncioClasificadoVehiculo(AnuncioClasificado):
    def __init__(self,precio, fecha_de_publicación, cantidad_de_días,marca, modelo, año, color, km):
        super().__init__(precio,fecha_de_publicación,cantidad_de_días,"Vehiculo")
        self.marca = marca
        self.modelo =modelo
        self.año =año
        self.color = color
        self.km =km

class AnuncioClasificadoVivienda(AnuncioClasificado):
    def __init__(self,precio, fecha_de_publicación, cantidad_de_días,m2, cuartos,baños,puestos,si_acepta_ley):
        super().__init__(precio,fecha_de_publicación,cantidad_de_días,"Vivienda")
        self.m2 = m2
        self.cuartos = cuartos
        self.baños = baños
        self.puestos = puestos
        self.si_acepta_ley = si_acepta_ley