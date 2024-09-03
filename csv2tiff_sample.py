# 091803


import numpy as np
from PIL import Image

# Generate a 1024x1024 array with values ranging from 0 to 3 in arithmetic growth
# For simplicity, we'll use a linearly spaced array reshaped into the 1024x1024 format

# Create an array with values ranging from 0 to 3
values = np.linspace(0, 3, 1024 * 1024)

print("Values array:", values)

# Reshape the array into 1024x1024
image_data = values.reshape((1024, 1024))

print("Image data array:", image_data)

# Convert the array to a single-channel float32 image
tiff_image = Image.fromarray(image_data.astype(np.float32))

# Save the image as a TIFF file
tiff_image.save('output_image.tiff', format='TIFF')

print("TIFF image has been successfully saved as 'output_image.tiff'")
