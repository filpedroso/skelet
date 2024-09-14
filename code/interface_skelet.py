from pyfiglet import Figlet
from tabulate import tabulate
import time
import os



# processing options
options = {
    "full color, no processing": "0",
    "full color, G2 is lum": "1",
    "BW from R": "2",
    "BW from G and G2": "3",
    "BW from B": "4",
    "-------------------------": "------------",
    "finish program": "exit",
}





# opening title
def title1():

    figlet = Figlet()
    figlet.setFont(font="cybermedium")
    return f"{figlet.renderText("skelet")} by fil_pedroso\n"




# thanks title
def title2():

    thanks_to = "cs50 | harvard_university | python | pyfyglet, rawpy\nnumpy, matplotlib, tabulate | open_ai | dearpygui\n"
    figlet = Figlet()
    figlet.setFont(font="cybermedium")
    return f"{figlet.renderText("very thanks")}{thanks_to}"




# freezes some text for some time, before moving on the script
def timed_display(text, duration):

    print(text)
    time.sleep(duration)
    os.system('cls' if os.name == 'nt' else 'clear')




# tabulates files in pictures folder
def loadfile(pictures):

    return tabulate(pictures, headers=["picture file", "input this"])




# tabulates processing options
def display_options():

    return tabulate(options.items(), headers=["processing type or exit", "input this"])




if __name__ == "__main__":
    pass