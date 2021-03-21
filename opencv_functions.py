import cv2
import numpy as np
import time


def cameracheck(camera):
    # Check if specified camera ID is plugged in
    cap = cv2.VideoCapture(camera)
    if cap is None or not cap.isOpened():
        # No camera found at ID position
        print(f"No camera found at ID: {camera}")
        return False
    else:
        # Camera found
        print(f"Using camera ID {camera}")
        cap.release()
        return True


# Sets coordinates of square based on click
def coordinatefunction(LED_x, LED_y, r_size):
    x1 = int(LED_x - r_size / 2)
    x2 = int(LED_x + r_size / 2)
    y1 = int(LED_y - r_size / 2)
    y2 = int(LED_y + r_size / 2)
    return [x1, x2, y1, y2]


# Checks if LED is on again value 1000
def LEDstatus(threshold):
    numwhite = np.sum(threshold == 255)
    if numwhite > 600:
        return True
    else:
        return False


def main():
    print("Have you run the correct file?")


if __name__ == "__main__":
    main()
