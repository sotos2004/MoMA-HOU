import tkinter as tk
from tkinter import ttk
from customization.color_styles import *
import datetime
from frames.work_window import WorkWindow



class MainWindow(ttk.Frame):
    @staticmethod
    def __doc__():
        """
        Δημιουργεί το κυρίως παράθυρο (Frame)
        :rtype: null
        """
        print('Documentation goes here')

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        """Ρυθμίσεις μεγέθους για τα 4 κύρια frames"""
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)


        style = ttk.Style()
        style.theme_use("clam")
        style.configure("LightText.TLabel",
                        background=COLOUR_PRIMARY,
                        foreground=COLOUR_LIGHT_TEXT,
                        font=("TkDefaultFont", 11)
                        )

        style.configure("Background.TFrame",
                        background=COLOUR_PRIMARY)
        self["style"] = "Background.TFrame"

        style.configure("TopBanner.TFrame",
                        background=COLOUR_PRIMARY)

        # Δημιουργία του Frame Νο1
        top_banner = ttk.Frame(self, style="TopBanner.TFrame", padding=10)
        top_banner.grid(row=0, columnspan=2, sticky="NE")

        style.configure("TopBannerText.TLabel",
                        background=COLOUR_PRIMARY,
                        foreground=COLOUR_LIGHT_TEXT,
                        font="Courier 12 bold"
                        )
        top_banner_label = ttk.Label(
            top_banner,
            text="Εφαρμογή πλοήγησης της Βιβλιοθήκης Έργων του Museum of Modern Art, New York City",
            style="TopBannerText.TLabel"
        )
        top_banner_label.grid(row=0, column=0, sticky="NE")

        # Δημιουργία του Frame Νο2
        left_banner = ttk.Frame(self, width=800, padding=10)
        left_banner.grid(row=1, column=0, sticky="W")

        style.configure("LeftBannerText.TLabel",
                        background='red',
                        foreground=COLOUR_DARK_TEXT,
                        font="Courier 12"
                        )
        left_banner_label = ttk.Label(
            left_banner,
            text="Frame Νο2",
            style="LeftBannerText.TLabel"
        )
        left_banner_label.grid(row=0, column=0, sticky="W")

        # Δημιουργία του Frame Νο3
        self.work_window = WorkWindow(self)
        self.work_window.grid(row=1, column=1, sticky="NSEW", pady=5)

        '''
        style.configure("RightBanner.TFrame",
                        background='yellow')

        right_banner = ttk.Frame(self,style="RightBanner.TFrame", padding=10)
        right_banner.grid(row=1, column=1, sticky="NSEW")

        style.configure("LeftBannerText.TLabel",
                        background='red',
                        foreground=COLOUR_DARK_TEXT,
                        font="Courier 12"
                        )
        right_banner_label = ttk.Label(
            right_banner,
            text="Frame Νο3",
            style="LeftBannerText.TLabel"
        )
        right_banner_label.grid(row=0, column=0, sticky="NSEW")
        '''
        # Δημιουργία του Frame Νο4
        style.configure("BottomBanner.TFrame",
                        background='cyan')

        bottom_banner = ttk.Frame(self,style="BottomBanner.TFrame", padding=10)
        bottom_banner.grid(row=2, columnspan=2, sticky="NSEW")

        style.configure("BottomBannerText.TLabel",
                        background='red',
                        foreground=COLOUR_DARK_TEXT,
                        font="Courier 12"
                        )
        bottom_banner_label = ttk.Label(
            bottom_banner,
            text="Frame Νο4",
            style="BottomBannerText.TLabel"
        )
        bottom_banner_label.grid(row=0, column=0, sticky="NSEW")


'''
 #      self.frames = {}   Αποθήκευση των frame sως λίστα !!!

        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        stat_frame = Timer(container, self, lambda: self.show_frame(Settings))
        settings_frame.grid(row=0, column=0, sticky="NEWS")
        timer_frame.grid(row=0, column=0, sticky="NEWS")

        self.frames[Settings] = settings_frame
        self.frames[Timer] = timer_frame

        self.show_frame(Timer)
'''