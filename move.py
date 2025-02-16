import os
import shutil

# Source parent directory (change this to the actual path where these folders exist)
source_dir = r"C:\Users\Jam\Documents\GitHub\SignLanguageDetection\dataset"

# Destination folder (where all images will be copied)
destination_dir = os.path.join(source_dir, "merged_images")
os.makedirs(destination_dir, exist_ok=True)  # Create if not exists

# List of folders (modify as needed)
folders = [
    "boy", "come", "drink", "eat", "excuse me", "girl", "go", "goodbye", 
    "happy", "hello", "help", "iloveyou", "love", "no", "Not Understand", 
    "please", "Sleep", "sorry", "stop", "thank_you", "Understand", "yes"
]

# Allowed image formats
image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")

# Copy images
for folder in folders:
    folder_path = os.path.join(source_dir, folder)
    
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.lower().endswith(image_extensions):  # Check if it's an image
                src_file = os.path.join(folder_path, file)
                dest_file = os.path.join(destination_dir, file)

                # Avoid overwriting duplicate names
                counter = 1
                while os.path.exists(dest_file):
                    name, ext = os.path.splitext(file)
                    dest_file = os.path.join(destination_dir, f"{name}_{counter}{ext}")
                    counter += 1

                shutil.copy2(src_file, dest_file)  # Copy file with metadata
                print(f"Copied: {src_file} ➝ {dest_file}")

print("\n✅ All images copied successfully!")
