import customtkinter as ctk


class InfoFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)
        # Δημιουργία frame και widgets
        self.infoFrame = ctk.CTkFrame(container, border_width=10)
        self.infoFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.infoFrame.columnconfigure(0, weight=1, uniform='f3')
        self.infoFrame.rowconfigure(0, weight=1, uniform='f3')

        self.title_label = ctk.CTkLabel(self.infoFrame,
                                        text="Πληροφορίες Εφαρμογής",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.title_label.pack(fill="x", pady=10, padx=10)
        text = '''        
        Η εφαρμογή αυτή δημιουργήθηκε για τις ανάγκες του τελικού project της Ομάδας Β του τμήματος ΗΛΕ53 
        του μαθήματος ΠΛΗΠΡΟ 2024-2024 του Ελληνικού Ανοιχτού Πανεπιστήμιου.
        \n
        \n
        Η ομάδα αποτελείται (κατά αλφαβητική σειρά) από τους :\n
        Μάμαλος Κωνσταντίνος
        Μπερνικόλας Μάριος
        Νούσας Γεώργιος
        Παπαδόπουλος Σωτήρης
        \n
        \n
        Όλες οι πληροφορίες και τα δεδομένα είναι ιδιοκτησία του Museum of Modem Art of New York και έχουν δημοσιευθεί με άδεια CC0.\n
        Digital Object Identifier 10.5281/zenodo.11469944   
        '''
        self.label = ctk.CTkLabel(self.infoFrame, text=text, font=("Arial", 14))
        self.label.pack(padx=20, pady=40)
