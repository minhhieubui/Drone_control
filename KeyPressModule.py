import pygame
import cv2
from djitellopy import tello
from time import sleep


def init ():
    pygame.init()     # Khởi tạo tất cả các module của thư viện Pygame
    win = pygame.display.set_mode((400,400))   # Đặt kích thước cửa sổ trò chơi

def getkey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main ():
    if getkey("LEFT"):
        print("Left key pressed")
    if getkey("RIGHT"):
        print("Right key pressed")




if __name__ == '__main__':
    init()
    while True:
        main()
