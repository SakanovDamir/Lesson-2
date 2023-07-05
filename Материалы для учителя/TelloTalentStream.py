from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (960, 720))

    # Выводим текст в поверх изображения
    cv2.putText(img, f"Battery: {me.get_battery()}", (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 255, 0), 2)

    #################################################################################
    '''
    фрагмент для выполнения Задания 1:
    '''
    cv2.putText(img, f"Temperature: {me.get_temperature()}", (20, 90), cv2.FONT_HERSHEY_DUPLEX, 1,
                (0, 255, 0), 1)
    cv2.putText(img, str(me.query_attitude())[1:-1], (20, 130), cv2.FONT_HERSHEY_COMPLEX, 1,
                (0, 255, 0), 1)
    #################################################################################
    cv2.imshow("Image", img)
    cv2.waitKey(1)