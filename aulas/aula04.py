import customtkinter as tk

app = tk.CTk(fg_color='blue')
app.title('App Teste')
app.geometry('500x500')
app._set_appearance_mode('dark')

#Adicionando multiplas janelas
def nova_tela(): # Função de abrir a janela
    while True:
        janela = tk.CTkToplevel(app, fg_color='red') #Para criar nova janela (fg_color define a cor de fundo)
        janela.title('Nova janela')
        janela.geometry('300x300')

btn = tk.CTkButton(app, text='Clique aqui !', command=nova_tela).place(x=200, y=250) #.place define o lugar na tela e command chama a função



app.mainloop()