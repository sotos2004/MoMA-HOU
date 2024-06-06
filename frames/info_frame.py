import customtkinter as ctk

class InfoFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.infoFrame = ctk.CTkFrame(container, border_width=20)
        self.infoFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.infoFrame.columnconfigure(0, weight=1, uniform = 'f3')
        self.infoFrame.rowconfigure(0, weight=1, uniform = 'f3')

        self.title_label = ctk.CTkLabel(self.infoFrame, text="Πληροφορίες Εφαρμογής", anchor="center",font=("Arial", 16, "bold"))
        self.title_label.pack(fill="x", pady=10, padx=20)
        text='''
        Η εφαρμογή αυτή δημιουργήθηκε για τις αναγκές του τελικου project της Ομάδας Β του τμήματος ΗΛΕ53\n 
        του μαθήματος ΠΛΗΠΡΟ 2024-2024\n
        Η ομάδα αποτελέιται από τους:
        # Μάμαλος Κωνσταντίνος\n
        # Μπερνικόλας Μάριος\n
        # Νούσας Γεώργιος\n
        # Παπαδόπουλος Σωτήρης\n
        \n
        \n
        Ολές οι πληροφορίες και τα δεδομένα είναι ιδιοκτησία του Museum of Modem Art of New York και έχουν δημοσιευθεί με άδεια CC0.\n
        Digital Object Identifier 10.5281/zenodo.11469944   
        '''
        self.label = ctk.CTkLabel(self.infoFrame, text=text,font=("Arial", 14))
        self.label.pack( padx=20)

