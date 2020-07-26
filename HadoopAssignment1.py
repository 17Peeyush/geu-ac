# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 09:17:21 2020

@author: Peeyush Pratap Singh
"""
#reading file
fp=open("a.txt","r")
content=fp.read()
#removing punctuations
punc="'!(),.?"
for w in content:
    if w in punc:
        content=content.replace(w,"")
#spliting sentence and storing unique words
l=content.split(" ")
s=set(l)
#storing words and their frequency in key value pair
d={}
for letter in s:
    d[letter]=content.count(letter);
print(d)
fp.close();
