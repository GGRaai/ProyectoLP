import requests
import pprint
from bs4 import BeautifulSoup

url = "https://www.emol.com/noticias/Economia/2020/05/14/986093/Pymes-creditos-garantia-estatal.html"
def formatear(url):
    pagina=dict()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    titulo = soup.find(id="cuDetalle_cuTitular_tituloNoticia")
    subtitulo = soup.find(id="cuDetalle_cuTitular_bajadaNoticia")
    datos= soup.find(id="barra-agencias-info")
    datos = datos.find(class_="info-notaemol-porfecha")
    datos_n = datos.text.replace('\n','')
    datos_n = datos_n.replace('\r','')
    datos_n = datos_n.replace('        ','')
    pagina.update({'titulo':titulo.text})
    pagina.update({'subtitulo':subtitulo.text})
    pagina.update({'autor y fecha':datos_n})
    cuerpo = soup.find(id="cuDetalle_cuTexto_textoNoticia")
    cuerp = cuerpo.find_all('div')
    for cue in cuerp:
        cuerpo = []
        noticias_relacionadas = cue.find('div',class_="flo_left cont_items_detalle_50")
        if(noticias_relacionadas == None):
            cuerpo.append(cue.text)
            #print(cuerpo)
    pagina.update({'cuerpo':cuerpo})
    print(pagina)
formatear(url)
