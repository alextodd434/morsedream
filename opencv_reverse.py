import cv2
import numpy as np
from morse import *
import time

from opencv_functions import *

# Camera location
cameraID = 0

# Click flag
ledClicked = False

# Rectangle size
r_size = 50
r_colour = (0, 128, 0)
r_thickness = 2

# LED Location
LED_x, LED_y = 0, 0

# Set up capture
cap = cv2.VideoCapture(cameraID)

# Check camera is plugged in
cameracheck(cameraID)

# LED status
previousStatus = False

# Start time
start_time = previousTime = currentTime = 0

# Set a dot time
dot = float(input("How long for a dot? (seconds)\n"))
symbol = dot
dash = 3 * dot
word = 7 * dot
letter = 3 * dot

# Number of truths (to help with start_time)
numTrue = 0
numCompleted = 0

# Reminds user to set box
print("Please select box around light")

# Generate symbol list
symbolList = []
stringWord = ''

# Mouse clicking
def mousepoints(event, x, y, flags, params):
    global LED_x, LED_y, ledClicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        ledClicked = True
        LED_x = x
        LED_y = y
        print("Button clicked")


# Window with live camera feed
while True:
    ret, frame = cap.read()
    cv2.imshow("Camera Feed", frame)
    cv2.setMouseCallback("Camera Feed", mousepoints)
    if ledClicked:
        break

    k = cv2.waitKey(1)
    if k == 27:  # Escape key
        break
    else:
        pass


while True:
    # Read camera
    ret, frame = cap.read()

    # Get cropping coordinates and crop
    sqc = coordinatefunction(LED_x, LED_y, r_size)  # Generates coordinates for square
    cv2.rectangle(frame, (sqc[0], sqc[2]), (sqc[1], sqc[3]), r_colour, r_thickness)  # Creates square
    crop = frame[sqc[2]:sqc[3], sqc[0]:sqc[1]]  # Crops to square

    # Threshold
    grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grey, 220, 255, cv2.THRESH_BINARY)

    # Show live camera feed and new cropped video
    cv2.imshow("Camera Feed", frame)
    cv2.imshow("LED Area", crop)
    cv2.imshow("grey", grey)
    cv2.imshow("thresh", thresh)

    # Counting pixels
    # Check current LED
    currentStatus = LEDstatus(thresh)

    # If same as last cycle, pass
    if currentStatus == previousStatus:
        pass

    # If state changed, print current state
    else:
        currentTime = round(time.time() - start_time, 2)
        diffTime = round(currentTime - previousTime, 2)
        numTrue = 1
        print(currentStatus, currentTime, diffTime)

        # Determines ends of letters '|' or words '\' when False
        if currentStatus == True:
            if 0.7 * word < diffTime:
                symbolList.append(stringWord)
                symbolList.append('/')  # Appending / for end of Word
                stringWord = ''
            elif 0.7 * letter < diffTime < 1.3 * letter:
                symbolList.append(stringWord)
                symbolList.append(' ')
                stringWord = ''
        # Adds . or - symbol when True
        else:
            if 2 * dot < diffTime:
                stringWord += '-'
            else:
                stringWord += '.'


    previousStatus = currentStatus
    previousTime = currentTime

    # Sets start_time until numTrue > 0
    # numCompleted needs to be set after completed phrase
    if numTrue == numCompleted:
        start_time = time.time()

    # Wait for escape key
    k = cv2.waitKey(1)
    if k == 27:  # Escape key
        print(symbolList)
        break
    else:
        pass

