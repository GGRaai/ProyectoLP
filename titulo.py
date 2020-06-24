import difflib
import noticias

def comparar_titulo(lista):
    lista_emol = []
    lista_tercera = []
    lista_parecidas = []
    for i in (lista):
        titulo = i.titulo
        
        
        if (type(i) is noticias.Emol):
            lista_emol.append(i)

        if (type(i) is noticias.La_Tercera):
            lista_tercera.append(i) 
    
    for i in (lista_emol):
        for j in (lista_tercera):
            ratio = difflib.SequenceMatcher(None, i.titulo, j.titulo).ratio()
            if (ratio >= 0.4):
                lista_parecidas.append((i,j))
                print("\nEstas noticias se parecen\n")
                print("El titulo\n", i.titulo, "\ntiene un", ratio*100, "% de similitud de con el titulo\n", j.titulo)
    return lista_parecidas
