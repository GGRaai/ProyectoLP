# ProyectoLP
## WebScraper Noticias

## Integrantes:
  * Raimundo Moraga
  * Romina Beretta
  * Matias Vidal
  * Sebastian Guzman
  * Andres Garcia

## Instrucciones para ocupar el programa:
  * Para ejecutar el programa, se debe primero descargar chromium y en la linea 93 de main.py se debe cambiar la direccion por la direccion donde esta el driver de chromium para poder ocupar selenium
  * Se debe ejecutar el siguiente comando por consola:
  ```console
  pip install -r requirements.txt
  ```
  * Luego se ejecuta el archivo main de la manera preferida, ya sea por consola con
  ```console
  python main.py
  ```
  o con la manera que su IDE le permita.

## Analisis hecho:
  * Primero se hace un analisis sobre los sentimientos de los tweets y las noticias, analizando si el tweet y la noticia tiene un tono Negativo, neutro o positivo, para luego crear un grafico por noticias y un grafico por tweets con las tendencias de estos, en graficos() y graficos_n()
  * Luego creamos una lista con las noticias de cada sitio que son parecidos, mediante el uso de un ratio de strings con la libreria fuzzywuzzy, y se imprimen los titulos de las noticias con sus ratios respectivos en porcentaje.
  * Posteriormente se analiza las horas de las noticias y tweets, viendo desfase entre que una noticia es publicada y un tweet es publicado sobre algo parecido a la noticia, usando la lista de noticias parecidas creada anteriormente
  * Despues se hace un analisis sobre el largo de las noticias y tweets del momento, dividiendo en **Corto**,**Medio** y **Largo** segun la cantidad de palabras que tenga la noticia o el tweet. Para esto se ocuparon distintos valores:
   * Corto:
      * Noticias que tengan menos de 400 palabras.
      * Tweets que tengan menos de 15 palabras.
   * Medio:
      * Noticias que tengan entre 400 y 2000 palabras.
      * Tweets que tengan entre 15 y 24 palabras.
   * Largo:
      * Noticias que tengan mas de 2000 palabras.
      * Tweets que tengan mas de 24 palabras.
  * Con esta informacion se crean 3 graficos para representar el largo de las noticias de Emol, La tercera y los tweets.
