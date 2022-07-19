import cv2 as cv
import os
from astropy.io import fits
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        x_var = x
        y_var = y
        #print(f"intensidad = {img[y_var,x_var]}, en x={x_var},y={y_var}")
        return x_var, y_var
path = os.getcwd()
data = "/data/"
imagenes = [path+data+imag for imag in os.listdir("./"+data)]
imagen = imagenes[3]

with fits.open(imagen) as hdul:
    #info = hdul.info()
    img = hdul[1].data

name = imagen.split("/")[-1]
cv.namedWindow(name, cv.WINDOW_NORMAL)
cv.imshow(name, img)
x,y = cv.setMouseCallback(name, click_event)
key = cv.waitKey(0)

if key == ord("q"):
    cv.destroyAllWindows()
