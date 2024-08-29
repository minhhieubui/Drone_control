import KeyPressModule as kp
from djitellopy import tello
import time
import cv2

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img

me.streamon()
start = 0


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getkey("LEFT"):
        lr = -speed
    elif kp.getkey("RIGHT"):
        lr = speed

    if kp.getkey("UP"):
        fb = speed
    elif kp.getkey("DOWN"):
        fb = -speed

    if kp.getkey("w"):
        ud = speed
    elif kp.getkey("s"):
        ud = -speed

    if kp.getkey("a"):
        yv = speed
    elif kp.getkey("d"):
        yv = -speed

    if kp.getkey("f"):
        if kp.getkey("LEFT"):
            me.flip_left()
        elif kp.getkey("RIGHT"):
            me.flip_right()
        elif kp.getkey("UP"):
            me.flip_forward()
        elif kp.getkey("DOWN"):
            me.flip_back()

    if kp.getkey("z"):
        out.write(img)
    if kp.getkey("q"):
        me.land()
    if kp.getkey("e"):
        me.takeoff()

    return [lr, fb, ud, yv]


fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (360, 240))

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    time.sleep(0.5)
