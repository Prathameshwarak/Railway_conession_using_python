import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk


class RailwayConcessionForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Railway Concession Form")
        self.root.geometry("1200x600")

        # Title
        tk.Label(root, text="Certificate for Railway Concession Ticket", font=("Arial", 14, "bold")).place(x=400, y=20)

        # Load and display the banner image
        self.banner_image = Image.open("icon/banner.jpg")
        self.banner_image = self.banner_image.resize((1000, 150))
        self.banner_photo = ImageTk.PhotoImage(self.banner_image)
        self.banner_label = tk.Label(root, image=self.banner_photo)
        self.banner_label.place(x=100, y=50, width=1000, height=150)

        # Form Fields
        self.fields = {
            "Fee Rec. No.": (320, 220), "Mobile No.": (320, 260), "Dept Rly. Name": (320, 300),
            "Arrival Rly. Name": (320, 340),
            "Pass Duration": (320, 380), "Pre. Tkt. Exp. Dt.": (320, 420), "Fees Pmt. Dt.": (650, 220),
            "Student ID": (650, 260),
            "Dept. Stn.": (650, 300), "Arrival Stn.": (650, 340), "Tkt. Class": (650, 380), "Pre. Cert. No.": (650, 420)
        }

        self.entries = {}
        for label, (x, y) in self.fields.items():
            tk.Label(root, text=label, font=("Arial", 10)).place(x=x, y=y)
            if label in ["Dept Rly. Name", "Arrival Rly. Name"]:
                self.entries[label] = ttk.Combobox(root, values=["Western Rly", "Central Rly"], state='readonly')
            elif label == "Pass Duration":
                self.entries[label] = ttk.Combobox(root, values=["Monthly", "Quarterly"], state='readonly')
            elif label == "Arrival Stn.":
                self.entries[label] = ttk.Combobox(root, values=["Malad", "Dadar", "Borivali"], state='readonly')
            elif label == "Tkt. Class":
                self.entries[label] = ttk.Combobox(root, values=["1st", "2nd"], state='readonly')
            else:
                self.entries[label] = tk.Entry(root, bg="white")
            self.entries[label].place(x=x + 130, y=y, width=150, height=25)

        # Submit Button
        submit_btn = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="blue", fg="white",
                               command=self.insert_data)
        submit_btn.place(x=530, y=480, width=150, height=40)

        # Note at Bottom
        tk.Label(root,
                 text="N.B.: The application must be submitted at least three working days prior to the date required.",
                 font=("Arial", 10, "bold"), fg="red").place(x=330, y=550)

    def insert_data(self):
        """ Insert form data into MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='rlwy_consession')
            cursor = conn.cursor()

            insert_query = """
            INSERT INTO concession_forms (Fee_Rec_No, Fees_Payment_Date, Mobile_No, Student_ID, Dept_Rlwy_Name, Dept_Station, 
            Arrival_Rlwy_Name, Arrival_Station, Pass_Duration, Tkt_Class, Pre_Tkt_Expire_Date, Pre_Cert_No, Status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'Pending')
            """

            values = (
                self.entries["Fee Rec. No."].get(), self.entries["Fees Pmt. Dt."].get(),
                self.entries["Mobile No."].get(),
                self.entries["Student ID"].get(), self.entries["Dept Rly. Name"].get(),
                self.entries["Dept. Stn."].get(),
                self.entries["Arrival Rly. Name"].get(), self.entries["Arrival Stn."].get(),
                self.entries["Pass Duration"].get(),
                self.entries["Tkt. Class"].get(), self.entries["Pre. Tkt. Exp. Dt."].get(),
                self.entries["Pre. Cert. No."].get()
            )

            cursor.execute(insert_query, values)
            conn.commit()
            messagebox.showinfo("Success", "Form submitted successfully!")
            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RailwayConcessionForm(root)
    root.mainloop()
