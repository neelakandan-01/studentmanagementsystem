from tkinter import *
window = Tk()

window.title("Login Form")
window.geometry("1550x850")
window.config(background='MediumSpringGreen')
frame = Frame(window,bg='PaleGreen')
frame.pack()
lbl_username = Label(frame, text="Username:",bg='PaleGreen')
lbl_username.grid(row=0, column=0, sticky=W)
ent_username = Entry(frame)
ent_username.grid(row=0, column=1)
lbl_password = Label(frame, text="Password:",bg='PaleGreen')
lbl_password.grid(row=1, column=0, sticky=W)
ent_password = Entry(frame, show="*")
ent_password.grid(row=1, column=1)
def login():
    username = ent_username.get()
    password = ent_password.get()
    if username == "admin" and password == "admin":
        lbl_result.config(text="Login successful!", fg="green")
        window.destroy()
        import page2

    else:
        lbl_result.config(text="Invalid username or password!", fg="red")
        return

btn_login = Button(frame, text="Login", command=login,bg='PaleGreen')
btn_login.grid(row=2, column=0, columnspan=2)
lbl_result = Label(frame, text="")
lbl_result.grid(row=3, column=0, columnspan=2)
window.mainloop()

