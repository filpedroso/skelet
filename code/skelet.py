from lib_skelet import (
    pics_list,
    loader,
    fullcolor_raw0,
    fullcolor_lum1,
    grayscale_red2,
    grayscale_green3,
    grayscale_blue4,
    display_image,
)
from interface_skelet import title1, title2, timed_display, loadfile, display_options
from pyfiglet import Figlet
import time
import os
import sys


def main():

    # shows both titles on terminal, timing their duration
    timed_display(title1(), 3)  # skelet
    timed_display(title2(), 4)  # thanks

    list_pictures = pics_list()  # function to return list of files in pictures folder

    pictures = {}  # empty dict

    for i in range(len(list_pictures)):
        pictures[list_pictures[i]] = i  # populates dict with {fileName: index}

    nicely_tabulated = loadfile(
        pictures.items()
    )  # passes a list of key-value tuples from previous dict to tabulate

    # inputs user for file to be processed
    while True:

        file_choice = input(
            f"{nicely_tabulated}\n\nfile number: "
        )  # passes table for user to choose the file

        # input error handling
        try:
            if list_pictures[int(file_choice)] in pictures:
                break
        except (ValueError, IndexError):
            os.system("cls" if os.name == "nt" else "clear")  # clears terminal
            print("usage: choose one of the files below:")
            pass

    # gets file name and path from user's choice and passes into loader function
    file = f"pictures/{list_pictures[int(file_choice)]}"
    raw_image = loader(file)  # loads chosen file
    os.system("cls" if os.name == "nt" else "clear")

    # inputs user to choose processing mode
    while True:

        file_ = file.split(".")[
            0
        ]  # starts editing file name to be used for file naming
        display_option = input(
            f"{display_options()}\n\nprocessing type: "
        )  # shows modes of display of the picture while capturing input

        # edits file name and passes processing function (or exit) according to user option
        if display_option == "0":
            file_ = f"{file_}raw"
            display_image(fullcolor_raw0(raw_image), file_)

        elif display_option == "1":
            file_ = f"{file_}lum"
            display_image(fullcolor_lum1(raw_image), file_)

        elif display_option == "2":
            file_ = f"{file_}red"
            display_image(grayscale_red2(raw_image), file_)

        elif display_option == "3":
            file_ = f"{file_}green"
            display_image(grayscale_green3(raw_image), file_)

        elif display_option == "4":
            file_ = f"{file_}blue"
            display_image(grayscale_blue4(raw_image), file_)

        # exits program and says goodbye
        elif display_option == "exit":
            os.system("cls" if os.name == "nt" else "clear")
            figlet = Figlet()
            figlet.setFont(font="cybermedium")
            timed_display(figlet.renderText("bye!!"), 2)
            sys.exit()

        # error handling
        else:
            timed_display("choose one of the options above", 2)
            os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
