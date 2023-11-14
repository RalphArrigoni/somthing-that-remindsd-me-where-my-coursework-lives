import random
import math
from flask import Flask, render_template, request, session
import sqlite3
import os
posX = "A"
posY = "1"
alist = []
markedList = ["A1"]
backtrack = ["A1"]
letter = 65
length = 0
counter = 0
reps = 1

length = int(input("maze size "))
length = length+1 #sorts out problem of maze being one smaller than input size
for i in range (1, length):
    alist.append(i)
lists = [[alist[i]] for i in range(0, length-1)] #creates a list in every variable on the list
for j in range (length-1):
    for k in range(length-1):
        lists[k].append(chr(letter)+ str(k+1))
    lists[j].pop(0) # removes initial value[kinda janky]
    letter = letter + 1# adds one to the ascii value
filled = (length - 1)**2

def marked(markedList, backtrack): # this marks the latest square touched onto a list of touched squares
    markedList.append(str(lists[int(posY)-1][ord(posX)-65]))
    backtrack.append(str(lists[int(posY)-1][ord(posX)-65]))
    return (markedList, backtrack)

def backUp(backtrack):# moves the current position back one
    actualPos = backtrack[-reps]
    print(actualPos)
    actualPos = actualPos[:1] + "`" + actualPos[1:3] # adds a character to the string ( bug with strings of more than 2 characters)
    x = actualPos.split("`") # removes said character and splits the string there
    global posX
    global posY
    posX = x[0]
    posY = x[1]
    return (backtrack) # this

def up():
    global posY
    posY = int(posY)
    posY = (posY - 1)
    posY = str(posY)
    marked(markedList, backtrack)

def down():
    global posY
    posY = int(posY)
    posY = (posY + 1)
    posY = str(posY)
    marked(markedList, backtrack)

def left():
    global posX
    posX = ord(posX)
    posX = (posX - 1)
    posX = chr(posX)
    marked(markedList, backtrack)

def right():
    global posX
    posX = ord(posX)
    posX = (posX + 1)
    posX = chr(posX)
    marked(markedList, backtrack)
actualPos = posX + posY
#how to change grid positions and whatnot^

print(lists)
while len(markedList) != filled: #temporary
    number = random.randint(1,4)
     #                                |<========================================>| -- This stops the ActualPos from moving onto A previously marked tile
    if number == 1 and posY != "1" and posX + str(int(posY)-1) not in markedList:
        up()
        counter = 0
        reps = 1
    elif number == 2 and posY != str(length-1)and posX + str(int(posY)+1) not in markedList:
        down()
        counter = 0
        reps = 1
    elif number == 3 and posX != "A" and chr(ord(posX)-1) + posY not in markedList:
        left()
        counter = 0
        reps = 1
    elif number == 4 and posX != (chr(letter - 1)) and chr(ord(posX) + 1) + posY not in markedList: # I dont know why its -7 but it is. don't change.
        right()
        counter = 0
        reps = 1
    elif counter > 6:
        backUp(backtrack)
        counter = 0
        reps = reps + 1
        print(backtrack)
        print(markedList)
    else:
        counter = counter + 1
    actualPos = posX + posY

