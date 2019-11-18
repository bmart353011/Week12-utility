# Brendan Martin
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(output):
    print("OUTPUT", output)
    
def LoadFile(file_name):
    with open(file_name) as file:
        contents_lines = file.readlines()
        for line in contents_lines:
            lines1 = line.split(' ')
    return lines1
    

def UpdateString(s1, s2, index):
    my_list = list(s1)
    my_list[index] = s2
    PrintOutput("".join(my_list))

def FindWordCount(list1, word):
    count = list1.count(word)
    return count
    
def Intersection(P1, P2):
    my_list = P1 + P2
    return my_list
