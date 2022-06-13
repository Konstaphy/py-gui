from tkinter import Label
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np


class ImagePresentation:
    def __init__(self, root):
        self.path = ""
        self.root = root

    def load_image(self):
        # load photo to the screen
        img_label = Image.open(self.path)
        image_label = ImageTk.PhotoImage(img_label)
        panel = Label(self.root, image=image_label)
        panel.image = image_label
        panel.grid(row=1)

    def open(self):
        # load and save the photo
        filename = filedialog.askopenfilename(title='Open')
        img = Image.open(filename)
        img = img.resize((256, 256))
        self.path = f'photos/{filename.split("/")[-1]}'
        img.save(self.path)
        self.load_image()

    def salty(self, amount, typea):
        if self.path == "":
            return
        if typea[0] == 1:
            self.gauss_noise()
            return
        output = np.copy(np.asarray(Image.open(self.path)))
        # add salt
        nb_salt = np.ceil(amount * output.size * 0.5)
        coords = [np.random.randint(0, i - 1, int(nb_salt)) for i in output.shape]
        output[tuple(coords)] = 1
        # add pepper
        nb_pepper = np.ceil(amount * output.size * 0.5)
        coords = [np.random.randint(0, i - 1, int(nb_pepper)) for i in output.shape]
        output[tuple(coords)] = 0
        Image.fromarray(output).save(self.path)
        self.load_image()

    def gauss_noise(self):
        row, col, ch = np.array(Image.open(self.path)).shape
        mean = 0
        var = 0.4
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col, ch))
        gauss = gauss.reshape(row, col, ch)
        noisy = np.array(Image.open(self.path)) + gauss
        Image.fromarray(noisy.astype(np.uint8)).save(self.path)
        self.load_image()

    def filter(self):
        data_final = self.median()
        Image.fromarray(data_final.astype(np.uint8)).save(self.path)
        self.load_image()

    def median(self):
        data = np.array(Image.open(self.path).convert("L"))
        temp = []
        indexer = 3 // 2
        data_final = np.zeros((len(data), len(data[0])))
        for i in range(len(data)):
            for j in range(len(data[0])):
                for z in range(3):
                    if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                        for c in range(3):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                            temp.append(0)
                        else:
                            for k in range(3):
                                temp.append(data[i + z - indexer][j + k - indexer])

                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []
        return data_final

    def save_image(self):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if file:
            Image.open(self.path).save(file)
