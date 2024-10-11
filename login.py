import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import bcrypt

from tkinter import *
import database
from tkinter import messagebox



janela = ctk.CTk()

class Aplication():
    def __init__(self):
        self.janela = janela
        self.tela()
        #self.tema()
        self.tela_login()
        janela.mainloop()
        "self.tela2()"

    #def tema(self):    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        #para abrir a janela do programa (primerira tela)
    def tela(self):
        janela.geometry("700x400")
        janela.title("Meu cadastro")
        janela.iconbitmap("logoIcon.ico")
        janela.resizable(False, False)

    def tela_login(self):
        #trabalhnado com as imagens
        img = tk.PhotoImage(file="rosto.png")
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

            
            username = username_login.get()
            password = password_entry.get()
            
            # Fetch user data from database
            database.cursor.execute("SELECT Username, Password FROM users WHERE Username = ?", (username,))
            user_data = database.cursor.fetchone()

            if user_data:  # Check if user exists
                hashed_password = user_data[1]  # Assuming the hashed password is at index 1

                # Verify password using bcrypt
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    # Login successful
                    # Remove login frame
                    login_frame.pack_forget()

                    # Create main window
                    rg_frame = ctk.CTkFrame(master=janela, width=370, height=396)
                    rg_frame.pack(side=RIGHT)

                    label = ctk.CTkLabel(master=rg_frame, text='Tela principal', font=('Roboto', 20, 'bold'), text_color=('black'))
                    label.place(x=25, y=35)
                else:
                    # Login failed - Incorrect password
                    messagebox.showerror(title="Estado de Login", message="Acesso negado, verifique a senha e tente novamente.")
            else:
                # Login failed - Username not found
                messagebox.showerror(title="Estado de Login", message="Usuário não encontrado.")
                        
                                
                                   
            #devolvendo o frame de login
            def back():
                rg_frame.pack_forget()

                login_frame.pack(side=RIGHT) 
                    
            back_button = ctk.CTkButton(master=rg_frame, text="Voltar", width=145, fg_color="green", hover_color="#2D9334", command=back)
            back_button.place(x=25, y=310)  
            
            def tela2(): 
             
              rg_frame.pack_forget()

              #criando a tela de cadastro de usuario
              rg_frame2 = ctk.CTkFrame(master=janela, width=370, height=396)
              rg_frame2.pack(side=RIGHT) 
              
              #frames de login
              label = ctk.CTkLabel(master=rg_frame2, text='Faça seu cadastro', font = ('Roboto', 20, 'bold'), text_color= ('black'))
              label.place(x=25, y=35)

              span = ctk.CTkLabel(master=rg_frame2, text='*Por favor preencha todos os campos corretamente', font = ('Roboto', 12), text_color= "gray")
              span.place(x=25, y=75)

              username_login = ctk.CTkEntry(master=rg_frame2, placeholder_text='Login do usuario',width=300, font = ('Roboto',15))
              username_login.place(x=25, y=105)

              email_login = ctk.CTkEntry(master=rg_frame2, placeholder_text='E-mail de usuario',width=300, font = ('Roboto',15))
              email_login.place(x=25, y=145)

              password_login = ctk.CTkEntry(master=rg_frame2, placeholder_text='Senha',width=300, font = ('Roboto',15), show="*")
              password_login.place(x=25, y=185)

              cpassword_login = ctk.CTkEntry(master=rg_frame2, placeholder_text='Confirme a Senha',width=300, font = ('Roboto',15), show="*")
              cpassword_login.place(x=25, y=225)

              checkbox = ctk.CTkCheckBox(master=rg_frame2, text="Aceito os termos e Politicas  da empresa")
              checkbox.place(x=25, y=270)
              
              #devolvendo o frame de login
              def back():
                rg_frame2.pack_forget()

                rg_frame.pack(side=RIGHT)
                
              back_button = ctk.CTkButton(master=rg_frame2, text="Voltar", width=145, fg_color="green", hover_color="#2D9334", command=back)
              back_button.place(x=25, y=310)
              
              #salvando os dados
              def save_user():

                Name =  username_login.get ()
                Email = email_login.get ()
                Password = password_login.get ()  
                Cpasswords = cpassword_login.get()

                #logica para cadastrar corretamente
                if Name == "" :
                    messagebox.showerror(title="Register erro", message= "Não deixe nenhum campo vazio")
                elif  Email == "":
                    messagebox.showerror(title="Register erro", message= "Não deixe nenhum campo vazio")
                    
                elif  Password == "" :
                    messagebox.showerror(title="Register erro", message= "Não deixe nenhum campo vazio")
                
                elif Cpasswords == "":
                    messagebox.showerror(title="Register erro", message= "Não deixe nenhum campo vazio")  

                elif Cpasswords != Password :  
                    messagebox.showerror(title="Estado do Cadastro", message="As senhas precisam ser iguais!.")
                
                else:    
                    database.cursor.execute(""" 
                                INSERT INTO users  (Username , Email , Password )  VALUES(?,?,?)
                    """,(Name,Email,Password)) 
                    database.conn.commit()                            
                    msg = messagebox.showinfo(title="Estado do Cadastro", message="Parabens! Usuario cadastrado com sucesso.")
                    pass
               

              save_button = ctk.CTkButton(master=rg_frame2, text="Cadastrar", width=145, fg_color="green", hover_color="#2D9334", command=save_user)
              save_button.place(x=180, y=310)         

                       
            cadastro_button = ctk.CTkButton(master=rg_frame, text="Cadastrar usuario", width=150, fg_color="green", hover_color="#2D9334", command=tela2)
            cadastro_button.place(x=25, y=240) 
            
            def tela3(): 
             
              rg_frame.pack_forget()

              #criando a tela de cadastro de senhas
              rg_frame2 = ctk.CTkFrame(master=janela, width=370, height=396)
              rg_frame2.pack(side=RIGHT) 


              #frames de login
              label = ctk.CTkLabel(master=rg_frame2, text='Faça seu cadastro', font = ('Roboto', 20, 'bold'), text_color= ('black'))
              label.place(x=25, y=35)

              span = ctk.CTkLabel(master=rg_frame2, text='*Por favor preencha todos os campos corretamente', font = ('Roboto', 12), text_color= "gray")
              span.place(x=25, y=75)

              username_login = ctk.CTkEntry(master=rg_frame2, placeholder_text='Login do usuario',width=300, font = ('Roboto',15))
              username_login.place(x=25, y=105)

              email_login = ctk.CTkEntry(master=rg_frame2, placeholder_text='E-mail de usuario',width=300, font = ('Roboto',15))
              email_login.place(x=25, y=145)

              password_login = ctk.CTkEntry(master=rg_frame2, placeholder_text='Senha',width=300, font = ('Roboto',15), show="*")
              password_login.place(x=25, y=185)

              cpassword_login = ctk.CTkEntry(master=rg_frame2, placeholder_text='Confirme a Senha',width=300, font = ('Roboto',15), show="*")
              cpassword_login.place(x=25, y=225)

              checkbox = ctk.CTkCheckBox(master=rg_frame2, text="Aceito os termos e Politicas  da empresa")
              checkbox.place(x=25, y=270)

              
              #devolvendo o frame a tela principal
              def back():
                rg_frame2.pack_forget()

                rg_frame.pack(side=RIGHT)
                
              back_button = ctk.CTkButton(master=rg_frame2, text="Voltar", width=145, fg_color="green", hover_color="#2D9334", command=back)
              back_button.place(x=25, y=310) 

              back_button = ctk.CTkButton(master=rg_frame2, text="Deletar cadastro", width=145, fg_color="green", hover_color="#2D9334", command=back)
              back_button.place(x=180, y=350) 
              
                
              # Função para visualizar os cadastros
              # Variável global para armazenar o nome de usuário logado (ajuste conforme sua implementação)
              
              
              def visualizar_cadastros():
              
                conn = database.conn.cursor()
                if conn is None:
                    messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
                    return 
                cursor = database.conn.cursor()
                cursor.execute("SELECT * FROM logins")  # Substitua 'logins' pelo nome da sua tabela
                # Cria uma nova janela para exibir os resultados
                resultados_window = tk.Toplevel(janela)
                resultados_window.title("Cadastros")
                
                
                
                tree = ttk.Treeview(resultados_window, columns=("user", "email", "password"), show="headings")
                tree.heading("user", text="Usuário")
                tree.heading("email", text="Email")
                tree.heading("password", text="Senha")
                tree.pack(fill="both", expand=True)
                
                
                # Insert the data into the text widget, displaying the password (not recommended)
                # Insere os dados no Treeview
                for row in cursor.fetchall():
                        tree.insert("", "end", values=(row[1], row[2], (row[3])))

                              
                conn.close()

              # Button to visualize passwords
              visualize_button = ctk.CTkButton(master=rg_frame2, text="Visualize Passwords", width=145, fg_color="green",  hover_color="#2D9334", command=visualizar_cadastros)
              visualize_button.place(x=25, y=350)

              #salvando os dados
              def save_user():

                Name =  username_login.get ()
                Email = email_login.get ()
                Password = password_login.get ()  
                Cpasswords = cpassword_login.get()

                #logica para cadastrar corretamente
                 # Input validation
                if not Name or not Email or not Password or not Cpasswords:
                 messagebox.showerror(title="Register Error", message="Por favor prencha todos os campos.")
                 return

                if Password != Cpasswords:
                 messagebox.showerror(title="Register Error", message="As senhas precisam ser iguais.")
                 return
                
                # Hashing the password with bcrypt
                hashed_password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt())

                # Logic to insert data into database (replace with your actual database interaction)
                try:    
                    database.cursor.execute(""" 
                                INSERT INTO logins  (Username , Email , Password )  VALUES(?,?,?)
                    """,(Name,Email,Password))
                    database.conn.commit()                            
                    msg = messagebox.showinfo(title="Estado do Cadastro", message="Parabens! Usuario cadastrado com sucesso.")
                except Exception as e:
                    messagebox.showerror(title="Registration Error", message=f"An error occurred: {str(e)}")

               

              save_button = ctk.CTkButton(master=rg_frame2, text="Cadastrar", width=145, fg_color="green", hover_color="#2D9334", command=save_user)
              save_button.place(x=180, y=310) 
                     
            cadastro_button = ctk.CTkButton(master=rg_frame, text="Guardar novo login", width=150, fg_color="green", hover_color="#2D9334", command=tela3)
            cadastro_button.place(x=195, y=240) 
            
                 
                
                                                        
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

            username_login = ctk.CTkEntry(master=rg_frame, placeholder_text='Login do usuario',width=300, font = ('Roboto',15))
            username_login.place(x=25, y=105)

            email_login = ctk.CTkEntry(master=rg_frame, placeholder_text='E-mail de usuario',width=300, font = ('Roboto',15))
            email_login.place(x=25, y=145)

            password_login = ctk.CTkEntry(master=rg_frame, placeholder_text='Senha',width=300, font = ('Roboto',15), show="*")
            password_login.place(x=25, y=185)

            cpassword_login = ctk.CTkEntry(master=rg_frame, placeholder_text='Confirme a Senha',width=300, font = ('Roboto',15), show="*")
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

                
                Name =  username_login.get ()
                Email = email_login.get ()
                Password = password_login.get ()
                Cpasswords = cpassword_login.get()

                hashed_password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt())    


                #logica para cadastrar corretamente
                if Name == "" :
                    messagebox.showerror(title="Register erro", message= "Não deixe nenhum campo vazio")
                elif  Email == "":
                    messagebox.showerror(title="Register erro", message= "Não deixe nenhum campo vazio")
                    
                elif  Password == "" :
                    messagebox.showerror(title="Register erro", message= "Não deixe nenhum campo vazio")
                
                elif Cpasswords == "":
                    messagebox.showerror(title="Register erro", message= "Não deixe nenhum campo vazio")  

                elif Cpasswords != Password :  
                    messagebox.showerror(title="Estado do Cadastro", message="As senhas precisam ser iguais!.")
                
                else:    
                    database.cursor.execute(""" 
                                INSERT INTO users (Username, Email, Password) VALUES (?, ?, ?)
                             """, (Name, Email, hashed_password)) 
                    database.conn.commit()                            
                    msg = messagebox.showinfo(title="Estado do Cadastro", message="Parabens! Usuario cadastrado com sucesso.")
                    pass
               

            save_button = ctk.CTkButton(master=rg_frame, text="Cadastrar", width=145, fg_color="green", hover_color="#2D9334", command=save_user)
            save_button.place(x=180, y=310)
            
            
                     

        cadastro_button = ctk.CTkButton(master=login_frame, text="Cadastrar usuario", width=150, fg_color="green", hover_color="#2D9334", command=tela_register)
        cadastro_button.place(x=175, y=330)




#para aparecer a janela
Aplication()



