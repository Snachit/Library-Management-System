class Livre:
    def __init__(self, titre, auteur, annee, disponibilite = True ):
        self.titre = titre 
        self.auteur = auteur
        self.annee = annee
        self.disponibilite = disponibilite
    @property
    def Emprunter(self):
        self.disponibilite = False
        
        
    @property
    def Retoutner(self):
        self.disponibilite == True
        
    
class biblio:
    def __init__(self) :
        self.liste_titre = []
        self.dispo = []

    def liste(self, livre ):
        self.liste_titre.append(livre)
        

    def afficher(self):
        dispo = [livre.titre and livre.auteur for livre in self.liste_titre if livre.disponibilite]
        if dispo :
            print("livre dispo:")
            for Livre.titre in dispo:
                print(f"*{Livre.titre}\n")

        else :
            print("Aucun livre dispo")


print("---------------------------biblio lharara---------------------------")


livre1 = Livre("Harry Potter", "J.K. Rowling", 1997)
livre2 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954)
livre3 = Livre("1984", "George Orwell", 1949)
livre4 = Livre("To Kill a Mockingbird", "Harper Lee", 1960)
livre5 = Livre("The Great Gatsbi", "Scott Fitzgrald",1925)
livre6 = Livre("Ninteen Eight-Four", "George Orwell", 1946)
livre7 = Livre("Animal Farm", "George Orwell", 1945)
Bibliotheque = biblio()
Bibliotheque.liste(livre1)
Bibliotheque.liste(livre2)
Bibliotheque.liste(livre3)
Bibliotheque.liste(livre4)
Bibliotheque.liste(livre5)
Bibliotheque.liste(livre6)
Bibliotheque.liste(livre7)
Bibliotheque.afficher()
print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------")
livre3.Emprunter
livre5.Emprunter
livre4.Emprunter
Bibliotheque.afficher()
print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------")

