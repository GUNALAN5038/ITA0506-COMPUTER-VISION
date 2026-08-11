import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    # Laplacian mask with positive center coefficient
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    # Apply filter
    sharpened = cv2.filter2D(img, -1, kernel)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Sharpened Image", sharpened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()