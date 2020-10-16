# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:11:57 2020

@author: markr
"""
from buildmaze import Maze
from priorityqueue import PriorityQueue
from pathhead import PathHead
from PIL import Image
from math import sqrt
import numpy

def main():
    maze = Maze("maze2.png")
    paths = PriorityQueue()
    
    start = maze.getStart()
    end = maze.getEnd()
    paths.insert(PathHead(start[0], start[1], calcDistance(start, end)))
    current = paths.minimum()
    
    while paths.size() > 0 and current.getDistance() != 0.0:
        current = paths.extractMin()
        maze.setNodeVisited(current.getCords())
        surroundings = maze.checkSurroundings(current.getCords())
        insertSurroundings(paths, surroundings, current, end)
    
    solved = maze.getMaze()           
    solved = numpy.array(solved)
    img = Image.fromarray(solved.astype('uint8'), 'RGB')
    img.save('solved.png')

def calcDistance(start, end):
        """
        Given two coordinates of form (y,x), this function calculates and
        returns the distance between the two
        """
        return sqrt(pow(end[0]-start[0], 2) + pow(end[1]-start[1],2))

def insertSurroundings(paths, surroundings, origin, end):
    """
    Based on the 4 boolean tuple surroundings, inserts each valid path into
    the priority queue
    """
    if surroundings[0]:
        newLoc = (origin.getY(), origin.getX()-1)
        newpath = PathHead(newLoc[0], newLoc[1], calcDistance(newLoc, end))
        paths.insert(newpath, rejectduplicates = True)
    if surroundings[1]:
        newLoc = (origin.getY(), origin.getX()+1)
        newpath = PathHead(newLoc[0], newLoc[1], calcDistance(newLoc, end))
        paths.insert(newpath, rejectduplicates = True)
    if surroundings[2]:
        newLoc = (origin.getY()-1, origin.getX())
        newpath = PathHead(newLoc[0], newLoc[1], calcDistance(newLoc, end))
        paths.insert(newpath, rejectduplicates = True)
    if surroundings[3]:
        newLoc = (origin.getY()+1, origin.getX())
        newpath = PathHead(newLoc[0], newLoc[1], calcDistance(newLoc, end))
        paths.insert(newpath, rejectduplicates = True)
    
main()