import numpy as np
from PIL import ImageGrab
import cv2

# def screen_record():
while(True):
    # 800x600 windowed mode - add 40 vertical for the titlebar
    area_box = [9, 40, 800, 640]

    # grab the image with PIL and convert to a numpy array
    img =  np.array(ImageGrab.grab(bbox=(area_box)))

    #show and refresh the captured image, converted in RGB,  until ctrl-c is pressed
    cv2.imshow('window',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
