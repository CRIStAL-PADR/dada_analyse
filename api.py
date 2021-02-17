# -*-coding: utf-*-
import file
tab = []
arr = []

def load():
    return file.content

class Tableau:
    def __init__(self, ligne, colonne, data):
        self.ligne = ligne
        self.colonne = colonne
        self.data = data

    def affiche(self, tab):
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                print(tab[i][j], end = ' ')
            print()
        
    def stockerDansTab(self):
        for x in range(self.ligne):
            for y in range(self.colonne):
                arr.append(self.data)
            tab.append(arr)

if __name__=="__main__":
    
    x = load()

    tableau = Tableau(10,5,1)
    tableau.stockerDansTab()
    tableau.affiche(tab)
   