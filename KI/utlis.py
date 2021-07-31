from pathlib import Path
import os

class Utlis:

    def initProjectStructur(self,startImgDirPath,endImgDirPath):
      
        if not startImgDirPath.is_dir():
            os.mkdir(startImgDirPath)
        if not endImgDirPath.is_dir():
            print('Exist')
            os.mkdir(endImgDirPath)
        if len(os.listdir(startImgDirPath))>0:
            return True
        else:
            return False
      