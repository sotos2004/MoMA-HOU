import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014]
artworks_count = [100, 120, 90, 150, 200]

plt.plot(years, artworks_count, marker='o')
plt.xlabel('Έτος')
plt.ylabel('Πλήθος Έργων')
plt.title ('Αύξηση Πλήθους Έργων με την Πάροδο του Χρόνου')
plt.grid(True)
plt.show()

categories = ['Ζωγραφική', 'Γλυπτική', 'Φωτογραφία', 'Βίντεο Τέχνη']
artworks_per_category = [300, 200, 150, 100]

plt.pie(artworks_per_category, labels=categories, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Κατανομή Έργων ανά Κατηγορία')
plt.show()

years = [2010, 2011, 2012, 2013, 2014]
artworks_count = [100, 120, 90, 150, 200]

plt.bar(years, artworks_count, color='skyblue')
plt.xlabel('Έτος')
plt.ylabel('Πλήθος Έργων')
plt.title('Ανάλυση Έργων ανά Χρονιά')
plt.show()

categories = ['Ζωγραφική', 'Γλυπτική', 'Φωτογραφία', 'Βίντεο Τέχνη']
artworks_per_category = [300, 200, 150, 100]

plt.bar(categories, artworks_per_category, color='lightgreen')
plt.xlabel('Κατηγορία')
plt.ylabel('Πλήθος Έργων')
plt.title('Συνολικά Έργα ανά Κατηγορία')
plt.xticks(rotation=45)
plt.show()

countries = ['ΗΠΑ', 'Γαλλία', 'Ισπανία', 'Ιταλία', 'Γερμανία']
artworks_per_country = [500, 400, 300, 250, 200]

plt.barh(countries, artworks_per_country, color='salmon')
plt.xlabel('Πλήθος Έργων')
plt.ylabel('Χώρα')
plt.title('Κατανομή Έργων ανά Χώρα')
plt.show()
