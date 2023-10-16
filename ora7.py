import cv2
import numpy as np
import random
##Gyakorlás a ZH-ra, próbaZH megoldása

#Képjavítók, korrekciók: világosság, szűrők pl boxfilter median, életsítés, kontrasztkiegyenlítés (színes képnél a 3d-s tömbből csinálok egy 3db 2d-set)

#1. feladat
def ElsoFeladat():
    #eleresiut = input("Kép elérési útja: ")
    #beolvas = cv2.imread(eleresiut,1)
    beolvas = cv2.imread(".\\Kepek\\rozsa.jpg",1)
    filtered = cv2.GaussianBlur(beolvas,(5,5),1.5)
    filtered = cv2.medianBlur(beolvas,5)
    cv2.imshow('Eredeti', filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def MasodikFeladat():
    beolvas = cv2.imread(".\\Kepek\\kep1.jpg",0)
    kernel = np.ones((5, 5), dtype=np.uint8)
    dilated = cv2.dilate(beolvas, kernel)
    eroded = cv2.erode(beolvas, kernel)
    contures = dilated - eroded
    cv2.imshow("Dilated", dilated)
    cv2.imshow("Eroded", eroded)
    cv2.imshow("Contures", contures)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def HarmadikFeladat():
    beolvas = cv2.imread(".\\Kepek\\rozsa.jpg",0)
    thresh1 = cv2.threshold(beolvas, 50, 255, cv2.THRESH_BINARY)
    thresh = cv2.threshold(beolvas, 0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    blockSize = 5
    thresh2 = cv2.adaptiveThreshold(beolvas, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize,2)
    cv2.imshow('Thresh1', thresh1[1])
    cv2.imshow('Thresh2', thresh[1])
    cv2.imshow('Thresh3', thresh2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def NegyedikFeladat():
    beolvas = cv2.imread(".\\Kepek\\rozsa.jpg",1)
    hsv = cv2.cvtColor(beolvas, cv2.COLOR_RGB2HSV)
    hue = int(input("hue="))
    hsv[:,:,0] += np.uint8((1 + hue / 100))
    cv2.imshow('Eredeti Kép', beolvas)
    cv2.imshow('Módosított Kép', hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ElsoFeladat()
MasodikFeladat()
HarmadikFeladat()
NegyedikFeladat()