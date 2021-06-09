from tkinter import *

root = Tk()


class Apliccation:
    def __init__(self):
        self.root = root
        self.screen()
        self.screen_frames()
        self.creating_buttons()
        root.mainloop()

    def screen(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#1e3743')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

    def screen_frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def creating_buttons(self):
        self.bt_clean = Button(self.frame_1)
        self.bt_clean.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)


Apliccation()
