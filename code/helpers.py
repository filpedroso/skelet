from interface_skelet import title1, title2, timed_display, loadfile, display_options
import lib_skelet
import multiprocessing as mp
import numpy as np


filename = None
raw_array = None
raw_img = None

def helper_loader(sender, app_data):
    global filename
    global raw_array
    for key, value in app_data["selections"].items():
        path = value
        filename = key

    raw_array = lib_skelet.loader(path)
    return raw_array



def helper_imager(sender):
    global raw_img

    if sender == 32:
        raw_img = lib_skelet.fullcolor_raw0(raw_array)

    elif sender == 33:
        raw_img = lib_skelet.fullcolor_lum1(raw_array)

    elif sender == 34:
        raw_img = lib_skelet.grayscale_red2(raw_array)

    elif sender == 35:
        raw_img = lib_skelet.grayscale_green3(raw_array)

    elif sender == 36:
        raw_img = lib_skelet.grayscale_blue4(raw_array)

    return helper_displayer(raw_img, filename)


def helper_displayer(raw_img, filename):
    p = mp.Process(target=lib_skelet.display_image, args=(raw_img, filename))
    p.start()
    p.join()


def helper_save():
    global raw_img
    raw_img = raw_img / np.max(raw_img)
    lib_skelet.save_img(raw_img, filename)


def main():
    ...

if __name__ == "__main__":
    main()
