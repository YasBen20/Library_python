from tkinter import *
from tkinter import ttk
from main import *
from menu import * 


class adherent(Tk):
    def __init__(self):
        super(adherent, self).__init__()
        self.maxid=0
        self.title("Gestion des adherents")
        self.geometry("1366x768")
        self.var=IntVar()
        self.bg = PhotoImage(file="bib3.png")
        self.lb=Label(image=self.bg)
        self.lb.place(x=0,y=0,relheight=1,relwidth=1)

        #titre
        self.titre = Label(self,text="GESTION DES ADHERENTS", font=("Courrier",40) ,fg="red")
        self.titre.place(x=420,y=100)
    
        #nom label
        self.nom = Label(self,text="Nom : ",font=("Courrier",18),fg="black")
        self.nom.place(x=170,y=270)
        #nom input
        self.nom_input = Entry(self)
        self.nom_input.place(x=330,y=270 , height=30 , width= 180)
       
        #prenom label
        self.prenom = Label(self, text="Prenom : ", font=("Courrier", 18),fg="black")
        self.prenom.place(x=170, y=340)
        #prenom input
        self.prenom_input = Entry(self)
        self.prenom_input.place(x=330, y=340 , height=30 , width= 180)
        #age label
        self.age = Label(self,text="Age : ",font=("Courrier", 18),fg="black")
        self.age.place(x=170,y=410)
        #age input
        self.age_input = Entry(self)
        self.age_input.place(x=330, y=410 , height=30 , width= 180)
        #email label
        self.email = Label(self, text="Email : ", font=("Courrier", 18),fg="black")
        self.email.place(x=170, y=480)
        #email input
        self.email_input = Entry(self)
        self.email_input.place(x=330, y=480 , height=30 , width= 180)
        #tel label
        self.tele = Label(self, text="Telephone : ", font=("Courrier", 18),fg="black")
        self.tele.place(x=170, y=550)
        #tel input
        self.tele_input = Entry(self)
        self.tele_input.place(x=330, y=550,height=30 , width= 180)
        #block_window
        self.tree = ttk.Treeview(self)
        self.tree.place(x=600,y=200,width=700,height=400)
        self.tree['columns']=("ID","NOM","PRENOM","AGE","EMAIL","TELEPHONE")
        self.tree.column("#0", width=40)
        self.tree.column("#1", width=60)
        self.tree.column("#2", width=60)
        self.tree.column("#3", width=50)
        self.tree.column("#4", width=130)
        self.tree.column("#5", width=100)
        self.tree.column("#6", width=0,stretch=NO)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("#1", text="NOM", anchor=CENTER)
        self.tree.heading("#2", text="PRENOM", anchor=CENTER)
        self.tree.heading("#3", text="AGE", anchor=CENTER)
        self.tree.heading("#4", text="EMAIL", anchor=CENTER)
        self.tree.heading("#5", text="TELE", anchor=CENTER)
        #ajout btn
        self.ajout_data = Button(self,text="AJOUTER",font=("Courrier",10),fg="white",background="black",command=self.insert_into_treeview)
        self.ajout_data.place(x=250,y=620,height=30,width=120)
        self.treeview_data()
        #search bar
        self.search_input = Entry(self,bg="white",fg="black")
        self.search_input.place(x=1160,y=620,height=30,width=90)
        #search btn
        self.search_btn = Button(self,text="SEARCH",font=("Courrier",10),fg="white",background="black",command=self.search)
        self.search_btn.place(x=1240,y=620)
        #suppr btn
        self.delete = Button(self,text="SUPPRIMER",font=("Courrier",10),fg="red",background="black",command=self.delete_by_select)
        self.delete.place(x=400,y=620,height=30,width=120)
        self.tree.bind('<Double-Button-1>', self.modifier_data)
        #back button
        self.back = Button(self, text="BACK",fg="white",background="black",command=self.menu)
        self.back.place(x=60,y=50,width=70)

    def insert_into_treeview(self):
        if self.ajout_data['text'] == "AJOUTER":
            self.identifier = self.get_max_id()
            self.n = self.nom_input.get()
            self.p = self.prenom_input.get()
            self.age = self.age_input.get()
            self.e = self.email_input.get()
            self.t=self.tele_input.get()
            self.tree.insert(parent="",index=self.identifier,text=self.identifier,iid=self.identifier,values=(self.nom_input.get(),self.prenom_input.get(),self.age_input.get(),self.email_input.get(),self.tele_input.get()))
            #insert into data base
            ajouter_adh(self.identifier,self.nom_input.get(),self.prenom_input.get(),self.age_input.get(),self.email_input.get(),self.tele_input.get())
            #make entries empty after inserting data
            self.empty_input()
        else:
            print(self.tree.selection()[0])
            modif_adh(self.nom_input.get(),self.prenom_input.get(),self.age_input.get(),self.email_input.get(),self.tele_input.get(),self.tree.selection()[0])
            self.reset_tree_view()
            self.treeview_data()
            self.empty_input()
   
    def get_max_id(self):
        ids=db.cursor()
        ids.execute("SELECT * FROM Adherent")
        for x in ids.fetchall():
            self.maxid = max(self.maxid,x[0])
        self.maxid +=1
        return self.maxid

    def menu(self):
        self.destroy()
        from menu import menu
        menu()
    
    def treeview_data(self):
        get_all_data = db.cursor()
        get_all_data.execute("SELECT * FROM Adherent")
        for x in get_all_data.fetchall():
            self.tree.insert(parent="", index=x[0], text=x[0], iid=x[0], values=x[1:])
   
    def search(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.get_data = int(self.search_input.get())
        print(recherch_adh(self.get_data))
        for x in recherch_adh(self.get_data):
            self.tree.insert(parent="",index=x[0],text=x[0],iid=x[0], values=x[1:])
   
    def delete_by_select(self):
        self.select = self.tree.selection()[0]
        supprim_adh(self.select)
        self.tree.delete(self.select)


    def empty_input(self):
        self.nom_input.delete(0, END)
        self.prenom_input.delete(0, END)
        self.age_input.delete(0, END)
        self.tele_input.delete(0, END)
        self.email_input.delete(0, END) 
        
    def modifier_data(self,event):
        ite=self.tree.selection()[0]
        self.gety = self.tree.item(self.tree.selection()[0])['values']
        self.nom_input.insert(0,self.gety[0])
        self.prenom_input.insert(0, self.gety[1])
        self.age_input.insert(0, self.gety[2])
        self.email_input.insert(0, self.gety[3])
        self.tele_input.insert(0, self.gety[4])
        self.ajout_data['text']="UPDATE" 

    def reset_tree_view(self):
        for x in self.tree.get_children():
            self.tree.delete(x)

if __name__ == "__main__":
     ad=adherent()
     ad.mainloop()