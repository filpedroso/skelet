import rawpy
import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    raw_image, height, width = loader()
   


def loader(): #loads raw file and generates empty numpy arrays
    
    raw = rawpy.imread('IMG_8788.CR2')   
    raw_image = raw.raw_image #get the raw data as a numpy array   
    height, width = raw_image.shape # Get the dimensions of the raw image
    return (raw_image, height, width)

main()

"""
    # Initialize empty image arrays for each color channel
    red_channel = np.zeros((height, width), dtype=np.uint16)
    green_channel = np.zeros((height, width), dtype=np.uint16)
    green_channel2 = np.zeros((height, width), dtype=np.uint16)
    blue_channel = np.zeros((height, width), dtype=np.uint16)

# Assuming the Bayer pattern is RGGB
for y in range(height):
    for x in range(width):
        if (y % 2 == 0) and (x % 2 == 0):
            red_channel[y, x] = raw_image[y, x]  # Red channel
        elif (y % 2 == 0) and (x % 2 == 1):
            green_channel[y, x] = raw_image[y, x] # Green channel (first)
        elif (y % 2 == 1) and (x % 2 == 0):
            green_channel2[y, x] = raw_image[y, x]  # Green channel (second)
        elif (y % 2 == 1) and (x % 2 == 1):
            blue_channel[y, x] = raw_image[y, x] # Blue channel

##luminosity_factor = 4  # Adjust this factor to modulate luminosity
##red_channel = np.clip(red_channel * luminosity_factor, 0, 12688).astype(np.uint16)
##green_channel = np.clip(green_channel * luminosity_factor, 0, 12688).astype(np.uint16)
##blue_channel = np.clip(blue_channel * luminosity_factor, 0, 12688).astype(np.uint16)

# Convert to 8-bit values
#red_channel = (red_channel / 12688) * 255
#green_channel = (green_channel2 / 12688) * 255
#blue_channel = (blue_channel / 12688) * 255

luminosity_factor = 1  # Adjust this factor to modulate luminosity
red_channel = np.clip(red_channel * luminosity_factor, 0, 255).astype(np.uint8)
green_channel = np.clip(green_channel * luminosity_factor, 0, 255).astype(np.uint8)
green_channel2 = np.clip(green_channel2 * luminosity_factor, 0, 255).astype(np.uint8)
blue_channel = np.clip(blue_channel * luminosity_factor, 0, 255).astype(np.uint8)
# Stack the channels to form a color image
color_image = np.stack((red_channel, green_channel, blue_channel), axis=-1).astype(np.uint8)

# Display the raw data with color
plt.imshow(color_image)
plt.title('RAW Image Data with 8-bit Color Values (CR2)')
if plt.show():
    sys.exit('program finished')"""


"""
fonts = [
"nancyj-improved",
"nancyj-fancy",
"stampate",
"thin",
"cybermedium",
"cyberlarge",
#"thorned",
#"electronic",
#"shadow",
"starwars",
"banner",
"Bell"
]
"""

"""
import rawpy
import numpy as np
import matplotlib.pyplot as plt
import sys

raw = rawpy.imread('IMG_8788.CR2')   
raw_image = raw.raw_image #get the raw data as a numpy array   
height, width = raw_image.shape # Get the dimensions of the raw image

import rawpy
import numpy as np
import matplotlib.pyplot as plt

# Load the RAW file
raw = rawpy.imread('your_file.cr2')

# Get the raw image data (unprocessed)
raw_image = raw.raw_image_visible

# Get the maximum value from the raw data to determine the bit depth
max_value = np.max(raw_image)

# Get the dimensions of the raw image
height, width = raw_image.shape
"""