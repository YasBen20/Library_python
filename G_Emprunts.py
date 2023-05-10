from tkinter import *
from tkinter import ttk
from main import *
from menu import *


class emprunt(Tk):
    def __init__(self):
        
        super(emprunt, self).__init__()
    
        self.maxid = 0
        self.title("Gestion des Emprunts")
        self.geometry("1366x768")
        self.bg = PhotoImage(file="bib3.png")
        self.lb = Label(image=self.bg)
        self.lb.place(x=0, y=0, relheight=1, relwidth=1)
        #titre
        self.titre=Label(self,text="GESTION DES EMPRUNTS", font=("Courrier",40) ,fg="red")
        self.titre.place(x=400 , y=100)
        #reference label
        self.ref=Label(self,text="Reférence du Document :" , font=("Courrier", 18), fg="black")
        self.ref.place(x=10,y=260)
        #reference input
        self.ref_input = Entry(self)
        self.ref_input.place(x=300,y=260 , height=30 , width= 180)
        #titre doc label
        self.doc_titre=Label(self,text="Titre du Document :" ,  font=("Courrier", 18), fg="black")
        self.doc_titre.place(x=10,y=330)
        #titre doc input
        self.doc_t_input=Entry(self)
        self.doc_t_input.place(x=300,y=330 , height=30 , width= 180)
        #adh label
        self.nom_adh = Label(self,text="Nom d'Adehrent: ",font=("Courrier",18),fg="black")
        self.nom_adh.place(x=10,y=400)
        #adh input
        self.nom_adh_input = Entry(self)
        self.nom_adh_input.place(x=300,y=400 , height=30 , width= 180)
        #date emprunt_label
        self.date_empr = Label(self,text="Date d'Emprunt :", font=("Courrier", 18), fg="black")
        self.date_empr.place(x=10,y=450)
        #date_emprunt input
        self.date_empr_inp = Entry(self)
        self.date_empr_inp.place(x=300,y=450, height=30 , width= 180)
        #date restitution_label
        self.date_rest = Label(self,text="Date de Restitution :", font=("Courrier", 18), fg="black")
        self.date_rest.place(x=10,y=500)
        #date_restitution input
        self.date_rest_inp = Entry(self)
        self.date_rest_inp.place(x=300,y=500, height=30 , width= 180)
        #back button
        self.back = Button(self, text="BACK",fg="black",command=self.menu)
        self.back.place(x=60,y=900,width=70)
        #_block_window
        self.tree=ttk.Treeview(self)
        self.tree.place(x=500,y=240,width=850,height=400)
        self.tree['columns']=("Reference du document","Titre du document","Nom d'Adherent","Date d'emprunt","Date de restitution")
        self.tree.column("#0",width=100)
        self.tree.column("#1",width=100)
        self.tree.column("#2",width=150)
        self.tree.column("#3",width=150)
        self.tree.column("#4",width=200)
        self.tree.column("#5",width=200)
        self.tree.heading("#0",text=" ID_emprunt", anchor=CENTER)
        self.tree.heading("#1",text="Reference", anchor=CENTER)
        self.tree.heading("#2",text="Titre du document", anchor=CENTER)
        self.tree.heading("#3",text="Nom de l'adherent", anchor=CENTER)
        self.tree.heading("#4",text="Date d'emprunt", anchor=CENTER)
        self.tree.heading("#5",text="Date de restitution", anchor=CENTER)
        #ajout btn
        self.ajout_data = Button(self,text="AJOUTER",font=("Courrier",10),fg="white",background="black" ,command=self.insert_into_treeview)
        self.ajout_data.place(x=100,y=620,height=30,width=120)
        self.treeview_data()  
        #suppr btn
        self.delete = Button(self,text="SUPPRIMER",font=("Courrier",10),fg="red",background="black",command=self.delete_by_select)
        self.delete.place(x=300,y=620,height=30,width=120)
        self.tree.bind('<Double-Button-1>', self.modifier_data)
        #search bar
        self.search_input = Entry(self,bg="white",fg="black")
        self.search_input.place(x=1100,y=650,height=30,width=100)
        #search btn
        self.search_btn = Button(self,text="SEARCH",font=("Courrier",10),fg="white",background="black" ,command=self.search)
        self.search_btn.place(x=1250,y=650)
        # back button
        self.back = Button(self, text="BACK",fg="white",background="black",command=self.menu)
        self.back.place(x=60,y=50,width=70)

    def insert_into_treeview(self):
        if self.ajout_data['text'] == "AJOUTER":
            self.identifier = self.get_max_id()
            self.r = self.ref_input.get()
            self.t = self.doc_t_input.get()
            self.d1 = self.date_empr_inp.get()
            self.d2 = self.date_rest_inp.get()
            self.tree.insert(parent="", index=self.identifier, text=self.identifier, iid=self.identifier,
                values=(self.ref_input.get(), self.doc_t_input.get(), self.nom_adh_input.get() ,self.date_empr_inp.get(),self.date_rest_inp.get()))
            # inserting into database
            ajout_empr(self.identifier, self.ref_input.get(), self.doc_t_input.get(), self.nom_adh_input.get(), self.date_empr_inp.get() , self.date_rest_inp.get())
            self.empty_input()
        else:
            selection = self.tree.selection()
            print(selection)
            if selection:
                modif_emp(self.ref_input.get(),self.doc_t_input.get(),self.nom_adh_input.get(),self.date_empr_inp.get(),self.date_rest_inp.get(), selection[0])
                self.reset_tree_view()
                self.treeview_data()
            else:
                print("No item selected in the treeview.")


    def get_max_id(self):
        ids = db.cursor()
        ids.execute("SELECT * FROM Emprunts")
        for x in ids.fetchall():
            self.maxid = max(self.maxid, x[0])
            self.maxid += 1
        return self.maxid

    def empty_input(self):
        self.ref_input.delete(0, END)
        self.doc_t_input.delete(0, END)
        self.nom_adh_input.delete(0, END)
        self.date_empr_inp.delete(0, END)
        self.date_rest_inp.delete(0, END)

    def modifier_data(self, event):
        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        self.ref_input.delete(0, END) # clear the input field
        self.ref_input.insert(0, values[0]) # fill the input field with the value from the selected row
        self.doc_t_input.delete(0, END)
        self.doc_t_input.insert(0, values[1])
        self.nom_adh_input.delete(0, END)
        self.nom_adh_input.insert(0, values[2])
        self.date_empr_inp.delete(0, END)
        self.date_empr_inp.insert(0, values[3])
        self.date_rest_inp.delete(0, END)
        self.date_rest_inp.insert(0, values[4])
        self.ajout_data["text"] = "UPDATE"

    def treeview_data(self):
        get_all_data = db.cursor()
        get_all_data.execute("SELECT * FROM Emprunts")
        for x in get_all_data.fetchall():
            self.tree.insert(parent="", index=x[0], text=x[0], iid=x[0], values=x[1:])

    def reset_tree_view(self):
        for x in self.tree.get_children():
            self.tree.delete(x)

    def delete_by_select(self):
        self.select = self.tree.selection()[0]
        print(self.select)
        supp_empr(self.select)
        self.tree.delete(self.select)


    def search(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.get_data = self.search_input.get()
        for x in recherch_empr(self.get_data):
            self.tree.insert(parent="",index=x[0],text=x[0],iid=x[0], values=x[1:])

    def menu(self):
        self.destroy()
        from menu import menu
        menu()

if __name__ == "__main__":
    em = emprunt()
    em.mainloop()
