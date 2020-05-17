import noticias
import test

url = "https://www.biobiochile.cl/noticias/nacional/chile/2020/05/17/minsal-confirma-ministros-ward-briones-estan-cuerentena-preventiva-explica-caso-sichel.shtml"


if __name__ == "__main__":
    if('emol' in url):
        test.formatear_emol(url)
    elif('meganoticias' in url):
        test.formatear_mega(url)
    elif('biobiochile' in url):
        test.formatear_bio_bio(url)
    elif('latercera' in url):
        test.formatear_la_tercera(url)
