import tkinter as tk
from tkinter import ttk
from customization.color_styles import *
import datetime
from frames.work_window import WorkWindow
import webbrowser


class MainWindow(ttk.Frame):
    @staticmethod
    def __doc__():
        """
        Δημιουργεί το κυρίως παράθυρο (Frame)
        :rtype: null
        """
        print('Documentation goes here')

    def __init__(self, container, root_terminate, *args, **kwargs):
        super().__init__(container, *args, **kwargs)


        """Ρυθμίσεις μεγέθους για τα 4 κύρια frames"""
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        styles = ColorStyles(self)

        self["style"] = "Background.TFrame"

        """ Δημιουργία του Frame Νο1 """
        top_banner = ttk.Frame(self, style="TopBanner.TFrame", padding=10)
        top_banner.grid(row=0, columnspan=2, sticky="NE")

        top_banner_label = ttk.Label(
            top_banner,
            text="Εφαρμογή πλοήγησης της Βιβλιοθήκης Έργων του Museum of Modern Art, New York City",
            style="TopBannerText.TLabel"
        )
        top_banner_label.grid(row=0, column=0, sticky="NE")

        """Δημιουργία του Frame Νο2"""
        left_banner = ttk.Frame(self,style="TopBanner.TFrame", padding=10)
        left_banner.configure(width=10)
        left_banner.grid(row=1, column=0, sticky="N")

        left_banner_label = ttk.Label(
            left_banner,
            text="Frame Νο2",
            style="LeftBannerText.TLabel"
        )
        left_banner_label.pack()
        #left_banner_label.grid(row=0, column=0, sticky="W")

        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        '''
        Left_b0 = tk.Button(left_banner, text="FLAT", relief="flat")
        Left_b0.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')
        '''

        Left_b1 = ttk.Button(left_banner, text="Αναζήτηση", style="LeftBannerButtonFlat.TButton") # command=raise() το
        Left_b1.pack(fill='x')
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b2 = ttk.Button(left_banner, text="Gallery", style="LeftBannerButtonsRaised.TButton") # command=raise() το
        Left_b2.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b3 = ttk.Button(left_banner, text="Σατιστικά", style="LeftBannerButtonsSunken.TButton") # command=raise() το
        Left_b3.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b4 = ttk.Button(left_banner, text="Πληροφορίες", style="LeftBannerButtonsGroove.TButton") # command=raise() το
        Left_b4.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b5 = ttk.Button(left_banner, text="Ρυθμίσεις", style="LeftBannerButtonsSolid.TButton") # command=raise() το
        Left_b5.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        # Δοκιμές εμφάνισης των κουμπιών
        '''
        Left_b1 = ttk.Button(left_banner, text="Αναζήτηση", style="LeftBannerButtonsFlat.TButton") # command=raise() το
        Left_b1.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b2 = ttk.Button(left_banner, text="Gallery", style="LeftBannerButtonsRaised.TButton") # command=raise() το
        Left_b2.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b3 = ttk.Button(left_banner, text="Σατιστικά", style="LeftBannerButtonsSunken.TButton") # command=raise() το
        Left_b3.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b4 = ttk.Button(left_banner, text="Πληροφορίες", style="LeftBannerButtonsGroove.TButton") # command=raise() το
        Left_b4.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b5 = ttk.Button(left_banner, text="Ρυθμίσεις", style="LeftBannerButtonsSolid.TButton") # command=raise() το
        Left_b5.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b6 = ttk.Button(left_banner, text="RIDGE", style="LeftBannerButtonsRidge.TButton") # command=raise() το
        Left_b6.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')
        '''

        """ Δημιουργία του Frame Νο3"""
        self.work_window = WorkWindow(self)
        self.work_window.grid(row=1, column=1, sticky="NSEW", pady=5)



        """Δημιουργία του Frame Νο4"""


        bottom_banner = ttk.Frame(self, style="BottomBanner.TFrame", padding=10)
        bottom_banner.grid(row=2, columnspan=5, sticky="NSEW")


        bottom_banner_label = ttk.Label(
            bottom_banner,
            text="Frame Νο4",
            style="BottomBannerText.TLabel"
        )
        bottom_banner_label.grid(row=0, column=0, sticky="W")

        video_tutorial = ttk.Button(bottom_banner, text="Βίντεο")   # command=
        video_tutorial.grid(row=0, column=1, sticky="W")

        pdf_manual_launch = ttk.Button(bottom_banner, text="Εγχειρίδιο Χρήσης") # command=
        pdf_manual_launch.grid(row=0, column=2, sticky="W")

        def _open_GitHub():
            webbrowser.open_new(r"https://github.com/sotos2004/MoMA-HOU/tree/main")

        GitHub_repo = ttk.Button(bottom_banner, text="Πηγαίος Κώδικας", command=_open_GitHub) # command=
        GitHub_repo.grid(row=0, column=3, sticky="W")

        terminate_app = ttk.Button(bottom_banner, text="Έξοδος", command=root_terminate)
        terminate_app.grid(row=0, column=4, sticky="E")


'''
 #      self.frames = {}   Αποθήκευση των frame sως λίστα !!!

        settings_frame = Settings(container, self, lambda: self.show_frame(WorkWindow))
        stat_frame = Timer(container, self, lambda: self.show_frame(Settings))
        settings_frame.grid(row=0, column=0, sticky="NEWS")
        timer_frame.grid(row=0, column=0, sticky="NEWS")

        self.frames[Settings] = settings_frame
        self.frames[Timer] = timer_frame

        self.show_frame(Timer)
'''

