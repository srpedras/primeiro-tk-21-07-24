import customtkinter as ctk
from tkinter import *



janela = ctk.CTk()

class Aplication():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.tema()
        self.tela_login()
        janela.mainloop()

    def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        #para abrir a janela do programa (primerira tela)
    def tela(self):
        janela.geometry("700x400")
        janela.title("Meu cadastro")
        janela.iconbitmap("icons/logoIcon.ico")
        janela.resizable(False, False)

    def tela_login(self):
        #trabalhnado com as imagens
        img = PhotoImage(file="icons/rosto.png")
        label_img = ctk.CTkLabel(master=janela, image=img, text=None)
        label_img.place(x=45, y=70)
        label_text = ctk.CTkLabel(master=janela, text='Bem vindo ao seu sitema cadastro', font = ('Roboto', 18), text_color= ('black'))
        label_text.place(x=15,y=10)

        #frame principal
        login_frame = ctk.CTkFrame(master=janela, width=370, height=396)
        login_frame.pack(side=RIGHT)

        #frames de login
        label = ctk.CTkLabel(master=login_frame, text='Login', font = ('Roboto', 20, 'bold'), text_color= ('black'))
        label.place(x=25, y=35)


        username_login = ctk.CTkEntry(master=login_frame, placeholder_text='Login do usuario',width=300, font = ('Roboto',15))
        username_login.place(x=25, y=105)
        label2 = ctk.CTkLabel(master=login_frame, text='* O campo Login é obrigatorio',text_color= ('green'), font = ('Roboto', 12))
        label2.place(x=25, y=135)

        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Password do usuario',width=300, font = ('Roboto',15),show="*")
        password_entry.place(x=25, y=175)
        label3 = ctk.CTkLabel(master=login_frame, text='* O campo Password do usuario é obrigatorio',text_color= ('green'), font = ('Roboto', 12))
        label3.place(x=25, y=205)


        checkbox = ctk.CTkCheckBox(master=login_frame, text="lembrar da senha")
        checkbox.place(x=25, y=235)

        #botão de login
        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300)
        login_button.place(x=25, y=285)

        #botão  cadastrar
        register_span = ctk.CTkLabel(master=login_frame, text="se não possui uma conta")
        register_span.place(x=20, y=330)
        cadastro_button = ctk.CTkButton(master=login_frame, text="Cadastrar usuario", width=150, fg_color="green", hover_color="#2D9334")
        cadastro_button.place(x=175, y=330)




#para aparecer a janela
Aplication()



