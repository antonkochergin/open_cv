import cv2
import numpy as np

# Видео
# ------------------------------------------------
# cap = cv2.VideoCapture("./src/videos/video.mp4")

# Обработка видео как массив изображений
""" while True:


    success, img = cap.read()

    # img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))  # ширина высота
    # img = cv2.GaussianBlur(img, (9, 9), 0)  # размытие
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert color
    img = cv2.Canny(img, 30, 30)  # бинарная картинка, всего 2 цвета ч/б
    # чем меньше значение, тем больше точность, ищет углы объектов

    # увеличиваем обводку (жирность)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    # при помощи dilate и Canny можно играть с контуром и подгонять его под требования (делать более целостным)

    cv2.imshow("Result", img)
    cv2.waitKey(5)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
 """

# ------------------------------------------------

# Отзеркаливание
# img = cv2.flip(img, -1)  # 0 - вертикаль, 1 - горизонталь, -1 - верт и гор


img = cv2.imread("./src/images/image.jpeg")
img = cv2.resize(img, (750, 500))

new_img = np.zeros(img.shape, dtype="uint8")


# Отступ внутрь окна
def transform(img_param, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))


# img = transform(img, 30, 30)


# Ратация
def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width // 2, height // 2)
    # матрица
    mat = cv2.getRotationMatrix2D(point, angle, 1)  # точка , угол, увеличение
    return cv2.warpAffine(img_param, mat, (width, height))


# img = rotate(img, 45)


# Контуры
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img - cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 100, 140)
# первый порог (100) - цвета ниже него будут проигнорированы (будут черными)
# второй порог (140) - цвета выше него будут проигнорированы (будут белыми)
# цвет точки из диапозона определяется тем, к какому порогу ближе значание

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 1 - позиции контуров
# 2 - иерархия объектов

cv2.drawContours(new_img, con, -1, (61, 111, 11), 1)

cv2.imshow("Result", new_img)
cv2.waitKey(0)
