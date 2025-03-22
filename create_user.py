import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3  # Change to MySQL connector if needed

class CreateUser:
    def __init__(self, root):
        self.root = root
        self.root.title("Signup Page")
        self.root.geometry("900x550")
        self.root.configure(bg="#A8CBFF")  # Background color

        # Title Label
        title_label = tk.Label(root, text="Atharva College of Engineering Student Portal",
                               font=("Serif", 20, "bold"), bg="#A8CBFF")
        title_label.place(x=250, y=30)

        # Student ID Label & Entry
        sid_label = tk.Label(root, text="Student ID", bg="#A8CBFF")
        sid_label.place(x=30, y=100)
        self.sid_txt = tk.Entry(root, bg="white")
        self.sid_txt.place(x=170, y=100, width=405)

        # Name Label & Entry
        name_label = tk.Label(root, text="Name", bg="#A8CBFF")
        name_label.place(x=30, y=150)
        self.pname_txt = tk.Entry(root, bg="white")
        self.pname_txt.place(x=170, y=150, width=405)

        # Email Label & Entry
        email_label = tk.Label(root, text="Email", bg="#A8CBFF")
        email_label.place(x=30, y=200)
        self.email_txt = tk.Entry(root, bg="white")
        self.email_txt.place(x=170, y=200, width=405)

        # Password Label & Entry
        password_label = tk.Label(root, text="Password", bg="#A8CBFF")
        password_label.place(x=30, y=250)
        self.password_txt = tk.Entry(root, show="*", bg="white")
        self.password_txt.place(x=170, y=250, width=405)

        # Load and Display Image
        self.load_image()

        # Create Button
        self.create_btn = tk.Button(root, text="Create", font=("Arial", 12, "bold"),
                                    bg="#427FDB", fg="black", command=self.create_user)
        self.create_btn.place(x=150, y=350, width=150, height=40)

        # Back Button
        self.back_btn = tk.Button(root, text="Back", font=("Arial", 12, "bold"),
                                  bg="#427FDB", fg="black", command=self.go_back)
        self.back_btn.place(x=400, y=350, width=150, height=40)

    def load_image(self):
        """Loads and displays an image on the right side."""
        try:
            image = Image.open("icon/student.png")  # Make sure "student.png" is in the same directory
            image = image.resize((250, 250), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)

            self.image_label = tk.Label(self.root, image=self.photo, bg="#A8CBFF")
            self.image_label.place(x=620, y=90, width=250, height=250)
        except Exception as e:
            print("Error loading image:", e)

    def create_user(self):
        """Inserts user data into the database."""
        sid = self.sid_txt.get()
        sname = self.pname_txt.get()
        email = self.email_txt.get()
        password = self.password_txt.get()

        if not (sid and sname and email and password):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            # Database Connection (Modify for MySQL if needed)
            conn = sqlite3.connect("railway_concession.db")
            cursor = conn.cursor()

            # Insert User Data
            query = "INSERT INTO cuser (sid, name, email, password) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (sid, sname, email, password))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "User Created Successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def go_back(self):
        """Closes the signup window."""
        self.root.destroy()
        import login  # Import your login page module here

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateUser(root)
    root.mainloop()
