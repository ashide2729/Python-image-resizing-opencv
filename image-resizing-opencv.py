import numpy as np
import cv2
import matplotlib.pyplot as plt 

image = cv2.imread("shahrukh_smile.jpg", 1)

half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
stretch = cv2.resize(image, (1050, 1610))

interpolated = cv2.resize(image, (780, 540), interpolation = cv2.INTER_NEAREST) 

sizes = ["Original", "Blur", "Long", "Wide"]
images = [image, half, stretch, interpolated]

count = 1

for size, image in zip(sizes, images):
    plt.subplot(2,2,count)
    plt.title(size)
    plt.imshow(image)
    count+=1

plt.show()
