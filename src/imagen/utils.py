import numpy as np
from astropy.io import fits

def verify_zeros(image, height, width):
    
    ## Verifying amount of zeros (mask)
    zeros_amount = [(vect==0).sum() for vect in image]
    porcentual_zeros = np.sum(zeros_amount) / (height*width)
    if porcentual_zeros > 0.4:
        image_visual = image.astype(np.uint8)
    else:
        image_visual = image
    
    return image_visual

def verify_image(path):

    with fits.open(path) as hdul:
        try:
                
            image = hdul["SCI"].data
            header = hdul["SCI"].header

        except KeyError:
            image = hdul[0].data
            header = hdul[0].header
            
    return image, header