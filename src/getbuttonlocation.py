import cv2
import numpy as np
import matplotlib.pyplot as plt

def get():

    img = cv2.imread('../images/Screenshot.png',0) #picture that it is using to match
    img2 = img.copy()
    template = cv2.imread('../images/button.png',0) #picture that it is looking for
    w, h = template.shape[::-1]

    methods = ['cv2.TM_CCORR_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Debug stuff        
        # print(res)
        # print(round(max_val, 1))
        # print(cv2.minMaxLoc(res))

        probability = round(max_val, 1)
        if probability > 0.8:
            print('\n\nA match has been founded, lets play!!\n')
        else:
            max_loc = None          
        
        return(max_loc) # returns the x and y values
