import noticias
import format

url = "https://www.biobiochile.cl/noticias/internacional/eeuu/2020/05/21/trump-confirma-planes-realizar-manera-presencial-la-cumbre-del-g7-junio-la-casa-blanca.shtml"

if __name__ == "__main__":
    if('emol' in url):
         res = format.formatear_emol(url)
         emol = noticias.Emol(res['titulo'],res['subtitulo'],res['autor y fecha'],res['autor y fecha'],res['cuerpo'],0,None,None)
    elif('publimetro' in url):
        res = format.formatear_publimetro(url)
        publimetro = noticias.Publimetro(res['titulo'],res['subtitulo'],res['fecha'],res['autor'],res['cuerpo'],None)
    elif('biobiochile' in url):
        res = format.formatear_bio_bio(url)
        biobio = noticias.Bio_Bio(res['titulo'],None,res['fecha y hora'],res['autor'],res['cuerpo'],0,res['categoria'],0)
    elif('latercera' in url):
        res = format.formatear_la_tercera(url)
        latercera = noticias.La_Tercera(res['titulo'],res['subtitulo'],res['autor y fecha'],res['autor y fecha'],res['cuerpo'],0,res['categoria'])
