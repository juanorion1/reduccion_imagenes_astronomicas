import cv2 as cv
import os
from astropy.io import fits
from astropy.wcs import WCS
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from src.mouse_event.event import MouseEvent
from src.image.load_image import LFI


def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell

        x_var = x
        y_var = y
        sky = w.pixel_to_world(y_var,x_var)
        hour_ra = sky.ra.hour
        minu_ra = (hour_ra - int(hour_ra))*60
        seg_ra = (minu_ra - int(minu_ra))*60

        hour_dec = sky.dec.deg
        minu_dec = (hour_dec - int(hour_dec))*60
        seg_dec = (minu_dec - int(minu_dec))*60
        print(params)
        print(f"\nintensidad = {image[y_var,x_var]}\n ra={int(hour_ra)}:{int(minu_ra)}:{seg_ra}\n dec={int(hour_dec)}:{int(minu_dec)}:{seg_dec}")
        #return x_var, y_var
path = os.getcwd()
data = "/data/"
imagenes = [path+data+imag for imag in os.listdir("./"+data)]
path_imagen = imagenes[4]


lfi = LFI()
lfi.load_image(path_imagen)
header = lfi.header
lfi.visualize_image()

#plt.imshow(lfi.image, cmap="gray")
#plt.show()
#imagen = lfi.image
w = WCS(header)
##img = img/img.max()
##img = img.astype(np.uint8)  ## Hay que considerar cambiar el format 
##plt.imshow(img, cmap="rainbow")
##plt.show()
#name = lfi.name
#cv.namedWindow(name, cv.WINDOW_GUI_NORMAL)
##cv.imshow(name, cv.cvtColor(img_, cv.COLOR_GRAY2BGR))
##cv.imshow(name, imagen.transpose())
##cv.setMouseCallback(name, draw_circle)
#key = cv.waitKey(0)
#
##if key == ord("q"):
##    cv.destroyAllWindows()
##cv.namedWindow(name, cv.WINDOW_GUI_NORMAL)
##img = np.zeros((512,512,3), np.uint8)
##clone = img.copy()
##me = MouseEvent()
##params = {"img":img, "name":name}
##cv.setMouseCallback(name,me.shape_selection, params)
#
## keep looping until the 'q' key is pressed
##print(me.ref_point)
#while True:
#     # display the image and wait for a keypress
#    cv.imshow(name, imagen.transpose())
#
#    key = cv.waitKey(0)# & 0xFF
#
#    # press 'r' to reset the window
##    if key == ord("r"):
##        img = clone.copy()
#
#    # if the 'q' key is pressed, break from the loop
#    if key == ord("q"):
#        break
#
## close all open windows
#cv.destroyAllWindows() 
##print(me.ref_point)
##plt.imshow(img.transpose(), cmap="grey")
##plt.savefig("imagen.png")