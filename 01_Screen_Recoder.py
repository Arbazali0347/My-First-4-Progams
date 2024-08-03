import cv2
import pyautogui
import numpy as np
import time
from win32api import GetSystemMetrics

waith = GetSystemMetrics(0)
hait = GetSystemMetrics(1)

dim = (waith,hait)

f = cv2.VideoWriter_fourcc(*"XVID")
output  = cv2.VideoWriter("01_My_Video.mp4",f,20,dim)

start = time.time()
dur = 200
end_time = start + dur
while True:
    image = pyautogui.screenshot()
    frame = np.array(image)
    frame_1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame_1)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()
print("thanks bro arbaz")