import customtkinter as ctk
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt

import moma_class as mc

class StatsFrame(ctk.CTkScrollableFrame):

    def __init__(self, container, *args, **kwargs):
        """
        Αρχικοποίηση της κλάσης
        """
        super().__init__(container, *args, **kwargs)
        self.md = mc.MoMA()
        # Δημιουργία frame και widgets
        self.statsFrame = ctk.CTkFrame(container, border_width=20)
        self.statsFrame.grid(row=1, column=1, columnspan=3, sticky="NSEW")
        self.statsFrame.columnconfigure(0, weight=1, uniform='stats')
        self.statsFrame.rowconfigure(0, weight=1, uniform='stats')

        self.title_label = ctk.CTkLabel(self.statsFrame,
                                        text="Στατιστικά",
                                        anchor="center",
                                        font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, sticky="WEN", pady=10 , padx=20 )
        self.search_frame = ttk.Frame(self.statsFrame, padding="10")
        self.search_frame.grid(row=1, column=0, sticky="WES", padx=40, pady=40)

        ttk.Label(self.search_frame, text="Αναζήτηση έργου:").grid(row=0, column=0, sticky="W")
        self.search_entry = ttk.Entry(self.search_frame, width=50)
        self.search_entry.grid(row=1, column=1, sticky="W")

        search_button = ttk.Button(self.search_frame, text="Αναζήτηση", command=self.search_artworks)
        search_button.grid(row=1, column=2, sticky="W")

        self.tree = ttk.Treeview(self.search_frame, columns=("Title", "Artist", "Date", "Medium", "Dimensions", "URL"), show='headings')
        self.tree.heading("Title", text="Τίτλος")
        self.tree.heading("Artist", text="Καλλιτέχνης")
        self.tree.heading("Date", text="Χρονολογία")
        self.tree.heading("Medium", text="Μέσο")
        self.tree.heading("Dimensions", text="Διαστάσεις")
        self.tree.heading("URL", text="URL")
        self.tree.grid(row=2, column=0 ,columnspan=6, sticky="NSEW")

       #self.root.grid_rowconfigure(1, weight=1)
       #self.root.grid_columnconfigure(0, weight=1)
        buttons_frame = ttk.Frame(self.search_frame, padding="10")
        buttons_frame.grid(row=6, column=0, sticky="WE")

        add_button = ttk.Button(buttons_frame, text="Προσθήκη Έργου", command=self.add_artwork)
        add_button.grid(row=0, column=0, sticky="W")

        edit_button = ttk.Button(buttons_frame, text="Επεξεργασία Έργου", command=self.edit_artwork)
        edit_button.grid(row=0, column=1, sticky="W")

        random_button = ttk.Button(buttons_frame, text="Τυχαίο Έργο", command=self.show_random_artwork)
        random_button.grid(row=0, column=2, sticky="W")

        stats_button = ttk.Button(buttons_frame, text="Στατιστικά", command=self.show_statistics)
        stats_button.grid(row=0, column=3, sticky="W")

    def search_artworks(self):

        search_term = self.search_entry.get()

        query = '''     SELECT artworks.title, artists.DisplayName, artworks.date, artworks.medium, 
                               artworks.Dimenssions, artworks.url
                        FROM artworks
                        join ArtworkArtists aa on aa.ConstituentID=artists.ConstituentID 
                        JOIN artists ON aa.ObjectID=artworks.ObjectID 
                        WHERE artworks.title LIKE \'%''' + search_term +'''%\' OR artists.DisplayName LIKE \'%''' + search_term +'''%\'
                    '''
        print(query)
        try:
            rows = self.md.getData(query,listResultset=True)

        except Exception as e:
            messagebox.showerror("Σφάλμα Αναζήτησης", f"Σφάλμα: {e}")

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in rows:
            self.tree.insert('', 'end', values=row)

    def add_artwork(self):
        # Μέθοδος προσθήκης νέου έργου
        pass

    def edit_artwork(self):
        # Μέθοδος επεξεργασίας υπάρχοντος έργου
        pass

    def show_random_artwork(self):

        query = '''     SELECT artworks.title, artists.DisplayName, artworks.date, artworks.medium, 
                               artworks.Dimenssions, artworks.url
                        FROM artworks
                        join ArtworkArtists aa on aa.ConstituentID=artists.ConstituentID 
                        JOIN artists ON aa.ObjectID=artworks.ObjectID 
                        ORDER BY RANDOM() LIMIT 1
                    '''
        print(query)
        try:
            row = self.md.getData(query,listResultset=True)
            print(row)
            print(type(row))
        except Exception as e:
            messagebox.showerror("Σφάλμα", f"Σφάλμα: {e}")

        row=row[0]
        if row:
            messagebox.showinfo("Τυχαίο Έργο", f"Τίτλος: {row[0]}\nΚαλλιτέχνης: {row[1]}\nΧρονολογία: {row[2]}\nΜέσο: {row[3]}\nΔιαστάσεις: {row[4]}\nURL: {row[5]}")
        else:
            messagebox.showinfo("Τυχαίο Έργο", "Δεν βρέθηκε τυχαίο έργο.")
    def show_statistics(self):
        try:
            query = '''
                    SELECT a.displayName, COUNT(*) 
                    FROM artworks aw
                    join ArtworkArtists aa on aa.ConstituentID=a.ConstituentID 
                    jOIN artists a ON aa.ObjectID=aw.ObjectID  GROUP BY a.DisplayName
            '''
            artist_counts = self.md.getData(query,listResultset=True)

            query =("SELECT medium, COUNT(*) FROM artworks GROUP BY medium")
            medium_counts = self.md.getData(query,listResultset=True)

            query = ("SELECT date, COUNT(*) cnt FROM artworks where date is not null GROUP BY date having cnt >10")
            year_counts = self.md.getData(query,listResultset=True)

        except Exception as e:
            messagebox.showerror("Σφάλμα Στατιστικών", f"Σφάλμα: {e}")


        if artist_counts and medium_counts and year_counts:
            fig, axs = plt.subplots(3, 1, figsize=(10, 15))

            # Πλήθος έργων ανά καλλιτέχνη
            axs[0].bar([x[0] for x in artist_counts], [x[1] for x in artist_counts])
            axs[0].set_title('Πλήθος έργων ανά καλλιτέχνη')
            axs[0].set_xticklabels([x[0] for x in artist_counts], rotation=90)
            # print(medium_counts)
            # x = self.mediums_dict.values()
            # print(x)
            # x1 = list(x)

            medium_counts_list = list(medium_counts)
            list_a = []
            list_b = []
            for i in medium_counts:
                if i[0] is not None and i[1] is not None:
                    list_a.append(i[0])
                    list_b.append(i[1])

            temp4 = []
            for i in list_a:
                temp1 = i.replace('\n', '').replace('\r', '').replace('\xa0', '').replace('(', '').replace(')', '')
                n = 10  # χαρακτηρες
                temp2 = temp1.split("(|;", -1)[0]
                temp3 = [temp2[i:i + n] for i in range(0, n, n)]
                temp4.append(temp3)
            medium_values_list = temp4
            mediums_temp = []

            mediums_graph_list = [mediums_temp[0] for mediums_temp in
                                  medium_values_list]

            #Πλήθος έργων για κάθε μέσο
            axs[1].bar([x for x in mediums_graph_list], [x for x in list_b])
            axs[1].set_title('Πλήθος έργων για κάθε μέσο')

            # Πλήθος έργων για κάθε μέσο
            # axs[1].bar([x([0][]) for x in medium_counts], [x([1][]) for x in medium_counts])
            # axs[1].set_title('Πλήθος έργων για κάθε μέσο')


            # Πλήθος έργων που δημιουργήθηκε κάθε έτος
            axs[2].bar([x[0] for x in year_counts], [x[1] for x in year_counts])
            axs[2].set_title('Πλήθος έργων που δημιουργήθηκε κάθε έτος')

            plt.tight_layout()
            plt.show()
        else:
            messagebox.showinfo("Στατιστικά", "Δεν υπάρχουν αρκετά δεδομένα για να εμφανιστούν στατιστικά.")

