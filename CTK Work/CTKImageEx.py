import customtkinter as CTk
import os
from PIL import Image

import ImageCarouselWidget


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")
        self.minsize(700, 450)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                  "../icons")
        self.logo_image = CTk.CTkImage(Image.open(os.path.join(image_path, "../bolt.png")),
                                       size=(50, 50))
        self.large_test_image = CTk.CTkImage(Image.open(os.path.join(image_path, "../bolt.png")),
                                             size=(500, 150))
        self.image_icon_image = CTk.CTkImage(Image.open(os.path.join(image_path, "settings.png")),
                                                       size=(20, 20))
        self.home_image = CTk.CTkImage(Image.open(os.path.join(image_path, "home.png")), size=(20, 20))
        self.chat_image = CTk.CTkImage(Image.open(os.path.join(image_path, "settings.png")), size=(20, 20))
        self.add_user_image = CTk.CTkImage(Image.open(os.path.join(image_path, "play.png")), size=(20, 20))

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = CTk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = CTk.CTkLabel(self.navigation_frame, text="Mirco FACS",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=CTk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = CTk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = CTk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = CTk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Run",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = CTk.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # ---------------- Create home frame ----------------
        self.home_frame = CTk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = CTk.CTkLabel(self.home_frame, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = CTk.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = CTk.CTkButton(self.home_frame, text="CTkButton",
                                                           image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = CTk.CTkButton(self.home_frame, text="CTkButton",
                                                           image=self.image_icon_image, compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = CTk.CTkButton(self.home_frame, text="CTkButton",
                                                           image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame_button_5 = CTk.CTkButton(self.home_frame, text="CTkButton",
                                                           image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_5.grid(row=1, column=1, padx=20, pady=10)

        self.spinbox_1 = ImageCarouselWidget.FloatSpinbox(self.home_frame, width=300, step_size=3)
        self.spinbox_1.grid(row=0, column=1, padx=20, pady=10)

        self.spinbox_1.set(35)
        print(self.spinbox_1.get())

        # ---------------- create second frame ----------------
        self.second_frame = CTk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # ---------------- create third frame ----------------
        self.third_frame = CTk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
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
        CTk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
