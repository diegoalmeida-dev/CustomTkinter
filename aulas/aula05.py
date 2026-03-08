import customtkinter as tk

app = tk.CTk()
app.title('App Teste')
app.geometry('500x500')

#Frames
frame1 = tk.CTkFrame(app, width=100, height=500, fg_color='red').place(x=0, y=0)

frame2 = tk.CTkFrame(app, width=100, height=500, fg_color='green').place(x=200, y=0)

frame3 = tk.CTkFrame(app, width=100, height=500, fg_color='blue', bg_color='white', corner_radius=10).place(x=400, y=0)




app.mainloop()