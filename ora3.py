import cv2
import numpy as np
import random
#Feladat 1 kép konvertálása hsv-be
'''img=cv2.cvtColor(cv2.imread("C:\\Users\\deakd\\OneDrive\\Dokumentumok\\Egyetem\\Felev3\\kepfeldolgozas\\Kepek\\kep1.jpg",cv2.IMREAD_UNCHANGED),cv2.COLOR_BGR2HSV_FULL)
print("Type:",type(img))
print("Shape of Image:", img.shape)
print('Total Number of pixels:', img.size)
print("Image data type:", img.dtype)
cv2.imwrite("C:\\Users\\deakd\\OneDrive\\Dokumentumok\\Egyetem\\Felev3\\kepfeldolgozas\\Kepek\\kimenet2.jpg",img)'''
#Feladat 2 kép világosítása
#img=cv2.convertScaleAbs(cv2.imread(".\\Kepek\\kep1.jpg"), alpha=1, beta=10.5)
#cv2.imwrite(".\\Kepek\\kimenet3.jpg",img)
#Feladat 3 kép színterének átalakítása véletlenszerűen
'''img = cv2.imread(".\\Kepek\\kep1.jpg")
width, height = 640, 480
img = np.round(np.random.rand(height, width, 3) * 255).astype(np.uint8)
cv2.imwrite(".\\Kepek\\kimenet4.jpg",img)'''
#Feladat 4 kép pixeleinek átmásolása 30% aránnyal
img = cv2.imread(".\\Kepek\\kep1.jpg")
width = 1920
height = 1080
resized_image = cv2.resize(img, (width, height))
target_image = cv2.imread(".\\Kepek\\black.jpg")
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        pixel = img[y, x]
        random_number = random.randint(0, 10)
        if(random_number <= 2):
            target_image[y, x] = pixel
cv2.imwrite('.\\Kepek\\kimenet5.jpg', target_image)
cv2.imshow('Original image', img) 
cv2.imshow('30%', target_image)
cv2.waitKey(0)
cv2.destroyAllWindows()