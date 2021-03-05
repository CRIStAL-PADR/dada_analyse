import include_graph as file


def load():
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

    print(dictionary)
            
    return dictionary

load()
