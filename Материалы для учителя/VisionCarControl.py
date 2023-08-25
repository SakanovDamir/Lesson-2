import cv2
import pygame
from threading import Thread
import time
from visioncar import Robot

pygame.init()
pygame.display.set_caption("Streaming from Visioncar")
screen = pygame.display.set_mode([576, 720])

# FPS = 720
# pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

hostname = "robot-fab0c0"
robot = Robot.discover(hostname)

robot.colorspace = "RGB"
robot.open_control()
robot.open_camera()

driving = False
steering = 0

robot.submit("stpwm;255") # ШИМ для поворота
robot.submit("tm;0") # сначала поворот, потом ехать
robot.submit("td;50") # задержка между поворотом и движением
robot.submit("br;1") # торможение драйвером

def steer(v):
    global steering
    if v != steering:
        steering = v
        robot.steer(v)
def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def video_cap():
    while True:
        frame = robot.capture()
        frame = cv2.flip(frame, 0)  # отзеркаливаем изображение, чтобы не было как через фронтальную камеру
        screen.fill([0, 0, 0])
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))
        pygame.display.update()

        if cv2.waitKey(1) == 27:
            quit()

video = Thread(target=video_cap, daemon=True)
video.start()

while True:
    speed = 75

    if driving and not (getKey("UP") or getKey("DOWN")):
        robot.stop()
        driving = False

    if getKey("UP"):
        if getKey("LEFT"):
            steer(-1)
        elif getKey("RIGHT"):
            steer(1)
        else:
            steer(0)

        if not driving:
            robot.set_speed(speed)
            robot.drive_continuously()
            driving = True
    elif getKey("DOWN"):
        if getKey("LEFT"):
            steer(-1)
        elif getKey("RIGHT"):
            steer(1)
        else:
            steer(0)

        if not driving:
            robot.set_speed(-speed)
            robot.drive_continuously()
            driving = True
    elif getKey("q"):
        robot.set_speed(speed)
        robot.turn(-180)
        while getKey("q"):
            time.sleep(0.05)
    elif getKey("a"):
        robot.set_speed(-60)
        robot.turn(-180)
        while getKey("a"):
            time.sleep(0.05)
    elif getKey("e"):
        robot.set_speed(speed)
        robot.turn(180)
        while getKey("e"):
            time.sleep(0.05)
    elif getKey("d"):
        robot.set_speed(-60)
        robot.turn(180)
        while getKey("d"):
            time.sleep(0.05)