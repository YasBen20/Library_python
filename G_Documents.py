from tkinter import *
from tkinter import ttk
from main import *
from menu import * 


class document(Tk):
    def __init__(self):
        super(document, self).__init__()
        self.maxid = 0
        self.title("Gestion des Documents")
        self.geometry("1366x768")
        self.bg = PhotoImage(file="bib3.png")
        self.lb=Label(image=self.bg)
        self.lb.place(x=0,y=0,relheight=1,relwidth=1)
        
        #titre
        self.titre=Label(self,text="GESTION DES DOCUMENTS", font=("Courrier",40) ,fg="red")
        self.titre.place(x=350 , y=100)

       
        #ref label
        self.ref=Label(self,text="Reférence du document :" , font=("Courrier", 18), fg="black")
        self.ref.place(x=150,y=260)
        #ref input
   
        self.ref_input = Entry(self)
        self.ref_input.place(x=440,y=260 , height=30 , width= 180)
        
        #titre doc label
        self.doc_titre=Label(self,text="Titre du document :" ,  font=("Courrier", 18), fg="black")
        self.doc_titre.place(x=150,y=380)
        #titre doc input
        self.doc_t_input=Entry(self)
        self.doc_t_input.place(x=440,y=380 , height=30 , width= 180)
        
        #type_doc label
        self.type_d=Label(text="Type du Document :",font=("Courrier", 18), fg="black")
        self.type_d.place(x=150,y=500)
        #type doc_input
        self.type_d_input=Entry(self)
        self.type_d_input.place(x=440,y=500 , height=30 , width= 180)
        #self.combo_type_d=ttk.Combobox(self)
        #self.combo_type_d['value']=('Livre','BD','Roman')
        #self.combo_type_d.place(x=440,y=500, height=30 , width= 180)
        #block_window
        self.tree=ttk.Treeview(self)
        self.tree.place(x=650,y=240,width=600,height=400)
        self.tree['columns']=("Reference du document","Titre","Type du document")
        self.tree.column("#0", width=100)
        self.tree.column("#1",width=100)
        self.tree.column("#2",width=200)
        self.tree.column("#3",width=200)
        self.tree.heading("#0",text=" ID_document", anchor=CENTER)
        self.tree.heading("#1",text="Reference", anchor=CENTER)
        self.tree.heading("#2",text="Titre du document", anchor=CENTER)
        self.tree.heading("#3",text="Type du document", anchor=CENTER)

        #back button
        self.back = Button(self, text="BACK",fg="white",background="black",command=self.menu)
        self.back.place(x=60,y=50,width=70)
        #ajout btn
        self.ajout_data = Button(self,text="AJOUTER",font=("Courrier",10),fg="white",background="black",command=self.insert_into_treeview)
        self.ajout_data.place(x=250,y=620,height=30,width=120)
        self.treeview_data()
        
        #search bar
        self.search_input = Entry(self,bg="white",fg="black")
        self.search_input.place(x=1090,y=640,height=30,width=90)
        #search btn
        self.search_btn = Button(self,text="SEARCH",font=("Courrier",10),fg="white",background="black",command=self.search)
        self.search_btn.place(x=1180,y=640)
        #suppr btn
        self.delete = Button(self,text="SUPPRIMER",font=("Courrier",10),fg="red",background="black",command=self.delete_by_select)
        self.delete.place(x=400,y=620,height=30,width=120)
        self.tree.bind('<Double-Button-1>', self.modifier_data)

           

    def insert_into_treeview(self):
        if self.ajout_data['text'] == "AJOUTER":
            self.identifier = self.get_max_id()
            self.r=self.ref_input.get()
            self.t=self.doc_t_input.get()
            self.i=self.type_d_input.get()
            self.tree.insert(parent="",index=self.identifier,text=self.identifier,iid=self.identifier,values=(self.ref_input.get(),self.doc_t_input.get(),self.type_d_input.get()))
            #inserting into database
            ajout_doc(self.identifier,self.r,self.t,self.i)
            self.empty_input()
        else:
            print(self.tree.selection()[0])
            modif_doc(self.ref_input.get(),self.doc_t_input.get(),self.type_d_input.get(), self.tree.selection()[0])
            self.reset_tree_view()
            self.treeview_data()
            


    def get_max_id(self):
        ids=db.cursor()
        ids.execute("SELECT * FROM Documents")
        for x in ids.fetchall():
            self.maxid = max(self.maxid,x[0])
        self.maxid +=1
        return self.maxid
    

    def modifier_data(self,event):
        ite=self.tree.selection()[0]
        self.gety = self.tree.item(self.tree.selection()[0])['values']
        self.ref_input.delete(0, END) #clear old value
        self.ref_input.insert(0, self.gety[0]) #set new value
        self.doc_t_input.delete(0, END) #clear old value
        self.doc_t_input.insert(0, self.gety[1]) #set new value
        self.type_d_input.delete(0, END) #clear old value
        self.type_d_input.insert(0, self.gety[2]) #set new value
        self.ajout_data['text']="UPDATE"


    def reset_tree_view(self):
        for x in self.tree.get_children():
            self.tree.delete(x)

    def search(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.get_data = int(self.search_input.get()) 
        print(recherch_doc(self.get_data))
        for x in recherch_doc(self.get_data):
            self.tree.insert(parent="",index=x[0],text=x[0],iid=x[0], values=x[1:])


    def treeview_data(self):
        get_all_data = db.cursor()
        get_all_data.execute("SELECT * FROM Documents")
        for x in get_all_data.fetchall():
            self.tree.insert(parent="", index=x[0], text=x[0], iid=x[0], values=x[1:])


    def reset_tree_view(self):
        for x in self.tree.get_children():
            self.tree.delete(x)

    def delete_by_select(self):
        self.select = self.tree.selection()[0]
        #print(self.select)
        supp_doc(self.select)
        self.tree.delete(self.select)

    def menu(self):
        self.destroy()
        from menu import menu
        menu()

    def empty_input(self):
        self.ref_input.delete(0, END)
        self.doc_t_input.delete(0, END)
        self.type_d_input.delete(0, END)        

if __name__ == "__main__":
    doc=document()
    doc.mainloop()