import cv2

img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel Y", sobely)

    cv2.waitKey(0)
    cv2.destroyAllWindows()