#Αυτό το αρχείο χρησιμοποιείται ώστε να οριστούν τα custom χρώματα της εφαρμογής MoMA εδώ για την καλύτερη
#αναγνωσιμότητα των υπολοίπων αρχείων.

#Επίσης εδώ θα οριστούνε τα τροποποιημένα styles του ttk
import tkinter as tk
from tkinter import ttk
import os
import customtkinter as ctk

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
            except EOFError:
                pass
            except :
                print("Error Opening File")
        return ob
    except FileNotFoundError:
        theme = "1"
        return theme

def change_next_theme(self):
    self.inform_user_window = None
    ob = read_theme()
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
    print(inform_user_window_exists)
    Inform_user(self)
    def Inform_user(self):
        if self.inform_user_window is None or not self.inform_user_window.winfo_exists():
            self.inform_user_window = Inform_user_Restart(self)  # create window if its None or destroyed
        else:
            self.inform_user_window.focus()  # if window exists focus it


def change_dark_light():
    ctk_light_mode = ctk.get_appearance_mode()
    if ctk_light_mode == "Dark":
        ctk.set_appearance_mode('light')
        print(ctk_light_mode)
    elif ctk_light_mode == "Light":
        ctk.set_appearance_mode('dark')
        print(ctk_light_mode)


class Inform_user_Restart(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Αλλαγή Θέματος")
        self.label.pack(padx=20, pady=20)