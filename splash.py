import tkinter as tk
from PIL import Image, ImageTk
import time
import subprocess


class Splash:
    def __init__(self, root):
        self.root = root
        self.root.title("Splash Screen")
        self.root.geometry("600x400+500+200")
        self.root.overrideredirect(True)  # Hide window frame

        # Load and display image
        self.load_image()

        # Delay and then open login window
        self.root.after(3000, self.open_login)

    def load_image(self):
        try:
            img = Image.open("icon/splash/Splash.jpg").resize((600, 400), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.img).pack()
        except Exception as e:
            print("Error loading splash image:", e)

    def open_login(self):
        self.root.destroy()
        subprocess.run(["python", "login.py"])  # Open login.py using subprocess


if __name__ == "__main__":
    root = tk.Tk()
    app = Splash(root)
    root.mainloop()