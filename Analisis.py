"""Nota:Este dataset solo contiene imagenes caras de frente y no de perfil."""
"""Osea si alguien sale de perfil no lo reconocera, si se quiere incluirlos debera actualizar el dataset."""
import numpy as np
import cv2

# Incluir imagen a analizar
image = cv2.imread("./Imagenes/mona-lisa.jpg")
#image = cv2.imread("./Imagenes/monjes.jpg")

result_image = image.copy()

def unirImagenes(image, result_image):
    
    """Nota: Usando esta forma de concatenacion, solo se aplica a imagenes con dimensiones iguales"""
    vis = np.concatenate((image, result_image), axis=1) #axis=0 para unir verticalmente y axis=1 para unir horizontalmente
    cv2.imwrite('Comparacion.png', vis)

def recortarCaras(image, result_image):
    
    if len(faces) != 0:         # Si hay muchas caras en una imagen
        for f in faces:         # Para cada imagen en la cara

            # Obtener las coordenadas, largo y ancho donde se encuentran las caras 
            x, y, w, h = [ v for v in f ]

            # Remarcar con un rectangulo, de color celeste y grosor de linea de 5, alrededor de la cara
            #cv2.rectangle(image, (x,y), (x+w,y+h), (255,255,0), 5)
            sub_face = image[y:y+h, x:x+w]
            
            # Aplicar un filtro gaussiano en el rectangulo para pixelar rostros
            sub_face = cv2.GaussianBlur(sub_face,(23, 23), 10)
            
            # Fusionar cara borrosa con la imagen original
            result_image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
            
            # Guardar los resultados de las caras detectadas pixeladas
            #face_file_name = "./face_" + str(y) + ".jpg"
            #cv2.imwrite(face_file_name, sub_face)

    return result_image 

# Especificar el clasificador en cascada para entrenamiento
face_cascade_name = "./haarcascade_frontalface_alt.xml"

# Crear un clasificador en cascada
face_cascade = cv2.CascadeClassifier()

# Cargar el clasificador entrenado
face_cascade.load(face_cascade_name)

# Preprocesamiento en imagenes
grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayimg = cv2.equalizeHist(grayimg)

# Run clasificador
faces = face_cascade.detectMultiScale(grayimg, 1.1, 2, 0|cv2.CASCADE_SCALE_IMAGE, (30, 30))

"""Nota: El factor de escala: por el cual la busqueda, la ventana se multiplica en cada paso"""
"""step_ratio: representa una busqueda exhaustiva y generalmente es lenta. Al establecer valores mas altos para este parametro, los resultados seran peores pero el calculo sera mucho mas rapido. Por los general sus valores rondan de 1 a 5"""
"""min_size y max_size determinan el tamano maximo y minimo de la ventana"""

result_image = recortarCaras(image, result_image)
 
#Mostrar resultados
print "Listo. Caras detectadas"
# cv2.imshow("Detected face", result_image)
cv2.imwrite("./Resultado.png", result_image) 

#Comparar imagen original con la de salida
unirImagenes(image, result_image)

#Bibliografia
#https://stackoverrun.com/es/q/4923564
#https://www.datacamp.com/courses/image-processing-in-python
