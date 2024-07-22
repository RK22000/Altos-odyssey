"""
This when run this script should auto click start and restart buttons on 
Alto's Odyssey
"""
import pyautogui as pag
import numpy as np
from alto_odyssey import utils
import logging
logger = logging.getLogger(__name__)

def find_and_click(text: str):
    """
    Find a button specified by the text and click it
    """
    img = np.array(pag.screenshot())
    tnf_exception = None
    for downscale in range(4, 0, -1):
        try:
            logger.debug(f"Searching for '{text}' at {downscale}x downscale")
            center = utils.find_button_center(img, text, utils.get_reader())
        except utils.TextNotFoundException as tnf:
            tnf_exception = tnf
    try: 
        center
    except UnboundLocalError:
        raise tnf_exception
    
    # print(f"Moving to {center} on screen of {pag.size()} from image of size {img.shape}")
    # pag.moveTo(*center, duration=1)
    pag.leftClick(*center, duration=1)
    # pag.moveTo(0, 0, 1)

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    find_and_click("tap to start")
