#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:43:11 2018

@author: sofiev
"""

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

sUnknownHero='/home/sofiev/Testaus/SW/ArenaClimber/UnknownHero.png'


sAgone='/home/sofiev/Testaus/SW/ArenaClimber/Agone.png'
sAmariel='/home/sofiev/Testaus/SW/ArenaClimber/Amariel.png'
sAnasi='/home/sofiev/Testaus/SW/ArenaClimber/Anasi.png'
sAshkar='/home/sofiev/Testaus/SW/ArenaClimber/Ashkar.png'
sAubren='/home/sofiev/Testaus/SW/ArenaClimber/Aubren.png'
sBella='/home/sofiev/Testaus/SW/ArenaClimber/Bella.png'
sClom='/home/sofiev/Testaus/SW/ArenaClimber/Clom.png'
sEliana='/home/sofiev/Testaus/SW/ArenaClimber/Eliana.png'
sFreya='/home/sofiev/Testaus/SW/ArenaClimber/Freya.png'
sHylok='/home/sofiev/Testaus/SW/ArenaClimber/Hylok.png'
sGlasha='/home/sofiev/Testaus/SW/ArenaClimber/Glasha.png'
sGorm='/home/sofiev/Testaus/SW/ArenaClimber/Gorm.png'
sKhar='/home/sofiev/Testaus/SW/ArenaClimber/Khar.png'
sKiri='/home/sofiev/Testaus/SW/ArenaClimber/Kiri.png'
sKutyr='/home/sofiev/Testaus/SW/ArenaClimber/Kutyr.png'
sLaertes='/home/sofiev/Testaus/SW/ArenaClimber/Laertes.png'
sLuther='/home/sofiev/Testaus/SW/ArenaClimber/Luther.png'
sOtuk='/home/sofiev/Testaus/SW/ArenaClimber/Otuk.png'
sMalik='/home/sofiev/Testaus/SW/ArenaClimber/Malik.png'
sMyrrhine='/home/sofiev/Testaus/SW/ArenaClimber/Myrrhine.png'
sPavuk='/home/sofiev/Testaus/SW/ArenaClimber/Pavuk.png'
sPhantic='/home/sofiev/Testaus/SW/ArenaClimber/Phantic.png'
sQuillen='/home/sofiev/Testaus/SW/ArenaClimber/Quillen.png'
sSaphi='/home/sofiev/Testaus/SW/ArenaClimber/Saphi.png'
sSaa='/home/sofiev/Testaus/SW/ArenaClimber/SaaRas.png'
sSidalis='/home/sofiev/Testaus/SW/ArenaClimber/Sidalis.png'
sVyona='/home/sofiev/Testaus/SW/ArenaClimber/Vyona.png'
sZuu='/home/sofiev/Testaus/SW/ArenaClimber/Zuu.png'



sCrewBella='/home/sofiev/Testaus/SW/ArenaClimber/CrewBella.png'

import os
os.chdir('/home/sofiev/Testaus/SW/ArenaClimber/')

import pyscreenshot as ImageGrab
import time, numpy, random
import cv2

##### Initialization
lScreens=['1','2','3'];

for i in lScreens:
    time.sleep(3)
    sCommand="xdotool set_desktop "+ i
    os.system(sCommand);
    os.system("xdotool mousemove 100 100")

    time.sleep(5);
    os.system("xdotool mousemove 1593 170")
    time.sleep(5);
    os.system("xdotool mousedown 1")
    time.sleep(1.7);
    os.system("xdotool mousemove 1593 218")
    time.sleep(1.7);
    os.system("xdotool mouseup 1")
    
    
    tchest=numpy.zeros(len(lScreens));
    t1=time.time()
    dArenaSimilarityLimit=0.1
    dSimilarityLimit=0.1
    

while(time.time()-t1<350000):
    time.sleep(5)
    for iScreen in range(len(lScreens)):
        sCommand="xdotool set_desktop "+ lScreens[iScreen]
        os.system(sCommand);


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


            if(time.time()-tchest[iScreen]>30*60):
                fChestOpener(sPath,sChests)
                time.sleep(5);
                tchest[iScreen]=time.time();
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
                    time.sleep(4.1);
                    os.system("xdotool click 1")
                    time.sleep(0.1);
                    os.system("xdotool click 1")
                    time.sleep(5.1);
                    
                    #arena,arena
                    os.system("xdotool mousemove 344 272")
                    time.sleep(4.1);
                    os.system("xdotool click 1")
                    time.sleep(0.1);
                    os.system("xdotool click 1")
                    time.sleep(5.1);
                else: 
                    #continue
                    break        
                
            # clicking to left border
            time.sleep(5);
            os.system("xdotool mousemove 1127 742")
            time.sleep(5);
            #            os.system("xdotool click 1")        
            #            time.sleep(0.3);
            #            os.system("xdotool click 1")        
            #            time.sleep(0.3);
            #            os.system("xdotool click 1")        
            #            time.sleep(0.3);
            #            os.system("xdotool click 1")        
            im = ImageGrab.grab();
            im.save(sPath);
        
            # Setting clom deck as default
            lPossibilities=['1'];
            #lPossibilities=['7','1', '4'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 1");
            time.sleep(1)




            lHeroes=[['Agone',      sAgone,     ['1','1'],                              ['1','3'],              ['1','3']],
                     ['Amariel',    sAmariel,   ['8','8','8','8','1'],                  ['1',],                 ['1']],
                     ['Anasi',      sAnasi,     ['1','4', '4','4','4','6'],             ['1'],                  ['1']],
                     ['Ashkar',     sAshkar,    ['1','1', '1'],                         ['1'],                  ['1']],
                     ['Aubren',     sAubren,    ['4','4', '4','4','1'],                 ['1'],                  ['1']],
                     ['Bella',      sBella,     ['2','2','2','2','2','8','1'],          ['1','2'],              ['1','2']],
                     ['Clom',       sClom,      ['1','1','1','1','1','3','1'],          ['3','3','3','2'],      ['3','3','3','2']],
                     ['Eliana',     sEliana,    ['1','6', '6','6','6','6','8'],         ['1','3'],              ['1','3']],
                     ['Freya',      sFreya,     ['1','1','1','7','5','1'],              ['1','2','3','3'],      ['1','2','3','3']],
                     ['Gorm',       sGorm,      ['3','3','9','9','9','1'],              ['1','3'],              ['1','3']],
                     ['Glasha',     sGlasha,    ['1','2','8','10','10','10'],           ['2'],                  ['2']],
                     ['Hylok',      sHylok,     ['3','3','7','7','7','1'],              ['1','2','3'],          ['1','2','3']],
                     ['Khar',       sKhar,      ['8','8','8','8','8','8','1','1','6'],  ['1','2'],              ['1','2']],
                     ['Kiri',       sKiri,      ['7','5','4'],                          ['1','2','3'],          ['1','2','3']],
                     ['Kutyr',      sKutyr,     ['8','8','8','8','8','8','1','4'],      ['1','2'],              ['1','2']],
                     ['Laertes',    sLaertes,   ['7','8','8','8'],                      ['1','2','3','3'],      ['1','2','3','3']],
                     ['Luther',     sLuther,    ['7','8','8','8'],                      ['1','2','3','3'],      ['1','2','3','3']],
                     ['Malik',      sMalik,     ['5','7'],                              ['1','3','3','3'],      ['1','3','3','3']],
                     ['Myrrhine',   sMyrrhine,  ['5'],                                  ['1','3','3','3'],      ['1','3','3','3']],
                     ['Otuk',       sOtuk,      ['4'],                                  ['1','2','2','2'],      ['1','2','2','2']],
                     ['Pavuk',      sPavuk,     ['1','4','7','8'],                      ['1','3','3','3'],      ['1','3','3','3']],
                     ['Phantic',    sPhantic,   ['8'],                                  ['1','2'],              ['1','2']],
                     ['Quillen',    sQuillen,   ['7','7','7','8'],                      ['1','3','3','3'],      ['1','3','3','3']],
                     ['Saa',        sSaa,       ['4','9','9'],                          ['1','3'],              ['1','3']],
                     ['Saphi',      sSaphi,     ['1','9','9','9','9'],                  ['1','2','3'],          ['1','2','3']],
                     ['Sidalis',    sSidalis,   ['3'],                                  ['2','3'],              ['2','3']],
                     ['Vyona',      sVyona,     ['1','5'],                              ['1','3','3','3'],      ['1','3','3','3']],
                     ['Zuu',        sZuu,       ['4','4','4','9','9','9','7','7','7'],  ['1','2'],              ['1','2']]               
                     ]
            
            bFoundHero=False;
            for iHero in range(len(lHeroes)):
                im1=cv2.imread(sPath);
                im2=cv2.imread(lHeroes[iHero][1]);
                aimg=im1[358:527, 771:932,:];
                bimg=im2[358:527, 771:932,:];   
                print lHeroes[iHero][0] +' suitability: '+ str(fSimilarity(aimg,bimg))
                
                if fSimilarity(aimg,bimg)<dSimilarityLimit :
                    print '-----------------'
                    print lHeroes[iHero][0] + ' opponent'
                    print '-----------------'
                    lPossibilities=lHeroes[iHero][1+int(lScreens[iScreen])];
                    sCommand="xdotool key "+ random.choice(lPossibilities)
                    os.system(sCommand);
                    time.sleep(1)
                    bFoundHero=True
                    break
                
            if bFoundHero==False:
                os.system('cp '+sPath +' ' + sUnknownHero)
            
            sCommand="xdotool mousemove "+str(845+numpy.random.randint(-2,2))+" "+str(676+numpy.random.randint(-2,2))
            os.system(sCommand)
            time.sleep(1);
            os.system("xdotool click 1")        
            time.sleep(1);

        
        
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
            time.sleep(5.1);
            os.system("xdotool click 1")
            time.sleep(0.1);
            os.system("xdotool click 1")
            time.sleep(5.1);
        else:
            print "Launching single"
            os.system("python single.py")
            time.sleep(1);






##from PIL import Image
##i=Image.open(sPath)

#aimg=im2[100:200,100:300,:];
#bimg=im2[200:300,100:300,:];
#
#
#print fSimilarity(aimg,bimg)

