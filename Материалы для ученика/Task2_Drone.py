from djitellopy import tello    # подключаем модуль для управления дроном

drone = tello.Tello()              # создаем объект drone
drone.connect()                    # устанавливаем соединение с дроном
print(drone.get_battery())         # выводим в консоль значение заряда батареи

# Дополните код для выполнения задания 2
