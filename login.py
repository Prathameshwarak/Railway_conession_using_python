import mysql.connector
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("640x300+400+200")
        self.root.configure(bg="#79b0d9")

        # Labels
        tk.Label(root, text="Email", bg="#79b0d9", font=("Arial", 10, "bold")).place(x=300, y=60)
        self.usertext = tk.Entry(root, bg="white", fg="black")
        self.usertext.place(x=400, y=60, width=150, height=25)

        tk.Label(root, text="Password", bg="#79b0d9", font=("Arial", 10, "bold")).place(x=300, y=100)
        self.passwordText = tk.Entry(root, show="*", bg="white", fg="black")
        self.passwordText.place(x=400, y=100, width=150, height=25)

        tk.Label(root, text="Login As", bg="#79b0d9", font=("Arial", 10, "bold")).place(x=300, y=140)
        self.loginChoice = tk.StringVar()
        self.loginChoice.set("Select Role")  # Default selection
        self.role_menu = tk.OptionMenu(root, self.loginChoice, "Select Role", "Admin", "Student")
        self.role_menu.config(bg="lightgray", fg="black")
        self.role_menu.place(x=400, y=140, width=150, height=25)

        # Buttons
        tk.Button(root, text="Login", command=self.login, bg="blue", fg="white").place(x=330, y=180, width=100)
        tk.Button(root, text="Cancel", command=root.quit, bg="red", fg="white").place(x=460, y=180, width=100)
        tk.Button(root, text="Signup", command=self.signup, bg="green", fg="white").place(x=400, y=215, width=100)

        # Load Image
        self.load_image()

    def load_image(self):
        try:
            img = Image.open("icon/graduates.png").convert("RGBA")
            img = img.resize((250, 250), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.img, bg="#79b0d9").place(x=5, y=25)
        except Exception as e:
            print("Error loading image:", e)

    def login(self):
        email = self.usertext.get().strip()
        password = self.passwordText.get().strip()
        role = self.loginChoice.get().strip()

        if not email or not password or role == "Select Role":
            messagebox.showerror("Error", "Please fill all fields and select a role.")
            return

        if self.check_credentials(email, password, role):
            messagebox.showinfo("Login Successful", f"Welcome, {role}!")
            self.root.destroy()  # Close login window

            if role == "Admin":
                self.open_admin_page()
            else:
                self.open_student_page()
        else:
            messagebox.showerror("Error", "Invalid Credentials")

    def check_credentials(self, email, password, role):
        try:
            conn = mysql.connector.connect(
                host="localhost",  # Change if using a remote server
                user="root",  # Default XAMPP user
                password="",  # Default XAMPP has no password (set yours if changed)
                database="rlwy_consession"
            )
            cursor = conn.cursor()
            query = "SELECT * FROM User WHERE Email=%s AND Password=%s AND Role=%s"
            cursor.execute(query, (email, password, role))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
            return False

    def signup(self):
        messagebox.showinfo("Signup", "Redirecting to Signup Page")
        self.root.destroy()
        subprocess.run(["python", "Signup.py"])

    def open_admin_page(self):
        subprocess.run(["python", "AdminPage.py"])  # Admin panel

    def open_student_page(self):
        subprocess.run(["python", "stud_insert.py"])  # Student dashboard


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
