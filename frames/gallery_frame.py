import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import ttk
import moma_class as mc



class GalleryFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):

        super().__init__(container, *args, **kwargs)

        # Create instance of Moma
        self.md = mc.MoMA()
        # Nationalitites from DB
        self.nationalityMappings = self.md.getNationalities()
        self.nationalityMappings[0] = ' None'
        self.nationalities = sorted(list(self.nationalityMappings.values()))

        self.md = mc.MoMA()
        self.OnViewsMappings = self.md.getOnviews()
        self.OnViewsMappings[0] = ' None'
        self.OnViews = sorted(list(self.OnViewsMappings.values()))

        self.md = mc.MoMA()
        self.DepartmentsMappings = self.md.getDepartments()
        self.DepartmentsMappings[0] = ' None'
        self.Departments = sorted(list(self.DepartmentsMappings.values()))

        self.md = mc.MoMA()   
        self.ClassificationsMappings = self.md.getClassifications()
        self.ClassificationsMappings[0] = ' None'
        self.Classifications = sorted(list(self.ClassificationsMappings.values()))

        # Δημιουργία frame και widgets
        self.galleryFrame = ctk.CTkFrame(container, border_width=10)
        self.galleryFrame.grid(row=1, column=1, sticky="NSEW")
        self.galleryFrame.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='gf')
        self.list_items = ['nothing']

        self.l1 = ctk.CTkLabel(self.galleryFrame, text="select Nationality", width=20, height=1)
        self.l2 = ctk.CTkLabel(self.galleryFrame, text="select Gender", width=20, height=1)
        self.l3 = ctk.CTkLabel(self.galleryFrame, text="select Name", width=20, height=1)
        self.l4 = ctk.CTkLabel(self.galleryFrame, text="select Begindate", width=20, height=1)
        self.l5 = ctk.CTkLabel(self.galleryFrame, text="select EndDate", width=20, height=1)
        self.l6 = ctk.CTkLabel(self.galleryFrame, text="select onViews", width=20, height=1)
        self.l7 = ctk.CTkLabel(self.galleryFrame, text="select Classification", width=20, height=1)

        self.l1.grid(row=0, column=0, padx=5, pady=5, sticky="EW")
        self.l2.grid(row=0, column=1, padx=5, pady=5, sticky="EW")
        self.l3.grid(row=0, column=2, padx=5, pady=5, sticky="EW")
        self.l4.grid(row=0, column=3, padx=5, pady=5, sticky="EW")
        self.l5.grid(row=0, column=4, padx=5, pady=5, sticky="EW")
        self.l6.grid(row=0, column=5, padx=5, pady=5, sticky="EW")
        self.l7.grid(row=0, column=6, padx=5, pady=5, sticky="EW")

        self.combobox_var_list = ctk.StringVar(value=self.list_items)
        self.combo_box1 = ctk.CTkComboBox(master=self.galleryFrame, values=self.nationalities, width=40)
        self.combo_box2 = ctk.CTkComboBox(master=self.galleryFrame, values=self.list_items, width=20)
        self.combo_box3 = ctk.CTkComboBox(master=self.galleryFrame, values=self.list_items, width=20)
        self.combo_box4 = ctk.CTkComboBox(master=self.galleryFrame, values=self.list_items, width=20)
        self.combo_box5 = ctk.CTkComboBox(master=self.galleryFrame, values=self.list_items, width=20)
        self.combo_box6 = ctk.CTkComboBox(self.galleryFrame, values=self.OnViews, width=20)
        self.combo_box7 = ctk.CTkComboBox(self.galleryFrame, values=self.Classifications, width=20)

        self.btnSubmit = ctk.CTkButton(self.galleryFrame,text="Select", width=20, height=1, command=self.getData)

        self.combo_box1.grid(row=1, column=0, padx=5, pady=5, sticky="EW")
        self.combo_box2.grid(row=1, column=1, padx=5, pady=5, sticky="EW")
        self.combo_box3.grid(row=1, column=2, padx=5, pady=5, sticky="EW")
        self.combo_box4.grid(row=1, column=3, padx=5, pady=5, sticky="EW")
        self.combo_box5.grid(row=1, column=4, padx=5, pady=5, sticky="EW")
        self.combo_box6.grid(row=1, column=5, padx=5, pady=5, sticky="EW")
        self.combo_box7.grid(row=1, column=6, padx=5, pady=5, sticky="EW")
        self.btnSubmit.grid(row=1, column=8, padx=5, pady=5, sticky="EW")

        self.combo_box1.set(self.list_items[0])
        self.combo_box2.set(self.list_items[0])
        self.combo_box3.set(self.list_items[0])
        self.combo_box4.set(self.list_items[0])
        self.combo_box5.set(self.list_items[0])
        self.combo_box6.set(self.list_items[0])
        self.combo_box7.set(self.list_items[0])

        self.combo_box1.bind('<KeyRelease>', lambda event: search(event, self.combo_box1))
        self.combo_box2.bind('<KeyRelease>', lambda event: search(event, self.combo_box2))
        self.combo_box3.bind('<KeyRelease>', lambda event: search(event, self.combo_box3))
        self.combo_box4.bind('<KeyRelease>', lambda event: search(event, self.combo_box4))
        self.combo_box5.bind('<KeyRelease>', lambda event: search(event, self.combo_box5))
        self.combo_box6.bind('<KeyRelease>', lambda event: search(event, self.combo_box6))
        self.combo_box7.bind('<KeyRelease>', lambda event: search(event, self.combo_box7))

        self.image_list = ["gallery/image_1.png", "gallery/image_2.png", "gallery/image_3.png",
                           "gallery/image_4.png", "gallery/image_5.png"]
        self.counter = 0

        self.image1 = self.image_list[self.counter]
        self.imageLabel_image = ctk.CTkImage(light_image=Image.open(self.image1), size=(510, 510))
        self.imageLabel = ctk.CTkLabel(master=self.galleryFrame, text="", image=self.imageLabel_image)

        self.imageLabel.grid(row=2, column=0, columnspan=8, pady=10, sticky="NSEW")
        self.infoLabel = ctk.CTkLabel(self.galleryFrame, text=f"Image {self.counter + 1} of {len(self.image_list)}", font=("Helvetica", 20))
        self.infoLabel.grid(row=3, column=0, columnspan=8, sticky="EW")

        self.button1 = ctk.CTkButton(self.galleryFrame, text="previous", width=20, height=2, command=self.ChangeImage1)
        self.button2 = ctk.CTkButton(self.galleryFrame, text="next", width=20, height=2,command=self.ChangeImage2 )

        self.imageLabel.grid(row=2, column=0, columnspan=8, pady=10, sticky="NSEW")
        self.infoLabel.grid(row=3, column=0, columnspan=8, sticky="EW")
        self.button1.grid(row=4, column=3, pady=10, sticky="EW")
        self.button2.grid(row=4, column=4, pady=10, sticky="EW")

        def search(event, combo_box):
            self.value = event.widget.get()
            if self.value == '':
                combo_box['values'] = self.list_items
            else:
                self.data = [item for item in self.list_items if self.value.lower() in item.lower()]
                combo_box['values'] = self.data

    def ChangeImage1(self):
        self.counter = (self.counter - 1) % len(self.image_list)
        self.update_image()

    def ChangeImage2(self):
        self.counter = (self.counter + 1) % len(self.image_list)
        self.update_image()

    def update_image(self):
        self.image1 = self.image_list[self.counter]
        self.imageLabel_image = ctk.CTkImage(light_image=Image.open(self.image1), size=(510, 510))
        self.imageLabel.configure(image=self.imageLabel_image)
        self.imageLabel.image = self.imageLabel_image  # Keep a reference to avoid garbage collection
        self.infoLabel.configure(text=f"Image {self.counter + 1} of {len(self.image_list)}")



    def getData(self):
        records = self.md.test()
        print(records)
        self.image_list=[]
