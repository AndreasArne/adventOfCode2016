#!/usr/bin/env python3
"""
Advent of code day1.
Find out how many blocks away the easter bunny is.
http://adventofcode.com/2016/day/1
"""
def result():
    blocksAway = -pos[0] if pos[0] < 0 else pos[0]
    blocksAway += -pos[1] if pos[1] < 0 else pos[1]
    print("Number of blocks away is: {}. With pos: {}".format(blocksAway, pos))

inp = ["L3", "R1", "L4", "L1", "L2", "R4", "L3", "L3", "R2", "R3", "L5", "R1", "R3", "L4", "L1", "L2", "R2", "R1", "L4", "L4", "R2", "L5", "R3", "R2", "R1", "L1", "L2", "R2", "R2", "L1", "L1", "R2", "R1", "L3", "L5", "R4", "L3", "R3", "R3", "L5", "L190", "L4", "R4", "R51", "L4", "R5", "R5", "R2", "L1", "L3", "R1", "R4", "L3", "R1", "R3", "L5", "L4", "R2", "R5", "R2", "L1", "L5", "L1", "L1", "R78", "L3", "R2", "L3", "R5", "L2", "R2", "R4", "L1", "L4", "R1", "R185", "R3", "L4", "L1", "L1", "L3", "R4", "L4", "L1", "R5", "L5", "L1", "R5", "L1", "R2", "L5", "L2", "R4", "R3", "L2", "R3", "R1", "L3", "L5", "L4", "R3", "L2", "L4", "L5", "L4", "R1", "L1", "R5", "L2", "R4", "R2", "R3", "L1", "L1", "L4", "L3", "R4", "L3", "L5", "R2", "L5", "L1", "L1", "R2", "R3", "L5", "L3", "L2", "L1", "L4", "R4", "R4", "L2", "R3", "R1", "L2", "R1", "L2", "L2", "R3", "R3", "L1", "R4", "L5", "L3", "R4", "R4", "R1", "L2", "L5", "L3", "R1", "R4", "L2", "R5", "R4", "R2", "L5", "L3", "R4", "R1", "L1", "R5", "L3", "R1", "R5", "L2", "R1", "L5", "L2", "R2", "L2", "L3", "R3", "R3", "R1"]
#X Y cordiantes
pos = [0, 0] # X and Y cordinates
posIndx = 1 #Change X or Y cordiante. Start by expecting to move north
nextMove = {0: 1, 1: 0} #If this turn is 0 next is 1 and other way around. Since expect to move north we know that we will change X pos next

#How to move
direction = [1, 1, -1, -1] #N,E,S,W
lrCirculareMovement = {"L": -1, "R": 1} #add or sub from direction
dirIndx = 0 #N,E,S or W movement

#Revisit same location
locations = set()
locations.add((0, 0))

for move in inp:
    posIndx = nextMove[posIndx] # X or Y move
    dirIndx += lrCirculareMovement[move[0]] # which direction, N,E,S,W
    for i in range(int(move[1:])):
        pos[posIndx] += direction[dirIndx % 4] #Move cordinate nr of blocks
        if (pos[0], pos[1]) in locations:
            result()
            exit(1)
        locations.add((pos[0], pos[1]))
