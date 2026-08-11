import cv2

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow("Original Image", img)
    cv2.imshow("Canny Edge Detection", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()