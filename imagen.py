import cv2 as cv
import os
from astropy.io import fits
from astropy.wcs import WCS
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
        sky = w.pixel_to_world(y_var,x_var)
        hour_ra = sky.ra.hour
        minu_ra = (hour_ra - int(hour_ra))*60
        seg_ra = (minu_ra - int(minu_ra))*60

        hour_dec = sky.dec.deg
        minu_dec = (hour_dec - int(hour_dec))*60
        seg_dec = (minu_dec - int(minu_dec))*60
        print(params)
        print(f"\nintensidad = {img[y_var,x_var]}\n ra={int(hour_ra)}:{int(minu_ra)}:{seg_ra}\n dec={int(hour_dec)}:{int(minu_dec)}:{seg_dec}")
        #return x_var, y_var
path = os.getcwd()
data = "/data/"
imagenes = [path+data+imag for imag in os.listdir("./"+data)]
imagen = imagenes[3]



with fits.open(imagen) as hdul:
    info = hdul.info()
    img = hdul[1].data
    header = hdul[1].header

w = WCS(header)

img_ = img.astype(np.uint8)  ## Hay que considerar cambiar el format 
#plt.imshow(img, cmap="rainbow")
#plt.show()
name = imagen.split("/")[-1]
cv.namedWindow(name, cv.WINDOW_GUI_NORMAL)
cv.imshow(name, cv.cvtColor(img_, cv.COLOR_GRAY2BGR))
#cv.imshow(name, img)
cv.setMouseCallback(name, click_event)
key = cv.waitKey(0)

if key == ord("q"):
    cv.destroyAllWindows()