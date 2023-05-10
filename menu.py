from tkinter import *
class menu(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1366x768")

        self.title("Menu de gestion")
        self.bg = PhotoImage(file="bib3.png")
        self.lb=Label(image=self.bg)
        self.lb.place(x=0,y=0,relheight=1,relwidth=1)
        self.adherent = Button(self,text="Gestion des adherents",background="orange",fg="white",font=("Courrier",15),command=self.open_adherent)
        self.adherent.place(x=200,y=300,width=250,height=100)
        self.document = Button(self, text="Gestion des documents",background="orange",fg="white",font=("Courrier",15),command=self.open_document)
        self.document.place(x=600, y=300, width=250, height=100)
        self.emprunt = Button(self, text="Gestion des emprunts",background="orange",fg="white",font=("Courrier",15),command=self.open_emprunt)
        self.emprunt.place(x=1000, y=300, width=250, height=100)
        self.resizable(height=False,width=False)
        #back button
        self.back = Button(self, text="Log Out",fg="white",background="black",command=self.open_login)
        self.back.place(x=60,y=800,width=70)
        
    def open_adherent(self):
        from G_Adherent import adherent
        self.destroy()
        adherent().mainloop()
    
    def open_document(self):
        from G_Documents import document
        self.destroy()
        document().mainloop()
    
    def open_emprunt(self):
        from G_Emprunts import emprunt
        self.destroy()
        emprunt().mainloop()

    def open_login(self):
        self.destroy()
        from Login import Login
        Login().mainloop()

if __name__ == "__main__":
    m=menu()
    m.mainloop()
