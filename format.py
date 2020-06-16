import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def formatear_emol(url):
    #TODO:
    #   -Arreglar cuerpo
    pagina=dict()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Sacar datos
    titulo = soup.find('h1')
    subtitulo = soup.find('h2')
    datos = soup.find(class_="info-notaemol-porfecha")
    comentarios = soup.find("span",class_="num_comentarios")
    categoria = soup.find(class_="tit_emol_des_2015")
    subcategoria = soup.find(class_="select")
    ############
    #Arreglar el autor/fecha
    if(datos == None):
        datos_n = 'None'
    else:
        datos_n = datos.text.strip()
    ############
    cuerpo = soup.find(id="cuDetalle_cuTexto_textoNoticia")
    if(cuerpo == None):
        cuerpo_n = ['None']
    else:
        cuerpo = cuerpo.find_all('div')
        cuerpo_n = []
        for parrafo in cuerpo:
            n_relacionadas = parrafo.find(class_="flo_left cont_descrip_noticia")
            if(parrafo.text in cuerpo_n):
                continue
            if(n_relacionadas != None):
                continue
            else:
                cuerpo_n.append(parrafo.text.strip())

    for par in cuerpo_n:
        if(par=='\n' or par==''):
            cuerpo_n.remove(par)
    #actualizar el diccionario
    pagina.update({'titulo':titulo.text})
    pagina.update({'subtitulo':subtitulo.text})
    pagina.update({'autor y fecha':datos_n})
    pagina.update({'cuerpo':cuerpo_n})
    pagina.update({'categoria':categoria.text.strip()})
    pagina.update({'subcategoria':subcategoria.text})
    ###########
    #print(pagina)
    return pagina


def formatear_la_tercera(url): #Faltan los comentarios
    pagina=dict()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #Sacar datos
    categoria = soup.find(class_="list-cat-y-tags")
    if(categoria==None):
        pagina.update({'categoria':'None'})
    else:
        pagina.update({'categoria':categoria.text})
    titulo = soup.find('h1')
    subtitulo = soup.find(class_="excerpt")
    if(subtitulo == None): #Hay algunas noticias que no tienen subtitulo
        pagina.update({'subtitulo': "None"})
    else:
        pagina.update({'subtitulo':subtitulo.text})
    datos= soup.find(class_="author d-flex-center m-bot-10")
    if(datos == None):
        pagina.update({'autor y fecha':'None'})
    else:
        pagina.update({'autor y fecha':datos.text})
    cuerpo = soup.find('div',class_="single-content")
    if(cuerpo==None):
        cuerp = []
    else:
        cuerpo = cuerpo.find_all('p',class_="paragraph")
        cuerp=[]
        for i in range(len(cuerpo)):
            cuerp.append(cuerpo[i].text.strip('\n'))
    ############
    #actualizar el diccionario
    pagina.update({'titulo':titulo.text})
    pagina.update({'cuerpo':cuerp})
    ###########
    #print(pagina)
    return pagina
