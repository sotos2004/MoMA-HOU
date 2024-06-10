import tkinter.messagebox
from tkinter import messagebox
import customtkinter as ctk
import moma_class as mc


class InputFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)

        # για χρήση της κλάσης για ενημέρωση/διαγραφή εγγραφής
        if 'type' in kwargs:
            self.type = kwargs["type"]
            if 'id' in kwargs:
                self.id = kwargs["id"]
            else:
                # αν δεν έχουμε και τις δύο παραμέτρους
                self.type = "new"
                self.id = 0
                tkinter.messagebox.showerror('MoMA Navigator', '''Πρόβλημα κατά την επεξεργασία δεδομένων.\n
                                                                            Προσπαθήστε ξανά.''')
        else:
            self.type = "new"
            self.id = 0

        # test values
        # self.type = 'artist'
        # self.type = 'artwork'
        # self.id = 137136
        # self.id = 471830

        self.parent = container
        
        self.md = mc.MoMA()
        # παίρνουμε τα δεδομένα των Καλλιτεχνών από τη βάση
        artists = self.md.getArtists(fields=" ConstituentID, DisplayName ")
        self.artistsMappings = dict(zip(artists['ConstituentID'], artists['DisplayName']))
        self.artistsMappings[0] = ' None'

        # Δημιουργία frame και widgets
        self.artistOption = ctk.StringVar(value="")
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

        match self.type:
            case "artwork":
                self.__showArtworkFields(id=self.id)
            case "artist":
                self.__showNewArtistFields(id=self.id)
            case _:
                self.__createInitialOptions()
                self.__startOverBtn = ctk.CTkButton(self.inputFrame,
                                                    text="Επανεκκίνηση διεργασίας",
                                                    command=self.__startOver)
                self.__startOverBtn.grid(row=5, column=1, rowspan=3, padx=15, pady=25, sticky="S")

    def __createInitialOptions(self):
        """
        Επιλογή υπάρχοντος καλλιτέχνη ή νέου
        """
        self.artistOption = ctk.StringVar(value="")
        self.artistLabel = ctk.CTkLabel(self.inputFrame, text="Καλλιτέχνης",
                                        anchor="e",
                                        font=("Arial", 14, "bold")
                                        )
        self.rbExisting = ctk.CTkRadioButton(self.inputFrame,
                                             text="Υπάρχων",
                                             variable=self.artistOption,
                                             value="existing",
                                             command=self.__artistOptionChanged)
        self.rbNew = ctk.CTkRadioButton(self.inputFrame,
                                        text="Νέος",
                                        variable=self.artistOption,
                                        value="new",
                                        command=self.__artistOptionChanged)

        self.artistLabel.grid(row=1, column=0, sticky="W", padx=30)
        self.rbExisting.grid(row=1, column=1, padx=5, pady=5, sticky="W")
        self.rbNew.grid(row=1, column=2, padx=30, pady=5, sticky="W")

        self.artistEntryFrame = None
        self.artworkEntryFrame = None

    def __artistOptionChanged(self):
        """
        Εμφάνιση αντίστοιχου frame ανάλογα την επιλογή
        """
        option = self.artistOption.get()
        if self.artistEntryFrame:
            self.artistEntryFrame.destroy()

        if self.artworkEntryFrame:
            self.artworkEntryFrame.destroy()

        if option == "new":
            self.__showNewArtistFields()
        else:
            self.__showExistingArtistSelection()

    def __showNewArtistFields(self, **kwargs):
        """
        Εμφάνιση πεδίων για εισαγωγή νέου καλλιτέχνη
        """
        # αν υπάρχει ήδη το frame το κάνουμε reset
        try:
            if self.artistEntryFrame:
                self.artistEntryFrame.destroy()
        except Exception as e:
            pass

        self.artistEntryFrame = ctk.CTkFrame(self.inputFrame)
        self.artistEntryFrame.grid(row=2, column=0, columnspan=3, rowspan=5, pady=10)

        # Δημιουργία widgets
        ctk.CTkLabel(self.artistEntryFrame,
                     text="Στοιχεία Νέου Καλλιτέχνη" if self.id == 0 else "Επεξεργασία Καλλιτέχνη",
                     font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        ctk.CTkLabel(self.artistEntryFrame, text="Όνομα:").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artistEntryFrame, text="Βιογραφία:").grid(row=2, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artistEntryFrame, text="Εθνικότητα:").grid(row=3, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artistEntryFrame, text="Φύλο").grid(row=4, column=0, padx=5, pady=5, sticky="E")

        ctk.CTkLabel(self.artistEntryFrame, text="Από:").grid(row=1, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artistEntryFrame, text="Έως:").grid(row=2, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artistEntryFrame, text="Wiki QID:").grid(row=3, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artistEntryFrame, text="ULAN").grid(row=4, column=2, padx=5, pady=5, sticky="E")

        self.displayNameEntry = ctk.CTkEntry(self.artistEntryFrame)
        self.artistBioEntry = ctk.CTkEntry(self.artistEntryFrame)

        # παίρνουμε τα δεδομένα των Nationalities από τη βάση
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

        if self.id == 0:
            colspan = 4
        else:
            colspan = 2
            artistData = self.md.getArtists(query=" constituentID = " + str(self.id))
            artistData.fillna('', inplace=True)
            print(':::::', artistData.loc[0,'Nationality'])
            print("Column names:", artistData.columns)
            #  print(type(artistData.loc[0,'Circumeferance']))
            # print(artistData.loc[0, 'Classification'])

            self.displayNameEntry.insert(0, artistData.loc[0, 'DisplayName'])
            self.artistBioEntry.insert(0, artistData.loc[0, 'ArtistBio'])
            self.nationalityIDEntry.set(artistData.loc[0, 'Nationality'])
            self.genderEntry.set(artistData.loc[0, 'Gender'])

            self.beginDateEntry.insert(0, artistData.loc[0, 'BeginDate'])
            self.endDateEntry.insert(0, artistData.loc[0, 'EndDate'])
            self.wikiQidEntry.insert(0, artistData.loc[0, 'WikiQID'])
            self.ulanEntry.insert(0, artistData.loc[0, 'ULAN'])

        self.submitArtistBtn = ctk.CTkButton(self.artistEntryFrame,
                                              text="Αποθήκευση Καλλιτέχνη",
                                              command=self.__submitArtistData)
        self.submitArtistBtn.grid(row=5, column=0, columnspan=colspan, pady=5, padx=5, sticky="E")

        def __deleteArtist(artistid):
            print(artistid)
            if messagebox.askyesno('MoMA Navigator', '''Είστε σίγουρος πως θέλετε να διαγράψετε τον καλλιτέχνη;'''):
                result = self.md.deleteArtist(artistid)
                if result:
                    messagebox.showinfo('MoMA Navigator',
                                        '''Επιτυχής διαγραφή του καλλιτέχνη!''')
                    self.id = 0
                    self.type = 'new'
                    self.__startOver()

        if self.id != 0:
            print(self.id)
            self.deleteArtworkBtn = ctk.CTkButton(self.artistEntryFrame,
                                                  text="Διαγραφή καλλιτέχνη")
            self.deleteArtworkBtn.bind("<Button-1>",
                                       lambda event: __deleteArtist(self.id))
            self.deleteArtworkBtn.grid(row=5, column=3, columnspan=colspan, pady=5, padx=5, sticky="E")

    def __showExistingArtistSelection(self):
        """
        Εμφάνιση πεδίων για επιλογή υπάρχοντος καλλιτέχνη
        """
        # αν υπάρχει ήδη το frame το κάνουμε reset
        if self.artistEntryFrame:
            self.artistEntryFrame.destroy()

        self.artists = sorted(list(self.artistsMappings.values()))

        self.artistEntryFrame = ctk.CTkFrame(self.inputFrame)
        self.artistEntryFrame.grid(row=2, column=0, columnspan=3, rowspan=1, pady=10)

        ctk.CTkLabel(self.artistEntryFrame, text="Επιλογή Καλλιτέχνη:").grid(row=0, column=0, padx=5, pady=5)
        self.artistCombobox = ctk.CTkComboBox(self.artistEntryFrame, values=self.artists)

        # καθώς η λίστα των καλλιτεχνών είναι τεράστια, προσθέτουμε ένα γεγονός
        # που φιλτράρει τη λίστα καθώς πληκτρολογούμε
        self.artistCombobox.bind("<KeyRelease>",
                                 lambda event: self.filterComboBox(self.artistCombobox, self.artists))

        self.artistCombobox.grid(row=0, column=1, padx=5, pady=5)

        self.submitArtistBtn = ctk.CTkButton(self.artistEntryFrame,
                                             text="Επιλογή Καλλιτέχνη",
                                             command=self.__submitArtistData)
        self.submitArtistBtn.grid(row=1, column=0, columnspan=2, pady=10)

    def __submitArtistData(self):
        """
        Υποβολή πεδίων για εισαγωγή νέου καλλιτέχνη στη βάση
        """

        if self.id != 0 :
            ConstituentID = self.getKey(self.id, self.artistsMappings)
        # else:
        #    ConstituentID = self.getKey(self.artistCombobox.get(), self.artistsMappings)
        try:
            option = self.artistOption.get()
        except Exception as e:
            option="new"

        if option == "new" or self.type == 'artist':
            displayName = self.displayNameEntry.get()
            # Έλεγχοι για τα πεδία
            # TODO: επιπλέων έλεγχοι για των τύπο των υπόλοιπων πεδίων
            if displayName == '':
                messagebox.showinfo('MoMA Navigator',
                                    'Το όνομα του καλλιτέχνη είναι υποχρεωτικό.\nΠροσπαθήστε ξανά!')
                return
            # Λεξικό που περιέχει τα δεδομένα που θα σταλούν στη βάση
            try:
                cId = self.selectedArtist
            except Exception as e:
                cId = self.id
            artistData = {
                "DisplayName": displayName,
                "ArtistBio": self.artistBioEntry.get(),
                "NationalityID": self.getKey(self.nationalityIDEntry.get(), self.nationalityMappings),
                "Gender": self.genderEntry.get(),
                "BeginDate": self.beginDateEntry.get(),
                "EndDate": self.endDateEntry.get(),
                "WikiQID": self.wikiQidEntry.get(),
                "ULAN": self.ulanEntry.get(),
                "id": self.id ,
                "ConstituentID": cId
            }
            # αποστολή στη βάση
            self.selectedArtist = self.md.insertArtist(artistData)
            # έλεγχος αποτελέσματος
            if self.selectedArtist is False:
                del self.selectedArtist
                self.__showNewArtistFields()
                return
            # ενημέρωση του χρήστη για επιτυχία εγγραφής - σε περίπτωση αποτυχίας έχει ενημερωθεί ο χρήστης
            # από την self.md.insertArtist(artistData) παραπάνω
            messagebox.showinfo('MoMA Navigator', 'Επιτυχής εισαγωγή Καλλιτέχνη.')
        else:
            # Υπάρχον καλλιτέχνης
            self.selectedArtist = self.artistCombobox.get()

        # Εκκαθάριση πεδίων καλλιτέχνη και εμφάνιση πεδίων έργου
        if self.type == "new":
            self.artistEntryFrame.destroy()
            self.__showArtworkFields()
        else:
            self.__startOver()

    def __showArtworkFields(self, **kwargs):
        """
        Εμφάνιση πεδίων για εισαγωγή νέου έργου
        """
        # αν υπάρχει ήδη το frame το κάνουμε reset
        try:
            if self.artworkEntryFrame:
                self.artworkEntryFrame.destroy()
        except Exception as e:
            pass
        # δημιουργία widgets
        self.artworkEntryFrame = ctk.CTkFrame(self.inputFrame)
        self.artworkEntryFrame.grid(row=1, column=0, columnspan=4, rowspan=10, pady=10)
        ctk.CTkLabel(self.artworkEntryFrame,
                     text="Στοιχεία Νέου Έργου" if self.id == 0 else "Επεξεργασία έργου",
                     font=("Arial", 14, "bold")).grid(row=0, column=0, padx=5, pady=5)

        ctk.CTkLabel(self.artworkEntryFrame, text="Τίτλος:").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Διαστάσεις").grid(row=2, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Credit Line:").grid(row=3, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Accession Number:").grid(row=4, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Έτος απόκτησης:").grid(row=5, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Καταγεγραμμένο:").grid(row=6, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="URL:").grid(row=7, column=0, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Έτος έργου:").grid(row=8, column=0, padx=5, pady=5, sticky="E")

        ctk.CTkLabel(self.artworkEntryFrame, text="URL Εικόνας:").grid(row=1, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Περίμετρος:").grid(row=2, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Βάθος:").grid(row=3, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Διάμετρος:").grid(row=4, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Ύψος:").grid(row=5, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Μήκος:").grid(row=6, column=2, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Βάρος:").grid(row=7, column=2, padx=5, pady=5, sticky="E")

        ctk.CTkLabel(self.artworkEntryFrame, text="Πλάτος:").grid(row=1, column=4, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Ύψος Βάσης:").grid(row=2, column=4, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Διάρκεια:").grid(row=3, column=4, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Μέσο:").grid(row=4, column=4, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Κατηγοριοποίηση:").grid(row=5, column=4, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Τμήμα:").grid(row=6, column=4, padx=5, pady=5, sticky="E")
        ctk.CTkLabel(self.artworkEntryFrame, text="Παρουσίαση:").grid(row=7, column=4, padx=5, pady=5, sticky="E")

        # λίστες για τα ComboBoxes από τη βάση
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
        self.cataloguedCombobox = ctk.CTkComboBox(self.artworkEntryFrame, values=["Ναι", "Οχι",])
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
        self.dateEntry = ctk.CTkEntry(self.artworkEntryFrame)
        self.classificationCombobox = ctk.CTkComboBox(self.artworkEntryFrame,
                                                      values=self.classification,
                                                      width=140,
                                                      height=20, )
        self.departmentCombobox = ctk.CTkComboBox(self.artworkEntryFrame,
                                                  values=self.department,
                                                  width=140,
                                                  height=20, )
        self.onViewCombobox = ctk.CTkComboBox(self.artworkEntryFrame,
                                              values=self.onView,
                                              width=140,
                                              height=20, )

        # Προσθήκη δυνατότητας φιλτραρίσματος
        self.classificationCombobox.bind("<KeyRelease>",
                                 lambda event: self.filterComboBox(self.classificationCombobox, self.classification))
        self.departmentCombobox.bind("<KeyRelease>",
                                 lambda event: self.filterComboBox(self.departmentCombobox, self.department))
        self.onViewCombobox.bind("<KeyRelease>",
                                 lambda event: self.filterComboBox(self.onViewCombobox, self.onView))

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

        if self.id == 0:
            colspan = 4
        else:
            colspan = 2
            artworkData = self.md.getArtworks(query=" objectID = " + str(self.id))
            artworkData.fillna('', inplace=True)
            print(artworkData)
            print("Column names:", artworkData.columns)
            #  print(type(artistData.loc[0,'Circumeferance']))
            print(artworkData.loc[0, 'Classification'])

            self.titleEntry.insert(0, artworkData.loc[0, 'Title'])
            self.dimenssionsEntry.insert(0, artworkData.loc[0, 'Dimenssions'])
            self.creditLineEntry.insert(0, artworkData.loc[0, 'CreditLine'])
            self.accessionNumberEntry.insert(0, artworkData.loc[0, 'AccessionNumber'])
            self.dateAcquiredEntry.insert(0, artworkData.loc[0, 'DateAcquired'])
            self.cataloguedCombobox.set("Ναι" if artworkData.loc[0, 'Catalogued'] == "Y" else "Όχι")
            self.urlEntry.insert(0, artworkData.loc[0, 'URL'])
            self.imageUrlEntry.insert(0, artworkData.loc[0, 'ImageURL'])
            self.circumferenceEntry.insert(0, artworkData.loc[0, 'Circumeferance'])
            self.depthEntry.insert(0, artworkData.loc[0, 'Depth'])
            self.diameterEntry.insert(0, artworkData.loc[0, 'Diameter'])
            self.heightEntry.insert(0, artworkData.loc[0, 'Height'])
            self.lengthEntry.insert(0, artworkData.loc[0, 'Length'])
            self.weightEntry.insert(0, artworkData.loc[0, 'Weight'])
            self.widthEntry.insert(0, artworkData.loc[0, 'Width'])
            self.seatHeightEntry.insert(0, artworkData.loc[0, 'SeatHeight'])
            self.durationEntry.insert(0, artworkData.loc[0, 'Duration'])
            self.mediumEntry.insert(0, artworkData.loc[0, 'Medium'])
            self.dateEntry.insert(0, artworkData.loc[0, 'Date'])
            self.classificationCombobox.set(artworkData.loc[0, 'Department'])
            self.departmentCombobox.set(artworkData.loc[0, 'Classification'])
            self.onViewCombobox.set(artworkData.loc[0, 'OnView'])

        self.submitArtworkBtn = ctk.CTkButton(self.artworkEntryFrame,
                                              text="Αποθήκευση έργου",
                                              command=self.__submitArtworkData)
        self.submitArtworkBtn.grid(row=8, column=3, columnspan=colspan, pady=5, padx=5, sticky="E")

        def __deleteArtwork(artworkid):
            if messagebox.askyesno('MoMA Navigator', '''Είστε σίγουρος πως θέλετε να διαγράψετε το έργο;'''):
                result = self.md.deleteArtwork(artworkid)
                if result:
                    messagebox.showinfo('MoMA Navigator',
                                        '''Επιτυχής διαγραφή του έργου!''')
                    self.id = 0
                    self.type = 'new'
                    self.__startOver()

        if self.id != 0:
            print(self.id)
            self.deleteArtworkBtn = ctk.CTkButton(self.artworkEntryFrame,
                                                  text="Διαγραφή έργου")
            self.deleteArtworkBtn.bind("<Button-1>",
                                     lambda event: __deleteArtwork(self.id))
            self.deleteArtworkBtn.grid(row=8, column=5, columnspan=colspan, pady=5, padx=5, sticky="E")

    def __submitArtworkData(self):
        """
        Υποβολή πεδίων για εισαγωγή νέου έργου στη βάση
        """
        title = self.titleEntry.get()
        # Έλεγχοι για τα πεδία
        # TODO: επιπλέων έλεγχοι για των τύπο των υπόλοιπων πεδίων
        if title == '':
            messagebox.showinfo('MoMA Navigator',
                                'Το όνομα του έργου είναι υποχρεωτικό.\nΠροσπαθήστε ξανά!')
            return
        if self.id != 0:
            ConstituentID = self.getKey(self.id, self.artistsMappings)
        else:
            ConstituentID = self.getKey(self.selectedArtist, self.artistsMappings)
        print(ConstituentID)
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
            "Classification": self.getKey(self.classificationCombobox.get(), self.classificationMappings),
            "Department": self.getKey(self.departmentCombobox.get(), self.departmentMappings),
            "OnView": self.getKey(self.onViewCombobox.get(), self.onViewMappings),
            "Date": self.dateEntry.get(),
            "ConstituentID": ConstituentID,
            "id": self.id
        }
        # αποστολή δεδομένων στη βάση
        result = self.md.insertArtwork(artworkData)
        if not result:
            del self.selectedArtist
            self.__createInitialOptions()
            return
        # ενημέρωση του χρήστη για επιτυχία εγγραφής - σε περίπτωση αποτυχίας έχει ενημερωθεί ο χρήστης
        # από την self.md.insertArtwork(artworkData) παραπάνω
        messagebox.showinfo('MoMA Navigator', 'Επιτυχής εισαγωγή Έργου.')

        # Εκκαθάριση frame για να συνεχίσει ο χρήστης
        self.__startOver()
        try:
            if self.artistEntryFrame:
                self.artistEntryFrame.destroy()
            if self.artworkEntryFrame:
                self.artworkEntryFrame.destroy()
        except Exception as e:
            pass

        self.__createInitialOptions()

    def __startOver(self):
        """
        Εκκαθάριση φόρμας
        """
        self.inputFrame.destroy()
        self.__init__(self.parent)

    @staticmethod
    def getKey(val, dictionary):
        """
        Κλειδί από τιμή λεξικού - χρησιμοποιήται στη μετατροπή για εισαγωγή του κλειδιού στη βάση
        """
        for key, value in dictionary.items():
            if val == value:
                return key
        return None

    @staticmethod
    def filterComboBox(widget, listitems):
        """
        Φιλτράρει τη λίστα ενός ComboBox καθώς πληκτρολογούμε
        """
        filterText = widget.get().lower()
        filteredList = [val for val in listitems if filterText in val.lower()]
        widget.configure(values=filteredList)
