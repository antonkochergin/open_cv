import cv2
import numpy as np

photo = img = cv2.imread("./src/images/image.jpeg")

img = np.zeros(photo.shape[:2], dtype="uint8")

circle = cv2.circle(img.copy(), (700, 700), 300, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)


# Пересечение - объединение
img = cv2.bitwise_and(circle, square)
# Объединение - объединение
img = cv2.bitwise_or(circle, square)
# Исключающее или - объединение
img = cv2.bitwise_xor(circle, square)
# Инверсия
img = cv2.bitwise_not(circle)


img = cv2.bitwise_and(photo, photo, mask=circle)


cv2.imshow("Result", img)
cv2.waitKey(0)
