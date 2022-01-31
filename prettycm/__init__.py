from .cm_object import confusion_matrix, confusion_matrix_by_cal
from .draw import palette

__version__ = "1.1.2"

import os
if not os.path.exists(f"{os.path.dirname(__file__)}/font"):
    os.makedirs(f"{os.path.dirname(__file__)}/font")
    os.system(f"wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=17CtaJWgItkcZjdWNPgr2VOTN5UXgZp1I' -O {os.path.dirname(__file__)}/font/gmarket.ttf")
    os.system(f"wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1Zrz2y0jJ9z-pTfEJFO5LtaMZbDDES_xW' -O {os.path.dirname(__file__)}/font/title.ttf")
    print("Font Cache downloaded. This only run first time.")