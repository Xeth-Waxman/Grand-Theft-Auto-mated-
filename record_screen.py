import numpy as np
from PIL import ImageGrab
import cv2
import time
from key_strokes import PressKey, W, A, S, D

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


def main():

    #countdown from 10 to give time to get to the GTA window
    for i in list(range(9))[::-1]:
        print(i+1)
        time.sleep(1)


    while(True):
        # grab the image with PIL and convert to a numpy array
        area_box = [0, 40, 800, 640]
        PressKey(W)
        img =  np.array(ImageGrab.grab(bbox=(area_box)))
        processed_img = process_img(img)

        #show and refresh the captured image, converted in RGB,  until ctrl-c is pressed
        # cv2.imshow('window',cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB))
        cv2.imshow('Widow', processed_img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__== "__main__":
  main()
