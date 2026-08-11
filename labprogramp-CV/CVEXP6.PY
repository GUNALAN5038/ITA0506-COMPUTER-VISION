import cv2

# Open video file (replace with 0 for webcam)
cap = cv2.VideoCapture(r"C:\Users\gunal\Downloads\CVEXP6EXAMPLE.mp4")
# cap = cv2.VideoCapture(0)   # Uncomment to use webcam

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 1. Resize the frame
    frame = cv2.resize(frame, (640, 480))

    # 2. Convert to Graykscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 3. Remove Noise using Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 4. Edge Detection
    edges = cv2.Canny(blur, 100, 200)

    # 5. Display Results
    cv2.imshow("Original Video", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Blur", blur)
    cv2.imshow("Edges", edges)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()