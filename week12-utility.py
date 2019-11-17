# Brendan Martin
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(output):
    print("OUTPUT", output)
    
def LoadFile(file_name):
    f = open(file_name, "r")
    contents_lines = f.readlines()
    my_list = []
    for line in contents_lines:
        lines1 = line.split('/n')
        my_list.append(lines1)
    return my_list
    f.close()

def UpdateString(s1, s2, index):
    my_list = list(s1)
    my_list[index] = s2
    PrintOutput("".join(my_list))

def FindWordCount(list1, word):
    count = list1.count(word)
    return count
    
