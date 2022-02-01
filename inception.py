import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
import os
import pandas as pd

#leemos las imágenes
path="./image/"
list_name = os.listdir(path)
list_name = sorted(list_name)

#Cargamos el modelo entrenado
model = tf.keras.models.load_model('inception.h5')


test=[]

for i in list_name:
    path2="./image/" + i
    #Cargamos la imagen
    im = cv2.imread(path2)        
        
    #Redimensionamos las imágenes 
    im = cv2.resize(im,(224,224)) 
    
    
    #convertimos las imágenes en arrays
    img_array = image.img_to_array(im)
    img_array = np.expand_dims(img_array, axis=0) / 255 
    
    
    #Generamos la predicción del modelo
    prediccion = model.predict(img_array)[0]

    #seleccionamos la clase de la predicción
    clase = np.argmax(prediccion)
        
    #llenamos la list_predict.

    if clase == 0: 
        test.append(0)
    else: 
        test.append(1)
    
    


lista=pd.DataFrame(test)
lista.to_csv("./evaluacion/list_predict_ince.csv", index=False, header=True) 
print("...Predicción Realizada !!!")