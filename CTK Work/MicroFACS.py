# import tkinter
# from tkinter import filedialog
import customtkinter as ctk
import os

import cv2
from PIL import Image, ImageTk
# import sqlite3
# import ImageCarouselWidget
# from ImageCarouselWidget import *
from MiscFunctions import *
from CTkCamera import *


def bright_callback(x, y, z):
    print("variable changed!")
    # bright_cam = (x[y])
    print(x[1])


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")
        self.minsize(700, 450)
        self.title("Micro FACS")

        self.bright_cap = cv2.VideoCapture(0)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icons")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "../bolt.png")), size=(50, 50))
        self.home_image = ctk.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
        self.settings_image = ctk.CTkImage(Image.open(os.path.join(image_path, "settings.png")), size=(20, 20))
        self.play_image = ctk.CTkImage(Image.open(os.path.join(image_path, "play.png")), size=(20, 20))
        self.refresh_image = ctk.CTkImage(Image.open(os.path.join(image_path, "refresh.png")), size=(15, 15))

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Mirco FACS",
                                                   image=self.logo_image,
                                                   compound="left",
                                                   font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="Home",
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                            border_spacing=10, text="Settings",
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=self.settings_image, anchor="w",
                                            command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                            border_spacing=10, text="Run",
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=self.play_image, anchor="w",
                                            command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame,
                                                      values=["Light", "Dark", "System"],
                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # -------------------------------- Create home frame --------------------------------
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # create ctk refresh camera button
        self.get_cameras = ctk.CTkButton(self.home_frame, image=self.refresh_image, text="Refresh Cameras",
                                         compound="left", command=lambda: load_cameras(self.camera_dropdown))
        # pack ctk button into home frame
        self.get_cameras.grid(row=0, column=1, padx=20, pady=10)

        # Create camera view group
        self.bright_cam_frame = ctk.CTkFrame(self.home_frame)
        self.bright_cam_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.bright_cam_frame.grid_columnconfigure(0, weight=1)
        self.bright_cam_frame.grid_rowconfigure(0, weight=1)
        # Create bright-view label
        self.bright_cam_label = ctk.CTkLabel(master=self.bright_cam_frame, text="Bright-view Camera")
        self.bright_cam_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="")
        # Create a drop-down list initialise text as select frame
        self.camera_var = ctk.StringVar()
        self.camera_var.set("Select Camera")
        self.camera_var.trace("w", bright_callback)
        self.camera_dropdown = ctk.CTkOptionMenu(self.bright_cam_frame, variable=self.camera_var, values=get_cameras(), command=lambda cam_id: self.update_camera(cam_id, self.bright_cap))
        self.camera_dropdown.grid(row=2, column=0, padx=20, pady=10)
        # Create bright-view camera
        # self.video_source = int(self.camera_var.get())
        # self.vid = MyVideoCapture(self.video_source, 500, 500)

        # -------------------------------- create second frame --------------------------------
        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # -------------------------------- create third frame --------------------------------
        self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    # set button color and frame display
    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def conversion(self, event=None):
        num = int(self.camera_var.get())
        print(num)

    def show_frame(self, cap, label):
        _, frame = cap.read()
        if frame is None:
            print("Error: No camera detected, please connect a camera and try again.")
            return
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        label.after(10, self.show_frame)

    def update_camera(self, cam_id, old_cap):
        cap = old_cap
        try:
            index = int(cam_id)
            if cap.get(cv2.CAP_PROP_POS_FRAMES) != index:
                cap.release()
                new_cap = cv2.VideoCapture(index)
            if not new_cap.isOpened():
                raise Exception("Could not open camera with index: ", index)
        except Exception as e:
            print("Error:", e)
            if old_cap is not None:
                cap = old_cap
        else:
            old_cap = new_cap
            print("Camera with index:", index, "opened successfully.")



if __name__ == "__main__":
    app = App()
    app.mainloop()



