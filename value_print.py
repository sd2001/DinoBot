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
    time.sleep(0.01)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box=(280,513,360,548)
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
while True:
    imageGrab()
