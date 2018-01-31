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

def fResultsShowing():
    #    a=numpy.load('/home/sofiev/Testaus/SW/ArenaClimber/ResultTable.dat.npz')
    #    b=a.items()
    #    c=b[0]
    #    a=c[1]
    #    del b, c
    a=aResults;
    for i in range(len(lScreens)):
        b=numpy.where(a[i,:,:,2]==a[i,:,:,2].min())
        print '------------------'
        print a[i,b[0][0],:,:]
    
    
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
        if fSimilarity(aimg,bimg)<0.0485 :
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

sArenaVictory='/home/sofiev/Testaus/SW/ArenaClimber/ArenaVictory.png'
sArenaLost='/home/sofiev/Testaus/SW/ArenaClimber/ArenaLost.png'

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
sQuilen='/home/sofiev/Testaus/SW/ArenaClimber/Quilen.png'
sSaphi='/home/sofiev/Testaus/SW/ArenaClimber/Saphi.png'
sSaa='/home/sofiev/Testaus/SW/ArenaClimber/SaaRas.png'
sSidalis='/home/sofiev/Testaus/SW/ArenaClimber/Sidalis.png'
sVyona='/home/sofiev/Testaus/SW/ArenaClimber/Vyona.png'
sZuu='/home/sofiev/Testaus/SW/ArenaClimber/Zuu.png'


sCrewAgone='/home/sofiev/Testaus/SW/ArenaClimber/crewAgone.png'
sCrewAmariel='/home/sofiev/Testaus/SW/ArenaClimber/crewAmariel.png'
sCrewAnasi='/home/sofiev/Testaus/SW/ArenaClimber/crewAnasi.png'
sCrewBella='/home/sofiev/Testaus/SW/ArenaClimber/crewBella.png'
sCrewClom='/home/sofiev/Testaus/SW/ArenaClimber/crewClom.png'
sCrewEliana='/home/sofiev/Testaus/SW/ArenaClimber/crewFreya.png'
sCrewFreya='/home/sofiev/Testaus/SW/ArenaClimber/crewEliana.png'
sCrewGlasha='/home/sofiev/Testaus/SW/ArenaClimber/crewGlasha.png'
sCrewHylok='/home/sofiev/Testaus/SW/ArenaClimber/crewHylok.png'
sCrewKhar='/home/sofiev/Testaus/SW/ArenaClimber/crewKhar.png'
sCrewKiri='/home/sofiev/Testaus/SW/ArenaClimber/crewKiri.png'
sCrewKutyr='/home/sofiev/Testaus/SW/ArenaClimber/crewKutyr.png'
sCrewLaertes='/home/sofiev/Testaus/SW/ArenaClimber/crewLaertes.png'
sCrewLuther='/home/sofiev/Testaus/SW/ArenaClimber/crewLuther.png'
sCrewMalik='/home/sofiev/Testaus/SW/ArenaClimber/crewMalik.png'
sCrewMyrrhine='/home/sofiev/Testaus/SW/ArenaClimber/crewMyrrhine.png'
sCrewOtuk='/home/sofiev/Testaus/SW/ArenaClimber/crewOtuk.png'
sCrewPhantic='/home/sofiev/Testaus/SW/ArenaClimber/crewPhantic.png'
sCrewSaa='/home/sofiev/Testaus/SW/ArenaClimber/crewSaa.png'
sCrewSaphi='/home/sofiev/Testaus/SW/ArenaClimber/crewSaphi.png'
sCrewSidalis='/home/sofiev/Testaus/SW/ArenaClimber/crewSidalis.png'
sCrewQuilen='/home/sofiev/Testaus/SW/ArenaClimber/crewQuilen.png'
sCrewVyona='/home/sofiev/Testaus/SW/ArenaClimber/crewVyona.png'
sCrewZuu='/home/sofiev/Testaus/SW/ArenaClimber/crewZuu.png'



