#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = int(input("Enter x: "))
y = int(input("Enter y: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

def insidefunction(x,y,x1,y1,x2,y2):
    
    if(x > x1 and x < x2) and (y > y1 and y < y2):
        print('True')
        
    else:
        print('False')
        
insidefunction(x,y,x1,y1,x2,y2)


# In[ ]:




