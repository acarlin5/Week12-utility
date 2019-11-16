# https://github.com/acarlin5/Week12-utility.git
# Abby Carlin
# CSCI 102 - Section C
# Week 11 - Part B

def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(file):
    with open(file, 'r') as myfile:
        lines = myfile.read().splitlines()
        return lines

def UpdateString(string1, string2, index):
    new = string1[:index] + string2 + string1[index +1:]
    print('OUTPUT', new)

def FindWordCount(mylist, string):
    num = mylist.count(string)
    return num

def ScoreFinder(players, scores, name):
    players_lower = [x.lower() for x in players]
    
    if name in players:
        index = players.index(name)
        print('OUTPUT', name, 'got a score of', scores[index])
    elif name in players_lower:
        index = players_lower.index(name)
        print('OUTPUT', name, 'got a score of', scores[index])
    else:
        print('OUTPUT player not found')

def Union(list1, list2):
    union = list1 + list2
    return union
