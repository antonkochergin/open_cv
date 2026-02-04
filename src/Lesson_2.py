import cv2
import numpy as np


# Изображение
img = cv2.imread("./src/images/image.jpeg")

# print(img.shape)   #высота ширина

img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  # ширина высота
# img = cv2.GaussianBlur(img, (9, 9), 0)  # размытие
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert color
img = cv2.Canny(img, 200, 200)  # бинарная картинка, всего 2 цвета ч/б
# чем меньше значение, тем больше точность, ищет углы объектов

# увеличиваем обводку (жирность)
kernel = np.ones((3, 3), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
# при помощи dilate и Canny можно играть с контуром и подгонять его под требования (делать более целостным)

# обратная команда
img = cv2.erode(img, kernel, iterations=1)


# img[0:100, 0:150])  # выборка части фото ширина:высота
cv2.imshow("Result", img)
cv2.waitKey(0)

# Видео
""" cap = cv2.VideoCapture("./src/videos/video.mp4")

cap = cv2.VideoCapture(0)
cap.set(3, 400)  # ширина
cap.set(4, 300)  # высота

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
 """
