# -*-coding: utf-*-
from PIL import Image
import include_graph as file
import displayMatrix


def get_color(val):
    """This function takes a key as a parameter and
    returns the corresponding color""" 
    color = {0 :(255, 255, 255), 1 :(0, 0, 204), 2 :(0, 153, 102), 3 :(51, 255, 204), 4 :(102, 0, 102), 5 : (169, 169, 169), 6 :(0, 136, 68), 7: (0, 153, 102), 8: (153, 0, 0), 9 :(51, 0, 0), 10: (153, 51, 254)}
    if val < 0:
        val = 0
    elif val >= 10:
        val = 10
    return color[val]

def draw_sparse_matrix_from_table(matrice, nom):
    """ This function is used to create from an array an image where the pixels correspond to the value of the indices contained in the array"""
    a = matrice.size[0]
    b = matrice.size[1]
    new_im = Image.new('RGB', (a, b), (255, 255, 255))
    for i in range(a):
        for j in range(b):
            if matrice.data[i][j] is None:
                key_color = 0
            else:
                key_color = matrice.data[i][j]
            color = get_color(key_color)
            new_im.putpixel((i, j), color)
    new_im.save(nom)

def load(file):
    """ Takes the file as a parameter then transforms it into a dictionary"""
    i = 'sources'
    dictionary = {}
    file.content
    liste = []
    for  key in file.content.keys():
        for j in file.content[key].keys():
            if j == i:
                for a in file.content[key][j]:
                    liste.append(a)
                dictionary[key] = liste
                liste = []

    return dictionary

