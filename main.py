import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from moma_class import *
from PIL import Image, ImageTk
from customization import *
from frames import MainWindow



set_dpi_awareness()  # Ρύθμιση μόνο για windows ώστε σε οθόνες με υπερ-υψηλή ανάλυση (2Κ+) να φαίνονται σωστά οι χαρακτήρες

# Main Aplication Launch functions
# Version 0.35_Alpha....
#
# Created on 16/04/2024
# Updated on 3/06/2024
# ΠΛΗΠΡΟ 2023-2024 Ομαδική εργασία
# Μάμαλος Κωνσταντίνος
# Μπερνικόλας Μάριος
# Νούσας Γεώργιος
# Παπαδόπουλος Σωτήριος


class MoMANavigator(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        ctk.set_appearance_mode('system')
        start_theme = next_theme()
        ctk.set_default_color_theme(start_theme)
        self.geometry("1366x768+50+50")
        self.minsize(1366, 768)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.iconbitmap('customization/MoMA_Icon_PNG_with_Alpha_16_to_256.ico')
        self.title("MoMA Navigator for EAP _-=2024=-_")

        self.main_frame = MainWindow(self, self.root_terminate)
        self.main_frame.grid(row=0, column=0, sticky="NSEW")

    def root_terminate(self):
        root.quit()
        # root.destroy()


class Splashscreen(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        width, height = 512, 512
        # print(self.winfo_screenwidth())
        # print(self.winfo_screenwidth())
        splash_width = ((self.winfo_screenwidth()//2)-(width//2))
        # print(splash_width)
        splash_height = ((self.winfo_screenheight()//2)-(height//2))
        # print(splash_height)
        # self.geometry("512x512+50+50")
        self.geometry('{}x{}+{}+{}'.format(width, height, splash_width, splash_height))
        self.overrideredirect(True)
        self.splash_frame = ctk.CTkFrame(self, width=510, height=510)
        self.splash_frame.grid(row=0, sticky="NSEW")
        self.image_file = "customization\\splashscreen_small.png"

        # splash_image = ImageTk.PhotoImage("customization\\splashscreen_small.png")
        # splash_image = ImageTk.PhotoImage(Image.open(image_file))

        self.splash_image = ctk.CTkImage(light_image=Image.open(self.image_file),    # https://customtkinter.tomschimansky.com/documentation/utility-classes/image/
                                         size=(510, 510)
                                         )     # https://customtkinter.tomschimansky.com/documentation/widgets/label/
        self.splash_label = ctk.CTkLabel(master=self.splash_frame,
                                         text="",                       # Αν το αφήσω κενό  εμφανίζει το κείμενο "CTkLabel" πάνω από την εικόνα!!
                                         image=self.splash_image)       # https://stackoverflow.com/questions/56880941/how-to-fix-attributeerror-jpegimagefile-object-has-no-attribute-read
        self.splash_label.image = self.splash_image   # https://stackoverflow.com/questions/23224574/tkinter-create-image-function-error-pyimage1-does-not-exist
        self.splash_label.pack()
        # terminate_splash = splash_terminate()
        self.after(200, self.splash_terminate)

    def splash_terminate(self):
        Splashscreen.withdraw(self)
        Splashscreen.quit(self)
        # Splashscreen.destroy(self)


def splashscreen_close():
    print("SplashScreen Shutdown")
    # root2.destroy()


def moma_close():               # Εκτλείται όταν ο χρήστης πατάει το "Χ" του παραθύρου για να κλείσει το πρόγραμμα.
    print("MoMA Shutting Down")
    root.destroy()
    root.quit()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.


if __name__ == '__main__':

    root2 = Splashscreen()

    # Με την .protocol γίνεται bind το κλείσιμο της εφαρμογής από το "Χ" του παραθύρου σε μια function, συγκεκριμμένα εδώ η function που θα εκτελεστεί θα κλείσει το παράθυρο
    root2.protocol("WM_DELETE_WINDOW", splashscreen_close)  # https://chat.stackoverflow.com/transcript/6/2022/8/24/0-19
    root2.mainloop()        # Η root2.protocol χρησιμοποιείται για τον χειρισμό των μηνυμάτων λάθους που παράγονται κατά το κλείσιμο του CustomTkInter παραθύρου της Splashscreen

    root = MoMANavigator()
    root.protocol("WM_DELETE_WINDOW", moma_close)  # https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter
    root.mainloop()

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
