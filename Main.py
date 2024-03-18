import customtkinter
from Back_End_App import read_user_information as read, write_user_information as write


# --------------------------------------------------------------------------------------- #
# Gabriel Sampaio Pichane
# Python APP with SQL back-end server
# Version - 1.0
# --------------------------------------------------------------------------------------- #
class Login_Window(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self, text="Login or Sign in")
        self.label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        # Instancia das caixas editaveis de texto
        self.login = customtkinter.CTkEntry(self, placeholder_text="Login")
        self.login.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

        self.password = customtkinter.CTkEntry(self, placeholder_text="Password")
        self.password.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
        # Instancias dos botoes de cadastro e login
        self.button = customtkinter.CTkButton(self, text="Login", command=self.change_to_after_login_window,
                                              fg_color=("#DB3E39", "#821D1A"))
        self.button.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.button_2 = customtkinter.CTkButton(self, text="Sign in", command=self.abrir_tela_de_cadastro,
                                                fg_color=("#DB3E39", "#821D1A"))
        self.button_2.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        self.float_window = None

        self.window = 1
        self.change_after_login_window = None

    #  Sistema "bruto" de verificação dos dados do usuario
    def change_to_after_login_window(self):
        read_data_bank = read()
        user_login = str(self.login.get()).lower()
        user_password = str(self.password.get()).lower()

        print(read_data_bank)
        for a in read_data_bank['USER_LOGIN']:
            if user_login in a:

                search_result = read_data_bank[read_data_bank['USER_LOGIN'] == f'{user_login}']

                for b in search_result['USER_PASSWORD']:
                    if user_password in b:
                        login_window.destroy()
                        self.change_after_login_window = After_Login_Window(master=app)
                        self.change_after_login_window.place(relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5,
                                                             anchor=customtkinter.CENTER)
            else:
                self.label = customtkinter.CTkLabel(self, text="Incorrect Email or Password")
                self.label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    def abrir_tela_de_cadastro(self):
        if self.float_window is None or not self.float_window.winfo_exists():
            self.float_window = sign_in_window(self)
        else:
            self.float_window.focus()


class After_Login_Window(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Instancias dos botao para voltar window
        self.button = customtkinter.CTkButton(self, text="Logout", command=self.change_to_login_window,
                                              fg_color=("#DB3E39", "#821D1A"))
        self.button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

        self.window = 2
        self.change_login_window = None

    def change_to_login_window(self):
        self.window = self.window - 1
        print(self.window)
        if self.window < 2:
            after_login_window.destroy()
            self.change_login_window = Login_Window(master=app)
            self.change_login_window.place(relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


class sign_in_window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("300x300")

        self.label = customtkinter.CTkLabel(self, text=f"To register,"
                                                       f"please follow the steps below:\n")
        self.label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.login = customtkinter.CTkEntry(self, placeholder_text="What's your email?")
        self.login.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.password = customtkinter.CTkEntry(self, placeholder_text="What's your password")
        self.password.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

        self.button_1 = customtkinter.CTkButton(self, text="Register", command=self.sign_in,
                                                fg_color=("#DB3E39", "#821D1A"))
        self.button_1.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

    def sign_in(self):
        read_data_bank = read()
        user_login = str(self.login.get()).lower()
        user_password = str(self.password.get()).lower()

        print(read_data_bank)
        for a in read_data_bank['USER_LOGIN']:
            if user_login in a:

                search_result = read_data_bank[read_data_bank['USER_LOGIN'] == f'{user_login}']


            else:
                write(user_login, user_password)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Registration application")
        self.geometry("400x400")
        self.initial_window = 1


app = App()

login_window = Login_Window(master=app)
after_login_window = After_Login_Window(master=app)
if app.initial_window == 1:
    login_window.place(relheight=1.0, relwidth=1.0, relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
