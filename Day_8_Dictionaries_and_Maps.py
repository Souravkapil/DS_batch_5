# -*- coding: utf-8 -*-
"""hackerrank.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Laal227yN8udY8n2lQR3Q8PN3y0jTHT
"""



# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

dict1 = dict()

for i in range(n):
    name, number = input().split() 
    dict1[name] = number

for i in range(n):
      try:
        name = input()
        if name in dict1:
            print(f"{name}={dict1[name]}")
        else:
            print('Not found')
      except:
        break