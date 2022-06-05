from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='"pen')
    return filename



def open_img():
    # Select the Imagename  from a folder
    x = openfilename()

    # opens the image
    img = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((128, 128), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label
    panel = Label(root, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=2)


def make_salty():
    print("huy")


root = Tk()

root['bg'] = '#fafafa'
root.geometry("500x400")
root.resizable(width=False, height=False)

frame = Frame(root)
frame.place(relwidth=1, relheight=1)

btn = Button(frame, text="load image", command=open_img)
btn.pack()

btn = Button(frame, text="make it salty", command=make_salty)
btn.pack()

btn = Button(frame, text="filter da salt", command=make_salty)
btn.pack()

btn = Button(frame, text="save image", command=make_salty)
btn.pack()

root.mainloop()
