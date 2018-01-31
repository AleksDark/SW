#import pyscreenshot as ImageGrab
#if __name__ == "__main__":
#    # fullscreen
#    im=ImageGrab.grab()
#    im.show()

import os
os.chdir("/home/sofiev/Testaus/SW/")

import time
time.sleep(5)
import cv2
import numpy as np
from matplotlib import pyplot as plt

import pyscreenshot as ImageGrab
import random


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
        
        #print top_left
        #print bottom_right
        
    #        plt.subplot(121),plt.imshow(res,cmap = 'gray')
    #        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    #        plt.subplot(122),plt.imshow(img,cmap = 'gray')
    #        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    #        plt.suptitle(meth)
    #    
    #        plt.show()
    #        print res[top_left]
    #        print numpy.unique(res)

    aTempShape=template.shape
    print aTempShape
    print top_left[1]+1
    print top_left[1]+1+aTempShape[0]
    try:
        aFound=img[top_left[1]+1:top_left[1]+1+aTempShape[0],top_left[0]:bottom_right[0]] -template;
    except ValueError:
        aFound=img[top_left[1]:top_left[1]+1+aTempShape[0],top_left[0]:bottom_right[0]] -template;
    #    aFound=img[top_left[1]+1:top_left[1]+1+aTempShape[0],top_left[0]:bottom_right[0]] -template;
    #    aFound=img[top_left[1]+1:bottom_right[1]+1,top_left[0]:bottom_right[0]] -template;
    aKoko=aFound.shape
    #print (img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]).shape
    #print template.shape
    print 1.0*aFound.sum()/(aKoko[0]*aKoko[1])
#    
    #    
    #    plt.subplot(131)
    #    plt.imshow(img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]])
    #    plt.subplot(132)
    #    plt.imshow(template)
    #    plt.subplot(133)
    #    plt.imshow(aFound)
    
    #aIm=img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
    return top_left,bottom_right,min_val 

#def fFindImageG(sPath1, sPath2):
#    img = cv2.imread(sPath1,1)
#    img2 = img.copy()
#    template = cv2.imread(sPath2,1)
#    w, h = template.shape[::-1]
#    
#    # All the 6 methods for comparison in a list
#    #methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#    #            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
#    methods = ['cv2.TM_SQDIFF_NORMED']
#    
#    for meth in methods:
#        img = img2.copy()
#        method = eval(meth)
#    
#        # Apply template Matching
#        res = cv2.matchTemplate(img,template,method)
#        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#        print min_val, max_val, min_loc, max_loc
#        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#            top_left = min_loc
#        else:
#            top_left = max_loc
#        bottom_right = (top_left[0] + w, top_left[1] + h)
#    
#        cv2.rectangle(img,top_left, bottom_right, 255, 1)
#        
#        #print top_left
#        #print bottom_right
#        
#    #        plt.subplot(121),plt.imshow(res,cmap = 'gray')
#    #        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#    #        plt.subplot(122),plt.imshow(img,cmap = 'gray')
#    #        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#    #        plt.suptitle(meth)
#    #    
#    #        plt.show()
#    #        print res[top_left]
#    #        print numpy.unique(res)
#
#    aFound=img[top_left[1]+1:bottom_right[1]+1,top_left[0]:bottom_right[0]] -template;
#    aKoko=aFound.shape
#    #print (img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]).shape
#    #print template.shape
#    print 1.0*aFound.sum()/(aKoko[0]*aKoko[1])
##    
#    #    
#    #    plt.subplot(131)
#    #    plt.imshow(img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]])
#    #    plt.subplot(132)
#    #    plt.imshow(template)
#    #    plt.subplot(133)
#    #    plt.imshow(aFound)
#    
#    #aIm=img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]
#    return top_left,bottom_right,min_valm_right,min_val 





if __name__== "__main__":
    t1=time.time()
    
    while(time.time()-t1<3):
        im = ImageGrab.grab()
        im.save('CurrentView.png')
        
        print "-------------------------------------"
        print "Zoom"
        
        sPath1='CurrentView.png'
        sPath2='Images/zoom_campaign.png'
        top_left,bottom_right,min_val=fFindImage(sPath1, sPath2)
        if min_val<0.45:
            print "Zoom button found"
            os.system("xdotool mousemove "+str(top_left[0])+" "+str(top_left[1]))
            time.sleep(2)
            os.system("xdotool mousemove "+str(bottom_right[0])+" "+str(bottom_right[1]))
            print bottom_right, top_left
        
