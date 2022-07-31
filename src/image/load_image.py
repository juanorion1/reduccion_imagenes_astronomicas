import cv2 as cv
from astropy.io import fits
import numpy as np
from pathlib import Path

from src.image.utils import verify_zeros, verify_image

class LFI:  #LoadFitsImage
    
    def __init__(self):
        self.path = Path.cwd()
        
    def load_image(self, path_imagenes: str):
        """
        This function load the image in the instance self.image
        Additionaly, create the instances, height, width, image_visual and name.
        The instance image_visual is the image shown in the plot. The visualization 
        not necesarilly shows the real image, somethimes some pixels do not represent
        the real value, but in the operations the real value is used.
        """
        self.path_image = self.path / path_imagenes
        self.image, self.header = verify_image(self.path_image)
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.image_visual = verify_zeros(self.image, self.height, self.width)
        self.name = self.path_image.parts[-1].split(".fits")[0]
        
    def visualize_image(self):
        """
        This functions shows the image.
        Press "q" to close the window.
        """
        cv.namedWindow(self.name, cv.WINDOW_GUI_NORMAL)
        cv.imshow(self.name, self.image_visual)
        key = cv.waitKey(0)
        if key == ord("q"):
            cv.destroyAllWindows()
    
    def interactive_visualization(self):
        """
        This functions allows the user to make different operations
        over the image. 
        """
        pass

            

        