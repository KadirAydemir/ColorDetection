# Python program for Detection of a
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np
import CalculateRealHSV
mouseX=0
mouseY=0
hsvcam = [0, 0, 0]
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0)
def mouseposition(event,x,y,flags,param):

    if event == cv2.EVENT_LBUTTONDOWN:
        global mouseX, mouseY

        mouseY,mouseX = x,y
        global hsvcam
        print(ima1[mouseX][mouseY][0], ima1[mouseX][mouseY][1], ima1[mouseX][mouseY][2])
        hsvcam = CalculateRealHSV.rgb_to_hsv(ima1[mouseX][mouseY][0], ima1[mouseX][mouseY][1], ima1[mouseX][mouseY][2])
        hsvcam = list(hsvcam)
        hsvcam[0] = hsvcam[0] / 2
        hsvcam[1] = hsvcam[1] * 2.55
        hsvcam[2] = hsvcam[2] * 2.55

# This drives the program into an infinite loop.
while (1):
    # Captures the live stream frame-by-frame
    _, frame = cap.read()
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ima1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured
    # objects found in the frame.
    mask = cv2.inRange(hsv, np.float32([hsvcam[0] - 20, hsvcam[1] - 100, hsvcam[2] - 50]), np.float32([hsvcam[0] + 20, hsvcam[1] + 100, hsvcam[2] + 50]))
    # The bitwise and of the frame and mask is done so
    # that only the blue coloured objects are highlighted
    # and stored in res
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.setMouseCallback('frame', mouseposition)

    # This displays the frame, mask
    # and res which we created in 3 separate windows.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    # Destroys all of the HighGUI windows.
cv2.destroyAllWindows()

    # release the captured frame
cap.release()