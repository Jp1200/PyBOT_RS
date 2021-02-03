import numpy as np
import pyautogui
import cv2
import keyboard
from matplotlib import pyplot as plt



class MinerLumb:
    def __init__(self, name):
        self.name = name
        self.rsClient = pyautogui.getWindowsWithTitle("RuneLite - OneChunkMunk")[0]


    def set_window_focus(self):
        self.rsClient.activate()
    def check_for_inv(self):
        pass

    def click_on_ore(self):
        # If will is availible click once
        # wait rand(20 seconds)
        # check if its still there
        # wait again
        # if not wait rand(8-10s)
        # click on ore if there
        pass

    def shift_click_ore(self):
        # Need to go through each log in the inventory, maybe randomly to seem more human
        # mouseover event for each point in the middle of the rectangle
        # do this until no more points
        # reloop by clicking on ore
        pass
    def check_for_availible_ore(self):
        # if tree is there, loop
        # if not break
        pass




# Template matching
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html#template-matching

# bot1 = MinerLumb("copper_boy")
# print(bot1.rsClient)
# bot1.set_window_focus()


img_rgb = cv2.imread('images/screen.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template_willow = cv2.imread('images/willow_log.png', 0)
w, h = template_willow.shape[::-1]
template_willow_tree = cv2.imread('images/willow.png', 0)
wT, hT = template_willow_tree.shape[::-1]
res = cv2.matchTemplate(img_gray,template_willow, cv2.TM_CCOEFF_NORMED)

resT = cv2.matchTemplate(img_gray,template_willow_tree, cv2.TM_CCOEFF_NORMED)

threshold = 0.8
thresholdT = 0.8
locT = np.where(resT >= thresholdT)
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0]+ w, pt[1] + h), (0,0,255),2)
for pt in zip(*locT[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0]+ wT, pt[1]+ hT),(255,0,255),2)


cv2.imwrite("result.png",img_rgb)


# while (1):

#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     pyautogui.displayMousePosition()
#     if keyboard.read_key() == "q":
#         break
    
        