# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 12:33:37 2022

@author: dougl
"""
import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
cv2.imwrite("picture1.png", frame_read.frame)

tello.land()