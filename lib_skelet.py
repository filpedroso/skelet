import rawpy
import numpy as np
import matplotlib.pyplot as plt
import os


# collects file names in "pictures" folder into a dictionary
def pics_list():
    path_here = os.path.abspath(__file__) # gets current path
    path_here = os.path.dirname(path_here) # update path to not include file name
    pics_list = os.listdir(f"{path_here}/pictures") # passes pictures folder to get list of pictures
    return pics_list


#loads raw file and generates empty numpy arrays
def loader(file):

    raw = rawpy.imread(file) # reads raw file with rawpy
    raw_image = raw.raw_image #get the raw data as a numpy array
    return (raw_image)


# processing function returning 'as it is' raw image
def fullcolor_raw0(raw_image):

    height, width = raw_image.shape # get the dimensions of the raw image
    color_image = np.zeros((height, width, 3), dtype=np.uint16) # initializes empty numpy array, same size of raw image, with 3 (RGB) channels

    # populates each pixel and its 3 channel values from raw image
    color_image[0:height:2, 0:width:2, 0] = raw_image[0:height:2, 0:width:2] # R channel
    color_image[0:height:2, 1:width:2, 1] = raw_image[0:height:2, 1:width:2] # G1 channel
    color_image[1:height:2, 0:width:2, 1] = raw_image[1:height:2, 0:width:2] # G2 channel
    color_image[1:height:2, 1:width:2, 2] = raw_image[1:height:2, 1:width:2] #B channel

    return color_image

# processing function returning raw image with second green as luminance and green as a median between first and second green
def fullcolor_lum1(raw_image):

    height, width = raw_image.shape
    color_image = np.zeros((height, width, 3), dtype=np.uint16)

    color_image[0:height:2, 0:width:2, 0] = raw_image[0:height:2, 0:width:2] #R channel
    color_image[0:height:2, 1:width:2, 1] = (raw_image[0:height:2, 1:width:2] + raw_image[1:height:2, 0:width:2]) / 2 # average from g1 and g2 channels
    green_second_set = raw_image[1:height:2, 0:width:2] # gets G2 values to create a gray luminance channel

    # copies G2 values into its R, G, B indexes, making it a gray pixel
    color_image[1:height:2, 0:width:2, 0] = green_second_set  #R value
    color_image[1:height:2, 0:width:2, 1] = green_second_set  #G value
    color_image[1:height:2, 0:width:2, 2] = green_second_set  #B value

    color_image[1:height:2, 1:width:2, 2] = raw_image[1:height:2, 1:width:2] #B channel
    return color_image


# processing function returning grayscale image using red channel only
# since only red pixel is being used, the image is halved for no rendundant pixels
def grayscale_red2(raw_image):

    height, width = raw_image.shape
    gray_image = np.zeros((round(height/2), round(width/2), 3), dtype=np.uint16) # empty array, half the original size, 3 channels per pixel

    # maps each channel in each pixel to each original R value
    gray_image[0:height, 0:width, 0] = raw_image[0:height:2, 0:width:2]
    gray_image[0:height, 0:width, 1] = raw_image[0:height:2, 0:width:2]
    gray_image[0:height, 0:width, 2] = raw_image[0:height:2, 0:width:2]
    return gray_image


# same as above, but with green (averaging both greens)
def grayscale_green3(raw_image):

    height, width = raw_image.shape 
    gray_image = np.zeros((round(height/2), round(width/2), 3), dtype=np.uint16) 

    green_average = (raw_image[0:height:2, 1:width:2] + raw_image[1:height:2, 0:width:2]) / 2
    gray_image[0:height, 0:width, 0] = green_average
    gray_image[0:height, 0:width, 1] = green_average
    gray_image[0:height, 0:width, 2] = green_average
    return gray_image


# same as above but with blue
def grayscale_blue4(raw_image):

    height, width = raw_image.shape
    gray_image = np.zeros((round(height/2), round(width/2), 3), dtype=np.uint16)

    gray_image[0:height, 0:width, 0] = raw_image[1:height:2, 1:width:2]
    gray_image[0:height, 0:width, 1] = raw_image[1:height:2, 1:width:2]
    gray_image[0:height, 0:width, 2] = raw_image[1:height:2, 1:width:2]
    return gray_image

# displays image and prompts to save
def display_image(image, file):

    image = image / np.max(image) # normalizes the image, for each value in each channel to be a float between 0 and 1

    plt.imshow(image) # expects float values between 0 and 1, and scales it for 8bit displays
    plt.title(file)
    plt.axis('off')
    plt.show()

    if input("save? (y/n): ") == "y":
        plt.imsave(f"output_{file}.png", image, format="png")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass



if __name__ == '__main__':
    pass