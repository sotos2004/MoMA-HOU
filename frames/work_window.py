import datetime
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from customization.color_styles import *



class WorkWindow(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container,background='red',scrollregion = (0,0,3800, 2160 ), *args, **kwargs, highlightthickness=0)

        self.work_frame = ctk.CTkFrame(container)
        # self.work_frame.pack()
        self.work_frame.grid(row=0, column=0,padx=10, pady=10, sticky="NSEW")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # test_worklabel = ctk.CTkLabel(self.work_frame, text = "A Label")
        # test_worklabel.grid(row=1,padx=20, pady=20, column=0, sticky="NSEW")
        # self.rowconfigure(0, weight=1)

        self.intro_Text = (
            "Καλώς ήρθατε στην εφαρμογή MoMA Navigator. Η MoMA Navigator είναι μια εφαρμογή η οποία σας δίνει "
            "την δυνατότητα να πλοηγηθείτε στην ψηφιακή βάση έργων σύγχρονων έργων τέχνης του μουσείου "
            "Museum of Modern Art της Νέας Υόρκης. Η ψηφιακή συλλογή περιλαμβάνει έργα αρχιτεκτονικής,  "
            "κεραμικής , γλυπτικής, σχέδιου, οπτικοακουστικής, ζωγραφικής καθώς και συγγράμματα όλων των"
            "κατηγοριών ")

        self.textbox_width = self.winfo_width()
        self.textbox = ctk.CTkTextbox(self.work_frame, width=self.textbox_width)
        self.textbox.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="NSEW")

        self.textbox.insert("0.0", self.intro_Text)
        self.create_window((0,0),
                           window = self.work_frame,
                           anchor = 'nw',
                           width= 3800,
                           height = 2160
                           )

        self.bind_all('<MouseWheel>', lambda event: self.yview_scroll(-int(event.delta / 60 ), "units"))
        self.bind('<Configure>', self.update_size)
        print(f'Start frame width:', self.winfo_width())
    def update_size(self, event):
        self.create_window((0,0), window = self.work_frame, anchor = 'nw', width = self.winfo_width(), height = self.winfo_width())
        self.textbox_width = self.winfo_width()
        self.textbox_height = self.winfo_width()
        self.textbox.configure(self.work_frame)
        self.textbox.insert("0.0", self.intro_Text)
        print(f'Work frame width:', self.winfo_width())
        print(f'Work frame height:', self.winfo_height())




'''
        self.scrollable_window = self.create_window((0, 0), window=self.work_frame, anchor="nw",
                                                    width=self.winfo_width())

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())






        work_banner_label = ctk.CTkLabel(
            work_frame,
            text="Frame Νο3 ddddddddggggfggggggggggggggggggggggggggggggggggggggggg",

        )
        work_banner_label.grid(row=0, column=0, sticky="NSEW")


        self.bind("<Configure>", configure_window_size)
        self.messages_frame.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)



        scrollbar = ctk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)

        # https://stackoverflow.com/a/17457843/1587271

    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta / 120), "units")

    def update_message_widgets(self, messages, message_labels):
        existing_labels = [
            (message["text"], time["text"]) for message, time in message_labels
        ]

        for message in messages:
            message_time = datetime.datetime.fromtimestamp(message["date"]).strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            if (message["message"], message_time) not in existing_labels:
                self._create_message_container(message["message"], message_time, message_labels)

    def _create_message_container(self, message_content, message_time, message_labels):
        container = ttk.Frame(self.messages_frame)
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(10, 50), pady=10)

        def reconfigure_message_labels(event):
            for label, _ in message_labels:
                label.configure(wraplength=min(container.winfo_width() - 130,
                                               MAX_MESSAGE_WIDTH))  # image width, frame padx, and image padx
            self.messages_frame.update()

        container.bind("<Configure>", reconfigure_message_labels)
        self._create_message_bubble(container, message_content, message_time, message_labels)

    def _create_message_bubble(self, container, message_content, message_time, message_labels):
        avatar_image = Image.open("./assets/male.png")
        avatar_photo = ImageTk.PhotoImage(avatar_image)

        avatar_label = tk.Label(
            container,
            image=avatar_photo
        )

        avatar_label.image = avatar_photo
        avatar_label.grid(
            row=0,
            column=0,
            rowspan=2,
            sticky="NEW",
            padx=(0, 10),
            pady=(5, 0)
        )

        time_label = ttk.Label(
            container,
            text=message_time,
        )

        time_label.grid(row=0, column=1, sticky="NEW")

        message_label = tk.Label(
            container,
            text=message_content,
            wraplength=800,
            justify="left",
            anchor="w"
        )

        message_label.grid(row=1, column=1, sticky="NEW")

        message_labels.append((message_label, time_label))


'''