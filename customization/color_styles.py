#Αυτό το αρχείο χρησιμοποιείται ώστε να οριστούν τα custom χρώματα τυης εφαρμογής MoMA εδώ για την καλύτερη
#αναγνωσιμότητα των υπολοίπων αρχείων.

#Επίσης εδώ θα οριστούνε τσ τροποποιημένα stytes του ttk της

from tkinter import ttk

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"

'''

style = ttk.Style()
style.theme_use("clam")

style.configure("Timer.TFrame",
    background=COLOUR_LIGHT_BACKGROUND)

style.configure("Background.TFrame",
    background=COLOUR_PRIMARY)

style.configure("TimerText.TLabel",
    background=COLOUR_LIGHT_BACKGROUND,
    foreground=COLOUR_DARK_TEXT,
    font="Courier 46"
)
style.configure("LightText.TLabel",
    background=COLOUR_PRIMARY,
    foreground=COLOUR_LIGHT_TEXT,
    font=("TkDefaultFont", 11)
)

style.configure("PomodoroButton.TButton",
    background=[COLOUR_SECONDARY],
    foreground=COLOUR_LIGHT_TEXT,
    font=("TkDefaultFont", 11)
)

style.map("PomodoroButton.TButton",
    background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
)
'''