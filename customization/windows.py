#Ρύθμιση μόνο για windows ώστε σε οθόνες με υπερ-υψηλή ανάλυση (2Κ+) να φαίνονται σωστά οι χαρακτήρες
def set_dpi_awareness():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass