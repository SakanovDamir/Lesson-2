import cv2 as cv2
from visioncar import Robot

robot = Robot.discover("robot-fab0c0")

robot.open_camera()
robot.open_control()

while True:
    img = robot.capture()
    cv2.imshow('VisionCar', img)

    if cv2.waitKey(1) == 27:
        quit()