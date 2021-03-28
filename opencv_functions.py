# Module for OpenCV functions within Morse Project

import cv2
from numpy import sum


def camera_check(camera):
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
def coordinate_function(LED_x, LED_y, r_size):
    x1 = int(LED_x - r_size / 2)
    x2 = int(LED_x + r_size / 2)
    y1 = int(LED_y - r_size / 2)
    y2 = int(LED_y + r_size / 2)
    return [x1, x2, y1, y2]


# Checks if LED is on again value 1000
def LED_status(threshold):
    num_white = sum(threshold == 255)
    if num_white > 50:
        return True
    else:
        return False


# Warning to confirm if functions file was run independently
def main():
    print("Have you run the correct file?")


if __name__ == "__main__":
    main()
