import numpy as np
import matplotlib.pyplot as plt
import time
import psutil

###apertura de archivo###
f = open("UNI_CORR_500_01.txt","r")
lista = [[float (cordenadas) for cordenadas in row.split()[-3:-1]] for row in f.readlines()[5:]]
f.close()

def coordenada_max(lista_original,indice):###calculo de los valores que mas repiten por coordenada###
    cord = {}
    for row in lista_original:
        valor = row[indice]
        if valor in cord:
            cord[valor] += 1
        else:
            cord[valor] = 1

    # Encontrar el valor que más se repite
    max_valor = max(cord.values())
    most_common_value = [key for key, valor in cord.items() if valor == max_valor]
    print("El valor que más se repite de la coordenada", indice, "es:", most_common_value)

def coordenadas_unidas(lista_original):###union de las coordenadas###
    coordenadas_dic = {}
    for indice in lista_original:
        
        x = (indice[0])  # Coordenada X
        y = (indice[1])  # Coordenada Y
        coordenada = (x, y)  # Crear una tupla con las coordenadas X y Y

        if coordenada in coordenadas_dic:
            coordenadas_dic[coordenada] += 1
        else:
            coordenadas_dic[coordenada] = 1

    for coordenada, repeticiones in coordenadas_dic.items():
        if repeticiones > 3:
            print(f"Coordenada {coordenada} se repite {repeticiones} veces")

def conversion_x(lista_cordenada):###conversion de metros a pixeles en x###
    lista_pixelx = []
    for i in lista_cordenada:
        a = i[0]
        pixel = (35.566 * float(a)) + 320
        lista_pixelx.append(pixel)
    return lista_pixelx
pixels_x = conversion_x(lista[:])

def conversion_y(lista_cordenada):###conversion de metros a pixeles en y###
    lista_pixel = []
    for i in lista_cordenada:
        a = i[1]
        pixel = (-96 * float(a)) + 480 
        lista_pixel.append(pixel)

    return lista_pixel
pixels_y = conversion_y(lista[:])

###redondeo de las coordenadnas para la matriz###
valores_redondeadosx = [round(valor, 0) for valor in pixels_x]
valores_redondeadosy = [round(valor, 0) for valor in pixels_y]
###union de coordenadas###
coordenada_pixel= list(zip(valores_redondeadosx, valores_redondeadosy))

###uso de coordenadas en metros###
coordenada_max(lista,0)
coordenada_max(lista,1)
coordenadas_unidas(lista)
###uso con coordenadas en pixel####
coordenada_max(coordenada_pixel,0)
coordenada_max(coordenada_pixel,1)
coordenadas_unidas(coordenada_pixel)

###varianza de los pixels###
print("---------------------------------------------------------------")
print("la varianza entre las coordenadas es:",np.var(coordenada_pixel))
print("y su desviacion estandar es de:",np.std(coordenada_pixel))
print("---------------------------------------------------------------")
print("la varianza de la coordenada x en pixel es:",np.var(pixels_x))
print("y su desviacion estandar es de:",np.std(pixels_x))
print("---------------------------------------------------------------")
print("la varianza de la coordenada y en pixel es:",np.var(pixels_y))
print("y su desviacion estandar es de:",np.std(pixels_y))
print("---------------------------------------------------------------")


###matriz de calor(de chat gpt el codigo)####
tamaño_x = 640
tamaño_y = 480
matriz = np.zeros((tamaño_y, tamaño_x))

for coord in coordenada_pixel:
    x, y = coord
    x = int(x)  
    y = int(y)
    if 0 <= x < tamaño_x and 0 <= y < tamaño_y:
        matriz[y, x] += 1  

# Crear el mapa de calor
plt.imshow(matriz, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Mapa de Calor')
plt.show()

plt.boxplot(pixels_x)
plt.show()

plt.boxplot(pixels_y)
plt.show()


def tarea_a_medir():
    suma = 0
    for i in range(1000000):
        suma += i
    print("Resultado:", suma)

# Medición de tiempo y memoria
inicio_tiempo = time.time()
inicio_memoria = psutil.virtual_memory().used

# Llamamos a la función que queremos medir
tarea_a_medir()

# Finalizamos la medición de tiempo y memoria
fin_tiempo = time.time()
fin_memoria = psutil.virtual_memory().used

# Cálculo del tiempo utilizado
tiempo_transcurrido = fin_tiempo - inicio_tiempo
print("Tiempo de ejecución:", tiempo_transcurrido, "segundos")

# Cálculo de la memoria utilizada
memoria_utilizada = fin_memoria - inicio_memoria
print("Memoria utilizada:", memoria_utilizada / 1024, "KB")
