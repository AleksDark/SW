#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 21:16:19 2017

@author: sofiev
"""



import datetime
import time
import cv2

import numpy
def fSamePicture(sPath1, sPath2, posX, posY):
    imgA=cv2.imread(sPath1);
    imgB=cv2.imread(sPath2);
    workA=numpy.int32(imgA[posX:posX+imgB.shape[0], posY:posY+imgB.shape[1], :]);
    workB=numpy.int32(imgB);
    
    return numpy.sum(abs(workA-workB)[:])/imgB.shape[0] /imgB.shape[1]


def fFindImage(sPath1, sPath2):
    img = cv2.imread(sPath1,0)
    img2 = img.copy()
    template = cv2.imread(sPath2,0)
    w, h = template.shape[::-1]
    
    # All the 6 methods for comparison in a list
    #methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    methods = ['cv2.TM_SQDIFF_NORMED']
    
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
    
        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print min_val, max_val, min_loc, max_loc
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
    
        cv2.rectangle(img,top_left, bottom_right, 255, 1)
        

    aTempShape=template.shape
    print aTempShape
    print top_left[1]+1
    print top_left[1]+1+aTempShape[0]
    try:
        aFound=img[top_left[1]+1:top_left[1]+1+aTempShape[0],top_left[0]:bottom_right[0]] -template;
    except ValueError:
        aFound=img[top_left[1]:top_left[1]+1+aTempShape[0],top_left[0]:bottom_right[0]] -template;
    aKoko=aFound.shape
    print 1.0*aFound.sum()/(aKoko[0]*aKoko[1])
    return top_left,bottom_right,min_val 




import pyautogui

from selenium import webdriver
print(datetime.datetime.now())


from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=/home/sofiev/.config/chromium/Default/Default/") #Path to your chrome profile

browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)
browser.maximize_window()
# drop the pleasantries, just open the Flash object
#browser.get('http://www.iltalehti.fi')

browser.get('http://www.kongregate.com/games/stormwars/storm-wars')
#pyautogui.moveTo(683, 333)
#        pyautogui.click()


time.sleep(5)
browser.execute_script("window.scrollTo(0, 250)")
#sound
pyautogui.moveTo(963, 213)
time.sleep(35)
pyautogui.click()
time.sleep(5)

#low
pyautogui.moveTo(463, 783)
time.sleep(5)
pyautogui.click()
time.sleep(1)
pyautogui.click()
time.sleep(1)
#pyautogui.moveTo(968,215)
#time.sleep(1)
#pyautogui.click()

#start
pyautogui.moveTo(634, 664)
time.sleep(5)
pyautogui.click()
time.sleep(10)

#--------------- pressing ok + claiming reward
browser.save_screenshot("CurrentView.png")

sPath1='CurrentView.png'
sPath2='Images/ok.png'
top_left,bottom_right,min_val=fFindImage(sPath1, sPath2)

#bClick=fSamePicture(sPath1, sPath2, top_left[0], top_left[1]);
posX=top_left[1];
posY=top_left[0];
bClick=fSamePicture(sPath1, sPath2, posX, posY);


while(bClick >30):
    time.sleep(1)    
    browser.save_screenshot("CurrentView.png")
    sPath1='CurrentView.png'
    sPath2='Images/ok.png'
    top_left,bottom_right,min_val=fFindImage(sPath1, sPath2)
    posX=top_left[1];
    posY=top_left[0];
    bClick=fSamePicture(sPath1, sPath2, posX, posY);

pyautogui.moveTo(posX+20, posY+20)



browser.save_screenshot(datetime.datetime.now().strftime('rds__%Y-%m-%d__%H.%M.png'))
time.sleep(10)
#browser.close()

print(datetime.datetime.now())



