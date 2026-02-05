import cv2

img = cv2.imread("./src/images/image.jpeg")
img = cv2.resize(img, (750, 500))


img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

# переход из БГР в РГБ
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# разбиваем все цвета по группам, которые можем потом вывести отдельно
# яем ближе к цвету - тем светлее
r, g, b = cv2.split(img)


# можем вернуть обратно , влияет порядок сборки
img = cv2.merge([r, g, b])
img = cv2.merge([b, g, r])


cv2.imshow("Result", img)
cv2.waitKey(0)
