from titulo import *


lista = comparar_titulo(objetos)
contador = 0
hora_LT = 0
for i,j in lista:
    ahora = datetime.now()
    contador +=1
    fecha_Lt = j.fecha.split('Hace')
    hora_LT = fecha_Lt[1].strip().split(' ')[0]
    if(contador > 4):
        fecha_emol = i.fecha.split("|")
        print("Hora: "+fecha_emol[1].strip())
    hora_hace_LT = ahora-timedelta(hours = int(hora_LT))
    print("Hora:",hora_hace_LT)
