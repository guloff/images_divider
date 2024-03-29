from PIL import Image
import os

class ImageDivider:
    def __init__(self, folder):
        self.folder = os.path.abspath(folder)
        
    def divide_image(self, image_file):
        try:
            image = Image.open(image_file)
            width, height = image.size
            new_width, new_height = width // 2, height // 2
            
            crops = {
                "top_left": (0, 0, new_width, new_height),
                "top_right": (new_width, 0, width, new_height),
                "bottom_left": (0, new_height, new_width, height),
                "bottom_right": (new_width, new_height, width, height)
            }
            
            for name, coords in crops.items():
                cropped_image = image.crop(coords)
                base_filename, ext = os.path.splitext(image_file)
                cropped_image.save(f"{base_filename}_{name}{ext}")
            print(f"Divided {os.path.basename(image_file)} into 4 parts successfully.")
        except Exception as e:
            print(f"Could not process {os.path.basename(image_file)}. Error: {e}")
    
    def divide_images_in_folder(self):
        if not os.path.exists(self.folder):
            print("The folder does not exist.")
            return
        
        image_files = [f for f in os.listdir(self.folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))]
        if not image_files:
            print("No image files found in the folder.")
            return
        
        print(f"Found {len(image_files)} images in the folder.")
        for counter, image_file in enumerate(image_files, start=1):
            print(f"Processing image {counter}/{len(image_files)}.")
            self.divide_image(os.path.join(self.folder, image_file))

# Example usage
folder = "images"  # Adjust the path as necessary
divider = ImageDivider(folder)
divider.divide_images_in_folder()
