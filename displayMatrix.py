def PrintInHtmlFormat(tableau):
    couleur = { 0 : "#FFFF00" ,1 : "#00FF00", 2 :" #f5ce62" , 3 : "#b0be6e", 4 : "#a4c073" , 5 : " #ecac67", 6 : "#e5926b", 7 : "#ecac67"}
    liste = tableau.indexToKey
    print ("""
    <html>
    <table width="70%" border = " 5" align="center" >
        <tr>
    """)
    for x in range(len(liste)):
        if x ==0:
            print('<td>&nbsp;</td>')
            print('<td>&nbsp;</td>')
            print( '<td class = "td">{}</td> '.format(x), end = ' ')
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
                keyC = tableau.data[i][j]
                print('<td style="background-color : {}">{}</td>'.format(couleur[keyC],tableau.data[i][j]) , end  = ' ')
        print('<td>{}</td>'.format(c))
    print(""" <tr> """)
    print("""
    </table>
    </h
    """)