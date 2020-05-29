import noticias
import format
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


def sacar_paginas(url):
    driver.get(url)
    links=[] #lista con todos los links de una pagina
    res=[] #lista con todos los links de noticias
    if("emol" in url): #revisa emol
        noticias = driver.find_elements_by_xpath("//a[@href]") #encuentra todos los objetos con href (todos los links)
        for i in noticias:
            links.append(i.get_attribute("href")) #Consigue el link de la href
            for link in links:
                if("www.emol.com" in link and ".html" in link): #ve si es realmente noticia, hay muchos links a otras cosas q no nos sirven
                    if("#comentarios" in link): #existen links a los comentarios, solo se los salta
                        continue
                    if(link in res):
                        continue
                    res.append(link)
    elif("latercera" in url):
        noticias = driver.find_elements_by_xpath("//*[@id='fusion-app']/div/main/section[2]//a[@href]") #encuentra los href de la seccion principal
        for i in noticias:
            links.append(i.get_attribute("href"))
            for link in links:
                if("www.latercera.com" in link):
                    if(link in res or "www.latercera.com/canal" in link or "www.latercera.com/autor"in link): #revisa si es autor o canal, esos no son noticias
                        continue
                    res.append(link)
    return res




if __name__ == "__main__":
    driver = webdriver.Chrome("C:/bin/chromedriver.exe") #Cambiar por direccion donde esta instalado chromedriver
    objetos = [] #Lista para guardar los objetos que despues van a ser analizados
    links = [] #Lista con los links para noticias
    url = ['http://www.emol.com','https://www.latercera.com/'] #Las dos paginas que analizaremos
    for i in url:
        links.extend(sacar_paginas(i)) #Agrega todos los links a noticias de una pagina a nuestra lista
        time.sleep(10) #Delay para que no explote
    for link in links:
        if('emol' in link): #revisa si es noticia de emol
            if("https://www.emol.com/noticias/Deportes" in link or "Grafico" in link):#Noticias de deporte generalmente son en vivos, Grafico son vivo, asi que no sirve
                continue
            res = format.formatear_emol(link) #crea un diccionario con los datos de la noticia
            objetos.append(noticias.Emol(res['titulo'],res['subtitulo'],res['autor y fecha'],res['autor y fecha'],res['cuerpo'],0,res['categoria'],res['subcategoria'])) #lo agrega a la lista
        elif('latercera' in link): #revisa si es noticia de la tercera
            if("https://www.latercera.com/encasa" in link):#manda a seccion en casa, no nos sirve
                continue
            res = format.formatear_la_tercera(link)
            objetos.append(noticias.La_Tercera(res['titulo'],res['subtitulo'],res['autor y fecha'],res['autor y fecha'],res['cuerpo'],0,res['categoria']))
    #loop de prueba, borrar en el producto final
    for cont in objetos:
        if(type(cont) is noticias.Emol):
            print("Emol")
        elif(type(cont) is noticias.La_Tercera):
            print("La Tercera")
        print(cont.titulo)
