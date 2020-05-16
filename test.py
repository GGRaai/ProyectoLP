import requests
import pprint
from bs4 import BeautifulSoup

url = "https://www.emol.com/noticias/Nacional/2020/05/16/986388/Manalich-senador-Quinteros-coronavirus-dolo.html"
def formatear(url):
    pagina=dict()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Sacar datos
    titulo = soup.find(id="cuDetalle_cuTitular_tituloNoticia")
    subtitulo = soup.find(id="cuDetalle_cuTitular_bajadaNoticia")
    datos= soup.find(id="barra-agencias-info")
    datos = datos.find(class_="info-notaemol-porfecha")
    ############
    #Arreglar el autor/fecha
    datos_n = datos.text.strip()
    ############
    #actualizar el diccionario
    pagina.update({'titulo':titulo.text})
    pagina.update({'subtitulo':subtitulo.text})
    pagina.update({'autor y fecha':datos_n})
    ###########
    cuerpo = soup.find(id="cuDetalle_cuTexto_textoNoticia")
    cuerp = cuerpo.find_all('div')
    cuerpo = []
    for cue in cuerp:
        noticias_relacionadas = cue.find('div',class_="flo_left cont_descrip_noticia")
        noticias_relacionadas_2 = cue.find('article',class_="flo_left cont_nota_relacionada")
        #print(cue.prettify())
        if noticias_relacionadas == None or noticias_relacionadas_2 == None:

            cuerpo.append(cue.text)
    i=0
    while i<len(cuerpo):
        if(cuerpo[i]=='' or cuerpo[i]=='\n'):
            cuerpo.remove(cuerpo[i])
        #print(cuerpo[i])
        i+=1
    pagina.update({'cuerpo':cuerpo})
    print(pagina)
    return pagina
formatear(url)
