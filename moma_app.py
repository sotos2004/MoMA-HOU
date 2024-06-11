import json
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt

class MoMAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MoMA Collection")
        self.create_widgets()
        self.insert_artists_and_artworks_from_files()

    def create_widgets(self):
        search_frame = ttk.Frame(self.root, padding="10")
        search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

        ttk.Label(search_frame, text="Αναζήτηση έργου:").grid(row=0, column=0, sticky=tk.W)
        self.search_entry = ttk.Entry(search_frame, width=50)
        self.search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        search_button = ttk.Button(search_frame, text="Αναζήτηση", command=self.search_artworks)
        search_button.grid(row=0, column=2, sticky=tk.W)

        self.tree = ttk.Treeview(self.root, columns=("Title", "Artist", "Date", "Medium", "Dimensions", "URL"), show='headings')
        self.tree.heading("Title", text="Τίτλος")
        self.tree.heading("Artist", text="Καλλιτέχνης")
        self.tree.heading("Date", text="Χρονολογία")
        self.tree.heading("Medium", text="Μέσο")
        self.tree.heading("Dimensions", text="Διαστάσεις")
        self.tree.heading("URL", text="URL")
        self.tree.grid(row=1, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        buttons_frame = ttk.Frame(self.root, padding="10")
        buttons_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))

        add_button = ttk.Button(buttons_frame, text="Προσθήκη Έργου", command=self.add_artwork)
        add_button.grid(row=0, column=0, sticky=tk.W)

        edit_button = ttk.Button(buttons_frame, text="Επεξεργασία Έργου", command=self.edit_artwork)
        edit_button.grid(row=0, column=1, sticky=tk.W)

        random_button = ttk.Button(buttons_frame, text="Τυχαίο Έργο", command=self.show_random_artwork)
        random_button.grid(row=0, column=2, sticky=tk.W)

        stats_button = ttk.Button(buttons_frame, text="Στατιστικά", command=self.show_statistics)
        stats_button.grid(row=0, column=3, sticky=tk.W)

    def insert_artists_and_artworks_from_files(self):
        # Read artists from JSON file
        try:
            with open(r'c:\Users\user\Downloads\Artists (1).json', 'r', encoding='utf-8') as file:
                artists = json.load(file)
        except FileNotFoundError:
            print("Το αρχείο καλλιτεχνών δεν βρέθηκε.")
            return

        # Read artworks from JSON file
        try:
            with open(r'c:\Users\user\Downloads\Artworks.json', 'r', encoding='utf-8') as file:
                artworks = json.load(file)
        except FileNotFoundError:
            print("Το αρχείο έργων δεν βρέθηκε.")
            return

        # Connect to SQLite database
        conn = sqlite3.connect(r'c:\Users\user\Downloads\MoMA.db3')
        cursor = conn.cursor()

        try:
            # Insert artists
            for artist in artists:
                cursor.execute('''
                    INSERT OR IGNORE INTO artists (name, nationality, gender, birth_year, death_year)
                    VALUES (?, ?, ?, ?, ?)
                ''', (artist['DisplayName'], artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate']))

            conn.commit()

            # Insert artworks
            for artwork in artworks:
                cursor.execute('''
                    INSERT OR IGNORE INTO artworks (title, artist_id, date, medium, dimensions, url)
                    VALUES (?, (SELECT id FROM artists WHERE name = ?), ?, ?, ?, ?)
                ''', (artwork['Title'], artwork['Artist'], artwork['Date'], artwork['Medium'], artwork['Dimensions'], artwork['URL']))

            conn.commit()
            print("Οι καλλιτέχνες και τα έργα τέχνης εισήχθησαν επιτυχώς.")
        except Exception as e:
            print(f"Σφάλμα: {e}")
        finally:
            conn.close()

    def search_artworks(self):
        search_term = self.search_entry.get()
        conn = sqlite3.connect(r'c:\Users\user\Downloads\MoMA.db3')
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT artworks.title, artists.name, artworks.date, artworks.medium, artworks.dimensions, artworks.url
                FROM artworks
                JOIN artists ON artworks.artist_id = artists.id
                WHERE artworks.title LIKE ? OR artists.name LIKE ?
            ''', ('%' + search_term + '%', '%' + search_term + '%'))
            rows = cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Σφάλμα Αναζήτησης", f"Σφάλμα: {e}")
        finally:
            conn.close()

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
        conn = sqlite3.connect(r'c:\Users\user\Downloads\MoMA.db3')
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT artworks.title, artists.name, artworks.date, artworks.medium, artworks.dimensions, artworks.url
                FROM artworks
                JOIN artists ON artworks.artist_id = artists.id
                ORDER BY RANDOM() LIMIT 1
            ''')
            row = cursor.fetchone()
        except Exception as e:
            messagebox.showerror("Σφάλμα", f"Σφάλμα: {e}")
        finally:
            conn.close()

        if row:
            messagebox.showinfo("Τυχαίο Έργο", f"Τίτλος: {row[0]}\nΚαλλιτέχνης: {row[1]}\nΧρονολογία: {row[2]}\nΜέσο: {row[3]}\nΔιαστάσεις: {row[4]}\nURL: {row[5]}")
        else:
            messagebox.showinfo("Τυχαίο Έργο", "Δεν βρέθηκε τυχαίο έργο.")

    def show_statistics(self):
        conn = sqlite3.connect(r'c:\Users\user\Downloads\MoMA.db3')
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT a.name, COUNT(*) FROM artworks aw JOIN artists a ON aw.artist_id = a.id GROUP BY a.name")
            artist_counts = cursor.fetchall()

            cursor.execute("SELECT medium, COUNT(*) FROM artworks GROUP BY medium")
            medium_counts = cursor.fetchall()

            cursor.execute("SELECT date, COUNT(*) FROM artworks GROUP BY date")
            year_counts = cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Σφάλμα Στατιστικών", f"Σφάλμα: {e}")
        finally:
            conn.close()

        if artist_counts and medium_counts and year_counts:
            fig, axs = plt.subplots(3, 1, figsize=(10, 15))

            # Πλήθος έργων ανά καλλιτέχνη
            axs[0].bar([x[0] for x in artist_counts], [x[1] for x in artist_counts])
            axs[0].set_title('Πλήθος έργων ανά καλλιτέχνη')
            axs[0].set_xticklabels([x[0] for x in artist_counts], rotation=90)

            # Πλήθος έργων για κάθε μέσο
            axs[1].bar([x[0] for x in medium_counts], [x[1] for x in medium_counts])
            axs[1].set_title('Πλήθος έργων για κάθε μέσο')

            # Πλήθος έργων που δημιουργήθηκε κάθε έτος
            axs[2].bar([x[0] for x in year_counts], [x[1] for x in year_counts])
            axs[2].set_title('Πλήθος έργων που δημιουργήθηκε κάθε έτος')

            plt.tight_layout()
            plt.show()
        else:
            messagebox.showinfo("Στατιστικά", "Δεν υπάρχουν αρκετά δεδομένα για να εμφανιστούν στατιστικά.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MoMAApp(root)
    root.mainloop()
