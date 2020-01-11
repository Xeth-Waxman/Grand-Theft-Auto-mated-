import numpy as np
from PIL import ImageGrab
import cv2
import time
from key_strokes import PressKey, ReleaseKey, W, A, S, D
import pyautogui




def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)
    except:
        pass


def process_img(original_img):
    """
    takes an image and converts it to grey scale and then applies
    Canny edging analysis
    """
    #greyscale the image
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

    #perform Canny edge detection
    processed_img = cv2.Canny(processed_img, threshold1=100, threshold2=400)

    #blur lines to help with anti-aliasing
    processed_img = cv2.GaussianBlur(processed_img, (5, 5), 0)

    #return the region of interest
    vertices = np.array([[0, 600], [0, 350], [300, 150],[500, 150], [800, 350], [800, 600]])
    processed_img = region_of_interest(processed_img, [vertices])

    #hough our lines here
    lines = cv2.HoughLines(processed_img, 1, np.pi/180, 180, 20, 15)

    #draw the lines
    draw_lines(processed_img, lines)

    return processed_img


def region_of_interest(img, vertices):
    """
    Takes an image and a set of vertices of a poly and applies a mask so that
    only the region of interest is edged
    """
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def main():

    #countdown from 10 to give time to get to the GTA window
    # for i in list(range(4))[::-1]:
    #     print(i+1)
    #     time.sleep(1)


    while(True):
        # grab the image with PIL and convert to a numpy array
        area_box = [0, 40, 800, 640]
        #PressKey(W)
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
