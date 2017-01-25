import cv2
import numpy as np

# Set up capture device
device = 0
cap = cv2.VideoCapture(device)

# Create windows for images
cv2.namedWindow('image')
cv2.namedWindow('threshold')

# Add sliders for setting color thresholds to image
def dummy_callback(x):
    pass

cv2.createTrackbar('min_hue', 'threshold', 0, 255, dummy_callback)
cv2.createTrackbar('max_hue', 'threshold', 0, 255, dummy_callback)
cv2.createTrackbar('min_saturation', 'threshold', 0, 255, dummy_callback)
cv2.createTrackbar('max_saturation', 'threshold', 0, 255, dummy_callback)
cv2.createTrackbar('min_value', 'threshold', 0, 255, dummy_callback)
cv2.createTrackbar('max_value', 'threshold', 0, 255, dummy_callback)

while True:
    # Grab image from camera
    ret, img = cap.read()

    # Convert image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Threshold HSV by Hue
    is_hue = (hsv[:, :, 0] > cv2.getTrackbarPos('min_hue', 'threshold')) \
         & (hsv[:, :, 0] < cv2.getTrackbarPos('max_hue', 'threshold')) \
         & (hsv[:, :, 1] > cv2.getTrackbarPos('min_saturation', 'threshold')) \
         & (hsv[:, :, 1] < cv2.getTrackbarPos('max_saturation', 'threshold')) \
         & (hsv[:, :, 2] > cv2.getTrackbarPos('min_value', 'threshold')) \
         & (hsv[:, :, 2] < cv2.getTrackbarPos('max_value', 'threshold'))
    is_hue = 255 * is_hue.astype(np.uint8)

    # TODO: detect largest color blob and draw

    # Display images
    cv2.imshow('image', img)
    cv2.imshow('threshold', is_hue)

    # Quit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break