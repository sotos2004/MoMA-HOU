import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt

class MoMAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MoMA Collection")
        self.create_widgets()

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

    def search_artworks(self):
        search_term = self.search_entry.get()
        conn = sqlite3.connect(r'c:\Users\user\Downloads\moma.db')
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
            messagebox.showerror("Σφάλμα Αναζήτησης", f"Error: {e}")
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
        conn = sqlite3.connect(r'c:\Users\user\Downloads\moma.db')
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
            messagebox.showerror("Σφάλμα", f"Error: {e}")
        finally:
            conn.close()

        if row:
            messagebox.showinfo("Τυχαίο Έργο", f"Τίτλος: {row[0]}\nΚαλλιτέχνης: {row[1]}\nΧρονολογία: {row[2]}\nΜέσο: {row[3]}\nΔιαστάσεις: {row[4]}\nURL: {row[5]}")
        else:
            messagebox.showinfo("Τυχαίο Έργο", "Δεν βρέθηκε τυχαίο έργο.")

    def show_statistics(self):
        conn = sqlite3.connect(r'c:\Users\user\Downloads\moma.db')
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT a.name, COUNT(*) FROM artworks aw JOIN artists a ON aw.artist_id = a.id GROUP BY a.name")
            artist_counts = cursor.fetchall()

            cursor.execute("SELECT medium, COUNT(*) FROM artworks GROUP BY medium")
            medium_counts = cursor.fetchall()

            cursor.execute("SELECT date, COUNT(*) FROM artworks GROUP BY date")
            year_counts = cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Σφάλμα Στατιστικών", f"Error: {e}")
        finally:
            conn.close()

        fig, axs = plt.subplots(3, 1, figsize=(10, 15))

        # Number of artworks per artist
        axs[0].bar([x[0] for x in artist_counts], [x[1] for x in artist_counts])
        axs[0].set_title('Πλήθος έργων ανά καλλιτέχνη')
        axs[0].set_xticklabels([x[0] for x in artist_counts], rotation=90)

        # Number of artworks per medium
        axs[1].bar([x[0] for x in medium_counts], [x[1] for x in medium_counts])
        axs[1].set_title('Πλήθος έργων για κάθε μέσο')

        # Number of artworks created per year
        axs[2].bar([x[0] for x in year_counts], [x[1] for x in year_counts])
        axs[2].set_title('Πλήθος έργων που δημιουργήθηκε κάθε έτος')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    def create_and_insert_data():
        conn = sqlite3.connect(r'c:\Users\user\Downloads\moma.db')
        cursor = conn.cursor()
        
        try:
            # Create artists table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS artists (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    nationality TEXT,
                    gender TEXT,
                    birth_year INTEGER,
                    death_year INTEGER
                );
            ''')

            # Create artworks table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS artworks (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    artist_id INTEGER,
                    date TEXT,
                    medium TEXT,
                    dimensions TEXT,
                    url TEXT,
                    FOREIGN KEY (artist_id) REFERENCES artists(id)
                );
            ''')

            # Insert sample artists
            cursor.execute('''
                INSERT INTO artists (name, nationality, gender, birth_year, death_year)
                VALUES
                ('Pablo Picasso', 'Spanish', 'Male', 1881, 1973),
                ('Vincent van Gogh', 'Dutch', 'Male', 1853, 1890)
                ON CONFLICT(name) DO NOTHING;
            ''')

            # Insert sample artworks
            cursor.execute('''
                INSERT INTO artworks (title, artist_id, date, medium, dimensions, url)
                VALUES
                ('Les Demoiselles d\'Avignon', 1, '1907', 'Oil on canvas', '243.9 cm × 233.7 cm', 'https://www.moma.org/collection/works/79766'),
                ('Starry Night', 2, '1889', 'Oil on canvas', '73.7 cm × 92.1 cm', 'https://www.moma.org/collection/works/79802')
                ON CONFLICT(title) DO NOTHING;
            ''')

            conn.commit()
            print("Tables created and sample data inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

    create_and_insert_data()

    root = tk.Tk()
    app = MoMAApp(root)
    root.mainloop()
