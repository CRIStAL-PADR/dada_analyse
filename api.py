# -*-coding: utf-*-
import file

def load():
    return file.content

class Tableau:
    def __init__(self, ligne, colonne, defaultValue = 0):
        self.ligne = ligne
        self.colonne = colonne
        self.defaultValue = defaultValue
        self.data = []
        self.fillWithValue(self.defaultValue)
                
    def compteColone(self, c, value):
        """ retourne le nombre de foix ou sur une ligne 'l' il y a la valeur "value" """
        count = 0
        for i  in range(len(self.data)):
            for j in range(len(self.data[c])):
                if (value == self.data[i][c]):
                    count = count+1
                    break
        return count
    
    def compterLigne(self, l, value):
        """retourne le nombre de foix ou sur une ligne 'l' il y a la valeur "value" """
        count = 0
        for j in range(len(self.data[l])):
            if (self.data[l][j]==value):
                count = count+1        
        return count
          
    
    def affiche(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                print(self.data[i][j], end  =' ')
            print()
                
    def fillWithValue(self, newValue):
        self.data = [] 
        for x in range(self.ligne):       # compte x et fait ce qui à l'intérieur self.ligne fois.
            sousTab = []                  # sousTab = [] <= list
            for y in range(self.colonne): # compte y et fait ce qui à l'intérieur self.ligne fois.
                sousTab.append(newValue)  # sousTab.push_back newValue                                           
            self.data.append(sousTab)     # 

def remplir(tab, content):
    # savoir boucle sur les éléments d'un tableau
    # savoir boucle sur le contenu du dictionnaire (clefs, et la valeurs)
    # savoir convertir un clef d'un dictionnaire en un indice. 
        # "file1.cpp" => 0
        # "file2.h" => 6 
        # faire une seconde fonction qui retourner l'indice et prend en paramètre le nom du fichier, ajouter d'autre paramètre si nécessaire (mais pas de variable globale)
        
if __name__=="__main__":
    
    x = load() 
    tableau = Tableau(len(x), len(x))
    tableau.data[1][1] = 1
    tableau.data[1][2] = 1
    tableau.data[1][3] = 1
    tableau.data[4][2] = 1
    tableau.affiche()
  
    print(tableau.compteColone(2,7))
    print(tableau.compterLigne(1,7))
