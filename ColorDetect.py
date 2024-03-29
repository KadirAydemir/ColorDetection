import cv2
import numpy as np
import CalculateRealHSV as CRH
from tkinter import *
import os
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
def ColorDetect():
    cap = cv2.VideoCapture(0)
    while(1):
        def show_values():
            cv2.destroyAllWindows()

            x = CRH.rgb_to_hsv(float(spinboxr.get()), float(spinboxg.get()), float(spinboxb.get()))
            x = list(x)
            x[0] = x[0] / 2
            x[1] = x[1] * 2.55
            x[2] = x[2] * 2.55

            frame = cv2.imread('colors.png')
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, np.float32([x[0] - 2, x[1] - 5, x[2] - 5]), np.float32([x[0] + 2, x[1] + 5, x[2] + 5]))
            res = cv2.bitwise_and(frame, frame, mask=mask)
            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            out.write(frame)
            master.destroy()

        master = Tk()
        master.geometry("200x100")
        spinboxr = Spinbox(master,from_=0,to=255,state=NORMAL)
        spinboxr.pack()
        spinboxg = Spinbox(master, from_=0, to=255, state=NORMAL)
        spinboxg.pack()
        spinboxb = Spinbox(master, from_=0, to=255, state=NORMAL)
        spinboxb.pack()

        Button(master, text='Show', command=show_values).pack()
        mainloop()

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


