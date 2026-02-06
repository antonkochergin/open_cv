import cv2

# import numpy as np
img = cv2.imread("./src/images/face.jpeg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# вытягиваем модель, данная команда вытягивает файл как натренированную модель
faces = cv2.CascadeClassifier("faces.xml")

# координаты найденных лиц
result = faces.detectMultiScale(img, scaleFactor=1, minNeighbors=3)


cv2.imshow("Result", img)
cv2.waitKey(0)


# P.S.: Используется натренерованная нейронка
