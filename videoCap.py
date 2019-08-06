# video record through webcam

import os
import sys
import re
import cv2
import numpy as np
from datetime import datetime


def videoCap():
    video = cv2.VideoCapture(0)

    while 1:
        r, frame = c.read()
        cv2.imshow('video :',frame)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    
    cv2.waitKey(1)
    c.release()
    cv2.destroyAllWindows()


def videoCap():
    c = cv2.VideoCapture(0) # 0 for the inbuilt camera i.e webcam

    # series of snapshots (for video)
    while True:
        r, frame = c.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert to gray
        cv2.imshow('frame :',gray)
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break             

    # single snapshot
    _, frame = c.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # gray image
    cv2.imshow('frame :',frame)  # color image

    cv2.waitKey()
    c.release()
    cv2.destroyAllWindows()

def save_image():
    base_path =  os.getcwd()
    gray_path = base_path + '/images/gray'
    color_path = base_path + '/images/color'
    if os.path.isdir(base_path+'/images'):
        if os.path.isdir(gray_path):
            image_name = re.sub(' ','_',str(datetime.now()).split('.')[0])
            cv2.imwrite(gray_path+'/'+image_name+'.png',frame)
        else:
            os.mkdir('gray')
            image_name = re.sub(' ','_',str(datetime.now()).split('.')[0])
            cv2.imwrite(gray_path+'/'+image_name+'.png',frame)
        if os.path.isdir(color_path):
            image_name = re.sub(' ','_',str(datetime.now()).split('.')[0])
            cv2.imwrite(color_path+'/'+image_name+'.png',frame)            
        else:
            os.mkdir('color')
            image_name = re.sub(' ','_',str(datetime.now()).split('.')[0])
            cv2.imwrite(color_path+'/'+image_name+'.png',frame)


if __name__ == "__main__":
    videoCap()