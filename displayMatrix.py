def PrintInHtmlFormat(oldtableau, newtableau):
    liste = oldtableau.getList()
    liste = liste[:30]
    print ("""
           <html>
           <table width="70%" border = " 5" align="center" >
           <link ref = "stylesheet" href = "style.css">
           <tr>""")
    for x in range(len(liste)):
        if x ==0:
            print('<td>&nbsp;</td>')
            print('<td>&nbsp;</td>')
            print( '<td class = "td">{}</td> '.format(x))
        elif x  <=9 and x >0:
            print('<td>{}</td> '.format(x), end = ' ')
        else : 
            print( '<td>{}</td> '.format(x) , end = ' ')
    print("""
          </tr>
          """)
    for i in range(len(newtableau.data)):
        c = newtableau.compterLigne(i)
        keyA = oldtableau.indexToKey[i]
        keyB = oldtableau.keyToIndex[keyA]
        print(""" <tr> """)
        print('<td>{}</td>'.format(keyA[-74:]),'<td>{}</td>'.format(keyB))
        for j in range(len(newtableau.data[i])):
            if newtableau.data[i][j] ==None:
                print('<td>-</td>', end  = ' ')
            else:
                print('<td>{}</td>'.format( newtableau.data[i][j]) , end  = ' ')
        print('<td>{}</td>'.format(c))
    print(""" </tr> """)
    print("""
          </table>
          </html>""")