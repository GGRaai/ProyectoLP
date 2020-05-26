import noticias
import format
from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
import time


def sacar_paginas(url):
    driver.get(url)
    links=[]
    res=[]
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content,'html.parser')
    res=[]
    if("biobiochile" in url):
        noticias = driver.find_elements_by_xpath("//a[@href]")
        for i in noticias:
            links.append(i.get_attribute("href"))
            for link in links:
                if("www.biobiochile.cl" in link and ".shtml" in link):
                    if("deporte" in link):
                        continue
                    if(link in res):
                        continue
                    res.append(link)
    elif("emol" in url):
        noticias = driver.find_elements_by_xpath("//a[@href]")
        for i in noticias:
            links.append(i.get_attribute("href"))
            for link in links:
                if("www.emol.com" in link and ".html" in link):
                    if("#comentarios" in link):
                        continue
                    if(link in res):
                        continue
                    res.append(link)
    elif("publimetro" in url):
        noticias = driver.find_elements_by_xpath("//a[@href]")
        for i in noticias:
            links.append(i.get_attribute("href"))
            for link in links:
                if("www.publimetro.cl" in link and ".html" in link):
                    if(link in res):
                        continue
                    res.append(link)
    elif("latercera" in url):
        noticias = driver.find_elements_by_xpath("//a[@href]")
        for i in noticias:
            links.append(i.get_attribute("href"))
            for link in links:
                if("www.latercera.com" in link):
                    if(link in res):
                        continue
                    res.append(link)
    return res




if __name__ == "__main__":
    driver = webdriver.Chrome("C:/bin/chromedriver.exe")
    url = ['http://www.emol.com','http://www.biobiochile.cl','http://www.publimetro.cl','https://www.latercera.com/']
    for i in url:
        res =sacar_paginas(i)
        time.sleep(10)
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
