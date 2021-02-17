# -*-coding: utf-*-
import file
tab = []
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
                print(tab[i][j], end  =' ')
            print()
                
    def stockerDansTab(self):
        for x in range(self.ligne):
            sousTab = []
            for y in range(self.colonne):
                sousTab.append(self.data)
            tab.append(sousTab)

if __name__=="__main__":
    
    x = load()

    tableau = Tableau(5,5,0)
    tableau.stockerDansTab()
    tableau.affiche(tab)
   