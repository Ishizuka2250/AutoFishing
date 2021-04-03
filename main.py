from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2
import win32gui
import pyautogui
import pydirectinput
import time
import datetime
import re
import sys
import math
import ctypes

WindowList = []
AvoidLogout = 60
ScriptEndTime = datetime.datetime.strptime("2021/04/03 20:23", "%Y/%m/%d %H:%M")

def main():
    print("Info:This script will start 5sec later.")
    time.sleep(5)
    
    hitCount = 0
    aboidLogoutCounter = 1
    print("Info:Script start.")
    while(True):
        if isHitting():
            hitCount += 1
            print(f"Info:{hitCount}Hit!")
            fishingRodAction()
            time.sleep(1.5)
            fishingRodAction()
            time.sleep(2)
        else:
            time.sleep(0.5)
        
        if aboidLogoutCounter == AvoidLogout:
            avoidAFKLogout()
            aboidLogoutCounter = 0
        
        #if ScriptEndTime < datetime.datetime.now():
        #    connectionClose()
        
        aboidLogoutCounter += 1

def connectionClose():
    keyDown('esc', 0.1)
    time.sleep(1)
    rect = windowRect("Minecraft.*")
    pyautogui.click(rect[0] + 435, rect[1] + 380, 1, 0.5, 'left')
    print("Info:Script end.")
    ctypes.windll.powrprof.SetSuspendState(1, 0, 0)
    sys.exit()

def avoidAFKLogout():
    keyDown('a', 0.2)
    keyDown('d', 0.2)

def fishingRodAction():
    x, y = windowCenterXY("Minecraft.*")
    pyautogui.click(x, y, 1, 0.5, 'right')

def keyDown(Key, pressTime):
    pydirectinput.keyDown(Key)
    time.sleep(pressTime)
    pydirectinput.keyUp(Key)

def isHitting():
    hsvImage = cv2.cvtColor(getWindowImage("Minecraft.*"), cv2.COLOR_BGR2HSV_FULL)
    
    # When fishing outdoors
    lower = (170, 0, 20)
    upper = (180, 255, 255)

    # When fishing indoors (with torch)
    #lower = (160, 0, 50)
    #upper = (170, 255, 255)

    binImage = cv2.inRange(hsvImage, lower, upper)
    contours, _ = cv2.findContours(binImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    """
    #contours = list(filter(lambda x: cv2.contourArea(x) > 5, contours))
    for i in range(0, len(contours)):
        #print(f"{i} area:{cv2.contourArea(contours[i])}")
        cv2.drawContours(hsvImage, contours, -1, color=(0, 0, 255), thickness=1)
    cv2.imshow('contours', hsvImage)
    cv2.imshow('bin', binImage)
    cv2.waitKey(0)
    """
    #sys.exit()

    if len(contours) == 0:
        return True
    else:
        return False

def getWindowImage(SearchWindowPattern):
    windowImage = centerClop(ImageGrab.grab(windowRect(SearchWindowPattern)), 200, 452)
    #windowImage = centerClop(Image.open("Minecraft_Fishing_Sample11.png"), 200, 452)
    return np.array(windowImage)

def centerClop(PillowImage, width, height):
    imageWidth, imageHeight = PillowImage.size
    if (width == 0):
        clopX1 = 0
        clopX2 = imageWidth
    else:
        clopX1 = (imageWidth / 2) - (width / 2)
        clopX2 = (imageWidth / 2) + (width / 2)
    
    if (height == 0):
        clopY1 = 0
        clopY2 = imageHeight
    else:
        clopY1 = (imageHeight / 2) - (height / 2)
        clopY2 = (imageHeight / 2) + (height / 2)
    
    if (clopX1 < 0):
        clopX1 = 0
    elif (clopX1 > imageWidth):
        cloxX1 = imageWidth
    
    if (clopX2 < 0):
        clopX2 = 0
    elif (clopX2 > imageWidth):
        clopX2 = imageWidth
    
    if (clopY1 < 0):
        clopY1 = 0
    elif (clopY1 > imageHeight):
        clopY1 = imageHeight
    
    if (clopY2 < 0):
        clopY2 = 0
    elif (clopY2 > imageHeight):
        clopY2 = imageHeight
    
    #print(str(clopX1) + " " + str(clopY1) + " " + str(clopX2) + " " + str(clopY2))
    return PillowImage.crop((clopX1,clopY1,clopX2,clopY2))

def enumWindowCallback(hwnd, _):
    windowName = win32gui.GetWindowText(hwnd)
    if (win32gui.GetWindowTextLength(hwnd) > 0) :
        WindowList.append(windowName)

def windowRect(SearchWindowPattern):
    targetWindowTitle = searchWindowTitle(SearchWindowPattern)
    hwnd = win32gui.FindWindow(None, targetWindowTitle)
    return win32gui.GetWindowRect(hwnd)

def windowCenterXY(SearchWindowPattern):
    rect = windowRect(SearchWindowPattern)
    width, height = (rect[2] - rect[0]), (rect[3] - rect[1])
    return math.floor(rect[0] + (width / 2)), math.floor(rect[1] + (height / 2))

def searchWindowTitle(SearchWindowPattern):
    WindowList.clear
    win32gui.EnumWindows(enumWindowCallback, 0)
    for windowTitle in WindowList:
        if re.match(SearchWindowPattern, windowTitle):
            return windowTitle
    print(f"Error:windowRect:Target window ({SearchWindowPattern}) does not exist.")
    sys.exit()

if __name__ == "__main__":
    main()