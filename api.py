# -*-coding: utf-*-
"""
    copyright (C) 2021
"""
from operator import itemgetter
from PIL import Image
import include_graph as file
import display_matrix


def get_color(val):
    """This function takes a key as a parameter and returns the
    corresponding color"""
    color = {0: (255, 255, 255),
             1: (0, 0, 204),
             2: (0, 153, 102),
             3: (51, 255, 204),
             4: (102, 0, 102),
             5: (169, 169, 169),
             6: (0, 136, 68),
             7: (0, 153, 102),
             8: (153, 0, 0),
             9: (51, 0, 0),
             10: (153, 51, 254)}
    if val < 0:
        val = 0
    elif val >= 10:
        val = 10
    return color[val]

def draw_sparse_matrix_from_table(matrice, nom):
    """ This function is used to create from an array an image where
    the pixels correspond to the value of the indices contained in the array"""
    length = matrice.size[0]
    width = matrice.size[1]
    new_im = Image.new('RGB', (length, width), (255, 255, 255))
    for i in range(length):
        for j in range(width):
            if matrice.data[i][j] is None:
                key_color = 0
            else:
                key_color = matrice.data[i][j]
            color = get_color(key_color)
            new_im.putpixel((i, j), color)
    new_im.save(nom)

def load(fichier):
    """ Takes the file as a parameter then transforms it into a dictionary"""
    i = 'sources'
    dictionary = {}
    liste = []
    for  key in fichier.content.keys():
        for j in fichier.content[key].keys():
            if j == i:
                for value in fichier.content[key][j]:
                    liste.append(value)
                dictionary[key] = liste
                liste = []

    return dictionary

def create_new_table(old_tableau, start, stop):
    """ When an array is given as a parameter, returns an
    array of smaller size"""
    new_tableau = Tableau()
    array = new_tableau.data
    if old_tableau is None:
        raise RuntimeError()

    new_tableau.ligne = stop - start    # mis à jour des tailles du tableau
    new_tableau.colonne = new_tableau.ligne
    new_tableau.size = [new_tableau.ligne, new_tableau.colonne]

    new_tableau.index_to_key = old_tableau.index_to_key.copy()
    new_tableau.index_to_key = new_tableau.index_to_key[start:stop]

    keys = list(old_tableau.content.keys())
    keys = keys[start: stop]
    length_keys = len(keys)
    for i in range(length_keys):
        new_tableau.key_to_index[keys[i]] = i  # mis à jour de keyTo index


    for i in range(start, stop):
        soustab = []
        for j in range(start, stop):
            soustab.append(
                old_tableau.data[i][j])    # remplissage du nouveau tableau
        array.append(soustab)
    return new_tableau



