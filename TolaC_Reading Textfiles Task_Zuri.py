#!/usr/bin/env python
# coding: utf-8

# In[7]:


def readfile(filename):
    filed=open(input("""First ensure your file is within this folder. 
    Please enter file name: """),"r")
    return (filed.read())

def count_words():
    text = readfile("story.text")
    words=(text.lower()).split()
    dict = {}
    for i in words:
        if i in dict:
            dict[i] +=1
        else:
            dict[i]=1
    print(dict)
        
count_words() 


# In[ ]:




