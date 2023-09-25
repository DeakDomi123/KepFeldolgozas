import cv2
import numpy as np
#Feladat1 kép élesítése
'''value = 3
sigma_value = 2
input = cv2.imread(".\\Kepek\\noisy-image.png")
output = cv2.boxFilter(input, -1, (value, value))
cv2.imshow('Kép', output)''' 
#Feladat2 kép élesítése 
'''image = cv2.imread(".\\Kepek\\noisy-image.png")
blurred = cv2.GaussianBlur(image, (image.shape[0], image.shape[1]), 1)
unsharped = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)
cv2.imshow("Original", image)
cv2.imshow("Unsharped", unsharped)
cv2.imshow("Blurred", blurred)'''
#Feladat3 hisztogram kiegyenlítése
value = 3
sigma_value = 2
image = cv2.imread(".\\Kepek\\foggy.jpg",0)
output = cv2.equalizeHist(image)
cv2.imshow('Módosított', output)
cv2.imshow('Eredeti', image)
cv2.waitKey(0)
cv2.destroyAllWindows()