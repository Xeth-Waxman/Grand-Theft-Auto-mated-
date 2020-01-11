import numpy as np
from PIL import ImageGrab
import cv2

def process_img(original_img):
    """
    takes an image and converts it to grey scale and then applies
    Canny edging analysis
    """
    #greyscale the image
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

    #perform Canny edge detection
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img


# def screen_record(area_box = [0, 40, 800, 540]):
#     """
#     Grabs an image area of the screen in a continuous loop
#     """
while(True):
    # grab the image with PIL and convert to a numpy array
    area_box = [0, 40, 800, 640]
    img =  np.array(ImageGrab.grab(bbox=(area_box)))
    processed_img = process_img(img)

    #show and refresh the captured image, converted in RGB,  until ctrl-c is pressed
    # cv2.imshow('window',cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB))
    cv2.imshow('Widow', processed_img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
