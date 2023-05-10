from tkinter import *
from main import *
from menu import *
from menu import menu



class login(Tk):
    def __init__(self):
        super(login,self).__init__()
        self.title("Login")
        self.geometry("1366x768")
        self.var=IntVar()
        self.bg = PhotoImage(file="bib3.png")
        self.lb=Label(image=self.bg)
        self.lb.place(x=0,y=0,relheight=1,relwidth=1)
        self.label=Label(self,text="BIENVENUE AU SYSTEME BIBLIOTHEQUE",font=("Courrier",30),fg="Red")
        self.label.place(x=260,y=150)
        self.username = Label(self,text="Username :",font=(50),background="black",fg="white")
        self.username.place(x=480,y=300)
        self.username_input = Entry(self)
        self.username_input.place(x=600,y=300,height=25,width=200)
        self.password = Label(self, text="Mot de passe :", font=(50),background="black",fg="white")
        self.password.place(x=480, y=350)
        self.password_input = Entry(self,show="*")
        self.password_input.place(x=600, y=350,height=25,width=200)
        self.login=Button(text="Log in",bd=0,font=("Courrier",20),fg="black",command=self.connexion)
        self.login.place(x=600,y=460)
        self.show = Label(self,text="Show Password",background="black",bg="white")
        self.show.place(x=600,y=400)
        self.show_btn=Checkbutton(self,variable=self.var,command=self.show_password)
        self.show_btn.place(x=730,y=400)

    def connexion(self):
        self.user=self.username_input.get()
        self.mot=self.password_input.get()
        if self.user == fetchdata()[0][0] and self.mot == fetchdata()[0][1]:
            self.destroy() #fermer la fenetre
            menu().mainloop()   #afficher la nouvelle fenetre à l'execusion
        else:
            self.create_label = Label(self,text="Username ou Mot de passe sont incorrect",fg="red",font=("Courrier",15))
            self.create_label.place(x=810,y=520)

    def show_password(self):
        if self.var.get():
            #if var.Get()==1 it means true (button checked)
            self.password_input.configure(show="")
        else:
            # if var.Get()==0 it means false (button not checked)
            self.password_input.configure(show="*")



if __name__ == "__main__":
    app=login()# create object
    app.mainloop()#execute the object