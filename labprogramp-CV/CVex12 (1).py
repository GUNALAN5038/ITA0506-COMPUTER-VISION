import cv2
import numpy as np

img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([[50,50],[250,50],[50,250],[250,250]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    perspective = cv2.warpPerspective(img, M, (300,300))

    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformation", perspective)

    cv2.waitKey(0)
    cv2.destroyAllWindows()