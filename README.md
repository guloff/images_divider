# Image Divider Script

## Description

This Python script processes all images in a given folder and divides each image into four equal parts: top-left, top-right, bottom-left, and bottom-right. The resulting image parts are saved with descriptive names indicating their position in the original image. The script supports image formats such as `.jpg`, `.jpeg`, `.png`, and `.bmp`.

## Features

- **Divide Images**: Splits each image into four equal sections based on width and height.
- **Batch Processing**: Automatically processes all compatible images in a specified folder.
- **Multiple Formats**: Supports image formats including `.jpg`, `.jpeg`, `.png`, and `.bmp`.

## Requirements

- **Python 3.x**
- **Pillow**: The `PIL` library is part of the `Pillow` package, which you need to install to run this script.

### Install Pillow

You can install Pillow via pip:

```bash
pip install pillow
```

## Usage

1. **Clone the repository** or download the script file to your local machine.

2. **Specify the folder containing the images**: Adjust the `folder` variable in the script to point to the folder with the images you want to process.

3. **Run the script**:

   ```bash
   python image_divider.py
   ```

   The script will find all compatible images in the specified folder, divide each image into four parts, and save the new images in the same folder with descriptive filenames.

### Example

Given an image named `example.jpg`, the script will output:

- `example_top_left.jpg`
- `example_top_right.jpg`
- `example_bottom_left.jpg`
- `example_bottom_right.jpg`

## Notes

- Ensure the folder contains image files in supported formats (`.jpg`, `.jpeg`, `.png`, `.bmp`).
- The original image files will not be modified. New images will be saved alongside the originals with modified filenames.
- If the script encounters an issue (e.g., unsupported file or corrupted image), an error message will be displayed.

## License

This project is licensed under the MIT License.

## Acknowledgements

This script utilizes the `Pillow` library for image processing. More information about `Pillow` can be found in its official documentation: https://pillow.readthedocs.io/en/stable/.
