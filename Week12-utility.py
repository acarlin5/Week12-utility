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
    
