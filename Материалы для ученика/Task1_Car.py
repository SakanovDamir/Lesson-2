import cv2 as cv2               # подключаем модуль OpenCV
from visioncar import Robot     # подключаем модуль для управления машинкой

robot = Robot.discover("robot-fab0c0")  # создаем объект robot  и устанавливаем соединение с ним

robot.open_camera()             # разрешаем доступ к камере
robot.open_control()            # разрешаем управление машинкой
get_battery = 97                # считываем значение батареи

while True:
    img = robot.capture()           # читаем кадр с камеры

    # Выводим текст в поверх изображения
    cv2.putText(img, f"Battery: {get_battery}", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 255, 0), 2)

    cv2.imshow('VisionCar', img)     # показываем кадры с камеры машинки с наложенным текстом

    if cv2.waitKey(1) == 27:
        quit()
