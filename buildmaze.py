# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:50:49 2020

@author: markr
"""

from PIL import Image
import os

class Maze():
    
    def __init__(self, filename):
        self._maze = []
        self._height = 0
        self._width = 0
        self._start = None
        self._end = None
        self.buildMaze(filename)
        
    def buildMaze(self, filename):
        """
        Reads the image at location filename and returns a 2D list
        interpretation of the image (height, width) where 1 represents
        traversable path and 0 an intraversable(wall)
        """
        path = os.getcwd()
    
        #px holds image object
        with Image.open(path + "\\Mazes\\" + filename) as im:
            px = im.load()
        
        self._width, self._height = im.size
        self._maze = [[] for x in range(self._height)]
        
        #First three are RGB, fourth is the scale used?
        for h in range(self._height):
            for w in range(self._width):
                if px[w,h] == (255,255,255,255):
                    self._maze[h].append([255,255,255])
                else:
                    self._maze[h].append([0,0,0])
                    
        #Assigning start and end. First checks left wall, then right wall,
        #Then top wall, then botton wall. Top->down or left->right where applicable
        
        #Left wall
        self.checkEdges(self._height, w = 0)
        #Right wall
        if self._start == None or self._end == None:
            self.checkEdges(self._height, w = self._width-1)
        #Top wall
        if self._start == None or self._end == None:
            self.checkEdges(self._width, h = 0)
        #Bottom wall
        if self._start == None or self._end == None:
            self.checkEdges(self._width, h = self._height-1)
        
                        
    def checkEdges(self, whichWall, h = None, w = None):
        """
        Helper function only ever called by buildmaze and is used to locate
        the beginning and end of the maze. Only one of h and w will not be
        None. whichwall is the limit of rows or columns depending on how the
        function was called
        """
        for i in range(whichWall):
            if h == None:
                if self._maze[i][w] == [255,255,255]:
                    if self._start == None:
                        self._start = (i,w)
                    else:
                        self._end = (i,w)
                        break
            else:
                if self._maze[h][i] == [255,255,255]:
                    if self._start == None:
                        self._start = (h,i) #Hello (:
                    else:
                        self._end = (h,i)
                        break
                    
    def checkSurroundings(self, origin):
        """
        Checks the four adjacent tiles to origin (y,x) and returns a tuple of four
        booleans, true for valid path, false otherwise. Tuple is ordered as
        (left, right, above, below)
        """
        #Checking left
        if origin[1] > 0:
            if self._maze[origin[0]][origin[1]-1] == [255,255,255]:
                l = True
            else:
                l = False
        else:
            l = False
            
        #Checking right
        if origin[1] < self._width-1:
            if self._maze[origin[0]][origin[1]+1] == [255,255,255]:
                r = True
            else:
                r = False
        else:
            r = False
            
        #Checking top
        if origin[0] > 0:
            if self._maze[origin[0]-1][origin[1]] == [255,255,255]:
                t = True
            else:
                t = False
        else:
            t = False
            
        #Checking bottom
        if origin[0] < self._height-1:
            if self._maze[origin[0]+1][origin[1]] == [255,255,255]:
                b = True
            else:
                b = False
        else:
            b = False
            
        return (l, r, t, b)
    
    def setNodeVisited(self, origin):
        self._maze[origin[0]][origin[1]] = [255,0,255]
                    
    def getHeight(self):
        return self._height
    
    def getWidth(self):
        return self._width
    
    def getMaze(self):
        return self._maze
    
    def getStart(self):
        return self._start
    
    def getEnd(self):
        return self._end
