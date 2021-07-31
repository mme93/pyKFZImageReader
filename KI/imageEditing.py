import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from pathlib import Path
import statistics
from PIL import Image
import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'D:\Python\Tesseract-OCR\tesseract.exe'


class ImageEditing:

    def textDetection(self,imageName,endPath):
        print('Text detection start')
        img = Image.open(endPath+imageName+'_tres.jpg')
        text = tess.image_to_string(img)
        print(text)

    #Bild Bearbeitung
    def testTresh(self):
        print("Test")
        path='KI/endImg/scan1_calibrate.jpg'
        image = cv2.imread(path)            
        height = np.size(image, 0)
        width = np.size(image, 1)
        cropped = image[0:height,int(width/10*3):int(width/10*6)]
        convertGrayImg = cv2.cvtColor(cropped, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(path,convertGrayImg)

    def tresholdImg(self,imageName,endPath):
        print('Treshold Img')
        path=endPath+imageName+'_calibrate.jpg'
        img = cv2.imread(path)
        image_gamma_correct=self.gamma_trans(1.5,img)
        cv2.imwrite(endPath+imageName+'_gamma.jpg',image_gamma_correct)
        imgGray = cv2.cvtColor(image_gamma_correct, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5,5),1)
        cv2.imwrite(endPath+imageName+'_bluer.jpg',imgBlur)
        ret,thresh = cv2.threshold(imgBlur,127,255,cv2.THRESH_BINARY_INV)
        #et,thresh = cv2.threshold(imgBlur,127,255,cv2.THRESH_BINARY)
        text = tess.image_to_string(thresh)
        print(text)
        cv2.imwrite(endPath+imageName+'_tres.jpg',thresh)

    def gamma_trans(self,gamma,img):
        gamma_table=[np.power(x/255.0,gamma)*255.0 for x in range(256)]
        gamma_table=np.round(np.array(gamma_table)).astype(np.uint8)
        return cv2.LUT(img,gamma_table)

    #Hier wird das Bild für Auswertung des Text vorbereitet
    def calibrateImage(self,imageName,path,endPath):
        print('Calibrate Img')
        self.croppedImg(path,imageName,endPath)
        path=endPath+imageName+'_calibrate.jpg'
        self.rotetImg(180,path)   
        self.croppedImg(path,imageName,endPath)
        self.rotetImg(180,path)

    def croppedImg(self,path,imageName,endPath):
        print('Start to cut Image: '+imageName)
        image = cv2.imread(path)            
        height = np.size(image, 0)
        width = np.size(image, 1)
        #Linke Seite wird ermittelt
        maxLeftSizeList=[]
        for i in range(0, height):
            for j in range(0, width):
                imgArray=image[i,j]
                averageRGB=(imgArray.item(0)+imgArray.item(1)+imgArray.item(2))/3
                if averageRGB<241:        
                    maxLeftSizeList.append(j)
                    break
        left=int(statistics.mean(maxLeftSizeList))
        if left<200:
            left=int(left/3);              
        else:
            left=int(left/100*97)

        #Ober Seite wird ermittelt         
        maxTopSizeList=[]
        for i in range(0, width):
            for j in range(0, height):
                imgArray=image[j,i]
                averageRGB=(imgArray.item(0)+imgArray.item(1)+imgArray.item(2))/3
                if averageRGB<241:        
                    maxTopSizeList.append(j)
                    break
        top=int(statistics.mean(maxTopSizeList))
        if top<200:
            top=int(top/3);              
        else:
            top=int(top/100*97)

        cropped = image[top:height,left:width]
        path=endPath+imageName+'_calibrate.jpg'
        cv2.imwrite(path,cropped)

    def rotetImg(self, percent,path):
        try:
            bild = Image.open(path)
            neuesbild = bild.rotate(percent)
            neuesbild.save(path)
        except IOError:
            print("Fehler: kann %s nicht bearbeiten." % path)