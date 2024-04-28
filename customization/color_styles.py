# Αυτό το αρχείο χρησιμοποιείται ώστε να οριστούν τα custom χρώματα τυης εφαρμογής MoMA εδώ για την καλύτερη
# αναγνωσιμότητα των υπολοίπων αρχείων.

# Επίσης εδώ θα οριστούνε τσ τροποποιημένα stytes του ttk της
import tkinter as tk
from tkinter import ttk

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


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
                         background='midnightblue')

        style2.configure("BottomBanner.TFrame",
                         background='LightSteelBlue2')

        style2.configure("BottomBannerText.TLabel",
                         background='red',
                         foreground=COLOUR_DARK_TEXT,
                         font="Courier 12"
                         )


'''








        style2.configure("Timer2.TFrame",
        background='yellow')

        style2.configure("Background2.TFrame",
        background=COLOUR_PRIMARY)

        style2.configure("TimerText2.TLabel",
        background=COLOUR_LIGHT_BACKGROUND,
        foreground=COLOUR_DARK_TEXT,
        font="Courier 46"
        )
        style2.configure("LightText2.TLabel",
        background=COLOUR_PRIMARY,
        foreground=COLOUR_LIGHT_TEXT,
        font=("TkDefaultFont", 11)
        )

        style2.configure("PomodoroButton2.TButton",
        background=[COLOUR_SECONDARY],
        foreground=COLOUR_LIGHT_TEXT,
        font=("TkDefaultFont", 11)
        )

        style2.map("PomodoroButton2.TButton",
        background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )

        '''


