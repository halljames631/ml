import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

pic = Image.open('pom.jpg')
pic_arr = np.asarray(pic)

print(type(pic_arr))

print(pic_arr.shape)
pic_red = pic_arr.copy()



plt.imshow(pic_red[:,:,2],cmap='gray')
plt.show()