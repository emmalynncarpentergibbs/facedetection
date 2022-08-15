# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.streamon()
frame_read = tello.get_frame_read()
cv2.imwrite("picture.png", frame_read.frame)

tello.move_right(50)
tello.rotate_counter_clockwise(90)
tello.move_right(50)
tello.rotate_counter_clockwise(90)
tello.move_right(50)
tello.rotate_counter_clockwise(90)
tello.move_right(50)
tello.rotate_counter_clockwise(90)
tello.move_right(50)
tello.rotate_counter_clockwise(90)


tello.land()
