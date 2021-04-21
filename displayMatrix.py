# -*-coding: utf-*-
def get_color(val):
    """This function takes a key as a parameter and returns the
    corresponding color """
    color = {0: "#000066",
             1: "#0000CC",
             2: "#009966",
             3: "#33FFCC",
             4: "#660066",
             5: "#660066",
             6: "#e5926b",
             7: "#ecac67",
             8: "#00FF00",
             9: "#FFFF00",
             10: "#008080"}
    if val < 0:
        val = 0
    elif val >= 10:
        val = 10
    for key, value in color.items():
        if key == val:
            return value

def PrintInHtmlFormat(tableau):   
    liste = tableau.index_to_key
    print("""
    <html>
    <style>
    .content{
        visibility: hidden;
        background : #bfbfbf;
        padding:15px;
        position: absolute;
        }
        .wrapper:hover .content{
            visibility: visible;
        }
        .content::before{
            content:"";
            border-style:solid;
            border-width:0px 10px 10px 10px;
            border-color : transparent transparent #bfbfbf transparent;
            position: absolute;
            top: -10px;
        }
    </style>
    <table width="70%" border = " 5" align="center" >
        <tr>
    """)
    for x in range(len(liste)):
        if x == 0:
            print('<td>&nbsp;</td>')
            print('<td>&nbsp;</td>')
            print('<td class = "td">{}</td> '.format(x), end=' ')
        if x <= 9 and x > 0:
            print('<td>{}</td> '.format(x), end=' ')
        if x >= 10:
            print('<td>{}</td> '.format(x), end=' ')
    print("""
          </tr>
          """)
    for i in range(len(tableau.data)):
        c = tableau.compter_ligne(i)
        keyA = tableau.index_to_key[i]
        keyB = tableau.key_to_index[keyA]
        print(""" <tr> """)
        print('<td>{}</td>'.format(keyA), '<td>{}</td>'.format(c))
        for j in range(len(tableau.data[i])):
            if tableau.data[i][j] is None:
                print('<td>-</td>', end=' ')
            else:
                keyC = tableau.data[i][j]
                color = get_color(keyC)
                print('<td class = "wrapper" style="background-color : {}"> <div class = "text">{}</div> <div class = "content"> {}</div> </td>'.format(color,tableau.data[i][j],keyA), end  = ' ')
        print('<td>{}</td>'.format(keyB))
    print(""" <tr> """)
    print("""
    </table>
    </h
    """)
