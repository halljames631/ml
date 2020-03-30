import cv2
import numpy as np 
import matplotlib.pyplot as plt 

blank_image = np.zeros(shape=(512,512,3), dtype=np.int16)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_image,text="shoot here",org=(170,190),fontFace=font,fontScale=1, color=(255,255,0),thickness=3,lineType=cv2.LINE_AA)

cv2.rectangle(blank_image,pt1=(200,200),pt2=(300,300), color=(0,255,0), thickness=10)
#cv2.circle(blank_image,center=(250,250), radius=100, color=(255,0,0), thickness=8)
#cv2.line(blank_image,pt1=(0,510),pt2=(200,0),color=(0,255,0),thickness=4)

plt.imshow(blank_image)

plt.show()