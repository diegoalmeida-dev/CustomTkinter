import customtkinter as tk
# import time

app = tk.CTk()

#Configurando a janela principal

app.title('APP TESTE') #Nome do app
app.geometry('700x350') #Define o tamanho da janela largura x altura em px
app.minsize(width=400, height=200) #Janela mínima
app.maxsize(width=1000, height=900) #Janela máxima
app.resizable(width=True, height=False) #Fixa a altura ou larura impossibilitando mover
app.iconify() #Fecha a janela
app.deiconify() #Reabre a janela

'''while True: #serve pra dar um sustinho achando que deu merda
    app.iconify()
    app.deiconify()'''

btn = tk.CTkButton(app, text='Teste')
btn.pack()

app.mainloop()