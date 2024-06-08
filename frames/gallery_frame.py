import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import ttk



class GalleryFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)
        # Δημιουργία frame και widgets
        self.galleryFrame = ctk.CTkFrame(container, border_width=10)
        self.galleryFrame.grid(row=1, column=1, sticky="NSEW")
        self.galleryFrame.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='gf')
        # self.galleryFrame.rowconfigure(0, weight=1, uniform='f3')
        #
        # self.title_label = ctk.CTkLabel(self.galleryFrame,
        #                                 text="Gallery",
        #                                 anchor="center",
        #                                 font=("Arial", 16, "bold"))
        # self.title_label.grid(row=0, column=0, padx=5, pady=5)

        list_items = ['adwad', 'fawefaw', 'fawefg']

        l1 = ctk.CTkLabel(self.galleryFrame, text="select Nationality", width=20, height=1)
        l2 = ctk.CTkLabel(self.galleryFrame, text="select Gender", width=20, height=1)
        l3 = ctk.CTkLabel(self.galleryFrame, text="select Name", width=20, height=1)
        l4 = ctk.CTkLabel(self.galleryFrame, text="select Begindate", width=20, height=1)
        l5 = ctk.CTkLabel(self.galleryFrame, text="select EndDate", width=20, height=1)
        l6 = ctk.CTkLabel(self.galleryFrame, text="select onViews", width=20, height=1)
        l7 = ctk.CTkLabel(self.galleryFrame, text="select Classification", width=20, height=1)
        l8 = ctk.CTkLabel(self.galleryFrame, text="select Departments", width=20, height=1)

        l1.grid(row=0, column=0, padx=5, pady=5, sticky="EW")
        l2.grid(row=0, column=1, padx=5, pady=5, sticky="EW")
        l3.grid(row=0, column=2, padx=5, pady=5, sticky="EW")
        l4.grid(row=0, column=3, padx=5, pady=5, sticky="EW")
        l5.grid(row=0, column=4, padx=5, pady=5, sticky="EW")
        l6.grid(row=0, column=5, padx=5, pady=5, sticky="EW")
        l7.grid(row=0, column=6, padx=5, pady=5, sticky="EW")
        l8.grid(row=0, column=7, padx=5, pady=5, sticky="EW")

        combobox_var_list = ctk.StringVar(value=list_items)
        combo_box1 = ctk.CTkComboBox(master=self.galleryFrame, values=list_items, width=40)
        combo_box2 = ctk.CTkComboBox(master=self.galleryFrame, values=list_items, width=20)
        combo_box3 = ctk.CTkComboBox(master=self.galleryFrame, values=list_items, width=20)
        combo_box4 = ctk.CTkComboBox(master=self.galleryFrame, values=list_items, width=20)
        combo_box5 = ctk.CTkComboBox(master=self.galleryFrame, values=list_items, width=20)
        combo_box6 = ctk.CTkComboBox(self.galleryFrame, values=list_items, width=20)
        combo_box7 = ctk.CTkComboBox(self.galleryFrame, values=list_items, width=20)
        combo_box8 = ctk.CTkComboBox(self.galleryFrame, values=list_items, width=20)

        combo_box1.grid(row=1, column=0, padx=5, pady=5, sticky="EW")
        combo_box2.grid(row=1, column=1, padx=5, pady=5, sticky="EW")
        combo_box3.grid(row=1, column=2, padx=5, pady=5, sticky="EW")
        combo_box4.grid(row=1, column=3, padx=5, pady=5, sticky="EW")
        combo_box5.grid(row=1, column=4, padx=5, pady=5, sticky="EW")
        combo_box6.grid(row=1, column=5, padx=5, pady=5, sticky="EW")
        combo_box7.grid(row=1, column=6, padx=5, pady=5, sticky="EW")
        combo_box8.grid(row=1, column=7, padx=5, pady=5, sticky="EW")

        combo_box1.set(list_items[0])
        combo_box2.set(list_items[0])
        combo_box3.set(list_items[0])
        combo_box4.set(list_items[0])
        combo_box5.set(list_items[0])
        combo_box6.set(list_items[0])
        combo_box7.set(list_items[0])
        combo_box8.set(list_items[0])

        combo_box1.bind('<KeyRelease>', lambda event: search(event, combo_box1))  #ComboboxSelected
        combo_box2.bind('<KeyRelease>', lambda event: search(event, combo_box2))
        combo_box3.bind('<KeyRelease>', lambda event: search(event, combo_box3))
        combo_box4.bind('<KeyRelease>', lambda event: search(event, combo_box4))
        combo_box5.bind('<KeyRelease>', lambda event: search(event, combo_box5))
        combo_box6.bind('<KeyRelease>', lambda event: search(event, combo_box6))
        combo_box7.bind('<KeyRelease>', lambda event: search(event, combo_box7))
        combo_box8.bind('<KeyRelease>', lambda event: search(event, combo_box8))



        def search(event, combo_box):
            value = event.widget.get()
            if value == '':
                combo_box['values'] = list_items
            else:
                data = [item for item in list_items if value.lower() in item.lower()]
                combo_box['values'] = data
        images_size_x = 400
        images_size_y = 400
        image1 = ctk.CTkImage(light_image=Image.open('gallery/images/fotos/01.jpg'),size=(images_size_x, images_size_y))
        image2 = ctk.CTkImage(light_image=Image.open('gallery/images/fotos/02.jpg'),size=(images_size_x, images_size_y))
        image3 = ctk.CTkImage(light_image=Image.open('gallery/images/fotos/03.jpg'),size=(images_size_x, images_size_y))
        image4 = ctk.CTkImage(light_image=Image.open('gallery/images/fotos/04.jpg'),size=(images_size_x, images_size_y))
        image5 = ctk.CTkImage(light_image=Image.open('gallery/images/fotos/05.jpg'),size=(images_size_x, images_size_y))
        image_list = [image1, image2, image3, image4, image5]
        counter = 0



        # image1 = ImageTk.PhotoImage(Image.open('images/fotos/01.jpg').resize((1166, 668)))
        # image2 = ImageTk.PhotoImage(Image.open('images/fotos/02.jpg').resize((1166, 668)))
        # image3 = ImageTk.PhotoImage(Image.open('images/fotos/03.jpg').resize((1166, 668)))
        # image4 = ImageTk.PhotoImage(Image.open('images/fotos/04.jpg').resize((1166, 668)))
        # image5 = ImageTk.PhotoImage(Image.open('images/fotos/05.jpg').resize((1166, 668)))
        # image_list = [image1, image2, image3, image4, image5]
        # counter = 0





        # imageLabel = ctk.CTkLabel(self.galleryFrame, image=image1)


        # imageLabel_image = ctk.CTkImage(light_image=Image.open(image1),
        #                                  # https://customtkinter.tomschimansky.com/documentation/utility-classes/image/
        #                                  size=(510, 510)
        #                                  )  # https://customtkinter.tomschimansky.com/documentation/widgets/label/
        imageLabel = ctk.CTkLabel(master=self.galleryFrame,
                                  text="",
                                  # Αν το αφήσω κενό  εμφανίζει το κείμενο "CTkLabel" πάνω από την εικόνα!!
                                  image=image1)  # https://stackoverflow.com/questions/56880941/how-to-fix-attributeerror-jpegimagefile-object-has-no-attribute-read

        imageLabel.image = image1  # https://stackoverflow.com/questions/23224574/tkinter-create-image-function-error-pyimage1-does-not-exist
        # self.splash_label.pack()



        infoLabel = ctk.CTkLabel(self.galleryFrame, text="Image 1 of 5", font=("Helvetica", 20))

        button1 = ctk.CTkButton(self.galleryFrame, text="previous", width=20, height=2, command=self.ChangeImage2)
        button2 = ctk.CTkButton(self.galleryFrame, text="next", width=20, height=2, command=self.ChangeImage1)

        imageLabel.grid(row=2, column=0, columnspan=8, pady=10, sticky="NSEW")
        infoLabel.grid(row=3, column=0, columnspan=8, sticky="EW")
        button1.grid(row=4, column=3, pady=10, sticky="EW")
        button2.grid(row=4, column=4, pady=10, sticky="EW")

    def ChangeImage1(self):
        counter = counter.get()
        counter = (counter + 1) % len(image_list)
        imageLabel.config(image=image_list[counter])
        infoLabel.config(text=f"Image {counter + 1} of {len(image_list)}")

    def ChangeImage2(self):

        counter = (counter - 1) % len(image_list)
        imageLabel.config(image=image_list[counter])
        infoLabel.config(text=f"Image {counter + 1} of {len(image_list)}")

