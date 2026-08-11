import cv2

img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel XY", sobelxy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()