# Proteccion-de-privacidad
Protección de privacidad mediante el pixelado del rostro en una imagen mediante clasificador en Cascada.

Desenfocar, pixelar o censurar parte de una imagen. Bastante útil para ocultar matrículas de automóviles, marcas conocidas o logos que no son sponsor cuando se transmite algún programa de televisión o preservar la identidad de los niños sin consentimiento de sus padres en documentales.

Este programa consiste en un clasificador en cascada para detectar caras en una imagen. Esta imagen se convierte a una escala de grises, posteriormente se analizan todas las caras encontradas dentro de la imagen, se recorta cada una y se le aplica un filtro gaussiano para suavizar y pixelar el rostro. Todos esas etapas se realizan para cada rostro detectado. Luego se fusiona la imagen original con los rostros pixeladas.

Imágenes obtenidas de Pixabay. La licencia ampara gratis para usos omerciales y no es necesario reconocimiento.
