import numpy as np
import matplotlib.pyplot as plt
import time
import psutil

inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()

crd=[]
archivo= open("UNI_CORR_500_01.txt","r")

for i in archivo.readlines():
    separa = i[0:29]
    aux = separa.split()
    crd.append(aux)
archivo.close()

listax = []
listay = []

for r in range(4,len(crd)):
    lista2 = crd[r]
    a = []
    X = lista2[2]
    Y = lista2[3]
    Z = lista2[4]
    a.append(float(X))
    a.append(float(Y))
    a.append(float(Z))
    listax.append(float(X))
    listay.append(float(Y))

frecuenciaX = {}

for x in listax:
    if x in frecuenciaX:
        frecuenciaX[x] += 1
    else:
        frecuenciaX[x] = 1

max_frecuencia = max(frecuenciaX.values())

indice_mayor = [a for a in frecuenciaX.keys() if frecuenciaX[a] == max_frecuencia]

print("---------------------------------------------------------------------------------------")
print("Las coordenadas x que mas se repiten son: " + str(indice_mayor) + " con un recuento de " + str(max_frecuencia) + " veces")
print("---------------------------------------------------------------------------------------")

frecuenciaY = {}

for x in listay:
    if x in frecuenciaY:
        frecuenciaY[x] += 1
    else:
        frecuenciaY[x] = 1

max_frecuenciaY = max(frecuenciaY.values())

indice_mayorY = [a for a in frecuenciaY.keys() if frecuenciaY[a] == max_frecuenciaY]

print("---------------------------------------------------------------------------------------")
print("Las coordenadas Y que mas se repiten son: " + str(indice_mayorY) + " con un recuento de " + str(max_frecuenciaY) + " veces")
print("-----------------------------------------------------------")

coordenadas = [str(listax[i]) + " " + str(listay[i]) for i in range(len(listax))]

Cord_frecuencias = {}

for e in coordenadas:
    if e not in Cord_frecuencias:
        Cord_frecuencias[e] = 1
    else:
        Cord_frecuencias[e] += 1

max_frecTotal = max(Cord_frecuencias.values())

indice_frecTotal = [h for h, frequency in Cord_frecuencias.items() if frequency == max_frecTotal]

print("---------------------------------------------------------------------------------------")
print("Las coordenadas totales que mas se repiten son: " + str(indice_frecTotal) + " con un recuento de " + str(max_frecTotal) + " veces")
print("---------------------------------------------------------------------------------------")

print("maximo lista X " + str(max(listax)))
print("Maximo lista Y " + str(max(listay)))

print("MIN lista x " + str(min(listax)))
print("MIn lista Y " + str(min(listay)))

print("---------------------------------------------------------------------------------------")
print("-----------------------varianza--------------------------------------------------------")
print("Varianza lista X  " + str(np.var(listax)))
print("Varianza lista Y  " + str(np.var(listay)))
print("---------------------------------------------------------------------------------------")

def convertidorEjeX(metro):
    ListaXpixel = []
    for i in range(len(metro)):
        pixel = int((float(metro[i]) + 9.0) * (640 / 18))
        ListaXpixel.append(pixel)
    return ListaXpixel

valXconvertidos = convertidorEjeX(listax)

def convertidorEjeY(metro): 
    ListaYpixel = []
    for i in range(len(metro)):
        pixel = int(480 - (float(metro[i] * (480 / 5))))
        ListaYpixel.append(pixel)
    return ListaYpixel


valYconvertidos = convertidorEjeY(listay)

combinadas = list(zip(valXconvertidos, valYconvertidos))

CONTADORPIX = {i:0 for i in combinadas}
for i in range(len(combinadas)):
    CONTADORPIX[combinadas[i]]+=1 

Matriz_frecuencias=np.zeros((481,641))

for i in CONTADORPIX.keys():
    columna, fila = i  
    Matriz_frecuencias[fila][columna] = CONTADORPIX[i]
    
import matplotlib.pyplot as plt
plt.imshow(Matriz_frecuencias, cmap='hot', interpolation='nearest')
plt.colorbar()

fin_tiempo = time.time()
tiempo_transcurrido = fin_tiempo - tiempo_inicio
print(f"Tiempo de ejecución: {tiempo_transcurrido} segundos")

# Cálculo de la memoria utilizada
fin_memoria = psutil.virtual_memory().used
memoria_utilizada = fin_memoria - inicio_memoria

print(f"Memoria utilizada: {memoria_utilizada} bytes")

plt.show()

print("---------------------------------------------------------------------------------------")
