import cv2
from tkinter import *
from PIL import Image, ImageTk


class CameraApp:
    def __init__(self, master):
        self.master = master
        master.geometry("640x480")
        master.title("OpenCV Camera Stream in Tkinter")

        self.valid_cameras = []
        for i in range(10):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                self.valid_cameras.append(i)
            cap.release()

        if not self.valid_cameras:
            print("Error: No camera detected, please connect a camera and try again.")
            master.destroy()
            return

        self.var = StringVar()
        self.var.set(self.valid_cameras[0])
        self.cap = cv2.VideoCapture(self.valid_cameras[0])

        self.label = Label(master)
        self.label.pack()
        self.option = OptionMenu(master, self.var, *self.valid_cameras, command=self.update_camera)
        self.option.pack()

        self.show_frame()

    def update_camera(self, varName):
        index = int(varName)
        self.cap.release()
        self.cap = cv2.VideoCapture(index)
        if self.cap.isOpened():
            print("Camera with index:", index, "opened successfully.")
        else:
            print("Error: Could not open camera with index: ", index)
            self.var.set(self.valid_cameras[0])
            self.cap = cv2.VideoCapture(self.valid_cameras[0])

    def show_frame(self):
        _, frame = self.cap.read()
        if frame is None:
            print("Error: No camera detected, please connect a camera and try again.")
            self.master.destroy()
            return
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        self.label.after(10, self.show_frame)


root = Tk()
my_gui = CameraApp(root)
root.mainloop()
