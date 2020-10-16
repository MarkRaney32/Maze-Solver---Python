# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 23:21:22 2020

@author: markr
"""

class PriorityQueue:
    def __init__(self, original = None):
        if original == None:
            self.construct()
        else:
            self.copyConstruct(original)
            
    def construct(self):
        #None at position 0 is necessary for parent location calculations
        self._minheap = [None]
        self._size = 0
    
    def copyConstruct(self, original):
        self._minheap = original._minheap.copy()
        self._size = original._size
        
    def size(self):
        return self._size
    
    def minimum(self):
        return self._minheap[1]
        
    def insert(self, element, rejectduplicates = False):
        """
        Inserts element into the priority queue. By default accepts duplicates but
        That can be dissalowed with rejectduplicates
        """
        
        #exiting if duplicate
        if(rejectduplicates):
            for count in range(1,self._size+1):
                if element == self._minheap[count]:
                    break
        
        self._size += 1
        self._minheap.append(element)
        
        #Fixing location if necessary
        if(self._size > 1):
            parentloc = self._size//2
            loc = self._size
            
            #Parent of a given node at position loc in _minheap can be
            #calculated as loc / 2 round down
            while loc > 1 and self._minheap[loc] < self._minheap[parentloc]:
                self._minheap[loc] = self._minheap[parentloc]
                self._minheap[parentloc] = element
                loc = parentloc
                parentloc //= 2
                
    def extractMin(self):
        """
        Extracts and returns the minimum element from the minheap
        """
        if self._size == 0:
            return None
        
        if self._size == 1:
            self._size -= 1
            return self._minheap.pop()
        
        minimum = self._minheap[1]
        self._minheap[1] = self._minheap[self._size]
        self._minheap.pop()
        self._size -= 1
        
        lchild = 2
        rchild = 3
        current = 1
        nextloc = 1
        exiting = False
        
        while current <= self._size:
            #Checking cases where the current location has two children
            if rchild <= self._size:
                if self._minheap[lchild] == self._minheap[rchild] and self._minheap[rchild] == self._minheap[current]:
                    exiting = True
                elif self._minheap[lchild] <= self._minheap[rchild]:
                    if self._minheap[lchild] < self._minheap[current]:
                        nextloc = current*2
                    else:
                        exiting = True
                else:
                    if self._minheap[rchild] < self._minheap[current]:
                        nextloc = current*2+1
                    else:
                        exiting = True
            #Checking case where the current location has only a left child
            elif lchild <= self._size:
                if self._minheap[lchild] < self._minheap[current]:
                    nextloc = current*2
                else:
                    exiting = True
            else:
                exiting = True
            
            #Exits loop if all elements in correct location
            if exiting:
                break
            
            #Swapping procedure
            temp = self._minheap[nextloc]
            self._minheap[nextloc] = self._minheap[current]
            self._minheap[current] = temp
            current = nextloc
            lchild = current*2
            rchild = lchild+1
            
        return minimum  

