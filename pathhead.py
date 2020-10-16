# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:28:09 2020

@author: markr
"""

class PathHead():
    
    def __init__(self, y, x, dist):
        self._x = x
        self._y = y
        self._dist = dist
        
    def getDistance(self):
        return self._dist
    
    def getCords(self):
        return (self._y, self._x)
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
        
    def __lt__(self, p2):
        return self._dist < p2._dist
    
    def __le__(self, p2):
        return self._dist <= p2._dist
    
    def __eq__(self, p2):
        return self._x == p2._x and self._y == p2._y
    
    def __ne__(self, p2):
        return self._x != p2._x or self._y != p2._y
    
    def __gt__(self, p2):
        return self._dist > p2._dist
    
    def __ge__(self, p2):
        return self._dist >= p2._dist