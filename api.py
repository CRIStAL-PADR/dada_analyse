# -*-coding: utf-*-
import file
import numpy
tab=[]

class File:

    def load(self):
        return file.content
    


if __name__=="__main__":
    x = File()
    y = x.load()
    line = 0
    for row in y:
        tab.append(row)
        tab.append('')
        line = line+1    # calcul le nombre de ligne dans le fichier
    print(tab)
    
