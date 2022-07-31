import cv2 as cv
import numpy as np

class ModifyImage:
    ## Aquí va todo lo relacionado con operaciones con imagenes, también la edición.
    def __init__(self, image):
        self.image = image
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
    
    #TODO poder ser capaz de cortar la imagen desde la selección del mouse