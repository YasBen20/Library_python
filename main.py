import mysql.connector

#connecteur de BD

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Yasben@20",
    auth_plugin="mysql_native_password",
    database="Gestion_bibliotheque",
)

A_cursor=db.cursor()

"""
#LOGIN DATABASE
A_cursor.execute("CREATE TABLE Login (username VARCHAR(15) NOT NULL , psswd VARCHAR(15) NOT NULL)")

#Adherent DATABASE
A_cursor.execute("CREATE TABLE Adherent (Id_adh int PRIMARY KEY NOT NULL , Nom VARCHAR(15) NOT NULL , Prenom VARCHAR(15) NOT NULL , Age int NOT NULL , Email VARCHAR(50) NOT NULL ,Tel VARCHAR(13) NOT NULL )")

#Documents DATABASE
A_cursor.execute("CREATE TABLE Documents (ID_doc int PRIMARY KEY NOT NULL , Ref_doc VARCHAR(20) NOT NULL , Titre VARCHAR(30) NOT NULL , type_d varchar(10) CHECK (type_d='BD' or type_d='ROMAN') )")

#Emprunts DATABASE
A_cursor.execute("CREATE TABLE Emprunts (ID_empr int  PRIMARY KEY NOT NULL , Ref_doc VARCHAR(20) NOT NULL , Titre VARCHAR(30) NOT NULL , Nom_adh VARCHAR(15) NOT NULL , Date_emprunt DATE , Date_restitution DATE )")
"""
#methode connexion
def connexion(username , psswd):
    data = (username,psswd)
    query="INSERT INTO Login (username,psswd) VALUES (%s,%s)"
    A_cursor.execute(query,data)
    db.commit()

#connexion("admin","123456")

#methode d'affichage des données
def fetchdata():
    A_cursor.execute("SELECT * FROM Login")
    data=A_cursor.fetchall()
    return data

#methode ajout adherant
def ajouter_adh(Id_adh , Nom , Prenom , Age , Email , Tel):
    data=(Id_adh,Nom,Prenom,Age,Email,Tel)
    query="INSERT INTO Adherent (Id_adh,Nom,Prenom,Age,Email,Tel) VALUES (%s,%s,%s,%s,%s,%s)"
    A_cursor.execute(query,data)
    db.commit()

#ajouter_adh(2,"fdfsdf","ddd",21,"zjjjzzzzz@gmail.com","+212612456975")

#methode supprimer adherant
def supprim_adh(Id_adh):
    #data = Id_adh
    #query="DELETE FROM Adherant WHERE Id_adh = %s "
    A_cursor.execute("DELETE FROM Adherent WHERE Id_adh = %s ",(Id_adh,))
    db.commit()
#supprim_adh(3)

#methode modifier adherant
def modif_adh(Nom , Prenom , Age , Email , Tel,Id_adh):
    A_cursor.execute("UPDATE Adherent set  Nom = %s , Prenom = %s , Age = %s , Email = %s , Tel = %s WHERE Id_adh = %s",(Nom,Prenom,Age,Email,Tel,Id_adh,))
    db.commit()



#methode recherche adherant
def recherch_adh(Id_adh):
    A_cursor.execute("SELECT * FROM Adherent WHERE id_adh = %s ",(Id_adh,))
    return A_cursor.fetchall()

#method afficher adherant

def affich_adh():
    A_cursor.execute("SELECT * FROM Adherent")
    for x in A_cursor:
        print(x)

#affich_adh()

#methode ajouter document*****************************************************************************************
def ajout_doc(ID_doc,Ref_doc,Titre,type_d):
    data=(ID_doc,Ref_doc,Titre,type_d)
    query="INSERT INTO Documents (ID_doc,Ref_doc,Titre,type_d) VALUES (%s,%s,%s,%s)"
    A_cursor.execute(query,data)
    db.commit()

#ajout_doc(1,"D1","Game Of Thrones","ROMAN")
#ajout_doc(2,"D2", "Titeuf","BD")
#ajout_doc(3,"D3","Madame Bovary","ROMAN")

#methode supprimer document
def supp_doc(iden):
    query="DELETE FROM Documents WHERE ID_doc= %s"
    A_cursor.execute(query,(iden,))
    db.commit()

#supp_doc("D2")

#methode modifier document
def modif_doc(Ref_doc,Titre,type_d,Iden):
    #data=(Ref_doc,Titre,type_d,Iden)
   # query="UPDATE Documents SET Ref_doc = %s , Titre = %s , type_d = %s WHERE ID_doc = %s"
    A_cursor.execute("UPDATE Documents SET Ref_doc = %s , Titre = %s , type_d = %s WHERE ID_doc = %s",(Ref_doc,Titre,type_d,Iden,))
    db.commit()  


    #def modif_adh(Nom , Prenom , Age , Email , Tel,Id_adh):
    #A_cursor.execute("UPDATE Adherent set  Nom = %s , Prenom = %s , Age = %s , Email = %s , Tel = %s WHERE Id_adh = %s",(Nom,Prenom,Age,Email,Tel,Id_adh,))
   # db.commit()


#modif_doc("test","Les Misérables","bd",1)

#recherhe doc
def recherch_doc(Ref_doc):
    A_cursor.execute("SELECT * FROM Documents WHERE Ref_doc = %s ", (Ref_doc,))
    return A_cursor.fetchall()

#methode afficher documents
def affich_doc():
    A_cursor.execute("SELECT * FROM Documents")
    for x in A_cursor:
        print (x)

#affich_doc()

#methode ajouter emprunt
def ajout_empr(ID_empr,Ref_doc,Titre,Nom_adh,Date_emprunt,Daterestitution):
    data=(ID_empr,Ref_doc,Titre,Nom_adh,Date_emprunt,Daterestitution)
    query="INSERT INTO Emprunts (ID_empr,Ref_doc,Titre,Nom_adh,Date_emprunt,Date_restitution) VALUES (%s,%s,%s,%s,%s,%s)"
    A_cursor.execute(query,data)
    db.commit()


"""
ajout_empr(1,"D2","Titeuf","Dybala","2022-5-1","2023-5-16")
ajout_empr(2,"D3","Les Misérables","Hugo","2022-5-1","2022-5-16")
ajout_empr(3,"D4","Madame Bovary","Gustave","2022-5-1","2022-5-16")
"""

#methode supprimer emprunts
def supp_empr(idemp):
    query="DELETE FROM Emprunts WHERE ID_empr = %s"
    A_cursor.execute(query,(idemp,))
    db.commit()

#supp_empr("D4")
#recherche emprunt

def recherch_empr(Ref_doc):
    A_cursor.execute("SELECT * FROM Emprunts WHERE Ref_doc = %s ", (Ref_doc,))
    return A_cursor.fetchall()


#methode afficher emprunts
def affich_empr():
    A_cursor.execute("SELECT * FROM Emprunts")
    for x in A_cursor:
        print(x)

#affich_empr()

def modif_emp(D_empr,Ref_doc,Titre,Nom_adh,Date_emprunt,Daterestitution):
    #data=(Ref_doc,Titre,type_d,Iden)
   # query="UPDATE Documents SET Ref_doc = %s , Titre = %s , type_d = %s WHERE ID_doc = %s"
    A_cursor.execute(f"UPDATE Emprunts SET Ref_doc = %s , Titre= %s , Nom_adh= %s , Date_emprunt= %s , Date_restitution= %s WHERE ID_empr= %s",(D_empr,Ref_doc,Titre,Nom_adh,Date_emprunt,Daterestitution))
    db.commit()  
