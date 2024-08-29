from djitellopy import tello
from time import sleep
import cv2
import pygame

me = tello.Tello()
me.connect()
power = me.get_battery()
print("Power level: ",power,"%")


me.streamon()

# me.takeoff()
me.send_rc_control(0,0,0,0)
sleep(2)
me.send_rc_control(0,50,0,0)
sleep(2)

me.send_rc_control(0,0,0,0)
me.land()

while True:
    ret, frame = me.get_frame_read()
    frame = cv2.resize(frame,(360,240))

    cv2.imshow("Frame",frame)
    cv2.waitKey(1)



