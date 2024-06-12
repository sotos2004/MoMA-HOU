from PIL import Image, ImageTk
from customization.color_styles import *


class StartFrame(ctk.CTkScrollableFrame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.start_frame1 = ctk.CTkFrame(self, border_width=10)
        self.start_frame1.pack(expand = True, fill = 'both', anchor='center')

        self.image_file = "customization/MoMA_Start_Frane_logo_small_transparent.png"
        self.start_image = ctk.CTkImage(light_image=Image.open(self.image_file),    # https://customtkinter.tomschimansky.com/documentation/utility-classes/image/
                                         size=(512, 369)
                                         )     # https://customtkinter.tomschimansky.com/documentation/widgets/label/
        self.start_label = ctk.CTkLabel(master=self.start_frame1,
                                         text="",                       # Αν το αφήσω κενό  εμφανίζει το κείμενο "CTkLabel" πάνω από την εικόνα!!
                                         image=self.start_image)       # https://stackoverflow.com/questions/56880941/how-to-fix-attributeerror-jpegimagefile-object-has-no-attribute-read
        self.start_label.image = self.start_image   # https://stackoverflow.com/questions/23224574/tkinter-create-image-function-error-pyimage1-does-not-exist
        self.start_label.pack(padx=10, pady=10,expand = True, fill = 'both', anchor='center')

        self.textbox_frame = ctk.CTkFrame(self, border_width=10)
        self.textbox_frame.pack(expand=True, fill='both', anchor='center')

        self.intro_Text = ("Καλώς ήρθατε στην εφαρμογή MoMA Navigator. Η MoMA Navigator είναι μια εφαρμογή η οποία σας δίνει "
                      "την δυνατότητα να πλοηγηθείτε στην ψηφιακή βάση έργων σύγχρονων έργων τέχνης του μουσείου "
                      "Museum of Modern Art της Νέας Υόρκης. Η ψηφιακή συλλογή περιλαμβάνει έργα αρχιτεκτονικής,  "
                      "κεραμικής , γλυπτικής, σχέδιου, οπτικοακουστικής, ζωγραφικής καθώς και συγγράμματα όλων των"
                      "κατηγοριών ")
        #
        # self.textbox_width = self.winfo_width()
        self.textbox = ctk.CTkTextbox(master=self.textbox_frame,font=('default',22), wrap='word')
        self.textbox.pack(padx=10, pady=10,expand = True, fill = 'both', anchor='center')
        self.textbox.insert("0.0", self.intro_Text)


