from abc import ABC,abstractmethod

class Noticia(ABC):
    def __init__(self,tit,sub,fech,aut,cuer,com,cat):
        self.titulo = tit
        self.subtitulo = sub
        self.fecha = fech
        self.autor = aut
        self.cuerpo = cuer
        self.comentarios = com
        self.categoria = cat

class Emol(Noticia):
    def __init__(self,tit,sub,fech,aut,cuer,com,cat,subcat):
        super().__init__(tit,sub,fech,aut,cuer,com,cat)
        self.subcategoria = subcat


class La_Tercera(Noticia):
    def __init__(self,tit,sub,fech,aut,cuer,com,cat):
        super().__init__(tit,sub,fech,aut,cuer,com,cat)
        #Agregar Pulso, La Tercera Domingo, La Tercera PM
