import cv2 as cv2
from visioncar import Robot
from threading import Thread

robot = Robot.discover("robot-fab0c0")
def video():
    while True:
        img = robot.capture()
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Car_Camera', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow()
robot.open_camera()
robot.open_control()

t1 = Thread(target=video, daemon=True)
t1.start()

while True:
    robot.set_speed(70)
    robot.drive(90)
    robot.set_speed(-70)
    robot.drive(90)