sColiAgone='/home/sofiev/Testaus/SW/ArenaClimber/coliAgone.png'
sColiAmariel='/home/sofiev/Testaus/SW/ArenaClimber/coliAmariel.png'
sColiAnasi='/home/sofiev/Testaus/SW/ArenaClimber/coliAnasi.png'
sColiBella='/home/sofiev/Testaus/SW/ArenaClimber/coliBella.png'
sColiClom='/home/sofiev/Testaus/SW/ArenaClimber/coliClom.png'
sColiEliana='/home/sofiev/Testaus/SW/ArenaClimber/coliEliana.png'
sColiFreya='/home/sofiev/Testaus/SW/ArenaClimber/coliFreya.png'
sColiGlasha='/home/sofiev/Testaus/SW/ArenaClimber/coliGlasha.png'
sColiHylok='/home/sofiev/Testaus/SW/ArenaClimber/coliHylok.png'
sColiKhar='/home/sofiev/Testaus/SW/ArenaClimber/coliKhar.png'
sColiKiri='/home/sofiev/Testaus/SW/ArenaClimber/coliKiri.png'
sColiKutyr='/home/sofiev/Testaus/SW/ArenaClimber/coliKutyr.png'
sColiLaertes='/home/sofiev/Testaus/SW/ArenaClimber/coliLaertes.png'
sColiLuther='/home/sofiev/Testaus/SW/ArenaClimber/coliLuther.png'
sColiMalik='/home/sofiev/Testaus/SW/ArenaClimber/coliMalik.png'
sColiMyrrhine='/home/sofiev/Testaus/SW/ArenaClimber/coliMyrrhine.png'
sColiOtuk='/home/sofiev/Testaus/SW/ArenaClimber/coliOtuk.png'
sColiPavuk='/home/sofiev/Testaus/SW/ArenaClimber/coliPavuk.png'
sColiPhantic='/home/sofiev/Testaus/SW/ArenaClimber/coliPhantic.png'
sColiSaa='/home/sofiev/Testaus/SW/ArenaClimber/coliSaa.png'
sColiSaphi='/home/sofiev/Testaus/SW/ArenaClimber/coliSaphi.png'
sColiSidalis='/home/sofiev/Testaus/SW/ArenaClimber/coliSidalis.png'
sColiQuilen='/home/sofiev/Testaus/SW/ArenaClimber/coliQuilen.png'
sColiZuu='/home/sofiev/Testaus/SW/ArenaClimber/coliZuu.png'



import os
os.chdir('/home/sofiev/Testaus/SW/ArenaClimber/')

import pyscreenshot as ImageGrab
import time, numpy, random
import cv2

##### Initialization
lScreens=['1','2','3'];
#lScreens=['2','3'];


