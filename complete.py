from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayBtn=(461,507)
    dinosaur=(170,515)
    #x_tree=230
    #y_c=528
def restartGame():
    pyautogui.click(Coordinates.replayBtn)
def pressSpace():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

def imageGrab():
    box=(270,513,340,548)
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    return a.sum()
def main():
      restartGame()
      while True:
        if(imageGrab()>3047):
            pressSpace()
            time.sleep(0.000001)
            continue


main()