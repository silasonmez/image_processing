import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\silas\\Downloads\\Iplik.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
blurred_image = cv2.GaussianBlur(image_rgb, (15, 15 ),0)

median_blurred_image = cv2.medianBlur(image_rgb, 15)
plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title('orijinal görsel')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(blurred_image)
plt.title('Gaussian Blur Uygulanmış Görsel')
plt.axis('off')

plt.show()
