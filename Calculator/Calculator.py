#!/usr/bin/env python
# coding: utf-8
import math

def addition(a,b):
    print('{} + {} = {}'.format(a,b,a+b))
    return a+b

def subtraction(a,b):
    print('{} - {} = {}'.format(a,b,a-b))
    return a-b

def multiplication(a,b):
    print('{} * {} = {}'.format(a,b,a*b))
    return a*b
    
def division(a,b):
    print('{} / {} = {}'.format(a,b,a/b))
    return a/b

def nth_power(a,n):
    print('({}) to the power {} = {}'.format(a,n,a**n))
    return a**n

def logarithms(a,base):
    print('log({}) with base {} = {}'.format(a,base,math.log(a,base)))
    return math.log(a,base)


# def calculator():
#     option = int(input("Enter the type of operation to be performed:\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Nth power \n 6. Logarithm \n"))
    
#     if(option in (1,2,3,4)):
#           print("Enter two numbers:\n")
#           a=float(input("First number:"))
#           b=float(input("\nSecond number:"))
#           if(option==1):
#               addition(a,b)
#           elif(option==2):
#               subtraction(a,b)
#           elif(option==3):
#               multiplication(a,b)
#           elif(option==4):
#               division(a,b)
#     elif(option==5):
#         print("Enter the number and it's power/exponent:\n")
#         a=float(input("Enter the number:"))
#         n=float(input("\nEnter the power/exponent value:"))
#         nth_power(a,n)
        
#     elif(option==6):
#         print("Enter the number and it's base:\n")
#         a=float(input("Enter the number:"))
#         base=float(input("\nEnter the base:"))
#         logarithms(a,base)
#     else:
#           print("Invalid Input")
   
# calculator()            
# ```



