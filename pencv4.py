import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('pom.jpg',1)

while True:

    cv2.imshow("pom puppy",img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
