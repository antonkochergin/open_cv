import cv2

# import numpy as np
img = cv2.imread("/home/anton-kochergin/Work/open_cv/src/images/faces_4.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# вытягиваем модель, данная команда вытягивает файл как натренированную модель
faces = cv2.CascadeClassifier("/home/anton-kochergin/Work/open_cv/src/faces.xml")

# координаты найденных лиц
result = faces.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5)

# визуализвация
for x, y, w, h in result:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
cv2.imshow("Result", img)
cv2.waitKey(0)

# P.S.: Используется натренерованная нейронка
