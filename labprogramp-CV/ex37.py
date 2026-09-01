import cv2

# Open the video
cap = cv2.VideoCapture(
    r"C:\Users\gunal\Downloads\CVLAB5.jpeg"
)

# Check whether video is opened
if not cap.isOpened():
    print("Error: Video not found!")
else:
    # Get total number of frames
    total_frames = int(
        cap.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    print("Total Frames:", total_frames)

    # Read frames in reverse order
    for frame_number in range(total_frames - 1, -1, -1):

        # Set frame position
        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            frame_number
        )

        ret, frame = cap.read()

        if not ret:
            continue

        # Display reverse video
        cv2.imshow(
            "Reverse Video",
            frame
        )

        # Press q to exit
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()