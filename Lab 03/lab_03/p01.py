import numpy as np
import matplotlib.pyplot as plt
import time
import psutil
import pandas as pd

inicio_memoria = psutil.virtual_memory().used
tiempo_inicio=time.time()

data_frame = pd.read_csv("UNI_CORR_500_01.txt", delimiter="\t", header=0 , skiprows=3)
data2 = pd.read_csv("UNI_CORR_500_08.txt", delimiter="\t", header=0, skiprows=3)

print("------------------------------------------------------------------------")

def calcular_velocidad_grupo(grupo):
    grupo["Distancia"] = np.sqrt(grupo["X"].diff(periods=-1)**2 + grupo["Y"].diff(periods=-1)**2)
    grupo["tiempo"] = 1 / 25
    grupo["Velocidad"] = grupo["Distancia"] / grupo["tiempo"]
    return grupo

grupos_01 = data_frame.groupby("# PersID", group_keys=False)
df_velocidad_01 = grupos_01.apply(calcular_velocidad_grupo)

Velocidad_prom_01 = df_velocidad_01.groupby("# PersID")["Velocidad"].agg(np.mean)
Promedio_velocidad_tot01 = df_velocidad_01["Velocidad"].mean()
print("Resultados de la Observacion 01")
print("Velocidad promedio de todas las personas: ", Promedio_velocidad_tot01)
print("Velocidad Maxima: ", Velocidad_prom_01.max())
print("Velocidad Minima: ", Velocidad_prom_01.min())
print("Varianza: ", Velocidad_prom_01.var())
      
print("------------------------------------------------------------------------")

grupos_08 = data2.groupby("# PersID", group_keys=False)
df_velocidad_08 = grupos_08.apply(calcular_velocidad_grupo)
Velocidad_prom_08 = df_velocidad_08.groupby("# PersID")["Velocidad"].agg(np.mean)
Promedio_velocidad_tot08 = df_velocidad_08["Velocidad"].mean()
print("Resultados de la Observacion 08")
print("Velocidad promedio de todas las personas: ", Promedio_velocidad_tot08)
print("Velocidad Maxima: ", Velocidad_prom_08.max())
print("Velocidad Minima: ", Velocidad_prom_08.min())
print("Varianza: ", Velocidad_prom_08.var())

print("------------------------------------------------------------------------")
fin_tiempo = time.time()
tiempo_transcurrido = fin_tiempo - tiempo_inicio
fin_memoria = psutil.virtual_memory().used
memoria_utilizada = (fin_memoria - inicio_memoria)/1048576
print(f"Tiempo de ejecución: {tiempo_transcurrido*1000} milisegundos")
print(f"Memoria utilizada: {memoria_utilizada} Mega bytes")

fig, ax = plt.subplots()
histograma = ax.hist(Velocidad_prom_01, bins=20, edgecolor='black', alpha=0.7, color='Pink')
plt.title("Histograma de Velocidades datos 01")
plt.xlabel("Velocidades")
plt.ylabel("Frecuencia de personas")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


fig, ax = plt.subplots()
histograma = ax.hist(Velocidad_prom_08, bins=20, edgecolor='black', alpha=0.7, color='purple')
plt.title("Histograma de Velocidades datos 08")
plt.xlabel("Velocidades")
plt.ylabel("Frecuencia de personas")
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()