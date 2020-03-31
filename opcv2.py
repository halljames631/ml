import cv2 
import matplotlib.pyplot as plt 

img = cv2.imread('pom.jpg',0)
ret, thresh1 = cv2.threshold(img,127.5,255,cv2.THRESH_BINARY_INV)

plt.imshow(thresh1,cmap='gray')
plt.show()