import customtkinter
from tkinter import *

#customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("dark-blue")

#para abrir a janela do programa (primerira tela)
janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Meu cadastro")
janela.iconbitmap("icons/logoIcon.ico")
janela.resizable(False, False)

#trabalhnado com as imagens
img = PhotoImage(file="icons/rosto.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=15, y=70)
label_text = customtkinter.CTkLabel(master=janela, text='Bem vindo ao seu sitema cadsatro', font = ('Roboto', 18), text_color= ('black'))
label_text.place(x=15,y=10)

#frame principal
frame = customtkinter.CTkFrame(master=janela, width=370, height=396)
frame.pack(side=RIGHT)

#frames de login
label = customtkinter.CTkLabel(master=frame, text='Login', font = ('Roboto', 20, 'bold'), text_color= ('black'))
label.place(x=25, y=35)


login = customtkinter.CTkEntry(master=frame, placeholder_text='Login do usuario',width=300, font = ('Roboto',20))
login.place(x=25, y=105)
label2 = customtkinter.CTkLabel(master=frame, text='* O campo Login é obrigatorio',text_color= ('green'), font = ('Roboto', 12))
label2.place(x=25, y=135)

password = customtkinter.CTkEntry(master=frame, placeholder_text='Password do usuario',width=300, font = ('Roboto',20))
password.place(x=25, y=175)
label3 = customtkinter.CTkLabel(master=frame, text='* O campo Password do usuario é obrigatorio',text_color= ('green'), font = ('Roboto', 12))
label3.place(x=25, y=205)


checkbox = customtkinter.CTkCheckBox(master=frame, text="lembrar da senha")
checkbox.place(x=25, y=235)

button = customtkinter.CTkButton(master=frame, text="Login", width=300)
button.place(x=25, y=275)









#para aparecer a janela
janela.mainloop()



