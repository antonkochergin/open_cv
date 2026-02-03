import cv2


import numpy as np

#              высота  ширина
photo = np.zeros((450, 400, 3), dtype="uint8")  # задается размер через матрицу с нулями


# SHAPE (высота , ширина)
print(photo.shape[0])
print(photo.shape[1])

# при работе с точками/фигурами у нас идет так:
# (отступ по ширине т.е. Х, отступ по высоте тюе У)
# все как в математике почти


# RGB - стандарт
# BGR - OpenCV
# диапозон по высоте, диапозон по ширине
photo[120:160, photo.shape[1] // 5 * 2 : photo.shape[1] // 5 * 2 + 100] = 145, 23, 78
# закрашиваем по высоте и ширине [диапозон по Y, диапозон по X]


# квадрат от точки 0 0 до 100 100с обводкой заданного цвета с толщиной 3 (hickness=cv2.FILLED - заливка)
cv2.rectangle(photo, (0, 0), (100, 100), (145, 23, 78), thickness=3)

# линия от 0 0 до 100 50 с цветом ... толщиной 3
cv2.line(photo, (0, 0), (100, 50), (119, 201, 105), thickness=3)

# круг
cv2.circle(
    photo, (photo.shape[1] // 2, photo.shape[0] // 2), 15, (256, 0, 0), thickness=3
)

# текст
cv2.putText(
    photo,
    "Hello!",
    (photo.shape[1] // 5 * 2, 150),
    cv2.FONT_HERSHEY_TRIPLEX,
    1,
    (255, 0, 0),
    3,
)


# перекрестие

# вертикальная
cv2.line(
    photo,
    # отступ по ширине ровно на центр и по высоте с разницами по 30 от центра
    (photo.shape[1] // 2, photo.shape[0] // 2 - 30),
    (photo.shape[1] // 2, photo.shape[0] // 2 + 30),
    (111, 111, 111),
    thickness=3,
)

# гаризонтальная
cv2.line(
    photo,
    (photo.shape[1] // 2 - 30, photo.shape[0] // 2),
    (photo.shape[1] // 2 + 30, photo.shape[0] // 2),
    (111, 111, 111),
    thickness=3,
)

cv2.imshow("Photo", photo)
cv2.waitKey(0)
