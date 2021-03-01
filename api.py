# -*-coding: utf-*-

import file

def PrintTable(tableau):
    liste = tableau.getList()
    print ("""
<html>
    <table width="70%" border = " 5" align="center">
        <tr>
""")
    for x in range(len(liste)):
        if x ==0:
            print('<td>&nbsp;</td> ')
            print('<td>&nbsp;</td> ')
            print( '<td>{}</td> '.format(x), end = ' ')
        if x <=9 and x>0:
            print('<td>{}</td> '.format(x), end = ' ')
        if x >=10:
            print( '<td>{}</td> '.format(x) , end = ' ')
    print("""
          </tr>
          """)
    for i in range(len(tableau.data)):
        c = tableau.compterLigne(i)
        keyA = tableau.indexToKey[i]
        keyB = tableau.keyToIndex[keyA]
        print(""" <tr> """)
        print('<td>{}</td>'.format(keyA),'<td>{}</td>'.format(keyB))
        for j in range(len(tableau.data[i])):
            if tableau.data[i][j] ==None:
                print('<td>-</td>', end  = ' ')
            else:
                print('<td>{}</td>'.format( tableau.data[i][j]) , end  = ' ')
        print('<td>{}</td>'.format(c))
    print(""" <tr> """)
print("""
    </table>
</h
""")
    

def load():
    return file.content


    
class Tableau:
    def __init__(self, ligne, colonne, defaultValue = None):
        self.ligne = ligne
        self.colonne = colonne
        self.defaultValue = defaultValue
        self.data = []
        self.fillWithValue(self.defaultValue)
        self.indexToKey = []
        self.keyToIndex = {}
        self.content = load()
        self.size = [ligne, colonne]
                
    def compteColone(self, c, value):
        """ retourne le nombre de foix ou sur une ligne 'l' il y a la valeur "value" """
        count = 0
        for i  in range(len(self.data)):
            for j in range(len(self.data[c])):
                if (value == self.data[i][c]):
                    count = count+1
                    break
        return count
    
    def compterLigne(self, l, value = None):
        """retourne le nombre de foix ou sur une ligne 'l' il y a la valeur "value" """
        count = 0
        for j in range(len(self.data[l])):
            if (self.data[l][j]!=value and self.data[l][j]!=0):
                count = count+1        
        return count
          
    
    def affiche(self):
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
            c = self.compterLigne(i)
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
                
                if self.data[i][j] ==None:
                    print('-', end  = '  ')
                else:
                    print(self.data[i][j], end = '  ')
                
            print(' ','|', c)



    def fillWithValue(self, newValue):
        """ This function is used to fill the matrix with new value"""
        self.data = [] 
        for x in range(self.ligne):      
            sousTab = []                 
            for y in range(self.colonne): 
                sousTab.append(newValue)                                            
            self.data.append(sousTab)
          
    
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
    
    def getPath(self, tableau=None):
        if tableau == None:
            tableau = Tableau(self.size[0],self.size[1])
        elif tableau.size != self.size:
            raise runtime_error()    
            
        tableau.indexToKey = self.indexToKey.copy()
        tableau.keyToIndex = self.keyToIndex.copy()
        
        array =  tableau.data
        v = len(array)
        for i in range(v):
            for j in range(v):
                if i ==j:
                    array[i][i] = 0
                elif self.data[i][j]==1:
                    array[i][j] = 1
                else:
                    array[i][j]=9999999
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if array[i][j] > array[i][k] + array[k][j]:
                        array[i][j] =  array[i][k] + array[k][j]
        for i in range(v):
            for j in range(v):
                if array[i][j] ==  9999999:
                    array[i][j]= None
        return tableau
    
        

    def loadDataFromFile(self):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        #Complexité = O(n²) => dépend de la taille de content au carré
        self.indexToKey = list(self.content.keys())                       
        self.keyToIndex = self.getDictFromFile()
        
        self.fillWithValue(0)
        
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
    tableau1.loadDataFromFile()
    
    tableau2 = tableau1.getPath( Tableau(tableau1.size[0], tableau1.size[1]) )
    #tableau3 = tableau2.getPath()
    
    #tableau1.affiche()
    #tableau2.affiche()
    PrintTable(tableau2)
    PrintTable(tableau1)
  