lHeroes=[['Agone',      sAgone,     sCrewAgone,     sColiAgone,         ['1','1'],                              ['3'],                  ['3']],
         ['Amariel',    sAmariel,   sCrewAmariel,   sColiAmariel,       ['8','8','8','8','1'],                  ['1'],                  ['1']],
         ['Anasi',      sAnasi,     sCrewAnasi,     sColiAnasi,         ['1','4', '4','4','4','6'],             ['1','1','1','5'],      ['1','1','1','5']],
         ['Ashkar',     sAshkar,    sPhantic,       sAgone,             ['1','1', '1'],                         ['1'],                  ['1']],
         ['Aubren',     sAubren,    sPhantic,       sAgone,             ['4','4', '4','4','1'],                 ['2','5'],              ['2','5']],
         ['Bella',      sBella,     sCrewBella,     sColiBella,         ['2','8','1'],                          ['1','5'],              ['1','5']],
         ['Clom',       sClom,      sCrewClom,      sColiClom,          ['1','1','1','1','1','3','1'],          ['1','3','3','3','5'],  ['1','3','3','3','5']],
         ['Eliana',     sEliana,    sCrewEliana,    sColiEliana,        ['1','6', '6','6','6','6','8'],         ['1','3'],              ['1','3']],
         ['Freya',      sFreya,     sCrewFreya,     sColiFreya,         ['1','1','1','7','5','7'],              ['1','5','3','3'],      ['1','5','3','3']],
         ['Gorm',       sGorm,      sPhantic,       sColiAgone,         ['3','3','9','9','9','1'],              ['1','2','3'],          ['1','2','3']],
         ['Glasha',     sGlasha,    sCrewGlasha,    sColiGlasha,        ['1','2','8','10','10','10'],           ['2','5'],              ['2','5']],
         ['Hylok',      sHylok,     sCrewHylok,     sColiHylok,         ['3','3','7','7','7','1'],              ['1','2','3'],          ['1','2','3']],
         ['Khar',       sKhar,      sCrewKhar,      sColiKhar,          ['8','8','8','8','8','8','1','1','6'],  ['1','2','5'],          ['1','2','5']],
         ['Kiri',       sKiri,      sCrewKiri,      sColiKiri,          ['7','5','4'],                          ['1','5','3'],          ['1','5','3']],
         ['Kutyr',      sKutyr,     sCrewKutyr,     sColiKutyr,         ['2','8','1','4'],                      ['1','2','5'],          ['1','2','5']],
         ['Laertes',    sLaertes,   sCrewLaertes,   sColiLaertes,       ['7','8','8','8'],                      ['1','5','5','3','3'],  ['1','5','5','3','3']],
         ['Luther',     sLuther,    sCrewLuther,    sColiLuther,        ['7','8','8','8'],                      ['1','2','3','3'],      ['1','2','3','3']],
         ['Malik',      sMalik,     sCrewMalik,     sColiMalik,         ['5','7'],                              ['1','3','3','3','5'],  ['1','3','3','3','5']],
         ['Myrrhine',   sMyrrhine,  sCrewMyrrhine,  sColiMyrrhine,      ['5'],                                  ['3','3','3'],          ['3','3','3']],
         ['Otuk',       sOtuk,      sCrewOtuk,      sColiOtuk,          ['4'],                                  ['1','5','5','5'],      ['1','5','5','5']],
         ['Pavuk',      sPavuk,     sPhantic,       sColiPavuk,         ['1','4','7','8'],                      ['1','3','3','3'],      ['1','3','3','3']],
         ['Phantic',    sPhantic,   sCrewPhantic,   sColiPhantic,       ['8'],                                  ['1','2'],              ['1','2']],
         ['Quilen',     sQuilen,    sCrewQuilen,    sColiQuilen,        ['7','7','7','8'],                      ['1','3','3','3'],      ['1','3','3','3']],
         ['Saa',        sSaa,       sCrewSaa,       sColiSaa,           ['4','9','9'],                          ['1','5'],              ['1','5']],
         ['Saphi',      sSaphi,     sCrewSaphi,     sColiSaphi,         ['1','9','9','9','9'],                  ['1','1','1','2','5'],  ['1','1','1','2','5']],
         ['Sidalis',    sSidalis,   sCrewSidalis,   sColiSidalis,       ['3'],                                  ['4'],                  ['1','1','4']],
         ['Vyona',      sVyona,     sCrewVyona,     sColiAgone,         ['1','5'],                              ['1','3','3','3'],      ['1','3','3','3']],
         ['Zuu',        sZuu,       sCrewZuu,       sColiZuu,           ['4','4','4','9','9','9','7','7','7'],  ['1','3'],              ['1','3']]               
         ]


iNumDecks=11;
aResults=numpy.ones([len(lScreens),len(lHeroes),iNumDecks,3]);
aScreenSelections=numpy.zeros([len(lScreens),2])









for i in lScreens:
    time.sleep(3)
    sCommand="xdotool set_desktop "+ i
    os.system(sCommand);
    os.system("xdotool mousemove 50 300")
    time.sleep(1.7);
    os.system("xdotool click 1")
    time.sleep(1.7);
    os.system("xdotool key Page_Up")
    
    time.sleep(5);
    os.system("xdotool mousemove 1593 170")
    time.sleep(5);
    os.system("xdotool mousedown 1")
    time.sleep(1.7);
    os.system("xdotool mousemove 1593 218")
    time.sleep(1.7);
    os.system("xdotool mouseup 1")
    
    
    t1=time.time()
    tchest=numpy.zeros(len(lScreens))+t1-500;
    
    dArenaSimilarityLimit=0.1
    dSimilarityLimit=0.1
    

