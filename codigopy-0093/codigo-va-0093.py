
# Importamos las librerias
# Pedro Martinez 0093
import cv2
import matplotlib.pyplot as plt
import os
ruta_imagen = os.path.join(
    "img-original-0093",
    "Leopardo-0093.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
leopardo = cv2.imread(ruta_imagen)
print(leopardo)
# Convertir de BGR a RGB
sub = cv2.cvtColor(leopardo, cv2.COLOR_BGR2RGB)
cv2.imshow("Subaru original-0093",leopardo)
cv2.waitKey(0)
cv2.destroyAllWindows()