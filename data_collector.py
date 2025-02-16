import cv2
import os
import time

# Define the list of signs
signs = [  "boy"]

# Image settings
num_images_per_sign = 50  # Adjust as needed
image_format = ".png"  # Use PNG for lossless quality

# Open webcam and set high resolution
cap = cv2.VideoCapture(0)

# Set the highest possible resolution (adjust if needed)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # Full HD Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Full HD Height
cap.set(cv2.CAP_PROP_FPS, 30)  # Set FPS for smooth capture
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)  # Enable autofocus

for sign_name in signs:
    output_folder = f"dataset/{sign_name}"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print(f"\n📸 Get ready for sign: {sign_name} (Starting in 5 seconds...)")
    time.sleep(5)  # Wait before capturing images

    for i in range(num_images_per_sign):
        ret, frame = cap.read()
        if not ret:
            break

        # Increase brightness & contrast for better visibility
        frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=30)

        # Save image in full resolution
        img_path = os.path.join(output_folder, f"{sign_name}_{i}{image_format}")
        cv2.imwrite(img_path, frame, [cv2.IMWRITE_PNG_COMPRESSION, 3])

        # Show preview
        cv2.imshow("Collecting Images", frame)

        time.sleep(0.1)  # Adjust delay if needed

        # Press 'q' to stop early
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print("\n✅ High-Resolution Dataset Collection Completed!")
cap.release()
cv2.destroyAllWindows()
