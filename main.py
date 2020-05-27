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
    if("emol" in url):
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
    url = ['http://www.emol.com','https://www.latercera.com/']
    for i in url:
        res =sacar_paginas(i)
        time.sleep(10)
    if('emol' in url):
        res = format.formatear_emol(url)
        emol = noticias.Emol(res['titulo'],res['subtitulo'],res['autor y fecha'],res['autor y fecha'],res['cuerpo'],0,None,None)
    elif('latercera' in url):
        res = format.formatear_la_tercera(url)
        latercera = noticias.La_Tercera(res['titulo'],res['subtitulo'],res['autor y fecha'],res['autor y fecha'],res['cuerpo'],0,res['categoria'])
