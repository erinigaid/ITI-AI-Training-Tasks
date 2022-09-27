# Edge Features
import numpy as np
from skimage.io import imread,imshow
from skimage.filters import prewitt_h,prewitt_v
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image=imread('coin.jpeg',as_gray=True)

edges_prewitt_horizontal=prewitt_h(image)
edges_prewitt_vertical=prewitt_v(image)

plt.imshow(edges_prewitt_horizontal,cmap='gray')
plt.show()

img=mpimg.imread('coin.jpeg')

x=img[:,:,0]

plt.xlabel("value")
plt.ylabel("pixels Frequency")

plt.title("Original Image")

plt.imshow(x,cmap='gray')
plt.show()

plt.title("Histogram for given Image ")

plt.xlabel("Value")
plt.ylabel("pixels Frequency")

plt.hist(x)
plt.show()
