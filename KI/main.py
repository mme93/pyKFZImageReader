from os import utime
from PIL import Image
import cv2 
import numpy as np
import re
from matplotlib import pyplot as plt
from imgWoker import ImgWoker
from utlis import Utlis

utlis = Utlis()
imageName='scan3'
utlis.calibrateImage(imageName,'startImg/scan3.jpg')
#utlis.testTresh()
utlis.tresholdImg(imageName)
utlis.textDetection(imageName)

















#myImgWorker =ImgWoker('startImg/scan1.jpg','cutImg/croppedGrayTestImg.jpg')
#myImgWorker.cutImg()
#myImgWorker.gammaTresholdImg('startImg/scan1.jpg')
#myImgWorker.tresImg('startImg/whatsapp.jpg')
#myImgWorker.adaptiveTreshold()
#
#text = tess.image_to_string(img)
#print(text)