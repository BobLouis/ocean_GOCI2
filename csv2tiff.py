from PIL import Image
import numpy as np
import pandas as pd

# Define the resolution and the array dimensions based on the given coordinates and resolution
lat_resolution = 0.0025
lon_resolution = 0.0025

# Define the coordinate boundaries
lat_min = 24.0000
lat_max = 48.4854
lon_min = 123.0000
lon_max = 150.0000

# Calculate the array dimensions
height = int((lat_max - lat_min) / lat_resolution) + 1  # Approx 9794 pixels
width = int((lon_max - lon_min) / lon_resolution) + 1  # Approx 10800 pixels

# Initialize the blank array with -1
array_2d = np.full((height, width), -1.0, dtype=np.float32)

# Read the CSV data
csv_data = pd.read_csv('data_all/091803.csv')

# Function to convert latitude and longitude to array indices


def lat_lon_to_indices(lat, lon, lat_min, lon_min, lat_resolution, lon_resolution):
    row = int((lat - lat_min) / lat_resolution)
    col = int((lon - lon_min) / lon_resolution)
    return row, col


# Populate the array with Chlorophyll values using nearest block insertion
for index, row in csv_data.iterrows():
    lat = row['GOCI2_Latitude']
    lon = row['GOCI2_Longitude']
    chlorophyll = row['Chlorophyll']

    # Get the array indices for the given coordinates
    array_row, array_col = lat_lon_to_indices(
        lat, lon, lat_min, lon_min, lat_resolution, lon_resolution)

    # Check if the indices are within the array bounds
    if 0 <= array_row < height and 0 <= array_col < width:
        array_2d[array_row, array_col] = chlorophyll

# Optionally, save the array as a TIFF image if required

# Convert to a TIFF image, scaling as needed for visualization
tiff_image = Image.fromarray(array_2d)
tiff_image.save('chlorophyll_output_image.tiff', format='TIFF')

print("Chlorophyll values have been inserted into the 2D array and saved as 'chlorophyll_output_image.tiff'")
