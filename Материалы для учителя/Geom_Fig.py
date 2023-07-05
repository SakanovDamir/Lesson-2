import cv2 as cv
from visioncar import Robot

robot = Robot.discover("robot-fab0c0")

robot.open_camera()
robot.open_control()
speed = 60

while True:
    robot.set_speed(speed)
   # ret, img = cap.read()
    frame = robot.capture()
    cv.imshow('Camera', frame)
    img = frame

    gr = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    bl = cv.medianBlur(gr, 5)

    canny = cv.Canny(bl, 10, 250)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    closed = cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel)

    contours = cv.findContours(closed.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    for cont in contours:
        approx = cv.approxPolyDP(cont, 0.01 * cv.arcLength(cont, True), True)
        #сглаживание и определение количества углов
        sm = cv.arcLength(cont, True)
        apd = cv.approxPolyDP(cont, 0.02*sm, True)
        area = cv.contourArea(apd)
        if area > 10000 and area < 13000:
            #выделение контуров
            if len(apd) == 3:
                cv.drawContours(img, [apd], -1, (0,0,0), 4)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
                cv.putText(img, str(area), (x, y + 30), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 11710
                robot.set_speed(-speed)
                robot.drive(50)
            elif len(apd) == 4:
                x1, y1, w, h = cv.boundingRect(approx)
                aspectRatio = float(w) / h
                if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                    cv.drawContours(img, [apd], -1, (0, 255, 0), 4)
                    x = approx.ravel()[0]
                    y = approx.ravel()[1] - 5
                    cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
                    cv.putText(img, str(area), (x, y + 30), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))  # 16435
                    robot.set_speed(75)
                    robot.turn(-180)
                else:
                    cv.drawContours(img, [apd], -1, (0, 255, 0), 4)
                    x = approx.ravel()[0]
                    y = approx.ravel()[1] - 5
                    cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
                    cv.putText(img, str(area), (x, y + 30), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))  #
            elif len(apd) == 5:
                cv.drawContours(img, [apd], -1, (255,0,0), 4)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
                cv.putText(img, str(area), (x, y + 30), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))  #
            elif len(apd) == 6:
                cv.drawContours(img, [apd], -1, (0,255,255), 4)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                cv.putText(img, "Hexagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,255,255))
                cv.putText(img, str(area), (x, y + 30), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255))  #
            elif len(apd) == 10:
                cv.drawContours(img, [apd], -1, (0,0,255), 4)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))
                cv.putText(img, str(area), (x, y+30), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255)) #11870
                robot.drive(50)
            elif len(apd) > 7 and len(apd) < 9:
                cv.drawContours(img, [apd], -1, (255,255,0), 4)
                x = approx.ravel()[0]
                y = approx.ravel()[1] - 5
                cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0))
                cv.putText(img, str(area), (x, y + 30), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 0))  # 11285
                robot.set_speed(75)
                robot.turn(180)
    # Подождите 25 мс
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Отменить выделение любого связанного использования памяти
cv.destroyAllWindows()