# Brendan Martin
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(output):
    print("OUTPUT", output)
def LoadFile(file_name):
    f = open(file_name, "r")
    contents_lines = f.readlines()
    for line in contents_lines:
        my_list = line.split(' ')
    return my_list
    f.close()
