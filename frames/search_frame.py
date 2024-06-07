import customtkinter as ctk


class SearchFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)
        # Δημιουργία frame και widgets
        self.searchFrame = ctk.CTkFrame(container, border_width=20)
        self.searchFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.searchFrame.columnconfigure(0, weight=1, uniform='f3')
        self.searchFrame.rowconfigure(0, weight=1, uniform='f3')

        self.title_label = ctk.CTkLabel(self.searchFrame,
                                        text="Αναζήτηση",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.title_label.pack(fill="x", pady=10, padx=20)
