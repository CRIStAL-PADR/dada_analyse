from yattag import Doc
from yattag import indent

doc, tag, text = Doc().tagtext( )

with tag('html'):
    with tag('table' , width = '70%' , border = '6'):
        with tag('tr'):
            with tag('td'):
                text(' &nbsp;')
                text('i = 0 ')
                text('i = 2')
                text('i = 3 ')
                text('i = 4 ')
        with tag('tr'):
            with tag('td'):
                text('File1.cpp')
                text(' j= 0 ')
                text('[0][0]')
                text('[0][1]')
                text('[0][2]')
                text('[0][3]')
        with tag('tr'):
            with tag('td'):
                text('File1.cpp')
                text(' j= 1 ')
                text('[1][0]')
                text('[1][1]')
                text('[1][2]')
                text('[1][3]')
              

result = indent(
        doc.getvalue(),
        indentation  =' ',
        newline = '\r\n',
        indent_text = True,
        )
print(result)