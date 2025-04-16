import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\silas\\Downloads\\Iplik.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blurred_image = cv2.GaussianBlur(image_rgb, (15, 15 ),0)

median_blurred_image = cv2.medianBlur(image_rgb,15)
                  


# ================= K-MEANS SEGMENTASYON =================
# Görseli gri yap
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


pixel_values = gray.reshape((-1, 1))
pixel_values = np.float32(pixel_values)

# K-Means parametreleri
k = 6
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Renkleri merkeze göre ayarla
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(gray.shape)




print("Cluster renkleri (RGB):")
for i, center in enumerate(centers):
    print(f"Cluster {i}: {center}")

brightness = np.sum(centers, axis=1) 
brightest_cluster_index = np.argmax(brightness)  
print(f"En parlak cluster: {brightest_cluster_index} - Renk: {centers[brightest_cluster_index]}")


masked_image = np.zeros_like(segmented_image)  
labels_reshaped = labels.reshape((gray.shape[0], image_rgb.shape[1]))  


masked_image[labels_reshaped == brightest_cluster_index] = centers[brightest_cluster_index]


plt.figure(figsize=(10, 8))

plt.subplot(3, 3, 1)
plt.imshow(image_rgb)
plt.title('orijinal görsel')
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(blurred_image)
plt.title('Gaussian Blur Uygulanmış Görsel')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.imshow(median_blurred_image)
plt.title('Median Blur Uygulanmış Görsel')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.imshow(segmented_image, cmap='gray')
plt.title('K-Means Segmentasyon (k=6)')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.imshow(masked_image, cmap='gray')
plt.title('Maskeleme(En Parlak Küme)')
plt.axis('off')


plt.tight_layout()
plt.show()
