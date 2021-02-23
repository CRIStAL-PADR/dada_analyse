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
            key = self.getFileFromIndex(i,content)
            
            if len(key[1])<9:
                if key[0]<=9:
                    print(key[1],'              ',key[0], '  ', end = '|')
                if key[0] >9 and key[0] <=99:
                    print(key[1],'              ',key[0], ' ', end = '|')  
                if key[0] >99 :
                    print(key[1],'              ',key[0], '',end = '|') 
                    
            if len(key[1])==9:
                if key[0]<=9:
                    print(key[1], '            ',key[0], '  ', end = '|')
                if key[0] >9 and key[0] <=99:
                    print(key[1],'            ',key[0], ' ', end = '|') 
                if key[0] >99 :
                    print(key[1],'          ',key[0],'', end = '|') 
            
            if len(key[1])>9:
                if key[0]<=9:
                    print(key[1][:3]+"..."+key[1][-5:], '          ',key[0], '  ', end = '|')
                if key[0] >9 and key[0] <=99:
                    print(key[1][:3]+"..."+key[1][-4:],'           ',key[0], ' ', end = '|') 
                if key[0] >99 :
                    print(key[1][:3]+"..."+key[1][-3:],'         ',key[0],'', end = '|') 
                    
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
        keys = self.getList(content)
        for i in range(len(keys)):
            dict[keys[i]] = i
        return dict
    
    def getTableFromFile2(self, content):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        #Complexité = O(i²) => dépend de la taille de content
        liste = self.getList(content)
        dictionnary = self.getDictFromFile(content)
        for i in range(len(liste)):
            keys_File = self.getFileFromIndex(i,content)[1]
            if liste[i]== keys_File:
                for j in  range(len(content[keys_File])):
                    a = content[keys_File][j]
                    b = dictionnary.get(a)
                    print(a, '=>',b)
                    self.data[i][dictionnary.get(content[keys_File][j])]=1
            keys_File = 0
    
    def getTableFromFile(self, content):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        #Complexité = O(i²) => dépend de la taille de content
        liste = self.getList(content)
        for i in range(len(liste)):

            keys_File = self.getFileFromIndex(i,content)[1]
            if liste[i]== keys_File:
                for j in  range(len(content[keys_File])):
                    for a in range(len(liste)):
                        if content[keys_File][j] == liste[a]:
                            self.data[i][a] = 1
            keys_File = 0
            
            
    def getFileFromIndex(self, index, content):
        """ This function takes as parameter a file which is a dictionary and an index number then returns a
        tuple which is the dictionary key and its index number"""
        #Complexité = O(len(content)) => dépend de la taille de content
        keys = []
        liste = self.getList(content)
        for i in range( len(liste)):
            keys.append(i)
        if index == keys[index]:
            return index,liste[index]

            
if __name__== "__main__" :
    x = load()
    
    tableau = Tableau(len(x), len(x) )
    tableau.getTableFromFile2(x)
    tableau.affiche(x)