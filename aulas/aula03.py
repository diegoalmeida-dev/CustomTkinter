import customtkinter as tk

app = tk.CTk()
app.title('App Teste')
app.geometry('500x500')

#Customizando o tema da aplicação:
app._set_appearance_mode('light') #Define a cor do sistema (light, dark, system)

app.mainloop()