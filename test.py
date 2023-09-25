import cv2
import numpy as np
open_mode = 1
Image = cv2.imread("C:\\Users\\deakd\\OneDrive\\Dokumentumok\\Egyetem\\Felev3\\kepfeldolgozas\\Kepek\\kep1.jpg",cv2.IMREAD_UNCHANGED)
print(Image.shape)
blue_channel = Image[:,:,0]
blue_img = np.zeros(Image.shape)
blue_img[:,:,0] = blue_channel
cv2.imwrite("C:\\Users\\deakd\\OneDrive\\Dokumentumok\\Egyetem\\Felev3\\kepfeldolgozas\\Kepek\\kimenet.jpg",blue_img) 
