#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:18:32 2017

@author: sofiev
"""
def fSimilarity(aimg,bimg):
    aimg=numpy.int32(aimg);
    bimg=numpy.int32(bimg);8448
    return 1.0*(abs(aimg-bimg)).sum() / aimg.size /255 ;

def fScreenshot():
    time.sleep(5)
    im = ImageGrab.grab();
    im.save(sPath);

def fChestOpener(sPath,sChests):
    # 241, 434  -- 422, 472
    # 447, 435 -- 626, 469
    # 652, 436 -- 831, 467
    # 854, 431 -- 1031, 468
    # 241, 686 -- 421, 719
    # 446, 686 -- 627, 717
    # 651, 681 -- 831, 718
    # 854, 686 -- 1035, 719 
    aChestsPos=numpy.array([[241,434,422,470],
            [447,435,626,469],
            [652,436,831,467],
            [854,435,1031,468],
            [241,686,421,719],
            [446,686,627,718],
            [651,681,831,718],
            [854,686,1035,719]
            ])
    
    # main menu treasures button:  638 501
    # return button x:168 y:800
    # arena x:639 y:354
    # chest x:447 y:193
    # arena's arena x:344 y:272
    # ok: x:640 y:735

    #return
    os.system("xdotool mousemove 168 800")
    time.sleep(3.1);
    os.system("xdotool click 1")
    time.sleep(0.1);
    os.system("xdotool click 1")
    time.sleep(5.1);
    
    #mm, treasures
    os.system("xdotool mousemove 638 501")
    time.sleep(1.1);
    os.system("xdotool click 1")
    time.sleep(0.1);
    os.system("xdotool click 1")
    time.sleep(5.1);
    
    #chest
    os.system("xdotool mousemove 447 193")
    time.sleep(1.1);
    os.system("xdotool click 1")
    time.sleep(0.1);
    os.system("xdotool click 1")
    time.sleep(5.1);
    
    im = ImageGrab.grab();
    im.save(sPath);
    
    im1=cv2.imread(sPath);
    im2=cv2.imread(sChests);
    for i in range(8):
        aimg=im1[aChestsPos[i][1]:aChestsPos[i][3],aChestsPos[i][0]:aChestsPos[i][2],:];
        bimg=im2[aChestsPos[i][1]:aChestsPos[i][3],aChestsPos[i][0]:aChestsPos[i][2],:];
        print fSimilarity(aimg, bimg)
        if fSimilarity(aimg,bimg)<0.05 :
            sCommand="xdotool mousemove " + str( (aChestsPos[i][0] + aChestsPos[i][2])/2) + " " +  str( (aChestsPos[i][1] + aChestsPos[i][3])/2) 
            os.system(sCommand)
            time.sleep(1);
            os.system("xdotool click 1")
            time.sleep(5);
            os.system("xdotool mousemove 640 735")
            time.sleep(1);
            os.system("xdotool click 1")
            time.sleep(5);

    #return
    os.system("xdotool mousemove 168 800")
    time.sleep(3.1);
    os.system("xdotool click 1")
    time.sleep(0.1);
    os.system("xdotool click 1")
    time.sleep(5.1);

    #mm,arena
    os.system("xdotool mousemove 639 354")
    time.sleep(3.1);
    os.system("xdotool click 1")
    time.sleep(0.1);
    os.system("xdotool click 1")
    time.sleep(5.1);
    
    #arena,arena
    os.system("xdotool mousemove 344 272")
    time.sleep(3.1);
    os.system("xdotool click 1")
    time.sleep(0.1);
    os.system("xdotool click 1")
    time.sleep(5.1);




            

sArena='/home/sofiev/Testaus/SW/ArenaClimber/Arena.png'
sChests='/home/sofiev/Testaus/SW/ArenaClimber/Chests.png'
sMain='/home/sofiev/Testaus/SW/ArenaClimber/MainMenu.png'
sPath='/home/sofiev/Testaus/SW/ArenaClimber/CurrentView.png'



sAgone='/home/sofiev/Testaus/SW/ArenaClimber/Agone.png'
sAmariel='/home/sofiev/Testaus/SW/ArenaClimber/Amariel.png'
sAnasi='/home/sofiev/Testaus/SW/ArenaClimber/Anasi.png'
sAshkar='/home/sofiev/Testaus/SW/ArenaClimber/Ashkar.png'
sAubren='/home/sofiev/Testaus/SW/ArenaClimber/Aubren.png'
sBella='/home/sofiev/Testaus/SW/ArenaClimber/Bella.png'
sClom='/home/sofiev/Testaus/SW/ArenaClimber/Clom.png'
sFreya='/home/sofiev/Testaus/SW/ArenaClimber/Freya.png'
sHylok='/home/sofiev/Testaus/SW/ArenaClimber/Hylok.png'
sGlasha='/home/sofiev/Testaus/SW/ArenaClimber/Glasha.png'
sGorm='/home/sofiev/Testaus/SW/ArenaClimber/Gorm.png'
sKhar='/home/sofiev/Testaus/SW/ArenaClimber/Khar.png'
sKutyr='/home/sofiev/Testaus/SW/ArenaClimber/Kutyr.png'
sLuther='/home/sofiev/Testaus/SW/ArenaClimber/Luther.png'
sOtuk='/home/sofiev/Testaus/SW/ArenaClimber/Otuk.png'
sPavuk='/home/sofiev/Testaus/SW/ArenaClimber/Pavuk.png'
sPhantic='/home/sofiev/Testaus/SW/ArenaClimber/Phantic.png'
sQuillen='/home/sofiev/Testaus/SW/ArenaClimber/Quillen.png'
sSaa='/home/sofiev/Testaus/SW/ArenaClimber/SaaRas.png'
sSidalis='/home/sofiev/Testaus/SW/ArenaClimber/Sidalis.png'
sVyona='/home/sofiev/Testaus/SW/ArenaClimber/Vyona.png'
sZuu='/home/sofiev/Testaus/SW/ArenaClimber/Zuu.png'


import os
os.chdir('/home/sofiev/Testaus/SW/ArenaClimber/')

import pyscreenshot as ImageGrab
import time, numpy, random
import cv2

##### Initialization
time.sleep(10);
os.system("xdotool mousemove 1593 170")
time.sleep(5);
os.system("xdotool mousedown 1")
time.sleep(0.7);
os.system("xdotool mousemove 1593 218")
time.sleep(0.7);
os.system("xdotool mouseup 1")


tchest=0;
t1=time.time()
dArenaSimilarityLimit=0.1
dSimilarityLimit=0.1
    
while(time.time()-t1<350000):
    time.sleep(3);
    im = ImageGrab.grab();
    im.save(sPath);
    
    im1=cv2.imread(sPath);
    im2=cv2.imread(sArena);
    im3=cv2.imread(sMain);
    aimg=im1[641:717,170:979,:];
    bimg=im2[641:717,170:979,:];
    
    
    
    print "Arena similarity "+ str(fSimilarity(aimg,bimg))
    if fSimilarity(aimg,bimg)<dArenaSimilarityLimit :
        print "Arena screen";
                 
        if(time.time()-tchest>30*60):
            fChestOpener(sPath,sChests)
            time.sleep(5);
            tchest=time.time();
            #verifying that we back in arena screen
            im = ImageGrab.grab();
            im.save(sPath);
        
            im1=cv2.imread(sPath);
            im2=cv2.imread(sArena);
            aimg=im1[641:717,170:979,:];
            bimg=im2[641:717,170:979,:];
            
            print fSimilarity(aimg,bimg)
            if fSimilarity(aimg,bimg)<dSimilarityLimit :
                print "Arena screen";
            elif fSimilarity(im1[263:752,544:736,:],im3[263:752,544:736,:])<dSimilarityLimit :        
                print 'Mainmenu suitability: '+ str(fSimilarity(im1[263:752,544:736,:],im3[263:752,544:736,:]))
                #mm,arena
                os.system("xdotool mousemove 639 354")
                time.sleep(3.1);
                os.system("xdotool click 1")
                time.sleep(0.1);
                os.system("xdotool click 1")
                time.sleep(5.1);
                
                #arena,arena
                os.system("xdotool mousemove 344 272")
                time.sleep(3.1);
                os.system("xdotool click 1")
                time.sleep(0.1);
                os.system("xdotool click 1")
                time.sleep(5.1);
            else: 
                continue
                #break        
        
        # clicking to left border
        time.sleep(5);
        os.system("xdotool mousemove 1127 742")
        time.sleep(5);
        os.system("xdotool click 1")        
        time.sleep(0.3);
        os.system("xdotool click 1")        
        time.sleep(0.3);
        os.system("xdotool click 1")        
        time.sleep(0.3);
        os.system("xdotool click 1")        
        im = ImageGrab.grab();
        im.save(sPath);
        
        # Setting rush deck as default
        lPossibilities=['1','2'];
        #lPossibilities=['7','1', '4'];
        sCommand="xdotool key "+ random.choice(lPossibilities)
        os.system(sCommand);
        #os.system("xdotool key 1");
        time.sleep(1)

            
        # if Glasha
        im1=cv2.imread(sPath);
        im2=cv2.imread(sGlasha);        
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];
        print fSimilarity(aimg,bimg)
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print "Glasha opponent"
            lPossibilities=['2','2','2','8','1','2','10','10','10','10','10'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            time.sleep(1)

        # if Amariel
        im1=cv2.imread(sPath);
        im2=cv2.imread(sAgone);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Agone suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Agone opponent"
            print '-----------------'
            os.system("xdotool key 1");
            time.sleep(1)

        # if Amariel
        im1=cv2.imread(sPath);
        im2=cv2.imread(sAmariel);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Amariel suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Amariel opponent"
            print '-----------------'
            os.system("xdotool key 8");
            time.sleep(1)

        # if Anasi
        im1=cv2.imread(sPath);
        im2=cv2.imread(sAnasi);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Anasi suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Anasi opponent"
            print '-----------------'
            lPossibilities=['1','4', '4','4','4','6'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)

        # if Amariel
        im1=cv2.imread(sPath);
        im2=cv2.imread(sAshkar);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Ashkar suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Ashkar opponent"
            print '-----------------'
            lPossibilities=['1','1', '1'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)

        # if Aubren
        im1=cv2.imread(sPath);
        im2=cv2.imread(sAubren);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Aubren suitability: '+str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Aubren opponent"
            print '-----------------'
            os.system("xdotool key 4");
            time.sleep(1)
        
        
        
        # if Bella
        im1=cv2.imread(sPath);
        im2=cv2.imread(sBella);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];
        print 'Bella suitability: '+str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Bella opponent"
            print '-----------------'
            lPossibilities=['2','8','8','8','8','8','1'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 2");
            time.sleep(1)

        # if Clom
        im1=cv2.imread(sPath);
        im2=cv2.imread(sClom);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Clom suitability: '+str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Clom opponent"
            print '-----------------'
            
            lPossibilities=['1','1','1','1','1','3','1'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            time.sleep(1)


        # if Freya
        im1=cv2.imread(sPath);
        im2=cv2.imread(sFreya);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Freya suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Freya opponent"
            print '-----------------'
            lPossibilities=['1','1','1','7','5','1'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)

        # if Gorm
        im1=cv2.imread(sPath);
        im2=cv2.imread(sGorm);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Gorm suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Gorm opponent"
            print '-----------------'
            lPossibilities=['3','3','9','9','9','1'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)


        # if Hylok
        im1=cv2.imread(sPath);
        im2=cv2.imread(sHylok);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Hylok suitability: '+str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print "Hylok opponent"
            lPossibilities=['3','3','7','7','7','1'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 3");
            time.sleep(1)

        # if Khar
        im1=cv2.imread(sPath);
        im2=cv2.imread(sKhar);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Khar suitability: '+str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Khar opponent"
            print '-----------------'
            lPossibilities=['8','8','8','8','8','8','1','1','6'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 8");
            time.sleep(1)

        # if Kutyr
        im1=cv2.imread(sPath);
        im2=cv2.imread(sKutyr);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Kutyr suitability: '+str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Kutyr opponent"
            print '-----------------'
            lPossibilities=['8','8','8','8','8','8','1','4'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 8");
            time.sleep(1)

        # if Luther
        im1=cv2.imread(sPath);
        im2=cv2.imread(sLuther);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Luther suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Luther opponent"
            print '-----------------'
            lPossibilities=['7','8','8','8'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)


        # if Otuk
        im1=cv2.imread(sPath);
        im2=cv2.imread(sOtuk);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Otuk suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print "Otuk opponent"
            os.system("xdotool key 4");
            time.sleep(1)

        # if Pavuk
        im1=cv2.imread(sPath);
        im2=cv2.imread(sPavuk);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Pavuk suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print "Pavuk opponent"
            os.system("xdotool key 8");
            time.sleep(1)

        # if Phantic
        im1=cv2.imread(sPath);
        im2=cv2.imread(sPhantic);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Phantic suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Phantic opponent"
            print '-----------------'
            lPossibilities=['8'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)


        # if Quilllen
        im1=cv2.imread(sPath);
        im2=cv2.imread(sQuillen);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Quillen suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Quillen opponent"
            print '-----------------'
            lPossibilities=['7','7','7','5','8'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)


        # if Saa-Ras
        im1=cv2.imread(sPath);
        im2=cv2.imread(sSaa);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Saa-Ras suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Saa-Ras opponent"
            print '-----------------'
            lPossibilities=['4','9','9'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)

        # if Sidalis
        im1=cv2.imread(sPath);
        im2=cv2.imread(sSidalis);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Sidalis suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print "Sidalis opponent"
            os.system("xdotool key 3");
            time.sleep(1)

        # if Vyon
        im1=cv2.imread(sPath);
        im2=cv2.imread(sVyona);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Vyona suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Vyona opponent"
            print '-----------------'
            lPossibilities=['1','5'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)

        # if Zuu
        im1=cv2.imread(sPath);
        im2=cv2.imread(sZuu);
        aimg=im1[358:527, 771:932,:];
        bimg=im2[358:527, 771:932,:];        
        print 'Zuu suitability: '+ str(fSimilarity(aimg,bimg))
        if fSimilarity(aimg,bimg)<dSimilarityLimit :
            print '-----------------'
            print "Zuu opponent"
            print '-----------------'
            lPossibilities=['4','4','4','9','9','9','8','7','7','7'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 6");
            time.sleep(1)


        sCommand="xdotool mousemove "+str(845+numpy.random.randint(-2,2))+" "+str(676+numpy.random.randint(-2,2))
        os.system(sCommand)
        time.sleep(1);
        os.system("xdotool click 1")        

        time.sleep(20)
        
    elif fSimilarity(im1[263:752,544:736,:],im3[263:752,544:736,:])<dArenaSimilarityLimit :        
        print 'Mainmenu suitability: '+ str(fSimilarity(im1[263:752,544:736,:],im3[263:752,544:736,:]))
        #mm,arena
        os.system("xdotool mousemove 639 354")
        time.sleep(3.1);
        os.system("xdotool click 1")
        time.sleep(0.1);
        os.system("xdotool click 1")
        time.sleep(5.1);
        
        #arena,arena
        os.system("xdotool mousemove 344 272")
        time.sleep(3.1);
        os.system("xdotool click 1")
        time.sleep(0.1);
        os.system("xdotool click 1")
        time.sleep(5.1);
    else:
        print "Launching single"
        os.system("python single.py")
        time.sleep(7);






##from PIL import Image
##i=Image.open(sPath)

#aimg=im2[100:200,100:300,:];
#bimg=im2[200:300,100:300,:];
#
#
#print fSimilarity(aimg,bimg)

