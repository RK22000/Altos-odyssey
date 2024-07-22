import cv2
import easyocr
import numpy as np

_reader = None
def get_reader():
    global _reader
    if _reader is None: _reader = easyocr.Reader(['en'])
    return _reader

class TextNotFoundException(Exception): pass
def find_button_center(img: np.ndarray, text: str, reader: easyocr.Reader, downscale=4) -> np.ndarray:
    img = cv2.resize(img, np.array(img.shape[:2][::-1])//downscale)
    result = reader.readtext(img)
    found_text = []
    for box, txt, cnf in result:
        if txt == text:
            return np.array(box).mean(0)*downscale
        found_text.append(txt)
    raise TextNotFoundException(f"Button with text '{text}' not found in given image. Text found in image: {found_text}")