from fuzzywuzzy import fuzz
import noticias

def comparar_titulo(lista):

    lista_emol = [i for i in lista if type(i) is noticias.Emol]
    lista_tercera = [i for i in lista if type(i) is noticias.La_Tercera]
    lista_parecidas = [f"El titulo: {i.titulo} tiene un {fuzz.ratio(i.titulo, j.titulo)} % de similitud de con el titulo {j.titulo}" for j in lista_emol for i in lista_tercera if fuzz.ratio(i.titulo, j.titulo) >= 45]
    lista_parecidas2 = [(j,i) for j in lista_emol for i in lista_tercera if fuzz.ratio(i.titulo, j.titulo) >= 45]
    for i in lista_parecidas:
        print(i)
        print("\n")
    return lista_parecidas2
