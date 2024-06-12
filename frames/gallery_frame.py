import customtkinter as ctk
from PIL import Image
import moma_class as mc
import os
import requests
from frames.settings_frame import SettingsFrame as sf

class GalleryFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)

        # Create instance of Moma and Settings frame to use readConfig
        self.md = mc.MoMA()
        self.config = sf.readConfig()

        self.imagePath=self.config.get('SETTINGS', 'imagepath')
        # Δημιουργία frame και widgets
        self.galleryFrame = ctk.CTkFrame(container, border_width=10)
        self.galleryFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW",padx=0, pady=0)
        self.galleryFrame.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='gallery')
        # self.galleryFrame.rowconfigure(0, weight=1, uniform='f3')
        #
        self.title_label = ctk.CTkLabel(self.galleryFrame,
                                         text="Gallery",
                                         anchor="center",
                                         font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10, sticky="EW")

        self.list_items = ['nothing']

        ctk.CTkLabel(self.galleryFrame, text="Τιτλος").grid(row=2, column=0, padx=(15,0), sticky="W")
        ctk.CTkLabel(self.galleryFrame, text="Έτος απόκτησης").grid(row=2, column=1,  sticky="W")
        ctk.CTkLabel(self.galleryFrame, text="Έτος έργου").grid(row=2, column=2,  sticky="W")
        ctk.CTkLabel(self.galleryFrame, text="Κατηγορία").grid(row=2, column=3,  sticky="W")
        ctk.CTkLabel(self.galleryFrame, text="Τμήμα").grid(row=2, column=4,  sticky="W")
        ctk.CTkLabel(self.galleryFrame, text="On View").grid(row=2, column=5,  sticky="W")

        self.titleEntry = ctk.CTkEntry(self.galleryFrame)
        self.acquisitionDateEntry = ctk.CTkEntry(self.galleryFrame)
        self.dateEntry = ctk.CTkEntry(self.galleryFrame)

        # παίρνουμε τα δεδομένα των classifications από τη βάση
        self.classificationsMappings = self.md.getClassifications()
        self.classificationsMappings[0] = ' None'
        self.classifications = sorted(list(self.classificationsMappings.values()))
        self.classificationComboBox = ctk.CTkComboBox(self.galleryFrame,
                                                      values=self.classifications,
                                                      width=140,
                                                      height=28, )
        self.classificationComboBox.bind("<KeyRelease>",
                                         lambda event: self.filterComboBox(self.classificationComboBox,
                                                                           self.classifications))

        # παίρνουμε τα δεδομένα των departments από τη βάση
        self.departmentsMappings = self.md.getDepartments()
        self.departmentsMappings[0] = ' None'
        self.departments = sorted(list(self.departmentsMappings.values()))
        self.departmentsComboBox = ctk.CTkComboBox(self.galleryFrame,
                                                   values=self.departments,
                                                   width=140,
                                                   height=28, )
        self.departmentsComboBox.bind("<KeyRelease>",
                                      lambda event: self.filterComboBox(self.departmentsComboBox, self.departments))

        # παίρνουμε τα δεδομένα των Onviews από τη βάση
        self.onviewsMappings = self.md.getOnviews()
        self.onviewsMappings[0] = ' None'
        self.onviews = sorted(list(self.onviewsMappings.values()))
        self.onviewsComboBox = ctk.CTkComboBox(self.galleryFrame,
                                               values=self.onviews,
                                               width=140,
                                               height=28, )
        self.onviewsComboBox.bind("<KeyRelease>",
                                  lambda event: self.filterComboBox(self.onviewsComboBox, self.onviews))

        self.titleEntry.grid(row=3, column=0, padx=(15,0), pady=5)
        self.acquisitionDateEntry.grid(row=3, column=1, padx=5, pady=5)
        self.dateEntry.grid(row=3, column=2, padx=5, pady=5)
        self.classificationComboBox.grid(row=3, column=3, padx=5, pady=5)
        self.departmentsComboBox.grid(row=3, column=4, padx=5, pady=5)
        self.onviewsComboBox.grid(row=3, column=5, padx=5, pady=5)
        self.image_list = [self.imagePath + "/image_not_found.jpg"]
        self.submitArtistBtn = ctk.CTkButton(self.galleryFrame,
                                             text="Εμφάνιση",
                                             command=self.__submitArtworkData)

        self.submitArtistBtn.grid(row=3, column=6, pady=5, padx=5, sticky="W")


        self.counter = 0

        self.image1 = self.image_list[self.counter]
        self.imageLabel_image = ctk.CTkImage(light_image=Image.open(self.image1), size=(310, 310))
        self.imageLabel = ctk.CTkLabel(master=self.galleryFrame, text="", image=self.imageLabel_image)

        self.imageLabel.grid(row=4, column=0, columnspan=8, pady=10, padx=10, sticky="NSEW")
        self.infoLabel = ctk.CTkLabel(self.galleryFrame, text=f"Image {self.counter + 1} of {len(self.image_list)}",
                                      font=("Helvetica", 20))
        self.infoLabel.grid(row=5, column=0, columnspan=8,padx=10, sticky="EW")

        self.button1 = ctk.CTkButton(self.galleryFrame, text="previous", width=20, height=2, command=self.ChangeImage1)
        self.button2 = ctk.CTkButton(self.galleryFrame, text="next", width=20, height=2,command=self.ChangeImage2 )

        self.imageLabel.grid(row=4, column=0, columnspan=8, padx=10,pady=10, sticky="NSEW")
        self.infoLabel.grid(row=5, column=0, columnspan=8,padx=10, sticky="EW")
        self.button1.grid(row=6, column=3, pady=10,padx=10, sticky="EW")
        self.button2.grid(row=6, column=4, pady=10,padx=10, sticky="EW")

    def ChangeImage1(self):
        self.counter = (self.counter - 1) % len(self.image_list)
        self.update_image()

    def ChangeImage2(self):
        self.counter = (self.counter + 1) % len(self.image_list)
        self.update_image()

    def update_image(self):
        self.image1 = self.image_list[self.counter]
        self.imageLabel_image = ctk.CTkImage(light_image=Image.open(self.image1), size=(310, 310))
        self.imageLabel.configure(image=self.imageLabel_image)
        self.imageLabel.image = self.imageLabel_image  # Keep a reference to avoid garbage collection
        self.infoLabel.configure(text=f"Image {self.counter + 1} of {len(self.image_list)}")
    @staticmethod
    def filterComboBox(widget, listitems):
        """
        Φιλτράρει τη λίστα ενός ComboBox καθώς πληκτρολογούμε
        """
        filterText = widget.get().lower()
        filteredList = [val for val in listitems if filterText in val.lower()]
        widget.configure(values=filteredList)

    def __submitArtworkData(self):

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

        query = '''     SELECT artworks.ObjectId, artworks.Title,  artworks.dateAcquired, artworks.date, class.classification, dept.department, ov.onView, imageURL
                                FROM artworks
                                left join Departments dept on dept.DepartmentID=artworks.Department                    
                                left join Classifications class on class.ClassificationID=artworks.Classification                                
                                left join OnViews ov on ov.OnViewID=artworks.OnView                                
                                where ''' + ' and '.join(where)
        rows = self.md.getData(query,listResultset=True)
        self.image_list = []
        for row in rows:
            path = self.imagePath + '/' + str(row[0]) + '.jpg'
            path = path.replace('/', '\\')
            if not os.path.exists(path):
                try:
                    self.download_image(row[7], path)
                    self.image_list.append(self.imagePath + '/' + str(row[0]) + '.jpg')
                except Exception as e:
                    pass
            else:
                self.image_list.append(self.imagePath + '/' + str(row[0]) + '.jpg')

        self.counter = 0
        self.image1 = self.image_list[0]
        self.update_image()



    @staticmethod
    def download_image(url,filename):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code==200:
            with open(filename, 'wb') as file:
                file.write(response.content)

    def getData(self):
        # get test records for rendering
        records = self.md.test()
        print(records)
        # εδω πρεπει να κανεις itterate τα records και να γεμισεις μια λιστα απο τη στήλη ImageURL
        self.image_list=[]
