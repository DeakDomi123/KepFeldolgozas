import cv2
import numpy as np
#Feladat1 rózsa szegmentálása sima globális küszöléssel
'''input = cv2.imread(".\\Kepek\\rozsa.jpg",0)
scale_percent = 50 # percent of original size
width = int(input.shape[1] * scale_percent / 100)
height = int(input.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(input, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Eredeti', resized)
tresh = cv2.threshold(resized, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Treshold', tresh[1])'''
#Feladat2 rózsa szegmentálésa algoritmusos küszöböléssel
'''input = cv2.imread(".\\Kepek\\rozsa.jpg",0)
scale_percent = 50 # percent of original size
width = int(input.shape[1] * scale_percent / 100)
height = int(input.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(input, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('Eredeti', resized)
tresh = cv2.threshold(resized,100, 400, cv2.THRESH_BINARY)
cv2.imshow('Treshold', tresh[1])'''
#Feladat3 adaptív küszöbölés
'''input = cv2.imread(".\\Kepek\\text.png",0)
scale_percent = 50 # percent of original size
width = int(input.shape[1] * scale_percent / 100)
height = int(input.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(input, dim, interpolation = cv2.INTER_AREA)
blockSize = 5
thresh = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize,2)
tresh2 = cv2.threshold(resized,20, 255, cv2.THRESH_BINARY)
cv2.imshow('Eredeti', resized)
cv2.imshow('Treshold', thresh)
cv2.imshow('Treshold2', tresh2[1])'''
#Feladat4 zajos kép küszöbölése
input = cv2.imread(".\\Kepek\\noisy-image.png",0)
scale_percent = 80 # percent of original size
width = int(input.shape[1] * scale_percent / 100)
height = int(input.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(input, dim, interpolation = cv2.INTER_AREA)
tresh = cv2.threshold(resized, 70, 255, cv2.THRESH_BINARY)
value = 3
sigma_value = 2
output = cv2.boxFilter(resized, -1, (value, value))
tresh2 = cv2.threshold(output, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Eredeti', resized)
cv2.imshow('Threshold', tresh[1])
cv2.imshow('Threshold 2', tresh2[1])
cv2.waitKey(0)
cv2.destroyAllWindows()