class Tableau:
    """ This class allows you to build an array"""
    def __init__(self, ligne=0, colonne=0, default_value=None):
        self.ligne = ligne
        self.colonne = colonne
        self.data = []
        self.fill_with_value(default_value)
        self.index_to_key = []
        self.content = {}
        self.key_to_index = {}
        self.size = [self.ligne, self.colonne]

    def compte_colone(self, column, value):
        """ retourne le nombre de foix ou sur une ligne 'l'
        il y a la valeur 'value' """
        count = 0
        for i in range(len(self.data)):
            for _ in range(len(self.data[column])):
                if value == self.data[i][column]:
                    count = count+1
                    break
        return count

    def compter_ligne(self, line, value=None):
        """retourne le nombre de foix ou sur une ligne 'l'
        il y a la valeur "value" """
        count = 0
        for j in range(len(self.data[line])):
            if (self.data[line][j] != value and self.data[line][j] != 0):
                count = count+1
        return count

    def affiche(self):
        """This function takes a generated file as a parameter and displays
        a dependency graph between the different
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
        for indice in range(len(liste)):
            if indice == 0:
                print('                                                       ', indice, end=' ')
            elif  indice in range(1, 10):
                print('', indice, '', end='')
            else:
                print('', indice, end='')
        print('')

        for i in range(len(liste)):
            print('  ')
            count = self.compter_ligne(i)
            key_a = self.index_to_key[i]
            key_b = self.key_to_index[key_a]

            if len(key_a) < 9:
                if key_b <= 9:
                    print(key_a, '                 ', key_b, '  ', end='|')
                elif key_b in range(10, 100):
                    print(key_a, '                 ', key_b, ' ', end='|')
                else:
                    print(key_a, '                 ', key_b, '', end='|')

            elif len(key_a) == 9:
                if key_b <= 9:
                    print(key_a, '               ', key_b, '  ', end='|')
                elif key_b in range(10, 100):
                    print(key_a, '               ', key_b, ' ', end='|')
                else:
                    print(key_a, '             ', key_b, '', end='|')

            else:
                if key_b <= 9:
                    print(key_a[:3]+"..."+key_a[-30:], '             ', key_b, '  ', end='|')
                elif key_b in range(10, 100):
                    print(key_a[:3]+"..."+key_a[-29:], '              ', key_b, ' ', end='|')
                else:
                    print(key_a[:3]+"..."+key_a[-28:], '            ', key_b, '', end='|')

            for j in range(len(self.data[i])):

                if self.data[i][j] is None:
                    print('-', end='  ')
                else:
                    print(self.data[i][j], end='  ')

            print(' ', '|', count)

    def fill_with_value(self, new_value):
        """ This function is used to fill the matrix with new value"""
        self.data = []
        for _ in range(self.ligne):
            sous_tab = []
            for _ in range(self.colonne):
                sous_tab.append(new_value)
            self.data.append(sous_tab)

    def get_list(self):
        """ This function returns the dictionaries keys of
        the content file as a list """
        return [*self.content]


    def get_dict_from_file(self):
        """this function returns a dictionary containing the files
        and their indexes """
        keys = list(self.content.keys())
        length_keys = len(keys)
        for i in range(length_keys):
            self.key_to_index[keys[i]] = i

    def floyd_warshall(self, tableau=None):
        "Use FLOYDWARSHALL algoritm to find all pairs shortest path  "

        if tableau is None:
            tableau = Tableau(self.size[0], self.size[1])
        elif tableau.size != self.size:
            raise RuntimeError()

        tableau.index_to_key = self.index_to_key.copy()
        tableau.key_to_index = self.key_to_index.copy()

        array = tableau.data
        length = len(array)
        for i in range(length):
            for j in range(length):
                if i == j:
                    array[i][i] = 0
                elif self.data[i][j] == 1:
                    array[i][j] = 1
                else:
                    array[i][j] = 9999999
        for k in range(length):
            for i in range(length):
                for j in range(length):
                    if array[i][j] > array[i][k] + array[k][j]:
                        array[i][j] = array[i][k] + array[k][j]
        for i in range(length):
            for j in range(length):
                if array[i][j] == 9999999:
                    array[i][j] = None
        return tableau



    def load_data_from_file(self, content):
        """ returns a new array, containing zeros when there is no
        link between two files and a 1 when there is a link"""
        # I load the file
        self.content = load(content)
        self.index_to_key = list(self.content.keys())

        self.key_to_index = self.get_dict_from_file
        self.ligne = len(self.content)+1
        self.colonne = len(self.content)+1
        self.size = [len(self.content)+1, len(self.content)+1]
        self.fill_with_value(0)

        for i in range(len(self.index_to_key)):
            key_i = self.index_to_key[i]
            for key_j in self.content[key_i]:
                if key_j in self.content:
                    j = self.key_to_index[key_j]
                    self.data[i][j] = 1
                else:
                    self.content.update({key_j: [key_i]})
                    self.index_to_key.append(key_j)
                    self.key_to_index = self.get_dict_from_file()
                    j = self.key_to_index[key_j]
                    self.data[i][j] = 1

    def count_path_from_tableau(self, tableau):
        """  This function takes an array as a parameter and returns a tuple
            containing filename, path and index, sorted by path
         """
        length = len(tableau.index_to_key)
        tab = []
        for i in range(length):
            count = self.compter_ligne(i)
            tab.append((tableau.index_to_key[i], count, i))
        return sorted(tab, key=itemgetter(1), reverse=True)

    def sorted_tableau(self, tableau, old_tableau):
        """ This function takes in parameter 2 array and returns a new
         sorted by the filename that contains the most path
        """
        liste = self.count_path_from_tableau(tableau)
        new_tableau = Tableau()
        length = len(tableau.index_to_key)
        for i in range(length):
            new_tableau.index_to_key.append(liste[i][0]) # je construit mon index_to_key

        for i in range(length):  # je reconstruit mon key_to_index
            new_tableau.key_to_index[new_tableau.index_to_key[i]] = i

        new_tableau.ligne = length
        new_tableau.colonne = length
        new_tableau.size = [length, length]
        new_tableau.fill_with_value(0)

        for i in range(length):
            key = old_tableau.content[new_tableau.index_to_key[i]]
            new_tableau.content[new_tableau.index_to_key[i]] = key

        for i in range(len(new_tableau.index_to_key)):
            key_i = new_tableau.index_to_key[i]
            for key_j in new_tableau.content[key_i]:
                if key_j in new_tableau.content:
                    j = new_tableau.key_to_index[key_j]
                    new_tableau.data[i][j] = 1
        return new_tableau

if __name__ == "__main__":

    tableau1 = Tableau()
    tableau1.load_data_from_file(file)
    tableau2 = create_new_table(tableau1, 30, 100)
    tableau3 = tableau2.floyd_warshall(Tableau(tableau2.size[0], tableau2.size[1]))
    tableau4 = tableau3.sorted_tableau(tableau3, tableau1)
    tableau4 = tableau4.floyd_warshall(Tableau(tableau4.ligne, tableau4.colonne))

    display_matrix.print_in_html_format(tableau3)
    print('\n')
    display_matrix.print_in_html_format(tableau4)
