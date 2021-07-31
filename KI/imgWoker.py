import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from pathlib import Path
import statistics
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'D:\Python\Tesseract-OCR\tesseract.exe'

class ImgWoker:

    startPath = ''
    destinationPath = ''

    def __init__(self, startPath, destinationPath) -> None:
        self.destinationPath = destinationPath
        self.startPath = startPath
        pass

    def gamma_trans(self,gamma,img):
        gamma_table=[np.power(x/255.0,gamma)*255.0 for x in range(256)]
        gamma_table=np.round(np.array(gamma_table)).astype(np.uint8)
        return cv2.LUT(img,gamma_table)
        
    def gammaTresholdImg(self,path):
        img = cv2.imread(path)
        image_gamma_correct=self.gamma_trans(1.5,img)
        cv2.imwrite('cutImg/gammaImg.jpg',image_gamma_correct)
        imgGray = cv2.cvtColor(image_gamma_correct, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5,5),1)
        cv2.imwrite('cutImg/bluerImg.jpg',imgBlur)
        ret,thresh = cv2.threshold(imgBlur,127,255,cv2.THRESH_BINARY_INV)
        text = tess.image_to_string(thresh)
        print(text)
        cv2.imwrite('cutImg/tresImg.jpg',thresh)
    def tresImg(self,path):
        img = cv2.imread(path)
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (5,5),1)
        cv2.imwrite('cutImg/bluerImg.jpg',imgBlur)
        ret,thresh = cv2.threshold(imgBlur,127,255,cv2.THRESH_BINARY_INV)
        text = tess.image_to_string(thresh)
        print(text)
        cv2.imwrite('cutImg/tresImg.jpg',thresh)
    def adaptiveTreshold(self):
        img = cv2.imread('startImg/scan1.jpg')
        #img_blur =cv2.imread('startImg/scan1.jpg', cv2.IMREAD_GRAYSCALE)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.medianBlur(img_gray,5)
        adaptiveTresh = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        text = tess.image_to_string(adaptiveTresh)
        #print(text)
        cv2.imwrite('cutImg/adaptiveTreshImg.jpg',adaptiveTresh)   
    def convertToJPG(self,path):
        im1 = Image.open(self.startPath)
        im1.save(path)
    def cutImg(self):
        self.croppedImg(True)
        self.rotetImg(180)
        self.croppedImg(False)
        self.rotetImg(180)
        self.calibrate()
    def calibrate(self):
        image = cv2.imread(self.destinationPath)
        height = np.size(image, 0)
        width = np.size(image, 1)
        if(height>width):
            print('Need to rotatet')
    def rotetImg(self, percent):
        try:
            bild = Image.open(self.destinationPath)
            neuesbild = bild.rotate(percent)
            neuesbild.save(self.destinationPath)
        except IOError:
            print("Fehler: kann %s nicht bearbeiten." % self.destinationPath)

    def croppedImg(self,isFirstCut):
        print('Start to cut Image')
        if isFirstCut:
            image = cv2.imread(self.startPath)
        else:
            image = cv2.imread(self.destinationPath)
            
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
        convertGrayImg = cv2.cvtColor(cropped, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(self.destinationPath,convertGrayImg)