#        print "-------------------------------------"
#        print "Campaign title"
#    
#            
#        top_left,bottom_right,min_val=fFindImage('CurrentView.png', 'Images/campaign_title.png')
#        if min_val<0.375:
#            print "Campaing title found"
#            os.system("xdotool mousemove "+str(top_left[1])+" "+str(top_left[0]))
#            time.sleep(2)
#            os.system("xdotool mousemove "+str(bottom_right[1])+" "+str(bottom_right[0]))
#            print bottom_right, top_left
#    
#        print min_val

        print "-------------------------------------"
        print "Battle"
        
        sPath1='CurrentView.png'
        sPath2='Images/battle_coliseum.png'
        top_left,bottom_right,min_val=fFindImage(sPath1, sPath2)
        if min_val<0.25 and min_val>0.235:
            print "Zoom button found"
            os.system("xdotool mousemove "+str(top_left[0])+" "+str(top_left[1]))
            time.sleep(2)
            os.system("xdotool mousemove "+str(bottom_right[0])+" "+str(bottom_right[1]))
            print bottom_right, top_left

            os.system("xdotool mousemove "+str((top_left[0]+bottom_right[0])/2 +random.randint(-3,3))+" "+str((top_left[1]+bottom_right[1])/2 +random.randint(-3,3)))
            time.sleep(1)
            os.system("xdotool click 1")
            time.sleep(10)
        
        print "-------------------------------------"
        print "Ok Button"
        im = ImageGrab.grab()
        im.save('CurrentView.png')
        
        sPath1='CurrentView.png'
        sPath2='Images/ok_coliseum.png'
        top_left,bottom_right,min_val=fFindImage(sPath1, sPath2)
        if min_val<0.2:
            print "Zoom button found"
            os.system("xdotool mousemove "+str(top_left[0])+" "+str(top_left[1]))
            time.sleep(2)
            os.system("xdotool mousemove "+str(bottom_right[0])+" "+str(bottom_right[1]))
            print bottom_right, top_left

            os.system("xdotool mousemove "+str((top_left[0]+bottom_right[0])/2 +random.randint(-3,3))+" "+str((top_left[1]+bottom_right[1])/2 +random.randint(-3,3)))
            time.sleep(1)
            os.system("xdotool click 1")
            time.sleep(2) 
        #---------------
        time.sleep(2) 
#    
#    plt.imshow(aFound-template)

#
#import pyscreenshot as ImageGrab
    ##from PIL import ImageGrab
#import cv2
#import numpy
#
#im=ImageGrab.grab(bbox=(240,94,275,127)) # X1,Y1,X2,Y2
#print type(im)
#im2=im.convert('RGB')
#print type(im2)
#im3 = numpy.array(im2)
        #print type(im3) 
#
#cv_img = im3.astype(numpy.uint8)
#cv_gray = cv2.cvtColor(cv_img, cv2.COLOR_RGB2GRAY)



#import os
#import random
#import time
#
#time.sleep(5)
#
#def fTimeClick():
#    time.sleep(random.randint(3,7)/10.0)
#    print "xdotool click 1"
#    os.system("xdotool click 1")
#    time.sleep(random.randint(3,7)/10.0)
#    
#    #os.system("xdotool mousedown 1")
#    #time.sleep(1+random.randint(3,7)/10.0)
#    #os.system("xdotool mouseup 1")
#    #time.sleep(1+random.randint(3,7)/10.0)
#    
#
#def fSceneSelectScreen():
#    print "xdotool mousemove " + str(793 + random.randint(-10,10)) +" "+str(448 + random.randint(-10,10))+""
#    os.system("xdotool mousemove " + str(793 + random.randint(-10,10)) +" "+str(448 + random.randint(-10,10))+"")
#    #os.system("
#    
#    fTimeClick();
#
#"""
#print "xdotool mousemove " + str(557 + random.randint(-15,15)) +" "+str(580 + random.randint(-3,3))+""
#os.system("xdotool mousemove " + str(557 + random.randint(-15,15)) +" "+str(580 + random.randint(-10,10))+"")
#
#fTimeClick();
#""""
#
#def fLowerDifficulity():
#    ## Changing difficulity
#    time.sleep(random.randint(3,7))
#    print "xdotool mousemove " + str(433 + random.randint(-15,15)) +" "+str(673 + random.randint(-2,2))
#    os.system("xdotool mousemove " + str(433 + random.randint(-15,15)) +" "+str(673 + random.randint(-3,3)))
#    
#    fTimeClick();
#    
#    # Lowering
#    time.sleep(random.randint(3,7))
#    print "xdotool mousemove " + str(626 + random.randint(-5,5)) +" "+str(476 + random.randint(-5,5))
#    os.system("xdotool mousemove " + str(626 + random.randint(-5,5)) +" "+str(476 + random.randint(-5,5)))
#    
#    fTimeClick();
#    
#    # Reduced
#    
#    time.sleep(random.randint(3,7))
#    print "xdotool mousemove " + str(619 + random.randint(-5,5)) +" "+str(626 + random.randint(-5,5))
#    os.system("xdotool mousemove " + str(619 + random.randint(-5,5)) +" "+str(626 + random.randint(-5,5)))
#    
#    #for i in range(3):
#    fTimeClick();
#    
#
#
#def fCombatWon():
#    ## Waiting till end of combat
#    time.sleep(100)
#    
#    # Closing combat window
#    time.sleep(random.randint(3,7))
#    print "xdotool mousemove " + str(757 + random.randint(-5,5)) +" "+str(790 + random.randint(-5,5))
#    os.system("xdotool mousemove " + str(757 + random.randint(-5,5)) +" "+str(790 + random.randint(-5,5)))
#    
#    fTimeClick();
