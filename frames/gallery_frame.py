import customtkinter as ctk


class GalleryFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)
        # Δημιουργία frame και widgets
        self.galleryFrame = ctk.CTkFrame(container, border_width=20)
        self.galleryFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.galleryFrame.columnconfigure(0, weight=1, uniform='f3')
        self.galleryFrame.rowconfigure(0, weight=1, uniform='f3')

        self.title_label = ctk.CTkLabel(self.galleryFrame,
                                        text="Gallery",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.title_label.pack(fill="x", pady=10, padx=20)
