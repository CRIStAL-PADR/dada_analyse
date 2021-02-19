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
          
    
    def affiche(self, content):
        for i in range(len(self.data)):
            key = self.getFileFromIndex(i, content)
            print( key[1], ' ', key[0], '    ', end = '|')
            for j in range(len(self.data[i])):
                print( self.data[i][j], end  = '  ')
            print('|')
                
    def fillWithValue(self, newValue):
        self.data = [] 
        for x in range(self.ligne):      
            sousTab = []                 
            for y in range(self.colonne): 
                sousTab.append(newValue)                                            
            self.data.append(sousTab)     
    
    def getList(self, content):
       return [*content]
    
    def getTableFromFile(self, content):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        list = self.getList(content)
        for i in range(len(list)):
            keys = self.getFileFromIndex(i,content)
            keys_File = keys[1]
            if list[i]== keys_File:
                for j in  range(len(content[keys_File])):
                    for a in range(len(list)):
                        if content[keys_File][j] == list[a]:
                            self.data[i][a] = 1
            keys = 0
            
            
    def getFileFromIndex(self, index, content):
        i = 0
        keys = []
        list = self.getList(content)
        for i in range( len(list)):
            keys.append(i)
        if index == keys[index]:
            return index,list[index]

            
if __name__== "__main__" :
    x = load()
    
    tableau = Tableau(len(x), len(x) )
    l = tableau.getFileFromIndex(2,x)
    tableau.getTableFromFile(x)
    tableau.affiche(x)