#τa παρακάτω είναι παρωχημένa καθώς πλέον συνδόμαστε στη βαση στον φάκελο data

#    def insert_artists_and_artworks_from_files(self):
#        # Read artists from JSON file
#        try:
#            with open(r'c:\Users\user\Downloads\Artists (1).json', 'r', encoding='utf-8') as file:
#                artists = json.load(file)
#        except FileNotFoundError:
#            print("Το αρχείο καλλιτεχνών δεν βρέθηκε."
#            return
#
#        # Read artworks from JSON file
#        try:
#            with open(r'c:\Users\user\Downloads\Artworks.json', 'r', encoding='utf-8') as file:
#                artworks = json.load(file)
#        except FileNotFoundError:
#            print("Το αρχείο έργων δεν βρέθηκε.")
#            return
#
#        # Connect to SQLite database
#        conn = sqlite3.connect(r'c:\Users\user\Downloads\MoMA.db3')
#        cursor = conn.cursor()
#
#        try:
#            # Insert artists
#            for artist in artists:
##                cursor.execute('''
#                   INSERT OR IGNORE INTO artists (name, nationality, gender, birth_year, death_year)
#                    VALUES (?, ?, ?, ?, ?)
#               ''', (artist['DisplayName'], artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate']))
#
#           conn.commit()
#
#            # Insert artworks
#            for artwork in artworks:
#                cursor.execute('''
#                    INSERT OR IGNORE INTO artworks (title, artist_id, date, medium, dimensions, url)
#                    VALUES (?, (SELECT id FROM artists WHERE name = ?), ?, ?, ?, ?)
#                ''', (artwork['Title'], artwork['Artist'], artwork['Date'], artwork['Medium'], artwork['Dimensions'], artwork['URL']))
#
#            conn.commit()
#            print("Οι καλλιτέχνες και τα έργα τέχνης εισήχθησαν επιτυχώς.")
#        except Exception as e:
#            print(f"Σφάλμα: {e}")
#        finally:
#            conn.close()
#
