from PIL import Image
import os

# Function to divide an image into four separate images
def divide_image(image_file):
    # Open the image file
    image = Image.open(image_file)

    # Get the dimensions of the image
    width, height = image.size

    # Calculate the dimensions of the four separate images
    new_width = width // 2
    new_height = height // 2

    # Crop the four separate images
    top_left = image.crop((0, 0, new_width, new_height))
    top_right = image.crop((new_width, 0, width, new_height))
    bottom_left = image.crop((0, new_height, new_width, height))
    bottom_right = image.crop((new_width, new_height, width, height))

    # Save the four separate images
    base_filename, ext = os.path.splitext(image_file)
    top_left.save(f"{base_filename}_top_left{ext}")
    top_right.save(f"{base_filename}_top_right{ext}")
    bottom_left.save(f"{base_filename}_bottom_left{ext}")
    bottom_right.save(f"{base_filename}_bottom_right{ext}")

# Function to scan a folder for image files and divide each one
def divide_images_in_folder(folder):
    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(folder) if f.endswith((".jpg", ".jpeg", ".png", ".bmp"))]

    print(f"There {len(image_files)} images in the folder.")

    # Divide each image in the folder
    counter = 1
    for image_file in image_files:
        print(f"Processing the image number {counter}.")
        image_path = os.path.join(folder, image_file)
        divide_image(image_path)
        print(f"Image number {counter} has been divided.")
        counter += 1

# Test the function with a sample folder
folder = "/Users/rustamgulov/MyDocs/Code/IMG Divider/images"
divide_images_in_folder(folder)
