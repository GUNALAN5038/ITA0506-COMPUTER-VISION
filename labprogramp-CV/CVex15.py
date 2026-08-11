import cv2
import numpy as np

img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    src = np.float32([[50,50],[250,50],[50,250],[250,250]])
    dst = np.float32([[0,0],[300,0],[50,300],[300,300]])

    H, status = cv2.findHomography(src, dst)

    output = cv2.warpPerspective(img, H, (300,300))

    cv2.imshow("Original Image", img)
    cv2.imshow("DLT Transformation", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()