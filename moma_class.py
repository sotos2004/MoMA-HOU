# Database functions
# Version 1.2
#
# Created on 10/04/2024
# Updated on 03/06/2024
# ΠΛΗΠΡΟ 2023-2024 Ομαδική εργασία
# Μάμαλος Κωνσταντίνος
# Μπερνικόλας Μάριος
# Νούσας Γεώργιος
# Παπαδόπουλος Σωτήρης
#
# ChangeLog
# 1. first official commit
# 1.1 Added getArtists()
# 1.2 Added kwargs to getArtists() and getArtworks()

import pandas as pd
import sqlite3 as sql


class MoMA:
    def test(self):
        a = self.getArtworks(query="Artworks.objectID>451410")
       #a = self.getArtworks(departments="1,2")
        print(a);

    @staticmethod
    def __doc__():
        """
        Εμφανίζει τις public μεθόδους της κλάσης δίνοντας μια μικρή περιγραφή της λειτουργίας καθεμιάς της
        :rtype: null
        """
        print('GetNationalities() : ')
        print('getOnviews() : ')
        print('getDepartments() : ')
        print('getClassifications() : ')
        print('getArtworks() : ')
        print('getArtists() : ')
        print('getData(query) : ')
        print('Adminstrative Functions:')
        print('importData() : Εισαγωγή δεδομένων απο το Github repository του MoMA ')
        print('createDb() : Δημιουργία/Αρχικοποίηση βάσης')
        print('main() : ')

    def __init__(self):
        """
        Αρχικοποίηση της κλάσης
        """
        # TODO: get values from config file
        self.repo = 'https://media.githubusercontent.com/media/MuseumofModernArt/collection/main/'
        self.db = 'DATA/MoMA.db3'

    def __fetch_csv(self, contenttype):
        """
        Κατεβάζει απο το διαδίκτυο το csv και επιστρέφει ενα Pandas DataFrame object με τα περιεχόμενα του
        :rtype: object
        :param contenttype: string
        :return: Pandas Dataframe object
        """
        match contenttype:
            case 'Artists':
                fdata = self.repo + contenttype + '.csv'
            case 'Artworks':
                fdata = self.repo + contenttype + '.csv'
            case _:
                fdata = ''
        data = pd.read_csv(fdata)
        return data

    def __getDbNationalities(self):
        """
        Επιστρέφει τις εθνικότητες (Nationalities) που βρίσκονται στη βάση με κλειδί την ονομασία της εθνικότητας
        Χρησιμοποιήται κατά την εισαγωγή των δεδομένων στη βάση
        :return: Dictionary object
        """
        conn = sql.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT NationalityID, Nationality FROM Nationalities")
        rows = cursor.fetchall()
        nationalities_dict = {}
        for row in rows:
            NationalityID, Nationality = row
            nationalities_dict[Nationality] = NationalityID
        return nationalities_dict

    def __getDbOnviews(self):
        """
        Επιστρέφει τις θέσεις (onviews) που βρίσκονται στη βάση με κλειδί την ονομασία της θέσης
        Χρησιμοποιήται κατά την εισαγωγή των δεδομένων στη βάση
        :return: Dictionary object
        """
        conn = sql.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT OnViewID, OnView FROM OnViews")
        rows = cursor.fetchall()
        onviews_dict = {}
        for row in rows:
            OnViewID, OnView = row
            onviews_dict[OnView] = OnViewID
        return onviews_dict

    def __getDbDepartments(self):
        """
        Επιστρέφει τα τμήματα (Departments) που βρίσκονται στη βάση με κλειδί την ονομασία του τμήματος
        Χρησιμοποιήται κατά την εισαγωγή των δεδομένων στη βάση
        :return: Dictionary object
        """
        conn = sql.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT DepartmentID, Department FROM Departments")
        rows = cursor.fetchall()
        departments_dict = {}
        for row in rows:
            DepartmentId, Department = row
            departments_dict[Department] = DepartmentId
        return departments_dict

    def __getDbClassifications(self):
        """
        Επιστρέφει τις κατηγοριοποιήσεις (Classifications) που βρίσκονται
        στη βάση με κλειδί την ονομασία της κατηγοριοποίησης
        Χρησιμοποιήται κατά την εισαγωγή των δεδομένων στη βάση
        :return: Dictionary object
        """
        conn = sql.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT classificationID, Classification FROM Classifications")
        rows = cursor.fetchall()
        classifications_dict = {}
        for row in rows:
            ClassificationId, Classification = row
            classifications_dict[Classification] = ClassificationId
        return classifications_dict

    def __insertArtist(self, data):
        """
        Εισάγει τους καλλιτέχνες στη βάση και έμμεσα και τις εθνικότητες.
        :param data: Pandas Dataframe object
        :return: bool TRUE αν είναι επιτυχής η εισαγωγή ή FALSE στην αντίθετη περίπτωση
        """
        data['Nationality'].fillna('No Data', inplace=True)
        nationalities = self.__getDbNationalities()
        conn = sql.connect(self.db)
        # iterate over artists

        i = 0
        for index, row in data.iterrows():
            i = i + 1
            # check if artist nationality exist,else create entry in db and update nationalities dictionary
            country = row['Nationality']
            if country in nationalities:
                # get nationality id
                nationID = nationalities[country]
            else:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Nationalities (Nationality) VALUES (?)", (country[0::],))
                #  conn.commit()
                nationID = cursor.lastrowid
                nationalities.update({country: nationID})
            # insert artist data / on duplicate update
            cursorA = conn.cursor()
            row.fillna(' ', inplace=True)
            cursorA.execute('''INSERT OR IGNORE INTO Artists (ConstituentID, DisplayName, ArtistBio, NationalityID, 
            Gender, BeginDate, EndDate, WikiQID, ULAN) VALUES (?,?,?,?,?,?,?,?,?)''',
                            (row['ConstituentID'], row['DisplayName'][0::], str(row['ArtistBio'])[0::], nationID,
                             str(row['Gender'])[0::], row['BeginDate'], row['EndDate'], row['Wiki QID'], row['ULAN']))
            cursorA.execute('''UPDATE Artists SET 
                              DisplayName = ?, ArtistBio = ?, BeginDate = ?, EndDate = ?, 
                              WikiQID = ?, ULAN = ? 
                              WHERE ConstituentID = ?''',
                            (row['DisplayName'], row['ArtistBio'], row['BeginDate'], row['EndDate'],
                             row['Wiki QID'], row['ULAN'], row['ConstituentID']))
            eol = ''
            if i == 60:
                eol = '\n'
                i = 0
            print('.', end=eol)
        conn.commit()
        conn.close()
        # TODO: try catch return false etc...
        return True

    def __insertArtworks(self, data):
        data=data.loc[data['Department'].isin(["Painting & Sculpture" , "Media and Performance"] )]
        data['Department'].fillna('No Data', inplace=True)
        data['Classification'].fillna(' ', inplace=True)
        data['OnView'].fillna(' ', inplace=True)
        departments = self.__getDbDepartments()
        classifications = self.__getDbClassifications()
        onviews = self.__getDbOnviews()
        conn = sql.connect(self.db)
        # iterate over artworks
        print('Importing Artworks')
        i = 0
        for index, row in data.iterrows():
            i = i + 1
            # check if artwork department exist,else create entry in db and update departments dictionary
            department = row['Department']
            if department in departments:
                departmentId = departments[department]
            else:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Departments (Department) VALUES (?)", (department[0::],))
                #  conn.commit()
                departmentId = cursor.lastrowid
                departments.update({department: departmentId})

            classification = row['Classification']
            if classification in classifications:
                classificationId = classifications[classification]
            else:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Classifications (Classification) VALUES (?)", (classification[0::],))
                #  conn.commit()
                classificationId = cursor.lastrowid
                classifications.update({classification: classificationId})

            onview = row['OnView']
            if onview in onviews:
                onviewId = onviews[onview]
            else:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO OnViews (OnView) VALUES (?)", (onview[0::],))
                #  conn.commit()
                onviewId = cursor.lastrowid
                onviews.update({onview: onviewId})

            # insert artwork data / on duplicate update
            cursorA = conn.cursor()

            row.fillna('', inplace=True)
            # print(row)

            cursorA.execute('''INSERT OR IGNORE INTO Artworks
                              (Title, Dimenssions, CreditLine, AccessionNumber, DateAcquired,
                               Catalogued, URL, ImageURL, Circumeferance,Depth,
                               Diameter, Height, Length, Weight, Width,
                               SeatHeight, Duration, Medium, Classification, Department,
                               OnView, objectID) VALUES
                              (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                            (row['Title'][0::], row['Dimensions'][0::], row['CreditLine'][0::],
                             row['AccessionNumber'][0::], row['DateAcquired'][0::],
                             row['Cataloged'][0::], row['URL'][0::], row['ImageURL'][0::], row['Circumference (cm)'],
                             row['Depth (cm)'],
                             row['Diameter (cm)'], row['Height (cm)'], row['Length (cm)'], row['Weight (kg)'],
                             row['Width (cm)'],
                             row['Seat Height (cm)'], row['Duration (sec.)'], row['Medium'][0::], classificationId,
                             departmentId,
                             onviewId, row['ObjectID']))
            cursorA.execute('''UPDATE Artworks SET
                               Title =?, Dimenssions =?, CreditLine =?, AccessionNumber =?, DateAcquired =?,
                               Catalogued =?, URL =?, ImageURL =?, Circumeferance =?,Depth =?,
                               Diameter =?, Height =?, Length =?, Weight =?, Width =?,
                               SeatHeight =?, Duration =?, Medium =?, Classification =?, Department =?,
                               OnView =? ''',
                            (row['Title'][0::], row['Dimensions'][0::], row['CreditLine'][0::],
                             row['AccessionNumber'][0::], row['DateAcquired'][0::],
                             row['Cataloged'][0::], row['URL'][0::], row['ImageURL'][0::], row['Circumference (cm)'],
                             row['Depth (cm)'],
                             row['Diameter (cm)'], row['Height (cm)'], row['Length (cm)'], row['Weight (kg)'],
                             row['Width (cm)'],
                             row['Seat Height (cm)'], row['Duration (sec.)'], row['Medium'][0::], classificationId,
                             departmentId,
                             onviewId))
            artists = row['ConstituentID'].split(', ')
            for artist in artists:
                cursorA.execute('''INSERT OR IGNORE INTO ArtworkArtists
                                             (ConstituentID, ObjectID) VALUES
                                             (?,?)''',
                                (artist, row['ObjectID']))
            eol = ''
            if i == 60:
                eol = '\n'
                i = 0
            print('.', end=eol)
            conn.commit()
        conn.close()
        print('\nΕπιτυχής εισαγωγή')
        return True

    def __importArtists(self):
        """
        Φέρνει το csv με τα δεδομένα των καλλιτεχνών και εισάγει τους καλλιτέχνες στη βάση
        :return: bool TRUE αν είναι επιτυχής η εισαγωγή ή FALSE στην αντίθετη περίπτωση
        """
        artists = self.__fetch_csv('Artists')
        return self.__insertArtist(artists)

    def __importArtworks(self):
        """
        Φέρνει το csv με τα δεδομένα των έργων και εισάγει τα έργα στη βάση
        :return: bool TRUE αν είναι επιτυχής η εισαγωγή ή FALSE στην αντίθετη περίπτωση
        """
        artworks = self.__fetch_csv('Artworks')
        return self.__insertArtworks(artworks)

    def getNationalities(self):
        """
        Διαβάζει και επιστρέφει τις εθνικότητες που υπάρχουν στη βάση
        :return: dictionary object με κλειδί το ID
        """
        conn = sql.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT NationalityID, Nationality FROM Nationalities")
        rows = cursor.fetchall()
        nationalities_dict = {}
        for row in rows:
            NationalityID, Nationality = row
            nationalities_dict[NationalityID] = Nationality
        return nationalities_dict

    def getOnviews(self):
        """
        Διαβάζει και επιστρέφει τις θέσεις που υπάρχουν στη βάση
        :return: dictionary object με κλειδί το ID
        """
        conn = sql.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT OnViewID, OnView FROM OnViews")
        rows = cursor.fetchall()
        onviews_dict = {}
        for row in rows:
            OnViewID, OnView = row
            onviews_dict[OnViewID] = OnView
        return onviews_dict

    def getDepartments(self):
        """
        Διαβάζει και επιστρέφει τα τμήματα που υπάρχουν στη βάση
        :return: dictionary object με κλειδί το ID
        """
        conn = sql.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT DepartmentID, Department FROM Departments")
        rows = cursor.fetchall()
        departments_dict = {}
        for row in rows:
            DepartmentID, Department = row
            departments_dict[DepartmentID] = Department
        return departments_dict

    def getClassifications(self):
        """
        Διαβάζει και επιστρέφει τις κατηγοριοποιήσεις που υπάρχουν στη βάση
        :return: dictionary object με κλειδί το ID
        """
        conn = sql.connect(self.db)
        cursor = conn.cursor()
        cursor.execute("SELECT classificationID, Classification FROM Classifications")
        rows = cursor.fetchall()
        classifications_dict = {}
        for row in rows:
            ClassificationId, Classification = row
            classifications_dict[ClassificationId] = Classification
        return classifications_dict

    def getArtworks(self,**kwargs):
        """
        Διαβάζει και επιστρέφει τα έργα που υπάρχουν στη βάση
        :return: Pandas dataframe object
        """

        # χρειαζομαστε τουλαχιστον μια συνθήκη για το where του query
        where = ['1=1'];
        if 'classifications' in kwargs:
            where.append('Classifications.ClassificationId in ( ' + kwargs["classifications"] +')')
        if 'departments' in kwargs:
            where.append('departments.DepartmentID in ( ' + kwargs["departments"] +')')
        if 'onviews' in kwargs:
            where.append('onViews.OnViewID in ( ' + kwargs["onviews"] +')')
        if 'query' in kwargs:
            where.append(kwargs.get("query"))

        conn = sql.connect(self.db)
        query = '''Select 
        Artworks.objectID, Artworks.Title, Artworks.Dimenssions, Artworks.CreditLine, 
        Artworks.AccessionNumber, Artworks.DateAcquired, Artworks.Catalogued, Artworks.URL, Artworks.ImageURL, 
        Artworks.Circumeferance, Artworks.Depth, Artworks.Diameter, Artworks.Height, Artworks.Length, 
        Artworks.Weight, Artworks.Width, Artworks.SeatHeight, Artworks.Duration, Artworks.Medium, 
        departments.Department, classifications.Classification, onViews.OnView 
        from Artworks 
        left join Classifications  on classifications.ClassificationId=Artworks.Classification 
        left join Departments on departments.DepartmentID=Artworks.Department 
        left join OnViews on onViews.OnViewID=Artworks.OnView 
        where ''' + ''' and '''.join(where)
        print(query)
        return pd.read_sql(query, conn)

    def getArtists(self,**kwargs):
        """
        Διαβάζει και επιστρέφει τους καλλιτέχνες που υπάρχουν στη βάση
        :return: Pandas dataframe object
        """
        # χρειαζομαστε τουλαχιστον μια συνθήκη για το where του query
        where=['1=1']
        if 'nationalities' in kwargs:
            where.append('natio.NationalityId in ( ' + kwargs["nationalities"] +')')
        if 'gender' in kwargs:
            where.append("art.Gender = '" + kwargs["gender"] + "'")
        if 'query' in kwargs:
            where.append(kwargs.get("query"))

        conn = sql.connect(self.db)
        query = '''
        Select art.*, nation.* 
        from Artists art
        left join Nationalities nation on natio.NationalityId = art.NationlityId 
        where '''+ ' and '.join(where)
        return pd.read_sql(query, conn)

    def getData(self, query):
        """
        Διαβάζει και επιστρέφει δεδομένα βάση του query που περνιέται παραμετρικά
        :return: Pandas dataframe object
        """
        conn = sql.connect(self.db)
        return pd.read_sql(query, conn)

    def importData(self):
        """
        Εισάγει ολα τα δεδομένα απο τα csv αρχεία στη βάση
        :return: dictionary object με κλειδί το ID
        """
        artists = self.__fetch_csv('Artists')
        self.__insertArtist(artists)
        artworks = self.__fetch_csv('Artworks')
        self.__insertArtworks(artworks)

    def createDb(self):
        """
        Δημιουργεί τη βάση δεδομένων - αν υπάρχει ήδη διαγράφει τα υπάρχοντα δεδομένα
        :return: boolean
        """
        # TODO : get filename from configuration
        # TODO : add try catch and return value
        # TODO : ask verification

        conn = sql.connect(self.db)
        cursor = conn.cursor()
        with open('DATA/main.sql', 'r') as sql_file:
            sql_script = sql_file.read()

        # Execute the SQL script
        cursor.executescript(sql_script)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def main(self):
        """
            Κυρίως μέθοδος
            Χρησιμοποιήται μόνο για την ανάπτυξη του προγράμματος
        """
        choice = 0
        # Υλοποίηση μενού επιλογών
        while True:
            # TODO : add option to fetch all departments
            print("Μενού Εισαγωγής Δεδομένων")
            print("1. Εισαγωγή Καλλιτεχνών απο web")
            print("2. Εισαγωγή Έργων απο web")
            print("4. (Επανα)Δημιουργία βάσης")
            print("5. Έξοδος")
            print("6. Test")
            # αμυντικός προγραμματισμός επιλογής μενού
            while choice < 1 or choice > 6:
                choice = int(input(f"Παρακαλώ εισάγετε την επιλογή σας: "))
                if choice < 1 or choice > 6:
                    print("Επιλογή εκτός ορίων. Παρακαλώ προσπαθήστε ξανά!")
            match choice:
                case 1:
                    choice = 0
                    self.__importArtists()
                case 2:
                    choice = 0
                    self.__importArtworks()
                case 3:
                    choice = 0
                case 4:
                    choice = 0
                    self.createDb()
                case 5:
                    print("Έξοδος. Καλή συνέχεια!")
                    exit(0)
                case 6:
                   choice = 0
                   self.test()


# για να μπορεί να εκτελείτε και ανεξάρτητα για την περίοδο ανάπτυξης
if __name__ == '__main__':
    m = MoMA()
    m.main()

 #   import moma_class as mc
#
#    if __name__ == '__main__':
 #       md = mc.MoMA()
  #      # md.main()
  #      a = md.getArtworks()
  #      print(a)
