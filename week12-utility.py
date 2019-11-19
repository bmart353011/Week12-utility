# Brendan Martin
# CSCI 102 - Section A
# Week 12 - Part A

import string
def PrintOutput(output):
    print("OUTPUT", output)
    
def LoadFile(file_name):
    with open(file_name) as file:
        my_list = file.read().splitlines()
        return my_list

def UpdateString(s1, s2, index):
    my_list = list(s1)
    my_list[index] = s2
    PrintOutput("".join(my_list))

def FindWordCount(list1, word):
    count = list1.count(word)
    return count

def ScoreFinder(list1, list2, name):
    name1 = name.upper()
    my_list = []
    for i in list1:
        i = i.upper()
        my_list.append(i)
    if name1 in my_list:
        index = my_list.index(name1)
        score = list2[index]
        print("OUTPUT", name, "got a score of", score)
    else:
        print("OUPUT player not found")

def Union(list1, list2):
    my_list = []
    my_list2 = []
    my_list1= []
    for i in list1:
        if i not in my_list1:
            my_list1.append(i)
    for i in list2:
        i = i.upper()
        if i not in my_list2:
            my_list2.append(i)
    my_list = my_list1 + my_list2
    return my_list
    
def Intersection(P1, P2):
    my_list = P1 + P2
    return my_list

def NotIn(list1, list2):
    my_list = []
    for i in list1:
        if i not in list2:
            my_list.append(i)
    return my_list
        


