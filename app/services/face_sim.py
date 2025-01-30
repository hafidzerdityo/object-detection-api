import base64
from io import BytesIO
from PIL import Image
import numpy as np
from deepface import DeepFace


def get_sim(img_b64str1: str, img_b64str2: str):
    img1 = Image.open(BytesIO(base64.b64decode(img_b64str1)))
    img2 = Image.open(BytesIO(base64.b64decode(img_b64str2)))
    img1 = np.array(img1)
    img2 = np.array(img2)
    result = DeepFace.verify(img1, img2)
    return result