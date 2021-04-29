# -*-coding: utf-*-
"""
    copyright (C) 2021
"""
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
    return color[val]

def print_in_html_format(tableau):
    """ This function takes an array as a parameter and displays it in HTML format"""
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
        .col{
            width : 50px !important;
            text-align : center;

        }
        .active:active {
            background-color : #df2545;
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
    <table border = "5" align="center" >
        <tr>
    """)
    for index in range(len(liste)):
        if index == 0:
            print('<td class = "col" >&nbsp;</td>')
            print('<td class = "col" >&nbsp;</td>')
            print('<td  class = "col">{}</td> '.format(index), end=' ')
        if index != 0:
            print('<td class = "col" >{}</td> '.format(index), end=' ')
    print("""
          </tr>
          """)

    for i in range(len(tableau.data)):
        count = tableau.compter_ligne(i)
        key_a = tableau.index_to_key[i]
        key_b = tableau.key_to_index[key_a]
        print(""" <tr> """)
        print('<td id = "{}" class="active">{}</td>'.format(i,key_a[-45:]), '<td class = "col">{}</td>'.format(count))
        for j in range(len(tableau.data[i])):
            if tableau.data[i][j] is None:
                print('<td class = "col" >-</td>', end=' ')
            else:
                key_c = tableau.data[i][j]
                color = get_color(key_c)
                key_d = tableau.index_to_key[j]
                print("""<td class = "wrapper col" style="background-color : {}">
                <div class = "text">{}</div>
                <div class =  "content"> <a href ="#{}"> {} {} {}</a> </div>
                </td>""".format(color, tableau.data[i][j], j, key_d, i, j), end=' ')
        print('<td class = "col" >{}</td>'.format(key_b))
    print(""" <tr> """)
    print("""
    </table>
    </h
    """)
