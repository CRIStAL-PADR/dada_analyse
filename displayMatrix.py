# -*-coding: utf-*-
def getColor(val):
    color = { 0 : "#FF00FF"  ,1 : "#00FF00", 2 :" #f5ce62" , 3 : "#b0be6e", 4 : "#a4c073" , 5 : " #ecac67", 6 : "#e5926b", 7 : "#ecac67", 8 : "#00FF00", 9 :"#FFFF00", 10 : " #008080"}
    if (val< 0):
        val = 0
    elif(val>=10):
        val = 10
    for key, value in color.items():
        if key == val:
            return value

def PrintInHtmlFormat(tableau):
    
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
        print('<td>{}</td>'.format(keyA),'<td>{}</td>'.format(c))
        for j in range(len(tableau.data[i])):
            if tableau.data[i][j] ==None:
                print('<td>-</td>', end  = ' ')
            else:
                keyC = tableau.data[i][j]
                color = getColor(keyC)
                print('<td style="background-color : {}">{}</td>'.format(color,tableau.data[i][j]) , end  = ' ')
        print('<td>{}</td>'.format(keyB))
    print(""" <tr> """)
    print("""
    </table>
    </h
    """)