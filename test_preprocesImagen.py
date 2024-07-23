import numpy as np
import cv2
import pytest
from preprocesImagen import preprocess

def test_preprocess():
    # Cargar una imagen de prueba desde un archivo
    image = cv2.imread('person1712_bacteria_4529.jpg')

    # Verificar que la imagen se haya cargado correctamente
    assert image is not None, "La imagen no se pudo cargar, Verificar la ruta."

    # Llamar a la función preprocess()
    preprocessed_image = preprocess(image)

    # Verificar los resultados
    assert preprocessed_image.shape == (1, 512, 512, 1)
    assert preprocessed_image.min() >= 0 and preprocessed_image.max() <= 1
