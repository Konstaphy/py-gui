from tkinter import *
from image import ImagePresentation

filters = ["median", "middle"]
salts = ["s&p", "bgsh"]


class App:
    def __init__(self):
        self.list_filters = None
        self.list = None
        self.frame = None
        self.root = Tk()
        self.root_setting()
        self.image_presentation = ImagePresentation(self.root)
        self.load_buttons()
        self.load_salt_select()
        self.load_filter_select()
        self.root.mainloop()

    def root_setting(self):
        self.root['bg'] = '#fafafa'
        self.root.geometry("800x700")
        self.root.resizable(width=False, height=False)
        self.frame = Frame(self.root)
        self.frame.place(relwidth=1, relheight=1)

    def load_buttons(self):
        btn_load = Button(self.frame, text="load image", command=self.image_presentation.open)
        btn_load.pack()

        btn_salt = Button(self.frame,
                          text="make it salty",
                          command=lambda: self.image_presentation.salty(0.01, self.list.curselection()))
        btn_salt.pack()

        btn_filter = Button(self.frame, text="filter da salt",
                            command=self.image_presentation.filter)
        btn_filter.pack()

        btn_save = Button(self.frame, text="save image", command=self.image_presentation.save_image)
        btn_save.pack()

    def load_salt_select(self):
        self.list = Listbox(self.frame)
        for salt in salts:
            self.list.insert(END, salt)

        self.list.pack()

    def load_filter_select(self):
        self.list_filters = Listbox(self.frame)
        for filter_section in filters:
            self.list_filters.insert(END, filter_section)

        self.list_filters.pack()


app = App()
