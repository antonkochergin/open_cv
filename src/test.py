import cv2
import numpy as np
import os

print("=== ТЕСТ 2: Работа с изображениями ===")

# 1. Создаем тестовое изображение
height, width = 300, 400
image = np.zeros((height, width, 3), dtype=np.uint8)

# 2. Рисуем различные фигуры
# Прямоугольник (зеленый)
cv2.rectangle(image, (50, 50), (150, 150), (0, 255, 0), 2)

# Круг (красный)
cv2.circle(image, (300, 150), 50, (0, 0, 255), -1)  # -1 значит залитый

# Линия (синяя)
cv2.line(image, (50, 200), (350, 200), (255, 0, 0), 3)

# Текст (желтый)
cv2.putText(image, 'OpenCV Test', (100, 250), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

# 3. Сохраняем
cv2.imwrite('test_image.jpg', image)
print(f"✅ Изображение создано и сохранено: test_image.jpg")
print(f"   Размер: {image.shape}")
print(f"   Тип данных: {image.dtype}")

# 4. Загружаем обратно
loaded = cv2.imread('test_image.jpg')
if loaded is not None:
    print(f"✅ Изображение загружено: {loaded.shape}")
else:
    print("❌ Ошибка загрузки")

# 5. Изменяем размер
resized = cv2.resize(image, (200, 150))
cv2.imwrite('test_resized.jpg', resized)
print(f"✅ Изображение изменено: 200x150")

# 6. Конвертируем в grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test_gray.jpg', gray)
print(f"✅ Конвертация в оттенки серого")

# 7. Размытие
blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite('test_blurred.jpg', blurred)
print(f"✅ Применено размытие")

print(f"\n📁 Созданные файлы:")
for f in ['test_image.jpg', 'test_resized.jpg', 'test_gray.jpg', 'test_blurred.jpg']:
    if os.path.exists(f):
        size = os.path.getsize(f) / 1024
        print(f"   - {f} ({size:.1f} KB)")