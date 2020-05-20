import noticias
import test

url = "https://www.publimetro.cl/cl/noticias/2020/05/20/desde-hoy-se-asumira-una-persona-desarrolla-sintomas-respiratorios-coronavirus.html"


if __name__ == "__main__":
    if('emol' in url):
        test.formatear_emol(url)
    elif('publimetro' in url):
        test.formatear_publimetro(url)
    elif('biobiochile' in url):
        test.formatear_bio_bio(url)
    elif('latercera' in url):
        test.formatear_la_tercera(url)
