class Product:
    def __init__(self, cout, prix, marque):
        self.cout = cout
        self.prix = prix
        self.marque = marque

    def __str__(self):
        return f"coût : {self.cout} €, prix : {self.prix} €, marque : {self.marque}"
        
class Meubles(Product):
    def __init__(self, cout, prix, marque, materiaux, couleur, dimensions):
        super().__init__(cout, prix, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimensions = dimensions

    def __str__(self):
        return f"Meuble en {self.materiaux} de couleur {self.couleur} et de dimension {self.dimensions}\n"+super().__str__()

class Canape(Product):
    def __init__(self, materiaux, couleur, dimensions, cout, prix, marque, nom):
        super().__init__(cout, prix, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimensions = dimensions
        self.nom = nom

    def __str__(self):
        return f"{self.nom} en {self.materiaux} de couleur {self.couleur} et de dimension {self.dimensions}\n"+super().__str__()

class Chaise(Product):
    def __init__(self, materiaux, couleur, dimensions, cout, prix, marque, nom):
        super().__init__(cout, prix, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimensions = dimensions
        self.nom = nom

    def __str__(self):
        return f"{self.nom} en {self.materiaux} de couleur {self.couleur} et de dimension {self.dimensions}\n"+super().__str__()

class Table(Product):
    def __init__(self, materiaux, couleur, dimensions, cout, prix, marque):
        super().__init__(cout, prix, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimensions = dimensions

    def __str__(self):
        return f"Table en {self.materiaux} de couleur {self.couleur} et de dimension {self.dimensions}\n"+super().__str__()


canape1 = Canape("Cuir","Blanc","200x100x80",1000,2000,"OKLM","Canapé")
canape2 = Canape ("Tissu","Bleu","150x90x70",800,1600,"SIESTA","Canapé")
chaise1 = Chaise("Plastique","Rouge","50x50x70",50,100,"PEPOUSE","Chaise")
chaise2 = Chaise("Métal","Gris","60x60x80",75,150,"PEPOUSE","Chaise")
table2 = Table("Bois","Chêne","150x80x75",250,500,"TEX")
table1 = Table("Verre","Transparent","120x60x75",350,700,"TEX")

print (canape1)
print (canape2)
print (chaise1)
print (chaise2)
print (table1)
print (table2)
