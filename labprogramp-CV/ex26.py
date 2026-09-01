import cv2

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    # Watermark text
    text = "MOTHI"

    # Position of watermark
    position = (50, 50)

    # Font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Add watermark
    watermarked = img.copy()

    cv2.putText(watermarked, text, position,
                font, 1, (255, 255, 255), 2,
                cv2.LINE_AA)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", watermarked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()