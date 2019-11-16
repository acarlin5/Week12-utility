# https://github.com/acarlin5/Week12-utility.git
# Abby Carlin
# CSCI 102 - Section C
# Week 11 - Part B

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(file):
    with open(file, 'r') as myfile:
        lines = myfile.readlines()
        print("OUTPUT", lines)

def UpdateString(string1, string2, index):
    new = string1[:index] + string2 + string1[index +1:]
    print('OUTPUT', new)
