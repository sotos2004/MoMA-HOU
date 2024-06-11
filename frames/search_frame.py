import customtkinter as ctk
import tkinter as ttk
from PIL import Image, ImageTk
import os
import moma_class as mc
from DATA import *
import requests

class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = ctk.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, item, image=None):
        label = ctk.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = ctk.CTkButton(self, text="Εμφάνιση Έργου", width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        label.grid(row=len(self.label_list), column=0, pady=(0, 2), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 2), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return

class SearchTermsFrame(ctk.CTkFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)


        self.search_terms = ctk.CTkFrame(master)
        self.search_terms.grid(row=1, column=0,padx=5, pady=2, sticky="EW")

        # παίρνουμε τα δεδομένα των Nationalities από τη ΒΔ
        self.md = mc.MoMA()
        self.nationalityMappings = self.md.getNationalities()
        self.nationalityMappings[0] = ' None'
        self.nationalities = sorted(list(self.nationalityMappings.values()))

        # παίρνουμε τα δεδομένα των Καλλιτεχνών από τη ΒΔ
        artists = self.md.getArtists(fields=" ConstituentID, DisplayName ")
        self.artistsMappings = dict(zip(artists['ConstituentID'], artists['DisplayName']))
        self.artistsMappings[0] = ' None'
        self.artists = sorted(list(self.artistsMappings.values()))

        # παίρνουμε τα δεδομένα των Μέσων από τη ΒΔ
        self.mediums = self.md.getData('SELECT distinct Medium FROM Artworks')
        self.mediums.fillna({'Medium': ''}, inplace=True)
        self.mediums_dict = self.mediums.to_dict()['Medium']
        # print(self.mediums_dict)
        x = self.mediums_dict.values()
        # print(x)
        self.x1 = list(x)
        # print(self.x1)
        self.x2 = []

        temp4 = []
        for i in self.x1:
            temp1 = i.replace('\n', '').replace('\r', '').replace('\xa0', '').replace('(', '').replace(')', '')
            # print(car1)
            n = 80  # χαρακτηρες
            temp2 = temp1.split("(|;", -1)[0]
            # print(temp2)
            # print(type(temp2))
            temp3 = [temp2[i:i + n] for i in range(0, n, n)]
            # print(temp3)
            # print(car3)
            temp4.append(temp3)
            # print(f'{i}')
        self.mediums_list = temp4
        # print(self.mediums_list)
        # print(type(self.mediums_list))
        # self.mediums_list = [self.x4.split("(", -1)[0] for self.x4 in self.x2]
        # Types = [line.split(",") for line in readlines]
        # self.mediums_list = [self.x2.split("(", -1)[0] for self.x2 in self.x1]

        # print(self.mediums_list)
        # print(type(self.mediums_list))
        # for i in self.x1:
        #     self.x2 = self.x1.split("(", 1)
        #     counter += 1
        # self.x2 = self.x1.split("(", 1)
        # print(type(self.x2))



        # self.mediums_list = list(x)
        # print(self.mediums_list)
        # print(self.mediums)
        # self.mediums = [self.mediums_temp[1] for self.mediums_temp in self.mediums_list]
        # print(self.mediums)

        # self.mediums = []
        # self.mediumMappings = self.md.getMediums()

        # self.mediumMappings[0] = ' None'
        # x = list(self.mediumMappings.values())
        # # print(x)
        # # print(type(self.mediums))
        # print(type(self.mediumMappings.values()))
        # # self.mediums = sorted(list(self.mediumMappings.values()))
        # self.mediums_list = list(self.mediumMappings.values())
        # # self.mediums_temp = sorted(list(self.mediumMappings.values()), key=lambda x: x[:1])
        self.mediums_combo_list = [self.mediums_temp[0] for self.mediums_temp in self.mediums_list] # https://community.spiceworks.com/t/customtkinter-combobox-not-working/962590
        # print(type(self.mediums))
        # print(self.mediums[1])
        # self.mediums = sorted(filter(None, list(self.mediumMappings.values())))


        # παίρνουμε τα δεδομένα των Ημερομηνίων των Μέσω από τη ΒΔ
        # self.dates = []
        # self.mediumMappings = self.md.getDates()

        self.entry_title = ctk.CTkEntry(self.search_terms, placeholder_text="Τίτλος Έργου")
        self.entry_title.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")

        self.entry_artist_name = ctk.CTkEntry(self.search_terms, placeholder_text="Όνομα Καλλιτέχνη")
        self.entry_artist_name.grid(row=0, column=2, padx=2, pady=2, sticky="nsew")

        self.combobox_artwork_year = ctk.CTkComboBox(self.search_terms,
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_artwork_year.grid(row=0, column=3, padx=2, pady=2)
        self.combobox_artwork_year.set("Χρονολογία Έργου")

        self.combobox_year_acquisition = ctk.CTkComboBox(self.search_terms,
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_year_acquisition.grid(row=0, column=4, padx=2, pady=2)
        self.combobox_year_acquisition.set("Έτος Απόκτησης")

        self.slider_distasi_ergou = ctk.CTkSlider(self.search_terms, from_=0, to=1, number_of_steps=4)
        self.slider_distasi_ergou.grid(row=0, column=5, padx=(5, 5), pady=(15, 5), sticky="ew")

        self.slider_diarkeia_ergou = ctk.CTkSlider(self.search_terms, from_=0, to=5000)   # number_of_steps=5000
        self.slider_diarkeia_ergou.grid(row=0, column=6, padx=(5, 5), pady=(15, 5), sticky="ew")



        self.search_terms2 = ctk.CTkFrame(master)
        self.search_terms2.grid(row=2, column=0,padx=5, pady=2, sticky="EW")

        self.combobox_artists_country = ctk.CTkComboBox(self.search_terms2,
                                                        values=self.nationalities,
                                                        state="readonly")
        self.combobox_artists_country.grid(row=2, column=0, padx=2, pady=2)
        self.combobox_artists_country.set("Χώρα Καλλιτέχνη")

        self.combobox_artists_sex = ctk.CTkComboBox(self.search_terms2,
                                                    values=["Άνδρας", "Γυναίκα"],
                                                    state="readonly")
        self.combobox_artists_sex.grid(row=2, column=1, padx=2, pady=2)
        self.combobox_artists_sex.set("Φύλλο Καλλιτέχνη")

        self.combobox_artworks_medium = ctk.CTkComboBox(self.search_terms2,
                                                       values=self.mediums_combo_list,
                                                       width=200)
        self.combobox_artworks_medium.grid(row=2, column=2, padx=2, pady=2)
        self.combobox_artworks_medium.set("Μέσο Έργου")

        self.combobox_6 = ctk.CTkComboBox(self.search_terms2,
                                                    values=self.artists)
        self.combobox_6.grid(row=2, column=3, padx=2, pady=2)
        self.combobox_6.set("Καλλιτέχνης")

        self.combobox_7 = ctk.CTkComboBox(self.search_terms2,
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_7.grid(row=2, column=4, padx=2, pady=2)
        self.combobox_7.set("CTkComboBox")

        self.combobox_8 = ctk.CTkComboBox(self.search_terms2,
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_8.grid(row=2, column=5, padx=2, pady=2)
        self.combobox_8.set("CTkComboBox")

        self.spinbox_1 = ttk.Spinbox(self.search_terms2, from_=0, to=10)
        self.spinbox_1.grid(row=2, column=6, padx=2, pady=2)




class SearchFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)
        # Δημιουργία frame και widgets


        self.searchFrame = ctk.CTkFrame(container, border_width=2)
        self.searchFrame.grid(row=1, column=1, columnspan=3, sticky="EW")
        self.searchFrame.columnconfigure(0, weight=1, uniform='search')
        self.searchFrame.rowconfigure(0, weight=1, uniform='search')
        self.searchFrame.rowconfigure(1, weight=1, uniform='search')
        self.searchFrame.rowconfigure(2, weight=1, uniform='search')
        self.searchFrame.rowconfigure(3, weight=15, uniform='search')

        self.title_label = ctk.CTkLabel(self.searchFrame,
                                        text="Αναζήτηση Έργων",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0,padx=5, pady=2, sticky="EW")


        self.search_terms_frame = SearchTermsFrame(master=self.searchFrame,
                                                                        command=self.label_button_frame_event,
                                                                        corner_radius=0)
        self.search_terms_frame.grid(row=1, column=0, padx=5, pady=2, sticky="NSEW")


        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = "./DATA"
        media_dir = "./DATA/Media"
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self.searchFrame, width=300,
                                                                        command=self.label_button_frame_event,
                                                                        corner_radius=0)
        self.scrollable_label_button_frame.grid(row=3, column=0, padx=5, pady=2, sticky="NSEW")

        # self.title_label = ctk.CTkLabel(self.searchFrame,
        #                                 text="Αναζήτηση2",
        #                                 anchor="center",
        #                                 font=("Arial", 16, "bold"))
        # self.title_label.grid(row=1, column=0, sticky="EW")

        for i in range(20):  # add items with images
            self.scrollable_label_button_frame.add_item(f"image and item {i}",
                                                        image=ctk.CTkImage(Image.open(os.path.join(data_dir, "Media", "MoMA_Icon_PNG_with_Alpha_256x256.png"))))
        self.scrollable_label_button_frame.remove_item("image and item 3")
        print(self.scrollable_label_button_frame)

    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")