class Tableau:
    def __init__(self, ligne=0, colonne=0, defaultValue=None):
        self.ligne = ligne
        self.colonne = colonne
        self.defaultValue = defaultValue
        self.data = []
        self.fill_with_value(self.defaultValue)
        self.index_to_key = []
        self.content = {}
        self.key_to_index = {}
        self.size = [self.ligne, self.colonne]

    def compte_colone(self, c, value):
        """ retourne le nombre de foix ou sur une ligne 'l' il y a la valeur 'value' """
        count = 0
        for i  in range(len(self.data)):
            for j in range(len(self.data[c])):
                if value == self.data[i][c]:
                    count = count+1
                    break
        return count

    def compter_ligne(self, l, value=None):
        """retourne le nombre de foix ou sur une ligne 'l' il y a la valeur "value" """
        count = 0
        for j in range(len(self.data[l])):
            if (self.data[l][j] != value and self.data[l][j] != 0):
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
        liste = self.index_to_key
        for x in range(len(liste)):
            if x == 0:
                print('                                                       ', x, end=' ')
            if x <= 9 and x > 0:
                print('', x, '', end='')
            if x > 9:
                print('', x, end='')
        print('')

        for x in range(len(liste)):
            print('------', end='')
        for i in range(len(liste)):
            print('  ')
            c = self.compterLigne(i)
            keyA = self.index_to_key[i]
            keyB = self.key_to_index[keyA]

            if len(keyA) < 9:
                if keyB <= 9:
                    print(keyA, '                 ', keyB, '  ', end='|')
                if keyB > 9 and keyB <= 99:
                    print(keyA, '                 ', keyB, ' ', end='|')
                if keyB > 99:
                    print(keyA, '                 ', keyB, '', end='|')

            if len(keyA) == 9:
                if keyB <= 9:
                    print(keyA, '               ', keyB, '  ', end='|')
                if keyB > 9 and keyB <= 99:
                    print(keyA, '               ', keyB, ' ', end='|')
                if keyB > 99:
                    print(keyA, '             ', keyB, '', end='|')

            if len(keyA) > 9:
                if keyB <= 9:
                    print(keyA[:3]+"..."+keyA[-30:], '             ', keyB, '  ', end='|')
                if keyB > 9 and keyB <= 99:
                    print(keyA[:3]+"..."+keyA[-29:], '              ', keyB, ' ', end='|')
                if keyB > 99:
                    print(keyA[:3]+"..."+keyA[-28:], '            ', keyB, '', end='|')

            for j in range(len(self.data[i])):

                if self.data[i][j] is None:
                    print('-', end='  ')
                else:
                    print(self.data[i][j], end='  ')

            print(' ', '|', c)

    def fill_with_value(self, newValue):
        """ This function is used to fill the matrix with new value"""
        self.data = []
        for x in range(self.ligne):
            sousTab = []
            for y in range(self.colonne):
                sousTab.append(newValue)
            self.data.append(sousTab)

    def get_list(self):
        """ This function returns the dictionaries keys of the content file as a list """
        return [*self.content]


    def get_dict_from_file(self):
        """this function returns a dictionary containing the files and their indexes """
        dict = {}
        keys = list(self.content.keys())
        for i in range(len(keys)):
            dict[keys[i]] = i
        return dict

    def floyd_warshall(self, tableau=None):
        "Use FLOYDWARSHALL algoritm to find all pairs shortest path  "
        if tableau is None:
            tableau = Tableau(self.size[0], self.size[1])
        elif tableau.size != self.size:
            raise RuntimeError()

        tableau.index_to_key = self.index_to_key.copy()
        tableau.key_to_index = self.key_to_index.copy()

        array = tableau.data
        v = len(array)
        for i in range(v):
            for j in range(v):
                if i == j:
                    array[i][i] = 0
                elif self.data[i][j] == 1:
                    array[i][j] = 1
                else:
                    array[i][j] = 9999999
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if array[i][j] > array[i][k] + array[k][j]:
                        array[i][j] = array[i][k] + array[k][j]
        for i in range(v):
            for j in range(v):
                if array[i][j] == 9999999:
                    array[i][j] = None
        return tableau



    def load_data_from_file(self, content):
        """ returns a new array, containing zeros when there is no link between two files and a 1 when 
        there is a link """
        # I load the file
        self.content = load(content)  
        self.index_to_key = list(self.content.keys())

        self.key_to_index = self.get_dict_from_file
        self.ligne = len(self.content)+1
        self.colonne = len(self.content)+1
        self.size = [len(self.content)+1, len(self.content)+1]
        self.fill_with_value(0)

        for i in range(len(self.index_to_key)):
            keyI = self.index_to_key[i]
            for keyJ in self.content[keyI]:
                if keyJ in self.content:
                    j = self.key_to_index[keyJ]
                    self.data[i][j] = 1
                else:
                    self.content.update({keyJ : [keyI]})        # I add the missing key to the dictionary
                    self.index_to_key.append(keyJ)              # I add the missing key to the list index_to_key
                    self.key_to_index = self.get_dict_from_file()       # Updates the key_to_index dictionary
                    j = self.key_to_index[keyJ]         #  Get the index when a key is given
                    self.data[i][j] = 1
    
    def create_new_table(self, old_tableau, start, stop):
        """ When an array is given as a parameter, returns an array of smaller size"""

        new_tableau = Tableau()

        array = new_tableau.data
        if old_tableau is None: 
            raise RuntimeError()

        new_tableau.ligne = stop - start # mis à jour des tailles du tableau
        new_tableau.colonne = new_tableau.ligne
        new_tableau.size = [new_tableau.ligne, new_tableau.colonne]

        new_tableau.index_to_key = old_tableau.index_to_key.copy()
        new_tableau.index_to_key = new_tableau.index_to_key[start: stop] # mis à jour de index_to_key

        keys = list(old_tableau.content.keys())
        keys = keys[start : stop]
        for i in range(len(keys)):
            new_tableau.key_to_index[keys[i]] = i  # mis à jour de keyTo index

        for i in range(start, stop):
            soustab = []
            for j in range(start, stop):
                a = old_tableau.data[i][j] 
                soustab.append(a)    # remplissage du nouveau tableau
            array.append(soustab)
        return new_tableau


if __name__ == "__main__":

    tableau1 = Tableau()
    tableau1.load_data_from_file(file)
    tableau2 = tableau1.create_new_table(tableau1, 10, 40)
    tableau3 = tableau1.floyd_warshall(Tableau(tableau1.size[0], tableau1.size[1]))
    draw_sparse_matrix_from_table(tableau2, "tableau.jpg")
    displayMatrix.PrintInHtmlFormat(tableau2)