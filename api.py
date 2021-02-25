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
        self.indexToKey = []
        self.keyToIndex = {}
        self.content = load()
                
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
          
    
    def affiche(self,n=0):
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
        """
        array = self.getPath()
        liste = self.getList()
        for x in range(len(liste)):
            if x == 0:
                print('                              ',x, end = ' ')
            if x<=9 and x>0:
                print('',x, '', end = '')
            if x >9 :
                print('',x,end = '') 
        print('')
       
        for x in range(len(liste)):
            print('------', end = '')
        for i in range(len(self.content)):
            print('  ') 
            c = self.compterLigne(i,1)
            print('i = ',i)
            keyA = self.indexToKey[i]
            keyB = self.keyToIndex[keyA]
           
            if len(keyA)<9:
                if keyB<=9:
                    print(keyA,'                 ',keyB, '  ', end = '|')
                if keyB >9 and keyB <=99:
                    print(keyA,'                 ',keyB, ' ', end = '|')  
                if keyB >99 :
                    print(keyA,'                 ',keyB, '',end = '|') 
                    
            if len(keyA)==9:
                if keyB<=9:
                    print(keyA, '               ',keyB, '  ', end = '|')
                if keyB >9 and keyB <=99:
                    print(keyA,'               ',keyB, ' ', end = '|') 
                if keyB>99 :
                    print(keyA,'             ',keyB,'', end = '|') 
            
            if len(keyA)>9:
                if keyB<=9:
                    print(keyA[:3]+"..."+keyA[-5:], '             ',keyB, '  ', end = '|')
                if keyB >9 and keyB <=99:
                    print(keyA[:3]+"..."+keyA[-4:],'              ',keyB, ' ', end = '|') 
                if keyB >99 :
                    print(keyA[:3]+"..."+keyA[-3:],'            ',keyB,'', end = '|') 
                    
            for j in range(len(self.data[i])):
                if n ==0:
                    if self.data[i][j] ==999999:
                        self.data[i][j] = 0
                    print(self.data[i][j], end  = '  ')
                if n==1:
                    if array[i][j] ==999999:
                        array[i][j] = 'r'
                    print(array[i][j], end  = '  ')
            if n ==0:
                print(' ','|', c)
            if n ==1:
                print(' ','|')


    def fillWithValue(self, newValue):
        """ This function is used to fill the matrix with new value"""
        self.data = [] 
        self.newdata = []
        for x in range(self.ligne):      
            sousTab = []                 
            for y in range(self.colonne): 
                sousTab.append(newValue)                                            
            self.data.append(sousTab)
            self.newdata.append(sousTab)
    
    def getList(self):
        """ This function returns the dictionaries keys of the content file as a list """
        return [*self.content]

    
    def getDictFromFile(self):
        """ this function returns a dictionary containing the files and their indexes """
        dict = {}
        keys = list(self.content.keys())
        for i in range(len(keys)):
            dict[keys[i]] = i
        return dict
    
    def getPath(self):
        v = len(self.content)
        array = []
        array = list(map(lambda i: list(map(lambda j: j, i)), self.data))
        for i in range(v):
            array[i][i] = 0
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if array[i][j] > array[i][k] + array[k][j]:
                        array[i][j] =  array[i][k] + array[k][j]
        return array
    
        """for i in range(len(self.newdata)):
            for j in range(len(self.newdata[i])):
                if self.newdata[i][j]==9:
                    self.newdata[i][j]= 'r'
                print(self.newdata[i][j], end = '  ')
            print('  ')
        """

    def loadDataFromFile(self):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        #Complexité = O(n²) => dépend de la taille de content au carré
        self.indexToKey = list(self.content.keys())                       
        self.keyToIndex = self.getDictFromFile()
        self.fillWithValue(999999)
        for i in range(len(self.indexToKey)):
            keyI = self.indexToKey[i]            
            for keyJ in self.content[keyI]:
                j = self.keyToIndex[keyJ] 
                self.data[i][j] = 1
    
    def getTableFromFile(self):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        #Complexité = O(i²) => dépend de la taille de content
        liste = self.getList(self.content)
        for i in range(len(liste)):

            keys_File = self.indexToKey
            if liste[i]== keys_File:
                for j in  range(len(self.content[keys_File])):
                    for a in range(len(liste)):
                        if self.content[keys_File][j] == liste[a]:
                            self.data[i][a] = 2
            keys_File = 0
            
            
if __name__== "__main__" :
    x = load()
    
    tableau1 = Tableau(len(x), len(x) ) 
    tableau2 = Tableau(len(x), len(x) )
    tableau3 = Tableau(len(x), len(x))
    
    tableau2.loadDataFromFile()
    tableau1.loadDataFromFile()  # rempli le tableau avec des 1 quand il y a un lien entre 2 fichiers
    tableau3.loadDataFromFile()
    
    tableau2.affiche() # affiche un tableau qui indique le lien entre 2 fichiers avec des 1
    print('')
    tableau1.affiche(1) # affiche le tableau rempli par les chemins les plus court
    print('    ')
    tableau3.getPath()
    #print(tableau3.data)
    print(tableau3.indexToKey)
    tableau3.affiche()
    #print(timeit.timeit('[func(x) for func in (tableau.getTableFromFile(x),tableau.loadDataFromFile(x))]', globals=globals()))