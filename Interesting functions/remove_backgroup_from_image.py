# Import the 'remove' function from the rembg module, which is used to remove backgrounds from images.
from rembg import remove

# Import the Image class from the PIL (Python Imaging Library) module, which is used to work with images in Python.
from PIL import Image

# Specify the path to the input image, which is the image from which we want to remove the background.
input_path = 'p22.jpg'

# Specify the path for the output image, which will be the result after the background is removed.
output_path = 'p22.png'

# Open the input image using the Image class we imported from PIL.
inp = Image.open(input_path)

# Call the 'remove' function from the rembg module on the input image to remove its background.
output = remove(inp)

# Save the output image with the background removed to the path we specified earlier.
output.save(output_path)

# Use case: This script can be used to automatically remove the background from images, which can be useful for creating product photos for e-commerce, profile pictures without distractions, or any situation where a clean image is required.
