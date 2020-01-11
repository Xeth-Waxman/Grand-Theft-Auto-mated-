import numpy as np
from PIL import ImageGrab
import cv2

def screen_record(area_box = [0, 40, 800, 540]):
    """
    Grabs an image area of the screen in a continuous loop
    """
    while(True):
        # grab the image with PIL and convert to a numpy array
        img =  np.array(ImageGrab.grab(bbox=(area_box)))

        #show and refresh the captured image, converted in RGB,  until ctrl-c is pressed
        cv2.imshow('window',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
