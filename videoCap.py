# video record through webcam

import cv2
import numpy as np

c = cv2.VideoCapture(0) # 0 for the inbuilt camera i.e webcam
# series of snapshots (for video)
# while True:
#     r, frame = c.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to gray
#     cv2.imshow('frame :',gray)
#     if cv2.waitKey(1) & 0XFF == ord('q'):
#         break             

# single snapshot
_, frame = c.read()
gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # gray image
cv2.imshow('frame :',frame)  # color image


cv2.waitKey()
c.release()
cv2.destroyAllWindows()
