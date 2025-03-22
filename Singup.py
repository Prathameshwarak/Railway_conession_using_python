from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import mysql.connector
import re

class Signup:
    def __init__(self, root):
        self.root = root
        self.root.title("Signup Page")
        self.root.geometry("900x550+200+100")
        self.root.config(bg="#A8CBFF")

        # Title Label
        stud_msg = Label(root, text="Atharva College of Engineering Student Portal", font=("Serif", 20, "bold"),
                         bg="#A8CBFF")
        stud_msg.place(x=250, y=30)

        # Student ID
        Label(root, text="Student ID", bg="#A8CBFF").place(x=30, y=100)
        self.sid_txt = Entry(root)
        self.sid_txt.place(x=170, y=100, width=150)

        # Gender
        Label(root, text="Gender", bg="#A8CBFF").place(x=350, y=100)
        self.stdGDR = StringVar()
        self.gender_dropdown = OptionMenu(root, self.stdGDR, "Male", "Female", "Other")
        self.gender_dropdown.place(x=400, y=100, width=175)

        # Name
        Label(root, text="Name", bg="#A8CBFF").place(x=30, y=135)
        self.pnametxt = Entry(root)
        self.pnametxt.place(x=170, y=135, width=405)

        # Date of Birth (Using DateEntry instead of Entry and Calendar button)
        Label(root, text="Date of Birth", bg="#A8CBFF").place(x=30, y=170)
        self.dob_txt = DateEntry(root, date_pattern='y-mm-dd')
        self.dob_txt.place(x=170, y=170, width=125)

        # Year
        Label(root, text="Year", bg="#A8CBFF").place(x=350, y=170)
        self.ageyr_txt = Entry(root)
        self.ageyr_txt.place(x=400, y=170, width=50)

        # Address
        Label(root, text="C/o. Address", bg="#A8CBFF").place(x=30, y=205)
        self.addresstxt1 = Entry(root)
        self.addresstxt1.place(x=170, y=205, width=405)

        Label(root, text="Perm. Address", bg="#A8CBFF").place(x=30, y=240)
        self.addresstxt2 = Entry(root)
        self.addresstxt2.place(x=170, y=240, width=405)

        # Email & Password
        Label(root, text="Email Id", bg="#A8CBFF").place(x=30, y=310)
        self.colemailtxt = Entry(root)
        self.colemailtxt.place(x=170, y=310, width=405)

        Label(root, text="Password", bg="#A8CBFF").place(x=30, y=345)
        self.colpasswordtxt = Entry(root, show="*")
        self.colpasswordtxt.place(x=170, y=345, width=405)

        # Buttons
        self.create = Button(root, text="Create", bg="#427FDB", fg="black", command=self.create_user)
        self.create.place(x=250, y=400, width=150, height=40)

        self.back = Button(root, text="Back", bg="#427FDB", fg="black", command=self.go_back)
        self.back.place(x=500, y=400, width=150, height=40)

        # Load and Display Image
        self.load_profile_image()

    def load_profile_image(self):
        try:
            image_path = "icon/student.png"  # Adjust path if needed
            image = Image.open(image_path)
            image = image.resize((250, 250), Image.Resampling.LANCZOS)  # Resize image
            self.profile_photo = ImageTk.PhotoImage(image)

            self.profile_label = Label(self.root, image=self.profile_photo, bg="#A8CBFF")
            self.profile_label.place(x=620, y=120, width=250, height=250)
        except Exception as e:
            print("Error loading image:", e)

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def validate_password(self, password):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{10,}$'
        return re.match(pattern, password)

    def create_user(self):
        email = self.colemailtxt.get()
        password = self.colpasswordtxt.get()

        if not self.validate_email(email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address!")
            return

        if not self.validate_password(password):
            messagebox.showerror("Invalid Password",
                                 "Password must contain at least 10 characters, one uppercase, one lowercase, one digit, and one special character.")
            return

        messagebox.showinfo("Success", "Validations Passed!")
        # Database insertion logic goes here

    def go_back(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Signup(root)
    root.mainloop()
