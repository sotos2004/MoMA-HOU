from tkinter import messagebox
import customtkinter as ctk
import moma_class as mc


class InputFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)

        self.md = mc.MoMA()

        # Δημιουργία frame και widgets
        self.inputFrame = ctk.CTkFrame(container)
        self.inputFrame = ctk.CTkFrame(container, border_width=20)
        self.inputFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.inputFrame.columnconfigure(0, weight=1, uniform='input')
        self.inputFrame.rowconfigure(0, weight=1, uniform='input')
        self.inputFrame.rowconfigure(1, weight=1, uniform='input')
        self.inputFrame.rowconfigure(2, weight=2, uniform='input')
        self.inputFrame.rowconfigure(3, weight=3, uniform='input')
        self.inputFrame.rowconfigure(4, weight=1, uniform='input')
        self.inputFrame.rowconfigure(5, weight=1, uniform='input')
        self.inputFrame.rowconfigure(6, weight=1, uniform='input')

        self.titleLabel = ctk.CTkLabel(self.inputFrame,
                                        text="Εισαγωγή Δεδομένων",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.titleLabel.grid(row=0, column=0, columnspan=10, padx=20, pady=10, sticky="NWE")
        self.createInitialOptions()

        self.startOverBtn = ctk.CTkButton(self.inputFrame, text="Start Over", command=self.startOver)
        self.startOverBtn.grid(row=5, column=1, padx=15, pady=5)

    def createInitialOptions(self):
        # Option to select existing or new artist
        self.artistOption = ctk.StringVar(value="")
        self.artistLabel = ctk.CTkLabel(self.inputFrame, text="Καλλιτέχνης",
                                        anchor="e",
                                        font=("Arial", 14, "bold")
                                        )
        self.rbExisting = ctk.CTkRadioButton(self.inputFrame, text="Υπάρχων", variable=self.artistOption,
                                             value="existing", command=self.artistOptionChanged)
        self.rbNew = ctk.CTkRadioButton(self.inputFrame, text="Νέος", variable=self.artistOption, value="new",
                                        command=self.artistOptionChanged)

        self.artistLabel.grid(row=1, column=0)
        self.rbExisting.grid(row=1, column=2, padx=5, pady=5, )
        self.rbNew.grid(row=1, column=4, padx=5, pady=5, )

        self.artistEntryFrame = None
        self.artworkEntryFrame = None

    def startOver(self):
        self.inputFrame.destroy()
        self.__init__(self.parent)

    def artistOptionChanged(self):
        option = self.artistOption.get()
        if self.artistEntryFrame:
            self.artistEntryFrame.destroy()

        if self.artworkEntryFrame:
            self.artworkEntryFrame.destroy()

        if option == "new":
            self.showNewArtistFields()
        else:
            self.showExistingArtistSelection()

    def showNewArtistFields(self):
        if self.artistEntryFrame:
            self.artistEntryFrame.destroy()
            
        self.artistEntryFrame = ctk.CTkFrame(self.inputFrame)
        self.artistEntryFrame.grid(row=2, column=0, columnspan=3, rowspan=5, pady=10)

        ctk.CTkLabel(self.artistEntryFrame,
                     text="Στοιχεία Νέου Καλλιτέχνη",
                     font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        ctk.CTkLabel(self.artistEntryFrame, text="Όνομα:").grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artistEntryFrame, text="Βιογραφία:").grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artistEntryFrame, text="Εθνικότητα:").grid(row=3, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artistEntryFrame, text="Φύλο").grid(row=4, column=0, padx=5, pady=5)

        ctk.CTkLabel(self.artistEntryFrame, text="Από:").grid(row=1, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artistEntryFrame, text="Έως:").grid(row=2, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artistEntryFrame, text="Wiki QID:").grid(row=3, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artistEntryFrame, text="ULAN").grid(row=4, column=2, padx=5, pady=5)

        self.displayNameEntry = ctk.CTkEntry(self.artistEntryFrame)
        self.artistBioEntry = ctk.CTkEntry(self.artistEntryFrame)
        self.nationalityMappings = self.md.getNationalities()
        self.nationalityMappings[0] = ' None'
        self.nationalities = sorted(list(self.nationalityMappings.values()))
        self.nationalityIDEntry = ctk.CTkComboBox(self.artistEntryFrame,
                                                  values=self.nationalities,
                                                  state="readonly",
                                                  width=140,
                                                  height=20, )
        self.genderEntry = ctk.CTkComboBox(self.artistEntryFrame,
                                           values=['male', 'female'],
                                           state="readonly",
                                           width=140,
                                           height=20, )

        self.beginDateEntry = ctk.CTkEntry(self.artistEntryFrame)
        self.endDateEntry = ctk.CTkEntry(self.artistEntryFrame)
        self.wikiQidEntry = ctk.CTkEntry(self.artistEntryFrame)
        self.ulanEntry = ctk.CTkEntry(self.artistEntryFrame)

        self.displayNameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.artistBioEntry.grid(row=2, column=1, padx=5, pady=5)
        self.nationalityIDEntry.grid(row=3, column=1, padx=5, pady=5)
        self.genderEntry.grid(row=4, column=1, padx=5, pady=5)

        self.beginDateEntry.grid(row=1, column=3, padx=5, pady=5)
        self.endDateEntry.grid(row=2, column=3, padx=5, pady=5)
        self.wikiQidEntry.grid(row=3, column=3, padx=5, pady=5)
        self.ulanEntry.grid(row=4, column=3, padx=5, pady=5)

        self.submitArtistBtn = ctk.CTkButton(self.artistEntryFrame, text="Υποβολή", command=self.submitArtistData)
        self.submitArtistBtn.grid(row=5, column=0, columnspan=4, pady=10)

    def showExistingArtistSelection(self):
        if self.artistEntryFrame:
            self.artistEntryFrame.destroy()

        artists = self.md.getArtists(fields=" ConstituentID, DisplayName ", query=" 1=1 limit 5 ")
        self.artistsMappings = dict(zip(artists['ConstituentID'], artists['DisplayName']))
        self.artistsMappings[0] = ' None'
        self.artists = sorted(list(self.artistsMappings.values()))

        self.artistEntryFrame = ctk.CTkFrame(self.inputFrame)
        self.artistEntryFrame.grid(row=2, column=0, columnspan=3, rowspan=1, pady=10)

        ctk.CTkLabel(self.artistEntryFrame, text="Επιλογή Καλλιτέχνη:").grid(row=0, column=0, padx=5, pady=5)
        self.artistCombobox = ctk.CTkComboBox(self.artistEntryFrame, values=self.artists)
        self.artistCombobox.grid(row=0, column=1, padx=5, pady=5)

        self.submitArtistBtn = ctk.CTkButton(self.artistEntryFrame,
                                             text="Επιλογή Καλλιτέχνη",
                                             command=self.submitArtistData)
        self.submitArtistBtn.grid(row=1, column=0, columnspan=2, pady=10)

    def submitArtistData(self):
        option = self.artistOption.get()
        if option == "new":
            displayName = self.displayNameEntry.get()
            if displayName == '':
                messagebox.showinfo('MoMA Navigator',
                                    'Το όνομα του καλλιτέχνη είναι υποχρεωτικό.\nΠροσπαθήστε ξανά!')
                return
            # Capture new artist data
            artistData = {
                "DisplayName": displayName,
                "ArtistBio": self.artistBioEntry.get(),
                "NationalityID": self.get_key(self.nationalityIDEntry.get(), self.nationalityMappings),
                "Gender": self.genderEntry.get(),
                "BeginDate": self.beginDateEntry.get(),
                "EndDate": self.endDateEntry.get(),
                "WikiQID": self.wikiQidEntry.get(),
                "ULAN": self.ulanEntry.get(),
            }
            self.selectedArtist = self.md.insertArtist(artistData)
            if self.selectedArtist is False:
                del self.selectedArtist
                self.showNewArtistFields()
                return
            messagebox.showinfo('MoMA Navigator', 'Επιτυχής εισαγωγή Καλλιτέχνη.')
            print("New artist data:", artistData)
        else:
            self.selectedArtist = self.artistCombobox.get()
            print("Selected existing artist:", self.selectedArtist)

        # Clear artist entry frame and show artwork entry fields
        self.artistEntryFrame.destroy()
        self.showArtworkFields()

    def showArtworkFields(self):
        if self.artworkEntryFrame:
            self.artworkEntryFrame.destroy()

        self.artworkEntryFrame = ctk.CTkFrame(self.inputFrame)
        self.artworkEntryFrame.grid(row=1, column=0, columnspan=4, rowspan=10, pady=10)
        ctk.CTkLabel(self.artworkEntryFrame,
                     text="Στοιχεία Νέου Έργου",
                     font=("Arial", 14, "bold")).grid(row=0, column=0, padx=5, pady=5)

        ctk.CTkLabel(self.artworkEntryFrame, text="Τίτλος:").grid(row=1, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Διαστάσεις").grid(row=2, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Credit Line:").grid(row=3, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Accession Number:").grid(row=4, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Έτος απόκτησης:").grid(row=5, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Καταγεγραμμένο:").grid(row=6, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="URL:").grid(row=7, column=0, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Έτος έργου:").grid(row=8, column=0, padx=5, pady=5)

        ctk.CTkLabel(self.artworkEntryFrame, text="URL Εικόνας:").grid(row=1, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Περίμετρος:").grid(row=2, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Βάθος:").grid(row=3, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Διάμετρος:").grid(row=4, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Ύψος:").grid(row=5, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Μήκος:").grid(row=6, column=2, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Βάρος:").grid(row=7, column=2, padx=5, pady=5)

        ctk.CTkLabel(self.artworkEntryFrame, text="Πλάτος:").grid(row=1, column=4, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Ύψος Βάσης:").grid(row=2, column=4, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Διάρκεια:").grid(row=3, column=4, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Μέσο:").grid(row=4, column=4, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Κατηγοριοποίηση:").grid(row=5, column=4, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Τμήμα:").grid(row=6, column=4, padx=5, pady=5)
        ctk.CTkLabel(self.artworkEntryFrame, text="Παρουσίαση:").grid(row=7, column=4, padx=5, pady=5)

        self.classificationMappings = self.md.getClassifications()
        self.classificationMappings[0] = ' None'
        self.classification = sorted(list(self.classificationMappings.values()))

        self.departmentMappings = self.md.getDepartments()
        self.departmentMappings[0] = ' None'
        self.department = sorted(list(self.departmentMappings.values()))

        self.onViewMappings = self.md.getOnviews()
        self.onViewMappings[0] = ' None'
        self.onView = sorted(list(self.onViewMappings.values()))

        self.titleEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.dimenssionsEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.creditLineEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.accessionNumberEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.dateAcquiredEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.cataloguedCombobox = ctk.CTkComboBox(self.artworkEntryFrame, values=["Ναι", "'Οχι'",])
        self.urlEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.imageUrlEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.circumferenceEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.depthEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.diameterEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.heightEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.lengthEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.weightEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.widthEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.seatHeightEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.durationEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.mediumEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.classificationCombobox = ctk.CTkComboBox(self.artworkEntryFrame,
                                                      values=self.classification,
                                                      state="readonly",
                                                      width=140,
                                                      height=20, )
        self.departmentCombobox = ctk.CTkComboBox(self.artworkEntryFrame,
                                                  values=self.department,
                                                  state="readonly",
                                                  width=140,
                                                  height=20, )
        self.onViewCombobox = ctk.CTkComboBox(self.artworkEntryFrame,
                                              values=self.onView,
                                              state="readonly",
                                              width=140,
                                              height=20, )

        self.dateEntry = ctk.CTkEntry(self.artworkEntryFrame)

        self.titleEntry.grid(row=1, column=1, padx=5, pady=5)
        self.dimenssionsEntry.grid(row=2, column=1, padx=5, pady=5)
        self.creditLineEntry.grid(row=3, column=1, padx=5, pady=5)
        self.accessionNumberEntry.grid(row=4, column=1, padx=5, pady=5)
        self.dateAcquiredEntry.grid(row=5, column=1, padx=5, pady=5)
        self.cataloguedCombobox.grid(row=6, column=1, padx=5, pady=5)
        self.urlEntry.grid(row=7, column=1, padx=5, pady=5)
        self.dateEntry.grid(row=8, column=1, padx=5, pady=5)

        self.imageUrlEntry.grid(row=1, column=3, padx=5, pady=5)
        self.circumferenceEntry.grid(row=2, column=3, padx=5, pady=5)
        self.depthEntry.grid(row=3, column=3, padx=3, pady=5)
        self.diameterEntry.grid(row=4, column=3, padx=5, pady=5)
        self.heightEntry.grid(row=5, column=3, padx=5, pady=5)
        self.lengthEntry.grid(row=6, column=3, padx=5, pady=5)
        self.weightEntry.grid(row=7, column=3, padx=5, pady=5)

        self.widthEntry.grid(row=1, column=5, padx=5, pady=5)
        self.seatHeightEntry.grid(row=2, column=5, padx=5, pady=5)
        self.durationEntry.grid(row=3, column=5, padx=5, pady=5)
        self.mediumEntry.grid(row=4, column=5, padx=5, pady=5)
        self.classificationCombobox.grid(row=5, column=5, padx=5, pady=5)
        self.departmentCombobox.grid(row=6, column=5, padx=5, pady=5)
        self.onViewCombobox.grid(row=7, column=5, padx=5, pady=5)

        self.submitArtworkBtn = ctk.CTkButton(self.artworkEntryFrame,
                                              text="Υποβολή έργου",
                                              command=self.submitArtworkData)
        self.submitArtworkBtn.grid(row=8, column=0, columnspan=6, pady=10)

    def submitArtworkData(self):
        title = self.titleEntry.get()
        if title == '':
            messagebox.showinfo('MoMA Navigator',
                                'Το όνομα του έργου είναι υποχρεωτικό.\nΠροσπαθήστε ξανά!')
            return

        artworkData = {
            "Title": title,
            "Dimenssion": self.dimenssionsEntry.get(),
            "CreditLine": self.creditLineEntry.get(),
            "AccesionNumber": self.accessionNumberEntry.get(),
            "DateAcquired": self.dateAcquiredEntry.get(),
            "Catalogued":   "Y" if self.cataloguedCombobox.get() == 'Ναι' else "N",
            "URL": self.urlEntry.get(),
            "ImageURL": self.imageUrlEntry.get(),
            "Circumference": self.circumferenceEntry.get(),
            "Depth": self.depthEntry.get(),
            "Diameter": self.diameterEntry.get(),
            "Height": self.heightEntry.get(),
            "Length": self.lengthEntry.get(),
            "Weight": self.weightEntry.get(),
            "Width": self.widthEntry.get(),
            "SeatHeight": self.seatHeightEntry.get(),
            "Duration": self.durationEntry.get(),
            "Medium": self.mediumEntry.get(),
            "Classification": self.get_key(self.classificationCombobox.get(), self.classificationMappings),
            "Department": self.get_key(self.departmentCombobox.get(), self.departmentMappings),
            "OnView": self.get_key(self.onViewCombobox.get(), self.onViewMappings),
            "Date": self.dateEntry.get(),
            "ConstituentID": self.get_key(self.selectedArtist, self.artistsMappings),
        }
        result = self.md.insertArtwork(artworkData)
        if not result:
            del self.selectedArtist
            self.createInitialOptions()
            return
        messagebox.showinfo('MoMA Navigator', 'Επιτυχής εισαγωγή Έργου.')
        if self.artistEntryFrame:
            self.artistEntryFrame.destroy()
        if self.artworkEntryFrame:
            self.artworkEntryFrame.destroy()
        self.createInitialOptions()

        print("New artist data:", artworkData)

    @staticmethod
    def get_key(val, dictionary):
        for key, value in dictionary.items():
            if val == value:
                return key
        return None
