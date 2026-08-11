import cv2
import numpy as np

img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    rows, cols = img.shape[:2]

    # Translation Matrix (Move Right = 100, Down = 50)
    M = np.float32([[1, 0, 100],
                    [0, 1, 50]])

    translated = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow("Original Image", img)
    cv2.imshow("Translated Image", translated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()