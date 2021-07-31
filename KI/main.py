from imageEditing import ImageEditing
from utlis import Utlis
from pathlib import Path
import os

class Main:
    imageEditing = ImageEditing()
    utlis = Utlis()

    #Müssen evtl in anderen Systemen angepasst werden
    startImgDir = Path('KI/startImg')
    endImgDir = Path('KI/endImg')

    if utlis.initProjectStructur(startImgDir,endImgDir):
        for img in os.listdir(startImgDir):
            
            imageNameArray =img.split(".")
            #Name der Datei
            imageName=imageNameArray[0]
            #Pfad der Datei mit Dateityp
            startImgPath=str(startImgDir)+ "/" + img
            #Endpfad mit Dateiname ohne Dateityp am Ende
            endImgPath=str(endImgDir)+ "/" + imageName

            imageEditing.calibrateImage(imageName,startImgPath,str(endImgDir)+'/')
            #Testtresh funktioniert nicht bei allen Bildern
            #imageEditing.testTresh()
            imageEditing.tresholdImg(imageName,str(endImgDir)+'/')
            imageEditing.textDetection(imageName,str(endImgDir)+'/')
    else:
        print('Es sind keine Bilder zum bearbeiten vorhanden.')
    
    