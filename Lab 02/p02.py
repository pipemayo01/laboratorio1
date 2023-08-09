import numpy as np
import time
import psutil

inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()

def locura(archivo2):
    import matplotlib.pyplot as plt
    crd=[]
    archivo= open(archivo2,"r")

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

    print("---------------------------------------------------------------------------------------")
    fig,ax = plt.subplots()
    ax.hist2d(valXconvertidos,valYconvertidos, bins=70, cmap="magma")
    plt.show()

    import matplotlib.pyplot as plt
    plt.imshow(Matriz_frecuencias, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title("Visualización de la Matriz de Frecuencias")
    plt.show()

locura("UNI_CORR_500_01.txt")
locura("UNI_CORR_500_08.txt")

fin_tiempo = time.time()
tiempo_transcurrido = fin_tiempo - tiempo_inicio
print(f"Tiempo de ejecución: {tiempo_transcurrido*1000} milisegundos")

fin_memoria = psutil.virtual_memory().used
memoria_utilizada = (fin_memoria - inicio_memoria)/1048576
print(f"Memoria utilizada: {memoria_utilizada} Mega bytes")