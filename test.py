#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:58:02 2021

@author: fabrice
"""

import include_graph as file


def load():

    i = 'sources'
    dictionary = {}
    file.content
    for  key in file.content.keys():
        for j in file.content[key].keys():
            if j == i:
                for a in file.content[key][j]:
                    dictionary[key] = a #cette partie est à revoir
    print(dictionary)
    return dictionary
    
load()