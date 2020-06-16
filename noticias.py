from abc import ABC,abstractmethod

class Noticia(ABC):
    def __init__(self,tit,sub,cuer,cat):
        self.titulo = tit
        self.subtitulo = sub
        self.cuerpo = cuer
        self.categoria = cat

class Emol(Noticia):
    def __init__(self,tit,sub,cuer,cat):
        super().__init__(tit,sub,cuer,cat)


class La_Tercera(Noticia):
    def __init__(self,tit,sub,cuer,cat):
        super().__init__(tit,sub,cuer,cat)
        #Agregar Pulso, La Tercera Domingo, La Tercera PM
