import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from moma_class import *
from PIL import Image, ImageTk
from customization import *
from frames import MainWindow


set_dpi_awareness()  #Ρύθμιση μόνο για windows ώστε σε οθόνες με υπερ-υψηλή ανάλυση (2Κ+) να φαίνονται σωστά οι χαρακτήρες

# Main Aplication Launch functions
# Version 0.3_Alpha....
#
# Created on 16/04/2024
# Updated on 2/06/2024
# ΠΛΗΠΡΟ 2023-2024 Ομαδική εργασία
# Μάμαλος Κωνσταντίνος
# Μπερνικόλας Μάριος
# Νούσας Γεώργιος
# Παπαδόπουλος Σωτήριος
#

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
        root.destroy()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    root = MoMANavigator()
    root.mainloop()

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
