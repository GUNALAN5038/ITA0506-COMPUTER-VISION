import cv2

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    result = img.copy()

    h, w = result.shape[:2]

    # Make sure the image is large enough
    if h >= 200 and w >= 200:
        
        # Crop a region
        crop = result[50:150, 50:150].copy()

        # Paste the cropped region at another location
        result[100:200, 150:250] = crop

        cv2.imshow("Original Image", img)
        cv2.imshow("Cropped and Pasted Image", result)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image is too small for this operation.")