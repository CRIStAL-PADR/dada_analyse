def PrintInHtmlFormat(tableau):
    liste = tableau.getList()
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
    for i in range(len(tableau.data)):
        c = tableau.compterLigne(i)
        keyA = tableau.indexToKey[i]
        keyB = tableau.keyToIndex[keyA]
        print(""" <tr> """)
        print('<td>{}</td>'.format(keyA[-5:]),'<td>{}</td>'.format(keyB))
        for j in range(len(tableau.data[i])):
            if tableau.data[i][j] ==None:
                print('<td>-</td>', end  = ' ')
            else:
                print('<td>{}</td>'.format( tableau.data[i][j]) , end  = ' ')
        print('<td>{}</td>'.format(c))
    print(""" </tr> """)
    print("""
          </table>
          </html>""")