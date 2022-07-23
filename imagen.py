import cv2 as cv
import os
from astropy.io import fits
from astropy.wcs import WCS
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

ref_point = []
def shape_selection(event, x, y, flags, param):
    # grab references to the global variables
    global ref_point, crop

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]

    # check to see if the left mouse button was released
    elif event == cv.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        ref_point.append((x, y))

        # draw a rectangle around the region of interest
        cv.rectangle(img, ref_point[0], ref_point[1], (255, 255, 0), 2)
        cv.imshow(name, img)

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
    #info = hdul.info()
    img = hdul[1].data
    header = hdul[1].header

w = WCS(header)

img = img.astype(np.uint8)  ## Hay que considerar cambiar el format 
#plt.imshow(img, cmap="rainbow")
#plt.show()
name = imagen.split("/")[-1]
#cv.namedWindow(name, cv.WINDOW_GUI_NORMAL)
#cv.imshow(name, cv.cvtColor(img_, cv.COLOR_GRAY2BGR))
#cv.imshow(name, img)
#cv.setMouseCallback(name, draw_circle)
#key = cv.waitKey(0)

#if key == ord("q"):
#    cv.destroyAllWindows()
cv.namedWindow(name, cv.WINDOW_GUI_NORMAL)
#img = np.zeros((512,512,3), np.uint8)
clone = img.copy()
cv.setMouseCallback(name,shape_selection)
# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv.imshow(name, img)
    key = cv.waitKey(1) & 0xFF

    # press 'r' to reset the window
    if key == ord("r"):
        img = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("q"):
        break

# close all open windows
cv.destroyAllWindows() 