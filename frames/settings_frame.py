from tkinter import messagebox
import customtkinter as ctk
import configparser
import os

class SettingsFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configLocation = 'DATA/config.ini'
        self.settingsFrame = ctk.CTkFrame(container, border_width=20)
        self.settingsFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.settingsFrame.columnconfigure(0, weight=1, uniform = 'f3')
        self.settingsFrame.rowconfigure(0, weight=1, uniform = 'f3')

        self.title_label = ctk.CTkLabel(self.settingsFrame, text="Ρυθμίσεις", anchor="center",font=("Arial", 16, "bold"))
        self.title_label.pack(fill="x", pady=5, padx=20)

        self.dbPathLabel = ctk.CTkLabel(self.settingsFrame, text="Τοποθεσία Βάσης")
        self.dbPathLabel.pack( padx=20)
        self.dbPathEntry = ctk.CTkEntry(self.settingsFrame, width=300)
        self.dbPathEntry.pack(padx=20, pady=5)

        self.webUrlLabel = ctk.CTkLabel(self.settingsFrame, text="Τοποθεσία διαδικτύου (Url)")
        self.webUrlLabel.pack( padx=20)
        self.webUrlEntry = ctk.CTkEntry(self.settingsFrame, width=300)
        self.webUrlEntry.pack(padx=20, pady=5)

        self.dbTypeLabel = ctk.CTkLabel(self.settingsFrame, text="Είδος Βάσης Δεδομένων")
        self.dbTypeLabel.pack(padx=20)
        self.dbTypeCombo = ctk.CTkComboBox(self.settingsFrame, values=["SqLite3", "MySQL"])
        self.dbTypeCombo.pack(padx=20, pady=5)

        self.buttonFrame = ctk.CTkFrame(self.settingsFrame)
        self.buttonFrame.pack(pady=10)
        self.saveButton = ctk.CTkButton(self.buttonFrame, text="Save", command=self.saveConfig())
        self.saveButton.pack(side="left", padx=10)
        self.resetButton = ctk.CTkButton(self.buttonFrame, text="Reset", command=self.resetFields())
        self.resetButton.pack(side="left", padx=10)

        self.__resetFields()

    def readConfig(self):
        config = configparser.ConfigParser()
        if not os.path.exists(self.configLocation):
            config['SETTINGS'] = {
                'databasepath': '',
                'webdataurl': '',
                'databasetype': 'SqLite3'
            }
            with open(self.configLocation, 'w') as configFile:
                config.write(configFile)
        else:
            config.read(self.configLocation)
            print('read')
            print(config['SETTINGS']['databasepath'])
            print(config['SETTINGS']['databasepath'])
        return config

    def __saveConfig(self):
        config = configparser.ConfigParser()
        config['SETTINGS'] = {
            'databasepath': self.dbPathEntry.get(),
            'webdataurl': self.webUrlEntry.get(),
            'databasetype': self.dbTypeCombo.get()
        }
        print(self.webUrlEntry.get())
        print(config['SETTINGS']['databasetype'])
        with open(self.configLocation, 'w') as configfile:
            config.write(configfile)
            #messagebox.showinfo('ΜoMA Navigator for EAP-2024','Επιτυχής ενημέρωση')
    def __resetFields(self):
        config = self.readConfig()
        print(config['SETTINGS']['databasePath'])
        self.dbPathEntry.delete(0, ctk.END)
        self.dbPathEntry.insert(0, config['SETTINGS']['databasepath'])
        self.webUrlEntry.delete(0, ctk.END)
        self.webUrlEntry.insert(0, config['SETTINGS']['webdataurl'])
        self.dbTypeCombo.set(config['SETTINGS']['databasetype'])

