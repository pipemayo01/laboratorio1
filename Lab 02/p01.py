import numpy as np
import matplotlib.pyplot as plt
import time
import psutil
import pandas as pd

inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()

data_frame = pd.read_csv("UNI_CORR_500_01.txt", delimiter="\t", header=0 , skiprows=3)

print(data_frame)

data_frame["XPIXEL"] = data_frame["X"] * 35.6 + 320
data_frame["YPIXEL"] = data_frame["Y"] * 35.6 + 320

fig, ax = plt.subplots()
hist = ax.hist2d(data_frame["XPIXEL"], data_frame["YPIXEL"], bins=60, cmap="magma")

plt.title("Distribución de Peatones en el Pasillo Observacion O1")

plt.xlabel("Coordenadas en Eje X")
plt.ylabel("Coordenandas en Eje Y")

cbar = plt.colorbar(hist[3])
cbar.set_label("Frecuencia")


print("--------------------------------------------------------------------------")

data2 = pd.read_csv("UNI_CORR_500_08.txt", delimiter="\t", header=0, skiprows=3)
fig, ax = plt.subplots()
hist = ax.hist2d((data2["X"] * 35.6 + 320), (data2["Y"] * -96) + 480, bins=70, cmap="magma")
plt.title("Distribución de Peatones en el Pasillo Observación 08")

plt.xlabel("Coordenadas en Eje X")
plt.ylabel("Coordenadas en Eje Y")

cbar = plt.colorbar(hist[3])
cbar.set_label("Frecuencia")
fin_tiempo = time.time()
tiempo_transcurrido = fin_tiempo - tiempo_inicio
plt.show()
plt.show()

print(f"Tiempo de ejecución: {tiempo_transcurrido*1000} milisegundos")

fin_memoria = psutil.virtual_memory().used
memoria_utilizada = (fin_memoria - inicio_memoria)/1048576

print(f"Memoria utilizada: {memoria_utilizada} Mega bytes")
