import cv2
import numpy as np
import random
scale_percent = 25
#Ismétlés, sima küszöbölés
'''input = cv2.imread(".\\Kepek\\rozsa.jpg",0)
width = int(input.shape[1] * scale_percent / 100)
height = int(input.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(input, dim, interpolation = cv2.INTER_AREA)
tresh = cv2.threshold(resized, 70, 255, cv2.THRESH_BINARY)
#cv2.imshow('Eredeti', resized)
#cv2.imshow('Treshold', tresh[1])'''
#Dilatáció, erózió
'''input = cv2.imread(".\\Kepek\\circle.jpg",0)
width = int(input.shape[1] * scale_percent / 100)
height = int(input.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(input, dim, interpolation = cv2.INTER_AREA)
kernel = np.ones((100,100), dtype=np.uint8)
eroded = cv2.erode(tresh[1], kernel)
dilated = cv2.dilate(eroded, kernel)
cv2.imshow('Eredeti', tresh[1])
cv2.imshow('Dilated', dilated)'''
#Feladatok
input = cv2.imread(".\\Kepek\\budapest.jpg",0)
input2 = cv2.imread(".\\Kepek\\black.jpg",0)
width = int(input.shape[1] * scale_percent / 100)
height = int(input.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(input, dim, interpolation = cv2.INTER_AREA)
resized2 = cv2.resize(input2, dim, interpolation = cv2.INTER_AREA)
blockSize = 5
thresh = cv2.threshold(resized, 70, 255, cv2.THRESH_BINARY)
kernel = np.ones((10,10), dtype=np.uint8)
eroded = cv2.erode(thresh[1], kernel)
dilated = cv2.dilate(eroded, kernel)
height, width = dilated.shape
for y in range(height):
    for x in range(width):
        random_number = random.randint(1, 3)
        if(random_number == 1 or random_number == 2):
            resized2[y,x] = dilated[y,x]
cv2.imshow('Kép', dilated)
cv2.imshow('Kép2', resized2)
cv2.waitKey(0)
cv2.destroyAllWindows()