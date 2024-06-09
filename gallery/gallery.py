from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from gallery import *

root = Tk()
root.title("efarmogi")
root.geometry("1366x768")
root.configure(bg="blue")
list_items = ['adwad','fawefaw','fawefg']

l1 = Label(root, text="select Nationality", width=20, height=1)
l2 = Label(root, text="select Gender", width=20, height=1)
l3 = Label(root, text="select Name", width=20, height=1)
l4 = Label(root, text="select Begindate", width=20, height=1)
l5 = Label(root, text="select EndDate", width=20, height=1)
l6 = Label(root, text="select onViews", width=20, height=1)
l7 = Label(root, text="select Classification", width=20, height=1)
l8 = Label(root, text="select Departments", width=20, height=1)

l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=0, column=1, padx=5, pady=5)
l3.grid(row=0, column=2, padx=5, pady=5)
l4.grid(row=0, column=3, padx=5, pady=5)
l5.grid(row=0, column=4, padx=5, pady=5)
l6.grid(row=0, column=5, padx=5, pady=5)
l7.grid(row=0, column=6, padx=5, pady=5)
l8.grid(row=0, column=7, padx=5, pady=5)

combo_box1 = ttk.Combobox(root, values=list_items, width=20)
combo_box2 = ttk.Combobox(root, values=list_items, width=20)
combo_box3 = ttk.Combobox(root, values=list_items, width=20)
combo_box4 = ttk.Combobox(root, values=list_items, width=20)
combo_box5 = ttk.Combobox(root, values=list_items, width=20)
combo_box6 = ttk.Combobox(root, values=list_items, width=20)
combo_box7 = ttk.Combobox(root, values=list_items, width=20)
combo_box8 = ttk.Combobox(root, values=list_items, width=20)

combo_box1.grid(row=1, column=0, padx=5, pady=5)
combo_box2.grid(row=1, column=1, padx=5, pady=5)
combo_box3.grid(row=1, column=2, padx=5, pady=5)
combo_box4.grid(row=1, column=3, padx=5, pady=5)
combo_box5.grid(row=1, column=4, padx=5, pady=5)
combo_box6.grid(row=1, column=5, padx=5, pady=5)
combo_box7.grid(row=1, column=6, padx=5, pady=5)
combo_box8.grid(row=1, column=7, padx=5, pady=5)

combo_box1.bind('<KeyRelease>', lambda event: search(event, combo_box1))
combo_box2.bind('<KeyRelease>', lambda event: search(event, combo_box2))
combo_box3.bind('<KeyRelease>', lambda event: search(event, combo_box3))
combo_box4.bind('<KeyRelease>', lambda event: search(event, combo_box4))
combo_box5.bind('<KeyRelease>', lambda event: search(event, combo_box5))
combo_box6.bind('<KeyRelease>', lambda event: search(event, combo_box6))
combo_box7.bind('<KeyRelease>', lambda event: search(event, combo_box7))
combo_box8.bind('<KeyRelease>', lambda event: search(event, combo_box8))

combo_box1.current(0)
combo_box2.current(0)
combo_box3.current(0)
combo_box4.current(0)
combo_box5.current(0)
combo_box6.current(0)
combo_box7.current(0)
combo_box8.current(0)

def search(event, combo_box):
    value = event.widget.get()
    if value == '':
        combo_box['values'] = list_items
    else:
        data = [item for item in list_items if value.lower() in item.lower()]
        combo_box['values'] = data


image1 = ImageTk.PhotoImage(Image.open('images/fotos/01.jpg').resize((1066,568)))
image2 = ImageTk.PhotoImage(Image.open('images/fotos/02.jpg').resize((1066,568)))
image3 = ImageTk.PhotoImage(Image.open('images/fotos/03.jpg').resize((1066,568)))
image4 = ImageTk.PhotoImage(Image.open('images/fotos/04.jpg').resize((1066,568)))
image5 = ImageTk.PhotoImage(Image.open('images/fotos/05.jpg').resize((1066,568)))
image_list = [image1, image2, image3, image4, image5]
counter = 0

def ChangeImage1():
    global counter
    counter = (counter + 1) % len(image_list)
    imageLabel.config(image=image_list[counter])
    infoLabel.config(text=f"Image {counter + 1} of {len(image_list)}")

def ChangeImage2():
    global counter
    counter = (counter - 1) % len(image_list)
    imageLabel.config(image=image_list[counter])
    infoLabel.config(text=f"Image {counter + 1} of {len(image_list)}")

imageLabel = Label(root, image=image1)
infoLabel = Label(root, text="Image 1 of 5", font="Helvetica, 20")
button1 = Button(root, text="previous", width=20, height=2, bg="blue", fg="white", command=ChangeImage2)
button2 = Button(root, text="next", width=20, height=2, bg="blue", fg="white", command=ChangeImage1)

imageLabel.grid(row=2, column=0, columnspan=8, pady=10)
infoLabel.grid(row=3, column=0, columnspan=8)
button1.grid(row=4, column=3, pady=10)
button2.grid(row=4, column=4, pady=10)

root.mainloop()
