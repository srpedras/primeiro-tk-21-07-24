import customtkinter as ctk
from tkinter import *
from tkinter import messagebox



janela = ctk.CTk()

class Aplication():
    def __init__(self):
        self.janela = janela
        self.tela()
        #self.tema()
        self.tela_login()
        janela.mainloop()

    #def tema(self):    
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
        label_text.place(x=20,y=15)

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
        def login():
            msg = messagebox.showinfo(title="Estado de Login",message="Parabens!login feito com sucesso.")
            pass
        login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, command=login)
        login_button.place(x=25, y=285)

        #botão  cadastrar
        register_span = ctk.CTkLabel(master=login_frame, text="se não possui uma conta")
        register_span.place(x=20, y=330)

        def tela_register():
            #remover o frame de login
            login_frame.pack_forget()

            #criando a tela de cadastro de usuario
            rg_frame = ctk.CTkFrame(master=janela, width=370, height=396)
            rg_frame.pack(side=RIGHT)

            #frames de login
            label = ctk.CTkLabel(master=rg_frame, text='Faça seu cadastro', font = ('Roboto', 20, 'bold'), text_color= ('black'))
            label.place(x=25, y=35)

            span = ctk.CTkLabel(master=rg_frame, text='*Por favor preencha todos os campos corretamente', font = ('Roboto', 12), text_color= "gray")
            span.place(x=25, y=75)

            username_login = ctk.CTkEntry(master=rg_frame, placeholder_text='Nome de usuario',width=300, font = ('Roboto',15))
            username_login.place(x=25, y=105)

            email_login = ctk.CTkEntry(master=rg_frame, placeholder_text='E-mail de usuario',width=300, font = ('Roboto',15))
            email_login.place(x=25, y=145)

            password_login = ctk.CTkEntry(master=rg_frame, placeholder_text='Login do usuario',width=300, font = ('Roboto',15), show="*")
            password_login.place(x=25, y=185)

            cpassword_login = ctk.CTkEntry(master=rg_frame, placeholder_text='Confirme o login',width=300, font = ('Roboto',15), show="*")
            cpassword_login.place(x=25, y=225)

            checkbox = ctk.CTkCheckBox(master=rg_frame, text="Aceito os termos e Politicas  da empresa")
            checkbox.place(x=25, y=270)

            #devolvendo o frame de login
            def back():
               rg_frame.pack_forget()

               login_frame.pack(side=RIGHT)

              

            back_button = ctk.CTkButton(master=rg_frame, text="Voltar", width=145, fg_color="green", hover_color="#2D9334", command=back)
            back_button.place(x=25, y=310)

            #salvando os dados
            def save_user():
                msg = messagebox.showinfo(title="Estado do Cadastro", message="Parabens! Usuario cadastrado com sucesso.")
                pass

            save_button = ctk.CTkButton(master=rg_frame, text="Cadastrar", width=145, fg_color="green", hover_color="#2D9334", command=save_user)
            save_button.place(x=180, y=310)
           

        cadastro_button = ctk.CTkButton(master=login_frame, text="Cadastrar usuario", width=150, fg_color="green", hover_color="#2D9334", command=tela_register)
        cadastro_button.place(x=175, y=330)




#para aparecer a janela
Aplication()



