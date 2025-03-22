from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class Signup:
    def __init__(self, root):
        self.root = root
        self.root.title("Signup Page")
        self.root.geometry("900x550+200+100")
        self.root.config(bg="#A8CBFF")

        # Title Label
        stud_msg = Label(root, text="Atharva College of Engineering Student Portal", font=("Serif", 20, "bold"), bg="#A8CBFF")
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

        # Date of Birth
        Label(root, text="Date of Birth", bg="#A8CBFF").place(x=30, y=170)
        self.dob_txt = Entry(root)
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

        # Branch
        Label(root, text="Branch", bg="#A8CBFF").place(x=30, y=275)
        self.sbranch_txt = StringVar()
        self.branch_dropdown = OptionMenu(root, self.sbranch_txt, "CMPN", "INFT", "ECS", "ELEC", "EXTC", "Other")
        self.branch_dropdown.place(x=170, y=275, width=125)

        # Class & Roll ID
        Label(root, text="Class", bg="#A8CBFF").place(x=350, y=275)
        self.sclass_txt = Entry(root)
        self.sclass_txt.place(x=400, y=275, width=50)

        Label(root, text="Roll Id", bg="#A8CBFF").place(x=475, y=275)
        self.srollid_txt = Entry(root)
        self.srollid_txt.place(x=525, y=275, width=50)

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

    def create_user(self):
        """ Connect to MySQL and insert the signup details """
        if not self.sid_txt.get() or not self.stdGDR.get() or not self.pnametxt.get() or not self.dob_txt.get() or \
           not self.ageyr_txt.get() or not self.addresstxt1.get() or not self.addresstxt2.get() or not self.sbranch_txt.get() or \
           not self.sclass_txt.get() or not self.srollid_txt.get() or not self.colemailtxt.get() or not self.colpasswordtxt.get():
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='rlwy_consession')
            cursor = conn.cursor()

            insert_query = """
            INSERT INTO registered_students (Student_ID, Gender, Name, DOB, Year, C_Address, P_Address, Branch, Class, Roll_ID, Email, Password)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                self.sid_txt.get(), self.stdGDR.get(), self.pnametxt.get(), self.dob_txt.get(), int(self.ageyr_txt.get()),
                self.addresstxt1.get(), self.addresstxt2.get(), self.sbranch_txt.get(), self.sclass_txt.get(),
                self.srollid_txt.get(), self.colemailtxt.get(), self.colpasswordtxt.get()
            )

            cursor.execute(insert_query, values)

            # Insert into users table with role as 'student'
            insert_query_user = """
                   INSERT INTO user (Email, Password, Role)
                   VALUES (%s, %s, %s)
                   """
            values_users = (self.colemailtxt.get(), self.colpasswordtxt.get(), "student")

            cursor.execute(insert_query_user, values_users)

            conn.commit()
            messagebox.showinfo("Success", "User Created Successfully!")
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")

    def go_back(self):
        """ Close the signup window """
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Signup(root)
    root.mainloop()
