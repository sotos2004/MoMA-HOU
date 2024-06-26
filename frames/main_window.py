from PIL import Image
from customization.color_styles import *
from frames.start_frame import StartFrame
from frames.settings_frame import SettingsFrame
from frames.info_frame import InfoFrame
from frames.input_frame import InputFrame
from frames.gallery_frame import GalleryFrame
from frames.stats_frame import StatsFrame
from frames.search_frame import SearchFrame
import webbrowser

class MainWindow(ctk.CTkFrame):
    @staticmethod
    def __doc__():
        """
        Δημιουργεί το κυρίως παράθυρο (Frame)
        :rtype: null
        """
        print('Documentation goes here')

    def __init__(self, container, root_terminate, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.config= SettingsFrame.readConfig()
        self.imagePath=self.config.get('SETTINGS', 'imagepath')
        def show_frame(frame,**kwargs):
            self.start_frame.destroy()
            self.start_frame = frame(self, **kwargs)

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

        """ Δημιουργία του Frame Νο1 """
        top_banner = ctk.CTkFrame(self, border_width=10)
        top_banner.grid(row=0, columnspan=2, sticky="NE")

        top_banner_label = ctk.CTkLabel(
            top_banner,
            text="Εφαρμογή πλοήγησης της Βιβλιοθήκης Έργων του Museum of Modern Art, New York City",
            font=("Courier",20,"bold")
        )
        top_banner_label.grid(row=0, column=0, padx=5, sticky="NE")

        """Δημιουργία του Frame Νο2"""
        left_banner = ctk.CTkFrame(self, width=50,)

        left_banner.grid(row=1, column=0, sticky="N", pady=5, padx=5)
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        self.image_file = self.imagePath + "/thumbnail_MoMA_Icon_PNG_with_Alpha_256x256.png"
        self.start_image = ctk.CTkImage(light_image=Image.open(self.image_file),
                                        # https://customtkinter.tomschimansky.com/documentation/utility-classes/image/
                                        size=(120, 120)
                                        )  # https://customtkinter.tomschimansky.com/documentation/widgets/label/
        self.start_label = ctk.CTkLabel(left_banner,
                                        text="",
                                        # Αν το αφήσω κενό εμφανίζει το κείμενο "CTkLabel" πάνω από την εικόνα!!
                                        image=self.start_image)
        self.start_label.image = self.start_image
        self.start_label.pack(padx=10, pady=10,expand = True, fill = 'both', anchor='center')

        Left_b1 = ctk.CTkButton(left_banner,
                                text="Αναζήτηση",
                                command= lambda: show_frame(SearchFrame) )
        Left_b1.pack(fill='x')
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b6 = ctk.CTkButton(left_banner,
                                text="Επεξεργασία",
                                command= lambda: show_frame(InputFrame) )
        Left_b6.pack(fill='x')
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b2 = ctk.CTkButton(left_banner,
                                text="Gallery",
                                command= lambda: show_frame(GalleryFrame) ) # command=raise() το
        Left_b2.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b3 = ctk.CTkButton(left_banner,
                                text="Στατιστικά",
                                command= lambda: show_frame(StatsFrame) ) # command=raise() το
        Left_b3.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b4 = ctk.CTkButton(left_banner,
                                text="Πληροφορίες",
                                command= lambda: show_frame(InfoFrame)) # command=raise() το
        Left_b4.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')

        Left_b5 = ctk.CTkButton(left_banner,
                                text="Ρυθμίσεις",
                                command= lambda: show_frame(SettingsFrame)) # command=raise() το
        Left_b5.pack()
        ttk.Separator(left_banner, orient="horizontal").pack(fill='x')
        """ Δημιουργία του Frame Νο3"""
        # self.work_window = WorkWindow(self)
        # self.work_window.grid(row=1, column=1, sticky="NSEW", pady=5)
        self.start_frame = StartFrame(self)
        self.start_frame.grid(row=1, column=1, columnspan=3, pady=2, padx=5, sticky="NSEW")


        """Δημιουργία του Frame Νο4"""
        bottom_banner = ctk.CTkFrame(self)
        bottom_banner.grid(row=2, columnspan=5,padx=5, pady=5, sticky="NSEW")
        ttk.Separator(bottom_banner, orient="vertical").grid(row=0, column=4, columnspan=1, sticky="NS")

        def _open_Video_Tutorial():
            webbrowser.open_new(r"https://www.youtube.com/watch?v=3jw-tuYpx-4")

        video_tutorial = ctk.CTkButton(bottom_banner, text="Βίντεο", command=_open_Video_Tutorial)
        video_tutorial.grid(row=0, column=1,padx=10, pady=5, sticky="W")
        ttk.Separator(bottom_banner, orient="vertical").grid(row=0, column=2, columnspan=1, sticky="NS")

        def _open_Manual():
            webbrowser.open_new(r"https://github.com/sotos2004/MoMA-HOU/blob/main/DATA/Manual.pdf")

        pdf_manual_launch = ctk.CTkButton(bottom_banner, text="Εγχειρίδιο Χρήσης", command=_open_Manual) # command=
        pdf_manual_launch.grid(row=0, column=3,padx=10, pady=5, sticky="W")
        ttk.Separator(bottom_banner, orient="vertical").grid(row=0, column=4, columnspan=1, sticky="NS")

        def _open_GitHub():
            webbrowser.open_new(r"https://github.com/sotos2004/MoMA-HOU/tree/main")

        GitHub_repo = ctk.CTkButton(bottom_banner, text="Πηγαίος\n Κώδικας", command=_open_GitHub)
        GitHub_repo.grid(row=0, column=5,padx=10, pady=5, sticky="EW")
        ttk.Separator(bottom_banner, orient="vertical").grid(row=0, column=6, columnspan=1, sticky="NS")


        Change_Color = ctk.CTkButton(bottom_banner,
                                  text="Εναλλαγή Φωτεινού\n\Σκοτεινού Θέματος",
                                  command=lambda: change_dark_light())
        Change_Color.grid(row=0, column=7, columnspan=1, padx=10, pady=5, sticky="EW")
        ttk.Separator(bottom_banner, orient="vertical").grid(row=0, column=8, columnspan=1, sticky="NS")


        Change_Color = ctk.CTkButton(bottom_banner,             # ΠΡΕΠΕΙ να γίνει επανεκκίνηση της εφαρμογής
                                  text="Εναλλαγή Θέματος",      #Μπορεί να γίνει και χωρίς επανεκκίνηση αλλά χάνονται τα δεδομένα του χρήστη
                                  command=lambda: change_next_theme(self))
        Change_Color.grid(row=0, column=9, columnspan=1, padx=10, pady=5, sticky="EW")
        ttk.Separator(bottom_banner, orient="vertical").grid(row=0, column=10, columnspan=1, sticky="NS")



        """Δημιουργία του Frame Νο5"""
        exit_banner = ctk.CTkFrame(self)
        exit_banner.grid(row=2, column=1,padx=5, pady=5, sticky="E")

        terminate_app = ctk.CTkButton(exit_banner, text="Έξοδος",hover_color = "red", command=root_terminate)
        terminate_app.pack(fill='x', padx=10, pady=5)
        terminate_app.grid (row=0, column=2,padx=10, pady=5, sticky="E")




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