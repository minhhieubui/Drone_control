import cv2
import numpy as np
from djitellopy import Tello
import time

# Tạo đối tượng Tello và kết nối
tello = Tello()
tello.connect()

# Khởi động camera
tello.streamon()
frame_read = tello.get_frame_read()

# Cài đặt ArUco dictionary và detector parameters
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

# Tọa độ mục tiêu (trung tâm)
target_position = np.array([320, 240])  # Giả sử trung tâm của khung hình

def detect_marker(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    if ids is not None:
        # Tính tọa độ trung tâm của marker
        marker_center = np.mean(corners[0][0], axis=0)
        return marker_center
    return None

def adjust_position(current_position):
    dx, dy = current_position - target_position
    if abs(dx) > 20:  # Ngưỡng điều chỉnh
        if dx > 0:
            tello.move_left(20)  # Di chuyển sang trái
        else:
            tello.move_right(20)  # Di chuyển sang phải
    if abs(dy) > 20:  # Ngưỡng điều chỉnh
        if dy > 0:
            tello.move_down(20)  # Di chuyển xuống
        else:
            tello.move_up(20)  # Di chuyển lên

# Cất cánh
tello.takeoff()
time.sleep(2)

try:
    while True:
        frame = frame_read.frame
        marker_position = detect_marker(frame)
        if marker_position is not None:
            adjust_position(marker_position)
        cv2.imshow("Tello Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    tello.land()
    tello.streamoff()
    cv2.destroyAllWindows()