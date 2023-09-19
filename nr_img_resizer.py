import os
from PIL import Image

# Configuration Constants

# Allowed file extensions for image files
ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg']

# Output directory for resized images
OUTPUT_DIR = 'dist'

# Maximum image height
MAX_IMAGE_HEIGHT = 80

# Possible width percentages for resizing
PERCENTAGE_WIDTHS = [33, 50]

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def resize_image(image_path, percentage_width):
    img = Image.open(image_path)
    max_image_width = int((600 * (percentage_width / 100)) - 40)
    original_width, original_height = img.size
    width_ratio = max_image_width / original_width
    new_height = int(original_height * width_ratio)
    
    if new_height > MAX_IMAGE_HEIGHT:
        height_ratio = MAX_IMAGE_HEIGHT / original_height
        new_width = int(original_width * height_ratio)
        new_height = MAX_IMAGE_HEIGHT
    else:
        new_width = max_image_width

    img = img.resize((new_width, new_height))
    
    # Append percentage to the end of the filename
    filename, ext = os.path.splitext(os.path.basename(image_path))
    new_image_path = f"{OUTPUT_DIR}/{filename}_{percentage_width}{ext}"
    img.save(new_image_path)
    print(f"Successfully created {new_image_path}")

# Welcome message
print("==========================================================================================================================")
print("      __                                                _____                                 __           _              ")
print("   /\ \ \_____      _____ _ __ ___   ___  _ __ ___      \_   \_ __ ___   __ _  __ _  ___     /__\ ___  ___(_)_______ _ __ ")
print("  /  \/ / _ \ \ /\ / / __| '__/ _ \ / _ \| '_ ` _ \      / /\/ '_ ` _ \ / _` |/ _` |/ _ \   / \/// _ \/ __| |_  / _ \ '__|")
print(" / /\  /  __/\ V  V /\__ \ | | (_) | (_) | | | | | |  /\/ /_ | | | | | | (_| | (_| |  __/  / _  \  __/\__ \ |/ /  __/ |   ")
print(" \_\ \/ \___| \_/\_/ |___/_|  \___/ \___/|_| |_| |_|  \____/ |_| |_| |_|\__,_|\__, |\___|  \/ \_/\___||___/_/___\___|_|   ")
print("                                                                             |___/                                        ")
print("==========================================================================================================================")

print("Welcome to Newsroom Image Resizer!")

# List all files in OUTPUT_DIR and the current directory
output_files = os.listdir(OUTPUT_DIR)
current_files = os.listdir()

# Identify image files in the current directory
image_files = [f for f in current_files if any(f.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)]

# Identify already resized images in OUTPUT_DIR to exclude their originals
already_resized_bases = set()
for f in output_files:
    for pw in PERCENTAGE_WIDTHS:
        if f"_{pw}" in f:
            base_name, ext = os.path.splitext(f.rsplit('_', 1)[0])
            already_resized_bases.add(f"{base_name}{ext}")

# Filter out already resized images and their originals
image_files_to_process = [f for f in image_files if os.path.splitext(f)[0] not in already_resized_bases]

# Display list of images to be processed
if image_files_to_process:
    print("The following images will be processed:")
    for image in image_files_to_process:
        print(f"  - {image}")
    proceed = input("Would you like to proceed? (y/n): ")
    if proceed.lower() != 'y':
        print("Operation aborted by the user.")
        exit()
else:
    print("No new image files found to process in the current directory.")
    exit()

# Resize images
for image_file in image_files_to_process:
    for percentage_width in PERCENTAGE_WIDTHS:
        resize_image(image_file, percentage_width)

# Final message
print("All images have been resized successfully!")
