import customtkinter as ctk
from tkinter import ttk
import moma_class as mc
from frames.input_frame import InputFrame
from frames.start_frame import StartFrame


class SearchFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)

        self.startFrame = StartFrame
        self.inputFrame = InputFrame
        self.md = mc.MoMA()
        self.parent = container
        # Δημιουργία frame και widgets
        self.searchFrame = ctk.CTkFrame(container, border_width=10)
        self.searchFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.searchFrame.columnconfigure(0, weight=1, uniform='search')
        self.searchFrame.rowconfigure(0, weight=1, uniform='search')
        self.searchFrame.rowconfigure(1, weight=1, uniform='search')
        self.searchFrame.rowconfigure(2, weight=1, uniform='search')
        self.searchFrame.rowconfigure(3, weight=15, uniform='search')

        self.title_label = ctk.CTkLabel(self.searchFrame,
                                        text="Αναζήτηση",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20, sticky="EW")



        self.__createInitialOptions()
    def __doubleclick(self,arttype,ids):
        self.searchFrame.destroy()
        self.show_frame(self.inputFrame, art=arttype, ids=ids)
        self.inputFrame.lift(self)


    def __createInitialOptions(self):
        """
        Επιλογή καλλιτέχνη ή έργου
        """
        self.option = ctk.StringVar(value="")
        self.optionLabel = ctk.CTkLabel(self.searchFrame, text="Αναζήτηση σε:",
                                        anchor="e",
                                        font=("Arial", 14, "bold")
                                        )
        self.rbArtist = ctk.CTkRadioButton(self.searchFrame,
                                             text="Καλλιτέχνες",
                                             variable=self.option,
                                             value="artist",
                                             command=self.__optionChanged)
        self.rbArtwork = ctk.CTkRadioButton(self.searchFrame,
                                        text="Έργα",
                                        variable=self.option,
                                        value="artwork",
                                        command=self.__optionChanged)
        self.optionLabel.grid(row=1, column=0, sticky="W", padx=30)
        self.rbArtist.grid(row=1, column=1, padx=5, pady=5, sticky="W")
        self.rbArtwork.grid(row=1, column=2, padx=30, pady=5, sticky="W")

        self.artistSearchFrame = None
        self.artworkSearchFrame = None

    def __optionChanged(self):
        """
        Εμφάνιση αντίστοιχου frame ανάλογα την επιλογή
        """
        option = self.option.get()
        if self.artistSearchFrame:
            self.artistSearchFrame.destroy()

        if self.artworkSearchFrame:
            self.artworkSearchFrame.destroy()

        if option == "artwork":
            self.__showArtworkFields()
        else:
            self.__showArtistFields()

    def __showArtistFields(self, **kwargs):
        """
        Εμφάνιση πεδίων για αναζήτηση καλλιτέχνη
        """
        # αν υπάρχει ήδη το frame το κάνουμε reset
        try:
            if self.artistSearchFrame:
                self.artistSearchFrame.destroy()
        except Exception as e:
            pass

        self.artistSearchFrame = ctk.CTkFrame(self.searchFrame)
        self.artistSearchFrame.grid(row=2, column=0,rowspan=2,columnspan=7,padx=10, pady=10,sticky="NEW")

        # Δημιουργία widgets
        ctk.CTkLabel(self.artistSearchFrame, text="Όνομα").grid(row=3, column=0, padx=5, sticky="W")
        ctk.CTkLabel(self.artistSearchFrame, text="Βιογραφία").grid(row=3, column=1, padx=5, sticky="W")
        ctk.CTkLabel(self.artistSearchFrame, text="Εθνικότητα").grid(row=3, column=2, padx=5, sticky="W")
        ctk.CTkLabel(self.artistSearchFrame, text="Φύλο").grid(row=3, column=3, padx=5, sticky="W")
        ctk.CTkLabel(self.artistSearchFrame, text="Από").grid(row=3, column=4, padx=5, sticky="W")
        ctk.CTkLabel(self.artistSearchFrame, text="Έως").grid(row=3, column=5, padx=5, sticky="W")

        self.displayNameEntry = ctk.CTkEntry(self.artistSearchFrame)
        self.artistBioEntry = ctk.CTkEntry(self.artistSearchFrame)

        # παίρνουμε τα δεδομένα των Nationalities από τη βάση
        self.nationalityMappings = self.md.getNationalities()
        self.nationalityMappings[0] = ' None'
        self.nationalities = sorted(list(self.nationalityMappings.values()))
        self.nationalityComboBox = ctk.CTkComboBox(self.artistSearchFrame,
                                                  values=self.nationalities,
                                                  width=140,
                                                  height=28, )
        self.nationalityComboBox.bind("<KeyRelease>",
                                 lambda event: self.filterComboBox(self.nationalityComboBox, self.nationalities))
        self.genderEntry = ctk.CTkComboBox(self.artistSearchFrame,
                                           values=['','male', 'female'],
                                           state="readonly",
                                           width=140,
                                           height=28, )

        self.beginDateEntry = ctk.CTkEntry(self.artistSearchFrame)
        self.endDateEntry = ctk.CTkEntry(self.artistSearchFrame)

        self.displayNameEntry.grid(row=4, column=0, padx=5, pady=5)
        self.artistBioEntry.grid(row=4, column=1, padx=5, pady=5)
        self.nationalityComboBox.grid(row=4, column=2, padx=5, pady=5)
        self.genderEntry.grid(row=4, column=3, padx=5, pady=5)
        self.beginDateEntry.grid(row=4, column=4, padx=5, pady=5)
        self.endDateEntry.grid(row=4, column=5, padx=5, pady=5)

        self.submitArtistBtn = ctk.CTkButton(self.artistSearchFrame,
                                              text="Αναζήτηση",
                                              command=self.__submitArtistData)

        self.submitArtistBtn.grid(row=4, column=6, pady=5, padx=5, sticky="W")



    def __submitArtistData(self):
        self.tree = ttk.Treeview(self.artistSearchFrame,
                                 columns=("ConstituentID","DisplayName", "ArtistBio", "Nationality", "Gender"),
                                 show='headings')
        self.tree.heading("ConstituentID", text="ID")
        self.tree.heading("DisplayName", text="Καλλιτέχνης")
        self.tree.heading("ArtistBio", text="Βιογραφία")
        self.tree.heading("Nationality", text="Εθνικότητα")
        self.tree.heading("Gender", text="Φύλο")
        self.tree.grid(row=5, column=0, columnspan=6, padx=10, pady=10, sticky="NSEW")
        self.tree.bind("<Double-1>", lambda event: self.__doubleclick('artist', self.tree.item(self.tree.focus(), 'values')[0]))

        ctk.CTkLabel(self.artistSearchFrame, text="Κάντε διπλό κλικ για επεξεργασία της εγγραφη").grid(row=6, column=0,columnspan=6,  padx=5, sticky="W")
        where = ['1=1']
        if  self.displayNameEntry.get() != '' :
            where.append(''' artists.displayName LIKE \'%''' + self.displayNameEntry.get() + '''%\' ''' )
        if  self.artistBioEntry.get() != '' :
            where.append(''' artists.artistBio LIKE \'%''' + self.artistBioEntry.get() + '''%\' ''' )
        if  self.nationalityComboBox.get() != ' None' :
            where.append(''' nation.nationality = \'''' + self.nationalityComboBox.get() + '''\' ''' )
        if  self.genderEntry.get() != '' :
            where.append(''' artists.Gender = \'''' + self.genderEntry.get() + '''\' ''' )
        if  self.beginDateEntry.get() != '' :
            where.append(''' artists.BeginDate >= \'''' + self.beginDateEntry.get() + '''\' ''' )
        if  self.endDateEntry.get() != '' :
            where.append(''' artists.EndDate <= \'''' + self.endDateEntry.get() + '''\' ''' )

        query = '''     SELECT artists.ConstituentID, artists.DisplayName,  artists.ArtistBio, nation.nationality, artists.Gender
                                FROM artists
                                left join Nationalities nation on nation.NationalityID=artists.NationalityID                                
                                where ''' + ' and '.join(where)

        rows = self.md.getData(query,listResultset=True)
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in rows:
            self.tree.insert('', 'end', values=row)



    def show_frame(self,frame,**kwargs):
            self.searchFrame.forget()
            self.startFrame = frame(self.parent, **kwargs)
            #self.startFrame.lift(self.startFrame)
    @staticmethod
    def filterComboBox(widget, listitems):
        """
        Φιλτράρει τη λίστα ενός ComboBox καθώς πληκτρολογούμε
        """
        filterText = widget.get().lower()
        filteredList = [val for val in listitems if filterText in val.lower()]
        widget.configure(values=filteredList)

    def __showArtworkFields(self, **kwargs):
        """
        Εμφάνιση πεδίων για αναζήτηση καλλιτέχνη
        """
        # αν υπάρχει ήδη το frame το κάνουμε reset
        try:
            if self.artworkSearchFrame:
                self.artworkSearchFrame.destroy()
        except Exception as e:
            pass

        self.artworkSearchFrame = ctk.CTkFrame(self.searchFrame)
        self.artworkSearchFrame.grid(row=2, column=0, rowspan=2, columnspan=7, padx=10, pady=10, sticky="NEW")

        # Δημιουργία widgets
        ctk.CTkLabel(self.artworkSearchFrame, text="Τιτλος").grid(row=3, column=0, padx=5, sticky="W")
        ctk.CTkLabel(self.artworkSearchFrame, text="Έτος απόκτησης").grid(row=3, column=1, padx=5, sticky="W")
        ctk.CTkLabel(self.artworkSearchFrame, text="Έτος έργου").grid(row=3, column=2, padx=5, sticky="W")
        ctk.CTkLabel(self.artworkSearchFrame, text="Κατηγορία").grid(row=3, column=3, padx=5, sticky="W")
        ctk.CTkLabel(self.artworkSearchFrame, text="Τμήμα").grid(row=3, column=4, padx=5, sticky="W")
        ctk.CTkLabel(self.artworkSearchFrame, text="On View").grid(row=3, column=5, padx=5, sticky="W")

        self.titleEntry = ctk.CTkEntry(self.artworkSearchFrame)
        self.acquisitionDateEntry = ctk.CTkEntry(self.artworkSearchFrame)
        self.dateEntry = ctk.CTkEntry(self.artworkSearchFrame)

        # παίρνουμε τα δεδομένα των classifications από τη βάση
        self.classificationsMappings = self.md.getClassifications()
        self.classificationsMappings[0] = ' None'
        self.classifications = sorted(list(self.classificationsMappings.values()))
        self.classificationComboBox = ctk.CTkComboBox(self.artworkSearchFrame,
                                                   values=self.classifications,
                                                   width=140,
                                                   height=28, )
        self.classificationComboBox.bind("<KeyRelease>",
                                      lambda event: self.filterComboBox(self.classificationComboBox, self.classifications))


        # παίρνουμε τα δεδομένα των departments από τη βάση
        self.departmentsMappings = self.md.getDepartments()
        self.departmentsMappings[0] = ' None'
        self.departments = sorted(list(self.departmentsMappings.values()))
        self.departmentsComboBox = ctk.CTkComboBox(self.artworkSearchFrame,
                                                   values=self.departments,
                                                   width=140,
                                                   height=28, )
        self.departmentsComboBox.bind("<KeyRelease>",
                                      lambda event: self.filterComboBox(self.departmentsComboBox, self.departments))


        # παίρνουμε τα δεδομένα των Onviews από τη βάση
        self.onviewsMappings = self.md.getOnviews()
        self.onviewsMappings[0] = ' None'
        self.onviews = sorted(list(self.onviewsMappings.values()))
        self.onviewsComboBox = ctk.CTkComboBox(self.artworkSearchFrame,
                                                   values=self.onviews,
                                                   width=140,
                                                   height=28, )
        self.onviewsComboBox.bind("<KeyRelease>",
                                      lambda event: self.filterComboBox(self.onviewsComboBox, self.onviews))


        self.titleEntry.grid(row=4, column=0, padx=5, pady=5)
        self.acquisitionDateEntry.grid(row=4, column=1, padx=5, pady=5)
        self.dateEntry.grid(row=4, column=2, padx=5, pady=5)
        self.classificationComboBox.grid(row=4, column=3, padx=5, pady=5)
        self.departmentsComboBox.grid(row=4, column=4, padx=5, pady=5)
        self.onviewsComboBox.grid(row=4, column=5, padx=5, pady=5)

        self.submitArtistBtn = ctk.CTkButton(self.artworkSearchFrame,
                                             text="Αναζήτηση",
                                             command=self.__submitArtworkData)

        self.submitArtistBtn.grid(row=4, column=6, pady=5, padx=5, sticky="W")

    def __submitArtworkData(self):

        self.tree = ttk.Treeview(self.artworkSearchFrame,
                                 columns=("ObjectID","Title", "AcquisitionDate", "Date", "Category", "Department", "OnView"),
                                 show='headings')
        self.tree.heading("ObjectID", text="ID")
        self.tree.heading("Title", text="Τίτλος")
        self.tree.heading("AcquisitionDate", text="Ημερομηνία απόκτησης")
        self.tree.heading("Date", text="Έτος έργου")
        self.tree.heading("Category", text="Κατηγορία")
        self.tree.heading("Department", text="Τμήμα")
        self.tree.heading("OnView", text="On View")
        self.tree.grid(row=5, column=0, columnspan=6, padx=10, pady=10, sticky="NSEW")
        self.tree.bind("<Double-1>", lambda event: self.__doubleclick("artwork",self.tree.item(self.tree.focus(), 'values')[0]))

        ctk.CTkLabel(self.artworkSearchFrame, text="Κάντε διπλό κλικ για επεξεργασία της εγγραφη").grid(row=6, column=0,
                                                                                                       columnspan=6,
                                                                                                       padx=5,
                                                                                                       sticky="W")
        where = ['1=1']
        if  self.titleEntry.get() != '' :
            where.append(''' artworks.title LIKE \'%''' + self.titleEntry.get() + '''%\' ''' )
        if self.dateEntry.get() != '':
            where.append(''' artworks.date LIKE \'%''' + self.dateEntry.get() + '''%\' ''' )
        if self.acquisitionDateEntry.get() != '':
            where.append(''' artworks.dateacquired LIKE \'%''' + self.acquisitionDateEntry.get() + '''%\' ''' )

        if  self.departmentsComboBox.get() != ' None' :
            where.append(''' dept.department = \'''' + self.departmentsComboBox.get() + '''\' ''' )
        if  self.classificationComboBox.get() != ' None' :
            where.append(''' class.classification = \'''' + self.classificationComboBox.get() + '''\' ''' )
        if  self.onviewsComboBox.get() != ' None' and self.onviewsComboBox.get() != '' :
            where.append(''' ov.onView = \'''' + self.onviewsComboBox.get() + '''\' ''' )

        query = '''     SELECT artworks.ObjectId, artworks.Title,  artworks.dateAcquired, artworks.date, class.classification, dept.department, ov.onView
                                FROM artworks
                                left join Departments dept on dept.DepartmentID=artworks.Department                    
                                left join Classifications class on class.ClassificationID=artworks.Classification                                
                                left join OnViews ov on ov.OnViewID=artworks.OnView                                
                                where ''' + ' and '.join(where)
        rows = self.md.getData(query,listResultset=True)
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in rows:
            self.tree.insert('', 'end', values=row)
