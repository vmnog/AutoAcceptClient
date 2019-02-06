import cv2
import numpy as np
import matplotlib.pyplot as plt

def get():

    img = cv2.imread('../images/Screenshot.png',0) #imagem que ele vai fazer o matching
    img2 = img.copy()
    template = cv2.imread('../images/button.png',0) #imagem que ele procura
    w, h = template.shape[::-1]

    methods = ['cv2.TM_CCORR_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        return(max_loc)