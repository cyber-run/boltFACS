import os
import sqlite3
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Viewer")

        self.conn = sqlite3.connect('../images.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS images (path text)''')
        self.conn.commit()

        self.select_folder_button = tk.Button(master, text="Select Folder", command=self.select_folder)
        self.select_folder_button.grid(row=0, column=0, sticky='W')

        self.image_label = tk.Label(master, height=500, width=500)
        self.image_label.grid(row=1, column=1, sticky='E')

        self.previous_button = tk.Button(master, text="<", command=self.previous_image)
        self.previous_button.grid(row=1, column=0, sticky='W')

        self.next_button = tk.Button(master, text=">", command=self.next_image)
        self.next_button.grid(row=1, column=2, sticky='E')

        self.image_list = []
        self.image_index = 0

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.cursor.execute("INSERT INTO images (path) VALUES (?)", (folder_path,))
        self.conn.commit()
        self.load_images(folder_path)

    def load_images(self, folder_path):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png"):
                    self.image_list.append(os.path.join(root, file))
        self.show_image()

    def previous_image(self):
        if self.image_index > 0:
            self.image_index -= 1
            self.show_image()

    def next_image(self):
        if self.image_index < len(self.image_list) - 1:
            self.image_index += 1
            self.show_image()

    def show_image(self):
        image_path = self.image_list[self.image_index]
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.image_label.config(image=image)
        self.image_label.image = image


root = tk.Tk()
app = App(root)
root.mainloop()
