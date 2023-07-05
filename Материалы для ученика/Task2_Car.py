from visioncar import Robot     # подключаем модуль для управления машинкой

robot = Robot.discover("robot-fab0c0")  # создаем объект robot  и устанавливаем соединение с ним

robot.open_camera()             # разрешаем доступ к камере
robot.open_control()            # разрешаем управление машинкой
get_battery = 97                # считываем значение батареи

# Дополните код для выполнения задания 2
