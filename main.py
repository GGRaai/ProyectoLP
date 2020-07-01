import noticias
import format
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import vader
import titulo
from datetime import datetime,timedelta
from fuzzywuzzy import fuzz
from largo import *


def sacar_paginas(url):
    driver.get(url)
    links=[] #lista con todos los links de una pagina
    res=[] #lista con todos los links de noticias
    if("emol" in url): #revisa emol
        noticias = driver.find_elements_by_xpath("//a[@href]") #encuentra todos los objetos con href (todos los links)
        for i in noticias:
            links.append(i.get_attribute("href")) #Consigue el link de la href
            for link in links:
                if(link == "https://www.emol.com/" or link == "https://automoviles.emol.com/"):
                    continue
                if("www.emol.com" in link and ".html" in link or "especiales" not in link): #ve si es realmente noticia, hay muchos links a otras cosas q no nos sirven
                    if("#comentarios" in link or "wom" in link): #existen links a los comentarios, solo se los salta
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
                    if(link in res or "www.latercera.com/canal" in link or "www.latercera.com/autor"in link or "https://www.latercera.com/etiqueta/" in link): #revisa si es autor o canal, esos no son noticias
                        continue
                    res.append(link)
    return res

def horas(lista_p):
    lista = lista_p
    contador = 0
    hora_LT = 0
    horas_emol = []
    horas_lt = []
    hora_emol = datetime.now()
    hora_hace_LT = datetime.now()
    for i,j in lista:
        ahora = datetime.now()
        contador +=1
        if(j.fecha!='None' or j.fecha !=['']):
            lower = j.fecha.lower()
            fecha_Lt = lower.split('hace')
        if(len(fecha_Lt)==1):
            fecha_Lt = fecha_Lt[0].split(" ")
            hora_LT = fecha_Lt[4].strip().split(':')[0]
        else:
            hora_LT = fecha_Lt[1].strip().split(' ')[0]
        if(i.fecha!='None'):
            fecha_emol = i.fecha.split("|")
            hora_emol = datetime.strptime(fecha_emol[1].strip(),"%H:%M")
            horas_emol.append(hora_emol.time())
            print("Hora:",hora_emol.time())
        if('minutos' in fecha_Lt[1]):
            hora_hace_LT = ahora-timedelta(minutes = int(hora_LT))
        else:
            hora_hace_LT = ahora-timedelta(hours = int(hora_LT))
        horas_lt.append(hora_hace_LT.time())
        print("Hora:",hora_hace_LT.time())
        for trend in fechas.keys():
            for palabra in i.titulo:
                if(fuzz.ratio(palabra,trend)>30):
                    minimo = sorted(fechas[trend])
                    print("Desfase entre noticia de Emol y el primer tweet fue de:",hora_emol.time()-minimo[0])
                    break
            for palabra in j.titulo:
                if(fuzz.ratio(palabra,trend)>30):
                    minimo = sorted(fechas[trend])
                    print("Desfase entre noticia La Tercera y el primer tweet fue de:",hora_hace_LT.time()-minimo[0])
                    break


if __name__ == "__main__":
    driver = webdriver.Chrome("C:/bin/chromedriver.exe") #Cambiar por direccion donde esta instalado chromedriver
    objetos = [] #Lista para guardar los objetos que despues van a ser analizados
    links = [] #Lista con los links para noticias
    url = ['https://www.emol.com/','https://www.latercera.com/'] #Las dos paginas que analizaremos
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
            if("https://www.latercera.com/encasa" in link or "https://www.latercera.com/asi-empieza/" in link):#manda a seccion en casa, no nos sirve
                continue
            res = format.formatear_la_tercera(link)
            objetos.append(noticias.La_Tercera(res['titulo'],res['subtitulo'],res['autor y fecha'],res['autor y fecha'],res['cuerpo'],0,res['categoria']))
    #loop de prueba, borrar en el producto final
    print("Valores tweets")
    vader.sacar_valores()#tweets
    print("Valores noticias")
    vader.sacar_valores_noticias(objetos)#Noticias
    vader.graficos()#tweets
    vader.graficos_n()
    parecidas = titulo.comparar_titulo(objetos)
    print("Cantidad de noticias parecidas: %d",len(parecidas))
    horas(parecidas)
    largo(objetos)
