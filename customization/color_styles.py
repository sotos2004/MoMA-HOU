#Αυτό το αρχείο χρησιμοποιείται ώστε να οριστούν τα custom χρώματα τυης εφαρμογής MoMA εδώ για την καλύτερη
#αναγνωσιμότητα των υπολοίπων αρχείων.

#Επίσης εδώ θα οριστούνε τσ τροποποιημένα stytes του ttk της
import tkinter as tk
from tkinter import ttk
import os
from pickle import dump , load

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"
RIGHT_FRAME_BACKGROUND = "#2689ad"


class ColorStyles(ttk.Style):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        style2 = ttk.Style()
        style2.theme_use("clam")

        style2.configure("Background.TFrame",
                         background=COLOUR_PRIMARY)

        style2.configure("LightText.TLabel",
                        background=COLOUR_PRIMARY,
                        foreground=COLOUR_LIGHT_TEXT,
                        font=("TkDefaultFont", 11)
                        )

        style2.configure("TopBanner.TFrame",
                         background=COLOUR_PRIMARY)

        style2.configure("TopBannerText.TLabel",
                        background=COLOUR_PRIMARY,
                        foreground=COLOUR_LIGHT_TEXT,
                        font="Courier 12 bold"
                        )

        style2.configure("LeftBannerButtonsFlat.TButton",
                         background=COLOUR_PRIMARY,
                         foreground=COLOUR_LIGHT_TEXT,
                         font=("TkDefaultFont", 11),
                         relief="flat"
                         )
        style2.configure("LeftBannerButtonsRaised.TButton",
                         background=COLOUR_PRIMARY,
                         foreground=COLOUR_LIGHT_TEXT,
                         font=("TkDefaultFont", 11),
                         relief="raised"
                         )
        style2.configure("LeftBannerButtonsSunken.TButton",
                         background=COLOUR_PRIMARY,
                         foreground=COLOUR_LIGHT_TEXT,
                         font=("TkDefaultFont", 11),
                         relief="sunken"
                         )
        style2.configure("LeftBannerButtonsGroove.TButton",
                         background=COLOUR_PRIMARY,
                         foreground=COLOUR_LIGHT_TEXT,
                         font=("TkDefaultFont", 11),
                         relief="groove"
                         )
        style2.configure("LeftBannerButtonsSolid.TButton",
                         background=COLOUR_PRIMARY,
                         foreground=COLOUR_LIGHT_TEXT,
                         font=("TkDefaultFont", 11),
                         relief="solid"
                         )
        style2.configure("LeftBannerButtonsRidge.TButton",
                         background=COLOUR_PRIMARY,
                         foreground=COLOUR_LIGHT_TEXT,
                         font=("TkDefaultFont", 11),
                         relief="ridge"
                         )

        style2.configure("LeftBannerText.TLabel",
                        background=COLOUR_PRIMARY,
                        foreground=COLOUR_LIGHT_TEXT,
                        font="Courier 12 bold"
                        )

        style2.configure("RightBanner.TFrame",
                        background='RIGHT_FRAME_BACKGROUND')

        style2.configure("BottomBanner.TFrame",
                        background='LightSteelBlue2')

        style2.configure("BottomBannerText.TLabel",
                        background='red',
                        foreground=COLOUR_DARK_TEXT,
                        font="Courier 12"
                        )


def next_theme():
    ob = []
    ob = read_theme()
    if ob == "1":
        theme = "customization/Oceanix.json"
    elif ob == "2":
        theme = "customization/sky.json"
    else:
        theme = "customization/Oceanix.json"
    return theme


def read_theme():
    ob = []
    try:
        with open("customization/theme_config", "r"):
            file = open("customization/theme_config", "r")
            ob = []
            try:
                ob = file.readline()
                # ob = load("customization/theme_config")
                # while ob is not None:
                #     print(ob)
                #     ob = open("customization/theme_config")
            except EOFError:
                pass
            except :
                print("Error Opening File")
        return ob
    except FileNotFoundError:
        theme = "customization/Oceanix.json"
        return theme

def change_next_theme():
    ob = read_theme()
    print(ob)
    if ob == "1":
        try:
            with open("customization/theme_config", "w") as save_file:
               save_file.write("2")
        except :
            pass
        #     print("Δεν έχετε τα απαραίτητα δικαιώματα για την εγγραφή του αρχείου. Επικοινωνήστε με τον διαχειριστή σας.")
    elif ob  == "2":
        try:
            with open("customization/theme_config", "w") as save_file:
                save_file.write("1")
        except:
            pass
        #     print("Δεν έχετε τα απαραίτητα δικαιώματα για την εγγραφή του αρχείου. Επικοινωνήστε με τον διαχειριστή σας.")
    else:
        try:
            with open("customization/theme_config", "w") as save_file:
                save_file.write("2")
        except:
            pass
        #     print("Δεν έχετε τα απαραίτητα δικαιώματα για την εγγραφή του αρχείου. Επικοινωνήστε με τον διαχειριστή σας.")


