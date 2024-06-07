import customtkinter as ctk
import configparser
import sys
import moma_class as mc
from tkinter import messagebox

sys.path.append('../')
configLocation = 'DATA/config.ini'

class SettingsFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)
        # Αρχικοποίηση μεταβλητών
        self.checkboxValue = ctk.StringVar()
        self.md = mc.MoMA()
        self.configLocation = configLocation

        # Λήψη δεδομένων παραμετροποίησης
        config = self.readConfig()

        # Δημιουργία frame και widgets
        self.settingsFrame = ctk.CTkFrame(container, border_width=20)
        self.settingsFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.settingsFrame.columnconfigure(0, weight=1, uniform='f3')
        self.settingsFrame.rowconfigure(0, weight=1, uniform='f3')

        self.titleLabel = ctk.CTkLabel(self.settingsFrame,
                                        text="Ρυθμίσεις",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.titleLabel.pack(fill="x", pady=5, padx=20)

        self.dbPathLabel = ctk.CTkLabel(self.settingsFrame, text="Τοποθεσία Βάσης")
        self.dbPathLabel.pack(padx=20)

        self.dbPathEntry = ctk.CTkEntry(self.settingsFrame, width=300)
        self.dbPathEntry.pack(padx=20, pady=5)
        self.dbPathEntry.insert(0, config.get('SETTINGS', 'databasepath'))

        self.webUrlLabel = ctk.CTkLabel(self.settingsFrame, text="Τοποθεσία διαδικτύου (Url)")
        self.webUrlLabel.pack(padx=20)

        self.webUrlEntry = ctk.CTkEntry(self.settingsFrame, width=300)
        self.webUrlEntry.pack(padx=20, pady=5)
        self.webUrlEntry.insert(0, config.get('SETTINGS', 'webdataurl'))

        self.dbTypeLabel = ctk.CTkLabel(self.settingsFrame, text="Είδος Βάσης Δεδομένων")
        self.dbTypeLabel.pack(padx=20)

        self.dbTypeCombo = ctk.CTkComboBox(self.settingsFrame, values=["SqLite3"])
        self.dbTypeCombo.set(config.get('SETTINGS', 'databasetype'))
        self.dbTypeCombo.pack(padx=20, pady=5)

        self.buttonFrame = ctk.CTkFrame(self.settingsFrame)
        self.buttonFrame.pack(pady=10)

        self.saveButton = ctk.CTkButton(self.buttonFrame, text="Αποθήκευση", command=lambda: self.__saveConfig())
        self.saveButton.pack(side="left", padx=10)

        self.resetButton = ctk.CTkButton(self.buttonFrame, text="Επαναφορά", command=lambda: self.__resetFields())
        self.resetButton.pack(side="left", padx=20)

        self.advancedTitleLabel = ctk.CTkLabel(self.settingsFrame,
                                        text="Προχωρημένες Ρυθμίσεις",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.advancedTitleLabel.pack(fill="x", pady=10, padx=20)

        self.advancedButtonFrame = ctk.CTkFrame(self.settingsFrame)
        self.advancedButtonFrame.pack(pady=10)

        self.resetDbButton = ctk.CTkButton(self.advancedButtonFrame, text="Αρχικοποίηση βάσης",
                                           command=lambda: self.__resetDatabase())
        self.resetDbButton.pack(side="left", padx=10)

        self.insertDataButton = ctk.CTkButton(self.advancedButtonFrame, text="Εισαγωγή δεδομένων απο web",
                                                 command=lambda: self.__importData(self.checkbox.get()))
        self.insertDataButton.pack(side="left", padx=10)

        # Το παρακάτω checkbox μας επιτρέπει να περιορίσουμε την εισαγωγή των δεδομένων
        # σύμφωνα με την εκφώνηση της εργασίας
        self.checkbox = ctk.CTkCheckBox(master=self.settingsFrame,
                                        text="Εισαγωγή μόνο 'Painting & Sculpture' & 'Media and Performance' τμήματα.",
                                        onvalue="yes", offvalue="no", variable=self.checkboxValue)
        self.checkbox.select("yes")
        self.checkbox.pack(padx=10, pady=10)

    @staticmethod
    def readConfig():
        """
        Διαβάζει της παραμέτρους της εφαρμογής
        :return:
        """
        config = configparser.ConfigParser()
        config.read(configLocation)
        return config

    def __saveConfig(self):
        """
        Ενημερώνει το αρχείο με της παραμέτρους της εφαρμογής
        :return: void
        """
        config = configparser.ConfigParser()
        config['SETTINGS'] = {
            'databasepath': self.dbPathEntry.get(),
            'webdataurl': self.webUrlEntry.get(),
            'databasetype': self.dbTypeCombo.get()
        }
        with open(self.configLocation, 'w') as configfile:
            config.write(configfile)
        return

    def __resetFields(self):
        """
        Επαναφέρει τα πεδία στις τιμές από το αρχείο της εφαρμογής
        :return:
        """
        config = self.readConfig()
        self.dbPathEntry.delete(0, ctk.END)
        self.dbPathEntry.insert(0, config.get('SETTINGS', 'databasepath'))
        self.webUrlEntry.delete(0, ctk.END)
        self.webUrlEntry.insert(0, config.get('SETTINGS', 'webdataurl'))
        self.dbTypeCombo.set(config.get('SETTINGS', 'databasetype'))
        return

    def __resetDatabase(self):
        """
        Αρχικοποίηση της βάσης με ανατροφοδότηση απο messageboxes
        :return:
        """
        response = messagebox.askyesno("MoMA Navigator",
                                       "Είστε σίγουρος πως θέλετε να κάνετε αρχικοποίηση της βάσης;\n"
                                       "Προσοχή! Όλα τα δεδομένα της θα διαγραφούν!")
        if response:
            self.settingsFrame.after(100, self.md.createDb())
            messagebox.showinfo("MoMA navigator", "Η διαδικασία ολοκληρώθηκε!")

    def __importData(self, value):
        """
        Εισαγωγή δεδομένων στη βάση με ανατροφοδότηση απο messageboxes
        :return:
        """
        response = messagebox.askyesno("MoMA Navigator",
                                           "Είστε σίγουρος πως θέλετε να κάνετε εισαγωγή δεδομένων στη βάση;\n"
                                           "Προσοχή! Η διαδικασία απαιτεί σύνδεση στο Διαδίκτυο και αρκετό χρόνο!")
        if response:
            self.settingsFrame.after(100, self.md.importData(value))
            messagebox.showinfo("MoMA navigator", "Η διαδικασία ολοκληρώθηκε!")
