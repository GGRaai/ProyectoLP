from abc import ABC,abstractmethod

class noticia(ABC):
    def __init__(self,tit,sub,fech,aut,cuer,com,cat):
        self.titulo = tit
        self.subtitulo = sub
        self.fecha = fech
        self.autor = aut
        self.cuerpo = cuer
        self.comentarios = com
        self.categoria = cat
