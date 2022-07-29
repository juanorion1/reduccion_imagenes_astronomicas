import cv2 as cv


class MouseEvent:
    def __init__(self):
        self.ref_point = []
        #pass

    drawing = False # true if mouse is pressed
    mode = True # if True, draw rectangle. Press 'm' to toggle to curve
    ix,iy = -1,-1

    

    def shape_selection(self, event, x, y, flags, params):
        img = params["img"]
        name = params["name"]
        # grab references to the global variables
        #global self.ref_point, crop

        # if the left mouse button was clicked, record the starting
        # (x, y) coordinates and indicate that cropping is being performed
        if event == cv.EVENT_LBUTTONDOWN:
            self.ref_point = [(x, y)]

        # check to see if the left mouse button was released
        elif event == cv.EVENT_LBUTTONUP:
            # record the ending (x, y) coordinates and indicate that
            # the cropping operation is finished
            self.ref_point.append((x, y))

            # draw a rectangle around the region of interest
            cv.rectangle(img, self.ref_point[0], self.ref_point[1], (255, 255, 0), 2)
            cv.imshow(name, img)