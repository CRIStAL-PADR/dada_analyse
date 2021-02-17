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
                
    def initialize(self):
        for x in range(self.ligne):
            sousTab = []
            for y in range(self.colonne):
                sousTab.append(self.defaultValue)
            self.data.append(sousTab)

if __name__=="__main__":
    
    x = load()

    tableau = Tableau(5,5, 'r')
    tableau.initialize()
    tableau.data[1][1] = 7
    tableau.data[1][2] = 7
    tableau.data[1][3] = 7
    tableau.data[4][2] = 7
    tableau.affiche()
  
    print(tableau.compteColone(2,7))
    print(tableau.compterLigne(1,7))