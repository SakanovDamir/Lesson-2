from djitellopy import tello    # подключаем модуль для управления дроном
import cv2 as cv2               # подключаем модуль OpenCV

drone = tello.Tello()              # создаем объект drone
drone.connect()                    # устанавливаем соединение с дроном
print(drone.get_battery())         # выводим в консоль значение заряда батареи

drone.streamon()

while True:
    img = drone.get_frame_read().frame          # читаем кадр с камеры
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # преобразуем цветопередачу из BGR в RGB
    img = cv2.resize(img, (960, 720))           # устанавливаем размер кадра

    # Выводим текст в поверх изображения
    cv2.putText(img, f"Battery: {drone.get_battery()}", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 255, 0), 2)
    cv2.imshow("Image", img)                    # показываем кадры с камеры машинки с наложенным текстом

    cv2.waitKey(1)