import cv2
import numpy as np

img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    src = np.float32([[50,50],[250,50],[50,250],[250,250]])
    dst = np.float32([[20,80],[260,40],[80,260],[280,280]])

    H, status = cv2.findHomography(src, dst)

    result = cv2.warpPerspective(img, H, (300,300))

    cv2.imshow("Original Image", img)
    cv2.imshow("Homography Transformation", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()