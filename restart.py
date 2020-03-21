from PIL import ImageGrab
import pyautogui
import time

class Coordinates():
    replayBtn=(461,507)
    dinosaur=(170,515)

def restartGame():
    pyautogui.click(Coordinates.replayBtn)
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')
restartGame()
time.sleep(2)
pressSpace()