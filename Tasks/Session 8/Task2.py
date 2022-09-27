   # Make noisy photo filterd
import matplotlib.pyplot as plt
import cv2
import numpy as np

color_image=cv2.imread('mnion.jpg')
gray_img=cv2.cvtColor(color_image,cv2.COLOR_BGR2RGB)
sliding_window_size_x=3
sliding_window_size_y=3
mean_filter_kernal=np.ones((sliding_window_size_x,sliding_window_size_y),np.float32)/(sliding_window_size_x*sliding_window_size_y)
filtered_image=cv2.filter2D(gray_img,-1,mean_filter_kernal)
plt.subplot(121),plt.imshow(gray_img,cmap=plt.cm.gray),plt.title('original noisy image')
plt.subplot(122),plt.imshow(filtered_image,cmap=plt.cm.gray),plt.title('filtered image')
plt.xticks([]),plt.yticks([])
plt.show()

