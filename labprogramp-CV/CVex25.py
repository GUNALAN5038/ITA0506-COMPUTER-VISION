import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gradient using Sobel operators
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Combine gradients
    gradient = cv2.magnitude(grad_x, grad_y)

    # Convert to displayable format
    gradient = cv2.convertScaleAbs(gradient)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gradient Mask Image", gradient)

    cv2.waitKey(0)
    cv2.destroyAllWindows()