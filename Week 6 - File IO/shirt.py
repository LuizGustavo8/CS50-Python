import sys
import os
from PIL import Image, ImageOps

def main():

    # Validate command-line arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Validate file extensions
    valid_extensions = ('.jpg', '.jpeg', '.png')
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Error: Input and output files must have .jpg, .jpeg, or .png extensions")

    if input_ext != output_ext:
        sys.exit("Error: Input and output files must have the same extension")

    # Validate input file existence
    if not os.path.isfile(input_path):
        sys.exit(f"Error: The file '{input_path}' does not exist")

    try:
        # Open the input image
        input_image = Image.open(input_path)

        # Open the shirt image
        shirt = Image.open("shirt.png")

        # Resize and crop the input image to the size of the shirt
        size = shirt.size
        input_image = ImageOps.fit(input_image, size)

        # Overlay the shirt image on the input image
        input_image.paste(shirt, (0, 0), shirt)

        # Save the resulting image to the output path
        input_image.save(output_path)

    except Exception as e:
        sys.exit(f"Error processing images: {e}")

if __name__ == "__main__":
    main()