while(time.time()-t1<350000):
    aResults[:,:,:,2]=aResults[:,:,:,0]/aResults[:,:,:,1];
    numpy.savez('/home/sofiev/Testaus/SW/ArenaClimber/ResultTable.dat', aResults);
    print "Worst result is:"
    for iScreen in range(len(lScreens)):
        a=numpy.where(aResults[iScreen,:,:,2]==aResults[iScreen,:,:,2].min())
        print "Screen "+ str(iScreen) +", Hero: "+ lHeroes[a[0][0]][0] + ", Deck: " + str(a[1][0]) +", Ratio: "+ str(aResults[iScreen,:,:,2].min())

    fResultsShowing()
    del a
    sCommand="xdotool set_desktop 0"
    os.system(sCommand);
    time.sleep(5)
    
    
    for iScreen in range(len(lScreens)):
        sCommand="xdotool set_desktop "+ lScreens[iScreen]
        os.system(sCommand);
        os.system("xdotool mousemove 50 300")
        time.sleep(0.7);


        time.sleep(3);
        im = ImageGrab.grab();
        im.save(sPath);

        im1=cv2.imread(sPath);
        im2=cv2.imread(sArena);
        im3=cv2.imread(sMain);
        im4=cv2.imread(sCrewBella);
        im5=cv2.imread(sColiAgone);
        
        
        if(time.time()-tchest[iScreen]>60*60):
            aimg=im1[773:838,133:198,:];
            bimg=im2[773:838,133:198,:];
            if fSimilarity(aimg,bimg)<dArenaSimilarityLimit*0.5:
                sCommand="xdotool mousemove "+str(150+numpy.random.randint(-2,2))+" "+str(800+numpy.random.randint(-2,2))
                os.system(sCommand)
                time.sleep(1);
                os.system("xdotool click 1")        
                time.sleep(1);

        
        aimg=im1[641:717,170:979,:];
        bimg=im2[641:717,170:979,:];
    
        #print "Arena similarity "+ str(fSimilarity(aimg,bimg))
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
                
                #print fSimilarity(aimg,bimg)
                if fSimilarity(aimg,bimg)<dSimilarityLimit :
                    print "Arena screen";
                elif fSimilarity(im1[263:752,544:736,:],im3[263:752,544:736,:])<dSimilarityLimit :        
                    #print 'Mainmenu suitability: '+ str(fSimilarity(im1[263:752,544:736,:],im3[263:752,544:736,:]))
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
            if(True):
            	#if(iScreen==0):
	        os.system("xdotool click 1")        
                time.sleep(0.3);
            	os.system("xdotool click 1")        
            	time.sleep(0.3);
            	os.system("xdotool click 1")        
            	time.sleep(0.3);
       		os.system("xdotool click 1")   
            	time.sleep(0.3);
            	os.system("xdotool click 1")        
            im = ImageGrab.grab();
            im.save(sPath);
        
            # Setting clom deck as default
            lPossibilities=['1'];
            #lPossibilities=['7','1', '4'];
            sCommand="xdotool key "+ random.choice(lPossibilities)
            os.system(sCommand);
            #os.system("xdotool key 1");
            time.sleep(1)



            
            bFoundHero=False;
            for iHero in range(len(lHeroes)):
                im1=cv2.imread(sPath);
                im2=cv2.imread(lHeroes[iHero][1]);
                aimg=im1[358:527, 771:932,:];
                bimg=im2[358:527, 771:932,:];   
                #print lHeroes[iHero][0] +' suitability: '+ str(fSimilarity(aimg,bimg))
                
                if fSimilarity(aimg,bimg)<dSimilarityLimit :
                    print '-----------------'
                    print lHeroes[iHero][0] + ' opponent'
                    print '-----------------'
                    lPossibilities=lHeroes[iHero][3+int(lScreens[iScreen])];
                    sSelectedAttacker=random.choice(lPossibilities);
                    sCommand="xdotool key "+ sSelectedAttacker
                    os.system(sCommand);
                    time.sleep(1)
                    bFoundHero=True
                    aScreenSelections[iScreen,0]=iHero; 
                    aScreenSelections[iScreen,1]=int(sSelectedAttacker); 
                    
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
        elif fSimilarity(im1[641:722, 389:892,:],im4[641:722, 389:892,:])<dArenaSimilarityLimit :
            print "Crew screen"

            sCommand="xdotool mousemove "+str(511+numpy.random.randint(-2,2))+" "+str(462+numpy.random.randint(-2,2))
            os.system(sCommand)
            time.sleep(1);
            os.system("xdotool click 1")        
            time.sleep(1);
            sCommand="xdotool key 1"
            os.system(sCommand);
            time.sleep(1.7)

            bFoundHero=False;
            for iHero in range(len(lHeroes)):
                im1=cv2.imread(sPath);
                im2=cv2.imread(lHeroes[iHero][2]);
                aimg=im1[354:536, 417:603,:];
                bimg=im2[354:536, 417:603,:];   
                print lHeroes[iHero][0] +' suitability: '+ str(fSimilarity(aimg,bimg))
                
                if fSimilarity(aimg,bimg)<dSimilarityLimit :
                    print '-----------------'
                    print lHeroes[iHero][0] + ' opponent'
                    print '-----------------'
                    sCommand="xdotool key 1"
                    os.system(sCommand);
                    time.sleep(1)
                    lPossibilities=lHeroes[iHero][3+int(lScreens[iScreen])];
                    sCommand="xdotool key "+ random.choice(lPossibilities)
                    os.system(sCommand);
                    time.sleep(1)
                    bFoundHero=True
                    break
                
            if bFoundHero==False:
                os.system('cp '+sPath +' ' + sUnknownHero)

            sCommand="xdotool mousemove "+str(505+numpy.random.randint(-2,2))+" "+str(682+numpy.random.randint(-2,2))
            os.system(sCommand)
            time.sleep(1);
            os.system("xdotool click 1")        
            time.sleep(1);

        elif fSimilarity(im1[655:729, 231:1047,:],im5[655:729, 231:1047,:])<dArenaSimilarityLimit :
            print "Coli screen"

            sCommand="xdotool mousemove "+str(348+numpy.random.randint(-2,2))+" "+str(475+numpy.random.randint(-2,2))
            os.system(sCommand)
            time.sleep(1);
            os.system("xdotool click 1")        
            time.sleep(1);
            sCommand="xdotool key 1"
            os.system(sCommand);
            time.sleep(1.7)
            
            bFoundHero=False;
            for iHero in range(len(lHeroes)):
                im1=cv2.imread(sPath);
                im2=cv2.imread(lHeroes[iHero][3]);
                aimg=im1[372:551, 248:434,:];
                bimg=im2[372:551, 248:434,:];   
                print lHeroes[iHero][0] +' suitability: '+ str(fSimilarity(aimg,bimg))
                                
                if fSimilarity(aimg,bimg)<dSimilarityLimit :
                    print '-----------------'
                    print lHeroes[iHero][0] + ' opponent'
                    print '-----------------'
                    
                    lPossibilities=lHeroes[iHero][3+int(lScreens[iScreen])];
                    sCommand="xdotool key "+ random.choice(lPossibilities)
                    os.system(sCommand);
                    time.sleep(1.7)
                    bFoundHero=True
                    break
                
            if bFoundHero==False:
                os.system('cp '+sPath +' ' + sUnknownHero)

            sCommand="xdotool mousemove "+str(644+numpy.random.randint(-2,2))+" "+str(688+numpy.random.randint(-2,2))
            os.system(sCommand)
            time.sleep(1);
            os.system("xdotool click 1")        
            time.sleep(1);

        
        else:
         
            #if win screen
            #print "Checking if win"
            im2=cv2.imread(sArenaVictory);
            aimg=im1[279:343, 542:750,:];
            bimg=im2[279:343, 542:750,:];   
                
            if fSimilarity(aimg,bimg)<dSimilarityLimit :
                print "Victory screen"
                aResults[iScreen,int(aScreenSelections[iScreen,0]),int(aScreenSelections[iScreen,1]),0]+=1;
                


            #if loss screen
            #print "Checking if loss"
            im2=cv2.imread(sArenaLost);
            aimg=im1[163:228, 404:785,:];
            bimg=im2[163:228, 404:785,:];   
                
            if fSimilarity(aimg,bimg)<dSimilarityLimit :
                print "Loss screen"
                aResults[iScreen,int(aScreenSelections[iScreen,0]),int(aScreenSelections[iScreen,1]),1]+=1;

            #Unoptimized ok pressing
            
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

