# -*- coding: utf-8 -*-
"""Priddy_Assignment_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1099urmjYEYwGBG054P0A2Gl-EdzhEzgO

**Flatten a list:**
 This will take a lists of lists and convert them to one list
"""

def flatten(lst):
    if lst==[]: 
        return []
    elif type(lst) != list: 
        return [lst]
    else:
        x = flatten(lst[0])
        y = flatten(lst[1:])
        x.extend(y)
        return x

"""**Powerset: ** This will return a power set of a list"""

def powerset(s):
    result = [[]]
    for x in s:
        result.extend([i + [x] for i in result])
    return result

"""**Permutation:**  Gives all possible combinations of a list"""

def permutation(x):
    lst=[]
    if len(x) <= 1:
        return [x]
    for z in set(x):
        y = x.copy()
        y.remove(z)
        lst += [[z] + i for i in permutation(y)]
    return lst

"""**Spiral Attempt** I was able to get the reversed list. Was unsure how to make a spiral"""

def spiral(x):
    g= []
    z = (x**2)
    for i in reversed(range(z)):
        if i == 0:
            break
        g.append(i)
    return g