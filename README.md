# pyKFZImageReader with Docker

## Installation Docker on Windows

Create Account on https://hub.docker.com/ and install Docker Desktop Application

Need to Activate on Windows the Windows-Features: "Windwos-Subsystem für Linux", "Windows-Hypervisor-Plattform", "Plattform für virtuelle Computer" 

Install WSL on Windows with the following URL https://docs.microsoft.com/de-de/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package

## Use Docker
https://docs.docker.com/language/python/build-images/

Create Dockerfile in your Python Project Folder. There are different Option in Dockerfile, this example show one Example.

---------------------------------------------
FROM python:3

ADD main.py .

CMD ["python","./main.py"]

---------------------------------------------

To Build docker, you need the following Command: "docker build -t dockerImageName ."

To Run the Docker Image: "docker run dockerImageName"

## Installation OpenCV on Raspberry Pi 
Tutorial-Video:
https://www.youtube.com/watch?v=OugQIz_vcFo

In folgendenen Schritten wird erklärt, was alles benötigt wird um OpenCV auf einem Linux System zu installieren.

sudo apt update

sudo apt upgrade

1) Installing Packges for OpenCV

sudo apt install cmak build-essential pkg-config git

sudo apt install libjpeg-dev libtiff-dev libjasper-dev libpng-dev libwebp-dev libopenexr-dev

sudo apt install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libdc1394-22-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev

sudo apt install libgtk-3-dev libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5

sudo apt install libatlas-base-dev liblapacke-dev gfortran

sudo apt install libhdf5-dev libhdf5-103

sudo apt install python3-dev python3-pip python3-numpy

2) Preparing your Raspberry Pi for Compiling OpenCV

sudo nano /etc/dphys-swapfile

change 'CONF_SWAPESIZE=100' to 'CONF_SWAPESIZE=2048'

sudo systemetcl restart dphys-swapfile

sudo git clone https://github.com/opencv/opencv.git

sudo git clone https://github.com/opencv/opencv_contrib.git

3) Compiling OpenCV on Rasperberry Pi

mkdir /home/pi/opencv/build

!Wichtig cmake muss im build verzeichnis geöffnet werden.

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules -D ENABLE_NEON=ON -D ENABLE_VFPV3=ON -D BUILD_TESTS=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D OPENCV_ENABLE_NONREE=ON -D CMAKE_SHARED_LINKER_FLAGS=-latomic -D BUILD_EXAMPLES=OFF ..

sudo ldconfig

sudo nano /etc/dphys-swapfile

change 'CONF_SWAPESIZE=2048' to 'CONF_SWAPESIZE=100

sudo systemetcl restart dphys-swapfile

## Bilderkennung Tool Tesseract-OCR

* sudo apt-get install tesseract-ocr



## Python Projekt Bibliotheken für Linux
* matplotlib
  * sudo apt-get install python3-matplotlib

