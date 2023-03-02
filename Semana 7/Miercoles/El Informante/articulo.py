class Articulo:
    def __init__(self,titulo,resumen,cuerpo,imágenes,fecha_de_creación,redactor):
        self.titulo=titulo
        self.resumen=resumen
        self.cuerpo= cuerpo
        self.imágenes= imágenes
        self.fecha_de_publicación= None
        self.fecha_de_creación= fecha_de_creación
        self.redactor = redactor