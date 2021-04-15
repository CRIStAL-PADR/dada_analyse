# -*-coding: utf-*-
import imgkit

with open('test.html') as f:
    imgkit.from_file(f, 'tableau.jpg')

