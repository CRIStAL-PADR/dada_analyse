# -*-coding: utf-*-
import file
import timeit

def load():
    return file.content

class Tableau:
    def __init__(self, ligne, colonne, defaultValue = 0):
        self.ligne = ligne
        self.colonne = colonne
        self.defaultValue = defaultValue
        self.data = []
        self.fillWithValue(self.defaultValue)
        self.indexToKey = []
        self.keyToIndex = {}

                
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
        """This function takes a generated file as a parameter and displays a dependency graph between the different
        files as an adjacency matrix shape
        
                                     | 0 1 2 3 4 5 6 7
        --------------------------------------------------- 
        file1.cpp                  0 | 1 0 0 0 1 0 0 1 |  3 
        file2.cpp                  1 | 0 1 0 0 1 0 0 0 |  2
        file3.cpp                  2 | 0 0 1 0 1 0 0 0 |  2 
        file2.h                    3 | 0 0 0 1 0 0 0 0 |  1 
        file3.h                    4 | 0 0 0 0 1 0 0 0 |  1
        /ceci/.../findfichier.h    5 | 0 0 0 0 0 1 0 0 |  1
        file5.h                    6 | 0 0 0 0 0 1 1 0 |  2
        file1.h                    7 | 0 0 0 0 0 0 0 0 |  0
        
        filename = "/ceci/est/un/très/long/nom/de/fichier.txt"
        shortFilaneme = filename[:10]+"..."+filename[-10:]
        
        """
        
        liste = self.getList(content)
        for x in range(len(liste)):
            if x == 0:
                print('                           ',x, end = ' ')
            if x<=9 and x>0:
                print('',x, '', end = '')
            if x >9 :
                print('',x,end = '') 
        print('')
       
        for x in range(len(liste)):
            print('------', end = '')
        for i in range(len(self.data)):
            print('  ') 
            c = self.compterLigne(i,1)
            keyA = self.indexToKey[i]
            keyB = self.keyToIndex[keyA]
           
            if len(keyA)<9:
                if keyB<=9:
                    print(keyA,'              ',keyB, '  ', end = '|')
                if keyB >9 and keyB <=99:
                    print(keyA,'              ',keyB, ' ', end = '|')  
                if keyB >99 :
                    print(keyA,'              ',keyB, '',end = '|') 
                    
            if len(keyA)==9:
                if keyB<=9:
                    print(keyA, '            ',keyB, '  ', end = '|')
                if keyB >9 and keyB <=99:
                    print(keyA,'            ',keyB, ' ', end = '|') 
                if keyB>99 :
                    print(keyA,'          ',keyB,'', end = '|') 
            
            if len(keyA)>9:
                if keyB<=9:
                    print(keyA[:3]+"..."+keyA[-5:], '          ',keyB, '  ', end = '|')
                if keyB >9 and keyB <=99:
                    print(keyA[:3]+"..."+keyA[-4:],'           ',keyB, ' ', end = '|') 
                if keyB >99 :
                    print(keyA[:3]+"..."+keyA[-3:],'         ',keyB,'', end = '|') 
                    
            for j in range(len(self.data[i])):
                print(self.data[i][j], end  = '  ')
            print(' ','|', c)


    def fillWithValue(self, newValue):
        """ This function is used to fill the matrix with new value"""
        self.data = [] 
        for x in range(self.ligne):      
            sousTab = []                 
            for y in range(self.colonne): 
                sousTab.append(newValue)                                            
            self.data.append(sousTab)     
    
    def getList(self, content):
        """ This function returns the dictionaries keys of the content file as a list """
        return [*content]

    
    def getDictFromFile(self,content):
        """ this function returns a dictionary containing the files and their indexes """
        dict = {}
        keys = list(content.keys())
        for i in range(len(keys)):
            dict[keys[i]] = i
        return dict
    
    def loadDataFromFile(self, content):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        #Complexité = O(n²) => dépend de la taille de content au carré
        
        self.indexToKey = list(content.keys())                      # O(n) 
        print(self.indexToKey)
        self.keyToIndex = self.getDictFromFile(content)
        print(self.keyToIndex)
        
        self.fillWithValue(0)
        for i in range(len(self.indexToKey)):
            keyI = self.indexToKey[i]            
            for keyJ in content[keyI]:
                j = self.keyToIndex[keyJ] 
                self.data[i][j] = 1
                
    
    def getTableFromFile(self, content):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        #Complexité = O(i²) => dépend de la taille de content
        liste = self.getList(content)
        for i in range(len(liste)):

            keys_File = self.indexToKey
            if liste[i]== keys_File:
                for j in  range(len(content[keys_File])):
                    for a in range(len(liste)):
                        if content[keys_File][j] == liste[a]:
                            self.data[i][a] = 1
            keys_File = 0
            
            
if __name__== "__main__" :
    x = load()
    
    tableau = Tableau(len(x), len(x) )
    tableau.getTableFromFile(x)
    tableau.loadDataFromFile(x)
    tableau.affiche(x)
    print(timeit.timeit('[func(x) for func in (tableau.getTableFromFile(x),tableau.loadDataFromFile(x))]', globals=globals()))