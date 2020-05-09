#!/usr/bin/env python
# coding: utf-8

# ### PT3 -  Name : Vivek Saini,  Roll No: 2K18CSUN01047,  SET A

# ## Theoritical Questions

# ### 1. What is the syntax to call a constructor of a base class from child class
# ### Answer: Super() is used call a constructor of a base class from child class
# ### super().__init__()

# ### 2. How is a class made as inherited class (syntax of child class)
# #### Answer: 
# ### class Parent:
# ### pass
# ### class Child(Parent):
# ###      pass

# ### 3. Print an element of a nested dictionary
# #### Answer: 
# #### Dict = { 'Dict1': {'name': 'vivek', 'age': '20'}, 
# 
# ####              'Dict2': {'name': 'Rahul', 'age': '21'}} 
# 
# #### print("\nNested dictionary 2-") 
# 
# #### print(Dict)

# ## Programming Questions

# ### Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.

# In[20]:


items = []
for i in range(1000, 3000):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        items.append(s)
print( ",".join(items))


# ### Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

# In[24]:


def calculateSum (a,b):
    s = int(a) + int(b)
    return s 

# Main code 
# take two integral numbers as strings
num1 = "65"
num2 = "35"

# calculate sum
sum = calculateSum (num1, num2)

# print sum
print ("Sum = ", sum)


# In[ ]:




