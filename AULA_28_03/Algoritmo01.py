import tkinter as tk

class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=0, column=0, sticky="e", padx=10, pady=5)

        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.message = tk.Label(master, text="", fg="red")
        self.message.grid(row=3, columnspan=2, padx=10, pady=5)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Verifica se o email e a senha são válidos
        if email == "teste@example.com" and password == "senha123":
            self.message.config(text="Login successful", fg="green")
            self.master.destroy()  # Fecha a janela de login
            self.open_registration_window(email)  # Abre a janela de cadastro
        else:
            self.message.config(text="Invalid email or password", fg="red")

    def open_registration_window(self, email):
        registration_window = tk.Tk()
        registration_window.title("Registration")

        welcome_label = tk.Label(registration_window, text=f"Welcome, {email}!")
        welcome_label.pack(padx=10, pady=10)

def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

