import pytest
import numpy as np
from PIL import Image
import cv2

# Import the functions to test
from leerImagen import read_dicom_file, read_jpg_file


# Define the corresponding tests
def test_read_dicom_file():
    # Test with a DICOM file
    dicom_path = "normal(3).dcm"
    img_rgb, img2show = read_dicom_file(dicom_path)

    # Verify that the returned values are of the expected types
    assert isinstance(img_rgb, np.ndarray)
    assert isinstance(img2show, Image.Image)

    # Verify that the image has the expected shape
    assert img_rgb.shape == (1024, 1024, 3)

    # Verify that the pixel values are different from zero
    assert np.any(img_rgb != 0)
    assert np.any(img2show != 0)


def test_read_jpg_file():
    # Test with a JPEG file
    jpg_path = "person1712_bacteria_4529.jpg"
    img2, img2show = read_jpg_file(jpg_path)

    # Verify that the returned values are of the expected types
    assert isinstance(img2, np.ndarray)
    assert isinstance(img2show, Image.Image)

    # Verify that the image has the expected shape
    assert img2.shape == (1064, 1328, 3)

    # Verify that the pixel values are different from zero
    assert np.any(img2 != 0)
    assert np.any(img2show != 0)


# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])
