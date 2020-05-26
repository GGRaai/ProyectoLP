import requests
import pprint
from bs4 import BeautifulSoup
from selenium import webdriver

def formatear_emol(url):
    #TODO:
    #   -Arreglar cuerpo
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
    #print(pagina)
    return pagina

def formatear_publimetro(url):
    pagina=dict()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Sacar datos
    titulo = soup.find('h1').text.strip()
    subtitulo = soup.find(class_="excerpt").text.strip()
    datos= soup.find(class_="autorandshare__autor").text.strip()
    fecha = soup.find(class_="autorandshare__date").text.strip()
    cuerpo = soup.find(class_="resumen").find_all("p")
    cuerp =[]
    for i in range(len(cuerpo)):
        cuerp.append(cuerpo[i].text.strip())
    ############
    #actualizar el diccionario
    pagina.update({'titulo':titulo})
    pagina.update({'subtitulo':subtitulo})
    pagina.update({'autor':datos})
    pagina.update({'fecha':fecha})
    pagina.update({'cuerpo':cuerp})
    ###########
    #print(pagina)
    return pagina

def formatear_bio_bio(url): #Faltan los comentarios
    pagina=dict()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Sacar datos
    visitas = soup.select('span[class*="numero-visitas-"]')
    categoria = soup.find(class_="categoria-titulo-nota").text.strip()
    titulo = soup.find(class_="nota-titular robotos").text.strip()
    fecha_hora = soup.find(class_="nota-fecha am-hide").text.replace('\n','').replace('\r','').replace('\t','')
    autor = soup.find(class_="autor-link").text.strip()
    cuerpo = soup.find(class_="nota-contenido text-19 robotos").find_all("p")
    cuerp =[]
    for i in range(len(cuerpo)):
        cuerp.append(cuerpo[i].text.replace('\n',''))
    ############
    #actualizar el diccionario
    #pagina.update({'visitas':visitas})
    pagina.update({'categoria':categoria})
    pagina.update({'titulo':titulo})
    pagina.update({'fecha y hora':fecha_hora})
    pagina.update({'autor':autor})
    pagina.update({'cuerpo':cuerp})
    ###########
    #print(pagina)
    return pagina

def formatear_la_tercera(url): #Faltan los comentarios
    pagina=dict()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Sacar datos
    categoria = soup.find(class_="list-cat-y-tags")
    titulo = soup.find('h1')
    subtitulo = soup.find(class_="excerpt")
    datos= soup.find(class_="author d-flex-center m-bot-10")
    cuerpo = soup.find('div',class_="single-content").find_all('p',class_="paragraph")
    cuerp=[]
    for i in range(len(cuerpo)):
        cuerp.append(cuerpo[i].text.strip('\n'))
    ############
    #actualizar el diccionario
    pagina.update({'categoria':categoria.text})
    pagina.update({'titulo':titulo.text})
    pagina.update({'subtitulo':subtitulo.text})
    pagina.update({'autor y fecha':datos.text})
    pagina.update({'cuerpo':cuerp})
    ###########
    #print(pagina)
    return pagina
