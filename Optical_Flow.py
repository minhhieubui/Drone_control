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

# Cài đặt các thông số cho Optical Flow
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Đọc khung hình đầu tiên
old_frame = frame_read.frame
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7))

# Cất cánh
tello.takeoff()
time.sleep(2)
try:
    while True:
        frame = frame_read.frame
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Tính toán Optical Flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        # Chọn các điểm tốt
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Vẽ các điểm theo dõi
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            frame = cv2.circle(frame, (a, b), 5, (0, 255, 0), -1)
            frame = cv2.line(frame, (a, b), (c, d), (0, 255, 0), 2)

        # Cập nhật các khung hình trước đó và các điểm theo dõi
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

        # Hiển thị khung hình
        cv2.imshow("Tello Camera", frame)

        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    tello.land()
    tello.streamoff()
    cv2.destroyAllWindows()