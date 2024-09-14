# SKELET

    a simple app for visualizing raw images "as-is", without processing it beyond just parsing the raw data in each channel and displaying it.


## table of contents

- [details]
- [installation]
- [usage]
- [contact]

## details

### introduction
as a photographer I always wanted to know how exactly a raw image would look like, without any processing. also I have met many colleagues who had the same curiosity. driven by the desire to discover the possible results from such a feature and get inspired by the looks of them, arised the idea of this simple app. skelet is a lightweight python app that lists the pictures available in its "pictures" folder and offers a few possibilities of displaying these images without algoritmically transforming their data, but only by "extracting" them in different forms. the application also offers the possibility of saving these images as uncompressed PNG 16 bit files.

### research
the research initially was done with openai's chatgpt 4.0 that suggested some libraries for image handling. some of them we already knew, from harvard's cs50 python's classes and we tried experimenting first with "imageio", but since it has its own algorithms for processing raw data we opted it out. then with more online reading and also pushing further openai's tool, we came out with the combination of "numpy", "rawpy" and "matplotlib". with these tools we were able to only extract as pure matrixes of values, and that was our goal. the central piece of our extracting algorithm was also suggested by chatgpt, namely:

"color_image[0:height:2, 0:width:2, 0] = raw_image[0:height:2, 0:width:2]"

we were previously using nested "for loops" and "modulo 2" to find each RGGB value and extract the raw data, but the new suggestion from chatgpt with array index notation was much faster and definitively more elegant and pythonic.

also chatgpt helped us to understand better about arrays and algorithms, providing us with online sources and books, such MIT's "introduction do algorithms" which we are still using as support materials for the development of the app. each of the libraries own documentations were as much important for clarifying its usages.

### ui, aesthetics and concept
since the idea was to show the barest form of a digital image, the name "skelet" refers to the skeleton as the innermost and most structural part of the being, the "truth" behind layers of added meaning. following the concept we chose to build the application's ui to be run by a simple command-line-interface, for simplicity of usage and installation, performance and directness. furthermore we chose the open source python libraries "pyfiglet" and "tabulate", to whose creators we are very much thankful, to provide a better looking and easy-to-understand-interface, since by dealing with photography we are also talking about beauty and art.

### designing choices

we chose to have our input "pictures" folder inside the root folder for simplicity's sake, but after, with some user feedback, we might evaluate if prompting the user for the input folder is more adequate. also why not prompting for an output folder?

we saw fit to have our "save" command to be run from inside the display function but that is also something that can be re-thinked

### further description
our display options are all undebayered, which means we see the actual values of pixels as recorded by the camera sensor. the result is an image with only R, G and B colors (our brain mix them and produces the other colors), as opposed to the debayered process, where these RGGB values are summed up to produce a given color in a given color space. our result may look somewhat "strange", and it gets more interesting as we zoom in and start to see the actual RGB pixels, while at the same time seeing the colors our brain extrapolate from these values.

it is our desire, for the future, to explore and build more processing algorithms, such as a gain amplifier simulating a tube compression and another simulating film compression, to amplify the gain without clipping. we always intend to be as bare as possible, not copying exposure algorithms from already existant software.

## installation
all required libraries can be installed with "pip" being run from terminal:

-pyfiglet
-tabulate
-numpy
-rawpy
-matplotlib

"skelet" is very easy to use. its folder with its contents is standalone, all what is needed is to have it placed somewhere in your storage. the "pictures" folder is where you must have the raw images you want to display and/or save. the "output_pictures" is where the app saves the image as a PNG.

## usage
to run the application, use the following command:

python (or python3) skelet.py

after seeing two opening titles, one with the app's name, and another with thanks, you will be prompted to choose a file from the "pictures" folder inside the app's root directory. a table with the file names in the folder and an index number for each will be displayed, and this index is what has to be typed in order to open the chosen file.

then another table will show up, giving the user the following options and the input to achieve it:

* full color, no processing - 0:
input 0 to display the image with all the data available (minus metadata). the algorithm assumes RGGB bayer pattern and displays the four channels with its values. each channel RGGB is mapped to a pixel of a 2x2 square of pixels. the seen result will often be very greenish, because of the presence of both green channels, but actually the displayed image has indeed values of red and blue as well.

* full color, G2 is lum - 1:
input 1 to display each 2x2 square of pixels as RGAB (A for "alpha", or luminance). this algorithm gets raw values for R and B channels in their pixels, displays an average from both green channels in the G pixel, and displays the alpha pixel as a gray pixel with the second green's value pasted to its R, G and B values. the result is somewhat brighter and just a little bit greenish.

* BW from R - 2:
input 2 for extracting only the red values from the RGGB matrix and mapping them to all RGB values in a single pixel. since we no more have a 2x2 square of pixels, because we are extracting only the R pixel values, we reduce the file to one quarter of its size in pixel count, in order not to have redundant pixels. the result is a grayscale image from the red channel.

* BW from G and G2 - 3:
input 3 for the same as the above option, but using an average from both green channels.

* BW from B - 4:
input 4 for the same as option 2, but using the blue channel

* finish program - exit:
type "exit" to exit the program and see a "bye!!" message

after choosing the displaying mode the user will se a python window with the image. this window has some options, and the one with the magnifying glass is, for us, the most important one, allowing the user to choose a portion of the image to magnify. we don't advise using the save button, because the file it generates is very compressed.

* save? (y/n):
for saving the image the user should close the displaying window and the app will prompt for a saving option. type "y" or "Y" as usual for saving the image. any other character will deny saving it. the output format will be PNG 16 bits and it will be stored in the output_pictures folder located in the app's root folder.
after saving or not the user can choose other displaying options or exit gracefully by typing "exit".

## contact

filpedroso3@gmail.com
# skelet
