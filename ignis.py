import cv2
import numpy as np
import pandas as pd
import os

#creamos la ruta de las imágenes
path="./image/"
list_name = os.listdir(path)
list_name = sorted(list_name)

list_test=[]
coo_test=[]

#recorremos todas las imágenes de la lista
for i in list_name:
    
    #Cargamos la imagen y la convertimos a HSV:
    path2="./image/" + i
    img = cv2.imread(path2)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #establecemos los parámetros del color
    hMin = 100
    hMax = 140
    sMin = 100
    sMax = 255
    vMin = 100
    vMax = 255

    #Creamos los arrays que definen el rango de colores:
    color_bajos=np.array([hMin,sMin,vMin])
    color_altos=np.array([hMax,sMax,vMax])
    
    #definimos las dimensiones del Kernel:
    kernelx = 2
    kernely = 1
    
    #Creamos el kernel:
    kernel = np.ones((kernelx,kernely),np.uint8)
    
    #Detectamos los colores y eliminamos el ruido en una máscara:
    mask = cv2.inRange(hsv, color_bajos, color_altos)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    #encontramos los contornos en la mascara
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  
    if len(contours) == 0: #"no fuego"
        list_test.append(1)
    else: #"fuego"
        list_test.append(0)
       
        coordenadas=[]
        boundarea=[]
        coorfinal=[]

        #encontramos los cuadros delimitadores y el área de los contornos
        for c in contours:
            bounding_rect=cv2.boundingRect(c)
            coordenadas.append(bounding_rect)
            area = (cv2.contourArea (c))/1000
            boundarea.append(area)
       
        #Realizamos supresión no máxima a los contornos encontrados
        coorfinal=cv2.dnn.NMSBoxes(coordenadas,boundarea,score_threshold=0.05,nms_threshold=0.5)  

        #dibujamos los cuadros en las imágenes y guardamos las coordenadas de cada cuadro
        for n in range(len(coorfinal)):
            p=coorfinal[n][0]
            c, d, e, f =coordenadas[p]
            cv2.rectangle(img,(c,d),(c+e,d+f),(255,233,0),2)
            cootest=[i,c,d,e,f]
            coo_test.append(cootest)

    #guardamos las imágenes con los cuadros dibujados
    resultado="./resultados/"+ i
    cv2.imwrite(resultado,img)

#guardamos la lista de coordenadas y la lista de predicciones
lista=pd.DataFrame(list_test)
lista2=pd.DataFrame(coo_test)
lista.to_csv("./evaluacion/list_predict_ignis.csv", index=False, header=True)
lista2.to_csv("./resultados/coordenadas.csv", index=False, header=True)
print("...Predicción Realizada !!!")
