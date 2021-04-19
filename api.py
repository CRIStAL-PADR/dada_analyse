# -*-coding: utf-*-
import include_graph as file
import displayMatrix
from PIL import Image

def getColor(val):
    color = { 0 : (0,0,102)  ,1 :(0,0,204), 2 :(0,153,102) , 3 :(51,255,204), 4 :(102,0,102), 5 : (169,169,169) , 6 :(0,136,68), 7 : (0,153,102), 8 : (153,0,0), 9 :(51,0,0), 10 : (153,51,254)}
    if (val< 0):
        val = 0
    elif(val>=10):
        val = 10
    for key, value in color.items():
        if key == val:
            return value

def drawSparseMatrixFromTable( matrice):

    a = matrice.size[0]
    b = matrice.size[1]
    new_im  = Image.new('RGB', (a,b), (255,255,255))
    for i in range(b):
        for j in range(a):
            if (matrice.data[i][j] == None):
                keyColor = 0
            else:
                keyColor = matrice.data[i][j]
            color = getColor(keyColor)
            new_im.putpixel( (i, j), color )
    new_im.save("MonImage.png", "PNG")

def load(file):
    """ Prend en paramètre le fichier puis le transforme en dictionnaire"""
    i = 'sources'
    dictionary = {}
    file.content
    liste  = []
    for  key in file.content.keys():
        for j in file.content[key].keys():
            if j == i:
                for a in file.content[key][j]:
                    liste.append(a)
                dictionary[key] = liste
                liste = []

    return dictionary

class Tableau:
    def __init__(self, ligne=0, colonne=0, defaultValue = None):
        self.ligne = ligne
        self.colonne = colonne
        self.defaultValue = defaultValue
        self.data = []
        self.fillWithValue(self.defaultValue)
        self.indexToKey = []
        self.content = {}
        self.keyToIndex = {}
        self.size = [self.ligne, self.colonne]

    def compteColone(self, c, value):
        """ retourne le nombre de foix ou sur une ligne 'l' il y a la valeur 'value' """
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
        liste = self.indexToKey
        
        for x in range(len(liste)):
            if x == 0:
                print('                                                       ',x, end = ' ')
            if x<=9 and x>0:
                print('',x, '', end = '')
            if x >9 :
                print('',x,end = '')
        print('')

        for x in range(len(liste)):
            print('------', end = '')
        for i in range(len(liste)):
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
                    print(keyA[:3]+"..."+keyA[-30:], '             ',keyB, '  ', end = '|')
                if keyB >9 and keyB <=99:
                    print(keyA[:3]+"..."+keyA[-29:],'              ',keyB, ' ', end = '|')
                if keyB >99 :
                    print(keyA[:3]+"..."+keyA[-28:],'            ',keyB,'', end = '|')

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

    def floydWarshall(self, tableau=None):
        "Use FLOYDWARSHALL algoritm to find all pairs shortest path  "
    
        if tableau == None:
            tableau = Tableau(self.size[0],self.size[1])
        elif tableau.size != self.size:
            raise RuntimeError()

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



    def loadDataFromFile(self, content):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when there is a link """
        #Complexité = O(n²) => dépend de la taille de content au carré

        self.content = load(content) #I load the file
        self.indexToKey = list(self.content.keys())

        self.keyToIndex = self.getDictFromFile()
        self.ligne = len(self.content)+1
        self.colonne = len(self.content)+1
        self.size = [len(self.content)+1,len(self.content)+1]
        self.fillWithValue(0)

        for i in range(len(self.indexToKey)):
            keyI = self.indexToKey[i]
            for keyJ in self.content[keyI]:
                if keyJ in self.content :
                    j = self.keyToIndex[keyJ]
                    self.data[i][j] = 1
                else :
                    self.content.update({keyJ : [keyI]}) # I add the missing key to the dictionary
                    self.indexToKey.append(keyJ) # I add the missing key to the list indexToKey
                    self.keyToIndex = self.getDictFromFile() # Updates the KeyToIndex dictionary
                    j = self.keyToIndex[keyJ] #  Get the index when a key is given
                    self.data[i][j] = 1
    
    def createNewTable(self, oldTableau, start , stop):
        """ When an array is given as a parameter, returns an array of smaller size"""

        newTableau = Tableau()

        array = newTableau.data
        if oldTableau == None : 
            raise RuntimeError()

        newTableau.ligne = stop - start # mis à jour des tailles du tableau
        newTableau.colonne = newTableau.ligne
        newTableau.size = [newTableau.ligne, newTableau.colonne]

        newTableau.indexToKey = oldTableau.indexToKey.copy()
        newTableau.indexToKey = newTableau.indexToKey[start: stop] # mis à jour de indexToKey

        keys = list(oldTableau.content.keys())
        keys = keys[start : stop]
        for i in range(len(keys)):
            newTableau.keyToIndex[keys[i]] = i  # mis à jour de keyTo index

        for i in range(start, stop):
            soustab = []
            for j in range(start, stop):
                a = oldTableau.data[i][j] 
                soustab.append(a)    # remplissage du nouveau tableau
            array.append(soustab)
        return newTableau


if __name__== "__main__" :

    tableau1 = Tableau( )
    tableau1.loadDataFromFile(file)

    tableau2 = tableau1.createNewTable(tableau1, 10, 40)
    
    tableau3 = tableau2.floydWarshall(Tableau(tableau2.size[0], tableau2.size[1]))
    drawSparseMatrixFromTable(tableau3)