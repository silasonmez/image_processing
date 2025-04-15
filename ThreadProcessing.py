import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\silas\\Downloads\\Iplik.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blurred_image = cv2.GaussianBlur(image_rgb, (15, 15 ),0)

median_blurred_image = cv2.medianBlur(image_rgb,15)
                  
median_blurred_image = cv2.medianBlur(image_rgb, 15)


# ================= K-MEANS SEGMENTASYON =================
# Görseli gri yap
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


pixel_values = gray.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# K-Means parametreleri
k = 6
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)


# Renkleri merkeze göre ayarla
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(gray.shape)


plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title('orijinal görsel')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(blurred_image)
plt.title('Gaussian Blur Uygulanmış Görsel')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(median_blurred_image)
plt.title('Median Blur Uygulanmış Görsel')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(segmented_image, cmap='gray')
plt.title('K-Means Segmentasyon (k=6)')
plt.axis('off')

plt.tight_layout()
plt.show()
