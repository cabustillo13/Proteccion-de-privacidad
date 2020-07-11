#Nota:Este dataset solo contiene imagenes caras de frente y no de perfil.
#Osea si alguien sale de perfil no lo reconocera, si se quiere incluirlos debera actualizar el dataset.
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

from skimage import io, data
from skimage.feature import Cascade
from skimage.filters import gaussian

def show_detected_face(result, detected, title = "Imagen de la cara"):
    
    plt.imshow(result)
    img_desc = plt.gca()
    plt.set_cmap('gray')
    plt.title(title)
    plt.axis('off')
    
    for patch in detected:
        img_desc.add_patch(
            mpatches.Rectangle((patch['c'], patch['r']), patch['width'], patch['height'], fill = False, color = "r",linewidth = 2))
        
    plt.show()
    

def getFace(d):
    
    #Extrae las coordenas del rectangulo que contiene la cara
    x, y = d['r'], d['c']
    
    #Se obtiene el ancho y alto del rectangulo
    width, height = d['r'] + d['width'], d['c'] + d['height']
    
    #Extraer la cara recortardas
    face = image[x:width, y:height]
    
    return face

def mergeBlurryFace(original, gaussian_image):
    
    #Recorda que x e y son coordenadas de inicio del rectangulo
    x, y = d['r'], d['c']
    
    #El ancho y alto del rectangulo
    width, height = d['r'] + d['width'], d['c'] + d['height']
    
    original[x:width, y:height]= gaussian_image
    
    return original

################################################################
#####                         MAIN                         #####
################################################################

#Imagen a analizar
#image = io.imread('./Imagenes/imagen_original.jpg')
#image = data.astronaut()
image = group_image #Ya esta precargada en el ejercicio de privacy protection del cuarto capitulo.

#Cargar el archivo entrenado del modulo de scikit image
trained_file = data.lbp_frontal_face_cascade_filename()

#Iniciar el detector de cascada
detector = Cascade(trained_file)
##detector = cv2.CascadeClassifier.detectMultiScale(trained_file)

#Detectar caras mediante clasificador en cascada
detected = detector.detect_multi_scale(img=image,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                      min_size=(50, 50),
                                       max_size=(100, 100))

"""Nota: El factor de escala: por el cual la busqueda, la ventana se multiplica en cada paso"""
"""step_ratio: representa una busqueda exhaustiva y generalmente es lenta. Al establecer valores mas altos para este parametro, los resultados seran peores pero el calculo sera mucho mas rapido. Por los general sus valores rondan de 1 a 5"""
"""min_size y max_size determinan el tamano maximo y minimo de la ventana"""

#Mostrar por pantalla caras detectadas
#show_detected_face(image, detected)

#Para cada cara detectada
for d in detected:
    #Obtener las coordenadas de las caras recortardas
    face = getFace(d)
    
    #Aplicar filtro gaussiano para suavizar y pixelar la cara
    gaussian_face = gaussian(face, multichannel = True, sigma = 8)
    
    #Fusion cara borrosa con la imagen original
    resulting_image = mergeBlurryFace(image, gaussian_face)
    
show_image(resulting_image, "Proteccion de privacidad")
