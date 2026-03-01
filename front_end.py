import tkinter as tk
from tkinter import messagebox
from db_helper import DBhelper


class FlipkartGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Flipkart")
        self.root.geometry("500x500")
        self.root.configure(bg="#f1f3f6")

        self.db = DBhelper()

        self.main_menu()

    # ================= COMMON =================
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_card(self):
        frame = tk.Frame(self.root, bg="black", bd=0, highlightthickness=0)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=350)
        return frame

    def styled_button(self, parent, text, command, bg="#2874f0"):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2"
        )

        # Hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg="#e80505"))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))

        return btn

    # ================= MAIN MENU =================
    def main_menu(self):
        self.clear_screen()

        tk.Label(
            self.root,
            text="Flipkart",
            font=("Arial", 24, "bold"),
            bg="#ea0a0a",
            fg="#2874f0"
        ).pack(pady=30)

        frame = self.create_card()

        tk.Label(frame, text="Welcome", font=("Arial", 16, "bold"), bg="white").pack(pady=20)

        self.styled_button(frame, "Register", self.register_screen).pack(pady=10, ipadx=10, ipady=5)
        self.styled_button(frame, "Login", self.login_screen).pack(pady=10, ipadx=10, ipady=5)
        self.styled_button(frame, "Exit", self.root.quit, bg="#d9534f").pack(pady=10, ipadx=10, ipady=5)

    # ================= REGISTER =================
    def register_screen(self):
        self.clear_screen()
        frame = self.create_card()

        tk.Label(frame, text="Create Account", font=("Arial", 16, "bold"), bg="white").pack(pady=15)

        name_entry = self.create_input(frame, "Name")
        email_entry = self.create_input(frame, "Email")
        pass_entry = self.create_input(frame, "Password", show="*")

        def register_user():
            name = name_entry.get()
            email = email_entry.get()
            password = pass_entry.get()

            if not name or not email or not password:
                messagebox.showwarning("Warning", "All fields required")
                return

            response = self.db.register(name, email, password)

            if response:
                messagebox.showinfo("Success", "Registration Successful 🎉")
                self.main_menu()
            else:
                messagebox.showerror("Error", "Registration Failed")

        self.styled_button(frame, "Register", register_user).pack(pady=10, ipadx=10, ipady=5)
        tk.Button(frame, text="Back", command=self.main_menu, bg="white", relief="flat").pack()

    # ================= LOGIN =================
    def login_screen(self):
        self.clear_screen()
        frame = self.create_card()

        tk.Label(frame, text="Login", font=("Arial", 16, "bold"), bg="white").pack(pady=15)

        email_entry = self.create_input(frame, "Email")
        pass_entry = self.create_input(frame, "Password", show="*")

        def login_user():
            email = email_entry.get()
            password = pass_entry.get()

            if not email or not password:
                messagebox.showwarning("Warning", "All fields required")
                return

            response = self.db.login(email, password)

            if response:
                messagebox.showinfo("Success", "Login Successful ✅")
                self.after_login()
            else:
                messagebox.showerror("Error", "Invalid Credentials")

        self.styled_button(frame, "Login", login_user).pack(pady=10, ipadx=10, ipady=5)
        tk.Button(frame, text="Back", command=self.main_menu, bg="white", relief="flat").pack()

    # ================= INPUT FIELD =================
    def create_input(self, parent, placeholder, show=None):
        tk.Label(parent, text=placeholder, bg="white", anchor="w").pack(fill="x", padx=30)
        entry = tk.Entry(parent, show=show, relief="flat", bg="#f1f3f6")
        entry.pack(padx=30, pady=5, ipady=5, fill="x")
        return entry

    # ================= AFTER LOGIN =================
    def after_login(self):
        self.clear_screen()
        frame = self.create_card()

        tk.Label(frame, text="Welcome 🎉", font=("Arial", 16, "bold"), bg="white").pack(pady=30)

        self.styled_button(frame, "Logout", self.main_menu).pack(pady=10, ipadx=10, ipady=5)


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = FlipkartGUI(root)
    root.mainloop()