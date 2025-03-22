import tkinter as tk
from tkinter import ttk
import mysql.connector  # Use MySQL Connector for XAMPP

class AdminPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Page - Railway Concession System")
        self.root.geometry("1300x600")

        # Title Label
        tk.Label(root, text="Admin Page - Railway Concession System", font=("Arial", 14, "bold")).pack(pady=10)

        # Frame for Table
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Create Treeview Table
        self.tree = ttk.Treeview(frame, columns=("Fee Rec No", "Fee Pay Date", "Mobile", "Student ID",
                                                 "Dept Railway", "Dept Station", "Arrival Railway", "Arrival Station",
                                                 "Pass Duration", "Ticket Class", "Pre-Ticket Expiry Date", "Pre-Certificate No", "Status"),
                                 show="headings", height=15)

        # Define Each Column
        columns = [
            ("Fee Rec No", 100), ("Fee Pay Date", 100), ("Mobile", 100), ("Student ID", 100),
            ("Dept Railway", 120), ("Dept Station", 120), ("Arrival Railway", 120), ("Arrival Station", 120),
            ("Pass Duration", 100), ("Ticket Class", 100), ("Pre-Ticket Expiry Date", 130),
            ("Pre-Certificate No", 130), ("Status", 120)
        ]
        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")

        # Pack the Treeview
        self.tree.pack(fill="both", expand=True)

        # Add Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Load Data
        self.load_data()

        # Approve Button
        self.approve_btn = tk.Button(root, text="Approve", font=("Arial", 12, "bold"), bg="green", fg="white",
                                     command=self.approve_application)
        self.approve_btn.place(x=500, y=550, width=150, height=40)

        # Reject Button
        self.reject_btn = tk.Button(root, text="Reject", font=("Arial", 12, "bold"), bg="red", fg="white",
                                    command=self.reject_application)
        self.reject_btn.place(x=700, y=550, width=150, height=40)

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",  # Change if you have set a password
            password="",  # Change if your MySQL has a password
            database="rlwy_consession"
        )

    def load_data(self):
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT Fee_Rec_No, Fees_Payment_Date, Mobile_No, Student_ID, Dept_Rlwy_Name, Dept_Station, Arrival_Rlwy_Name, Arrival_Station, Pass_Duration, Tkt_Class, Pre_Tkt_Expire_Date, Pre_Cert_No, Status FROM concession_forms")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
            conn.close()
        except Exception as e:
            print("Error loading data:", e)

    def update_status(self, status):
        selected_item = self.tree.selection()
        if selected_item:
            row_data = self.tree.item(selected_item)["values"]
            fee_rec_no = row_data[0]  # Get Fee_Rec_No as the unique identifier
            try:
                conn = self.connect_db()
                cursor = conn.cursor()
                cursor.execute("UPDATE concession_forms SET Status = %s WHERE Fee_Rec_No = %s", (status, fee_rec_no))
                conn.commit()
                conn.close()
                self.tree.item(selected_item, values=(*row_data[:-1], status))
            except Exception as e:
                print("Error updating status:", e)

    def approve_application(self):
        self.update_status("Approved")

    def reject_application(self):
        self.update_status("Rejected")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminPage(root)
    root.mainloop()
