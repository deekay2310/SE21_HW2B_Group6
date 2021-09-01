#!/usr/bin/env python
# coding: utf-8

# # Welcome to Jupyter!

# In[2]:


from math import *

def addition(a,b):
    print('{} + {} = {}'.format(a,b,a+b))

def subtraction(a,b):
    print('{} - {} = {}'.format(a,b,a-b))

def multiplication(a,b):
    print('{} * {} = {}'.format(a,b,a*b))
    
def division(a,b):
    print('{} / {} = {}'.format(a,b,a/b))

def nth_root(a,n):
    print('root({}) to the power {} = {}'.format(a,n,a**n))

          
def logarithms(a,base):
          print('log({}) with base {} = {}'.format(a,base,log(a,base)))
    
def calculator():
    option = int(input("Enter the type of operation to be performed:\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Nth root \n 6. Logarithm \n"))
    
    if(option in (1,2,3,4)):
          print("Enter two numbers:\n")
          a=float(input("First number:"))
          b=float(input("\nSecond number:"))
          if(option==1):
              addition(a,b)
          elif(option==2):
              subtraction(a,b)
          elif(option==3):
              multiplication(a,b)
          elif(option==4):
              division(a,b)
    elif(option==5):
        print("Enter the number and it's power/exponent:\n")
        a=float(input("Enter the number:"))
        n=float(input("\nEnter the power/exponent value:"))
        nth_root(a,n)
        
    elif(option==6):
        print("Enter the number and it's base:\n")
        a=float(input("Enter the number:"))
        base=float(input("\nEnter the base:"))
        logarithms(a,base)
    else:
          print("Invalid Input")
   
calculator()            


# This repo contains an introduction to [Jupyter](https://jupyter.org) and [IPython](https://ipython.org).
# 
# Outline of some basics:
# 
# * [Notebook Basics](../examples/Notebook/Notebook%20Basics.ipynb)
# * [IPython - beyond plain python](../examples/IPython%20Kernel/Beyond%20Plain%20Python.ipynb)
# * [Markdown Cells](../examples/Notebook/Working%20With%20Markdown%20Cells.ipynb)
# * [Rich Display System](../examples/IPython%20Kernel/Rich%20Output.ipynb)
# * [Custom Display logic](../examples/IPython%20Kernel/Custom%20Display%20Logic.ipynb)
# * [Running a Secure Public Notebook Server](../examples/Notebook/Running%20the%20Notebook%20Server.ipynb#Securing-the-notebook-server)
# * [How Jupyter works](../examples/Notebook/Multiple%20Languages%2C%20Frontends.ipynb) to run code in different languages.

# In[ ]:





# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/ipython/ipython-in-depth
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook
