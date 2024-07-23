import pytest
import numpy as np
from PIL import Image
import cv2

# Importar la funcion leerImagen
from leerImagen import read_dicom_file, read_jpg_file


# Define the corresponding tests
def test_read_dicom_file():
    # Prueba con un archivo DICOM 
    dicom_path = "normal(3).dcm"
    img_rgb, img2show = read_dicom_file(dicom_path)

    # Comprobar que los valores devueltos son de los tipos esperados
    assert isinstance(img_rgb, np.ndarray)
    assert isinstance(img2show, Image.Image)

    # Verificar que la imagen tenga la forma esperada
    assert img_rgb.shape == (1024, 1024, 3)

    # Comprobar que los valores de píxel son diferentes de cero
    assert np.any(img_rgb != 0)
    assert np.any(img2show != 0)


def test_read_jpg_file():
    # Prueba con un archivo JPEG
    jpg_path = "person1712_bacteria_4529.jpg"
    img2, img2show = read_jpg_file(jpg_path)

    # Comprobar que los valores devueltos son de los tipos esperados
    assert isinstance(img2, np.ndarray)
    assert isinstance(img2show, Image.Image)

    # Verificar que la imagen tenga la forma esperada
    assert img2.shape == (1064, 1328, 3)

    # Comprobar que los valores de píxel son diferentes de cero
    assert np.any(img2 != 0)
    assert np.any(img2show != 0)


# Correr el test
if __name__ == "__main__":
    pytest.main([__file__])
