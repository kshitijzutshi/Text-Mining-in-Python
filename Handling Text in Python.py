#Examples for text handling using python

#!/usr/bin/env python# 
-*- coding: utf-8 -*-

text1="Hi my name is Maxwell edward Stark"
text2=text1.split(' ')
print (text2)
for w in text2:
    if len(w) > 3:
        print(w)

print("Words in caps =")
for w in text2:
    if w.istitle():
        print(w)
