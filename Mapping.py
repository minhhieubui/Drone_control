import KeyPressModule as kp
from djitellopy import tello
import time
import cv2
import numpy as np
import math
from time import sleep

######## PARAMETERS ##########
fSpeed = 117/10  # Forward Speed in cm/s (tốc độ mỗi giây đi được trên lý thuyết)     (15cm/s) : actual speed
aSpeed = 360/10  # Angular Speed Degree/s    (50d/s)
interval = 0.25   # thời gian thực 0.25s

dInterval = fSpeed * interval        # Khoảng cách sau mỗi lần di chuyển
aInterval = aSpeed * interval        # Góc di chuyển sau mỗi dây
##############################

x,y = 500,500
a = 0
yaw = 0

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
points =[(0,0),(0,0)]    # Khởi tạo giá trị điểm đầu, điểm cuối


me.streamon()
start = 0


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    global x,y,yaw,a
    d = 0

    if kp.getkey("LEFT"):
        lr = -speed
        d = dInterval         # update d và a
        a = -180

    elif kp.getkey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getkey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getkey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getkey("w"):
        ud = speed
    elif kp.getkey("s"):
        ud = -speed

    if kp.getkey("a"):
        yv = -aspeed
        yaw -= aInterval

    elif kp.getkey("d"):
        yv = aspeed
        yaw += aInterval

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

    sleep(interval)
    a += yaw
    x += int(d*math.cos(math.radians(a)))       # x = d*cos(a)
    y += int(d * math.sin(math.radians(a)))     # y = d*sin(a)

    return [lr, fb, ud, yv, x, y]


fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))



def drawPoint(img, points):
    for point in points:     # chia nhỏ từng điểm nhỏ ( lặp qua từng điểm point trong points
        cv2.circle(img,point,5,(0,0,255),cv2.FILLED)     # màu đỏ ( theo BGR)
    cv2.circle(img, points[-1], 8, (0, 255, 0), cv2.FILLED)     # [-1] : vẽ điểm cuối cùng
    cv2.putText(img,f'({(points[-1][0] - 500)/100},{(points[-1][1] - 500)/100})m', # Hiển thị thông tin tọa độ điểm cuối cùng được tính bằng mét ( dịch chuyển 500
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN,1,
                (255,0,0),1)

       #f'({(points[-1][0] - 500) / 100},{(points[-1][1] - 500) / 100})m': Văn bản để hiển thị, được định dạng dưới dạng tọa độ của điểm cuối cùng ( gồm x và y) tính bằng mét.
while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    # img = me.get_frame_read().frame
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img = cv2.resize(img, (360, 240))
    # time.sleep(0.5)
    img = np.zeros((1000,1000,3), np.uint8)      # Một mảng màu đen 1000x1000x3 lưu các giá trị số nguyn 8 bit
    if (points[-1][0] !=vals[4] or points[-1][1] !=vals[5]):
        points.append((vals[4],vals[5]))
    drawPoint(img, points)
    cv2.imshow("Output",img)
    cv2.waitKey(1)
