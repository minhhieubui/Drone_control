import cv2 as cv2
import numpy as np
from djitellopy import tello
from time import sleep
import math

me = tello.Tello()
me.connect()
print(me.get_battery())

arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_1000)      # Lấy Data ( từ điển Aruco)
arucoParams = cv2.aruco.DetectorParameters_create()                # lấy parameter
print("Enter the value")
h = int(input())      # giá trị ID của ArUco market muốn Drone tìm kiếm
me.takeoff()
print(me.get_height())
p = me.get_height()
me.streamon()
sleep(2)

if (p > 85):        # độ cao hiện tại > 85
    u = 85 - p      # độ chênh lệch giữa độ cao hiện tại với độ cao mục tiêu (85)
    if (h <= 4):
        u = -u       # đổi dấu để u >0
        me.move_down(u)       # Drone bay xuống

else:
    u = 85 - p
    if (h <= 4):
        me.move_up(u)         # Drone bay lên

if (h > 4 and h <= 8):
    me.move_up(u + 30)

elif (h > 8 and h <= 12):
    me.move_up(u + 60)

elif (h > 12 and h <= 16):
    me.move_up(u + 100)

sleep(1)

print(me.get_height())

while True:
    img = me.get_frame_read().frame
    image: None = cv2.resize(img, (360, 240))

    cv2.imshow("Image", image)

    (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)  # output : góc, IDs, đối tượng bị loại bỏ


    if len(corners) > 0:
        # flatten the ArUco IDs list
        ids = ids.flatten()      # làm phẳng danh sách IDs của các đánh dấu ArUco để dễ dàng duyệt qua
        # loop over the detected ArUCo corners
        for (markerCorner, markerID) in zip(corners, ids):     # duyệt qua từng cặp corners và ids
            i = 0

            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))   # 4 hàng: chứa các điểm góc , 2 cột: chứa tọa độ x, y của điểm góc tương ứng
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            # convert each of the (x, y)-coordinate pairs to integers
            topRight = [int(topRight[0]), int(topRight[1])]
            bottomRight = [int(bottomRight[0]), int(bottomRight[1])]
            bottomLeft = [int(bottomLeft[0]), int(bottomLeft[1])]
            topLeft = [int(topLeft[0]), int(topLeft[1])]
            cor = np.array([topRight, bottomRight, bottomLeft, topLeft])
            area = cv2.contourArea(cor)

            print(area)

            cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
            # compute and draw the center (x, y)-coordinates of the ArUco
            # marker
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)

            # vel_mag = math.sqrt((cX-180)**2+(cY-120)**2)
            # z = (120-cY)
            # x = (cX - 180)
            # if(area < 2300):
            #     y = 30
            # elif(area > 3000):
            #     y = -30

            x = 0
            y = 0
            z = 0

            if (markerID == h):
                me.land()
                print("ITEM DETECTED")

                break
            me.send_rc_control(x, y, z, 0)
            sleep(0.5)
            me.move_right(42 + 10 * i)
            if (i > 0):
                me.move_back(10 * i)

            i = i + 1
            print(x, y, z)

            # if key == ord("q"):
            #     me.land()
            #     break

        # if abs(x) >= 5:
        #     x = int(30 * x/vel_mag)
        #     z = int(30 * z/vel_mag)
        #     me.send_rc_control(x, y, z, 0)
        #     sleep(0.5)
        #     print(x,y,z)

    else:
        me.send_rc_control(0, 0, 0, 0)
        sleep(0.1)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        me.land()
        print(me.get_battery())
        break
me.streamoff()
cv2.destroyAllWindows()

